#!/usr/bin/env node
/** Capture full-page legacy-site screenshots through Chrome DevTools Protocol. */

import { spawn } from 'node:child_process';
import { mkdir, rm, writeFile } from 'node:fs/promises';
import { setTimeout as delay } from 'node:timers/promises';

const outputDir = new URL('./full-page-screenshots/', import.meta.url);
const profileDir = '/tmp/opencode/plexus-legacy-chrome-profile';
await mkdir(outputDir, { recursive: true });
await rm(profileDir, { recursive: true, force: true });
await mkdir(profileDir, { recursive: true });

const pages = {
  home: 'https://plexusdevelopmentgroup.ca/',
  projects: 'https://plexusdevelopmentgroup.ca/nova-scotia-construction-projects',
  residential: 'https://plexusdevelopmentgroup.ca/residential-construction',
  commercial: 'https://plexusdevelopmentgroup.ca/commercial-construction',
  industrial: 'https://plexusdevelopmentgroup.ca/industrial-construction',
  community: 'https://plexusdevelopmentgroup.ca/community',
  contact: 'https://plexusdevelopmentgroup.ca/contact-for-real-estate-opportunities',
};

const port = 9333;
const chrome = spawn('google-chrome', [
  '--headless=new', '--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage',
  '--disable-background-networking', '--hide-scrollbars', '--no-first-run',
  `--remote-debugging-port=${port}`, `--user-data-dir=${profileDir}`, 'about:blank',
], { stdio: 'ignore' });

async function getTarget() {
  for (let attempt = 0; attempt < 60; attempt++) {
    try {
      const response = await fetch(`http://127.0.0.1:${port}/json/list`);
      const targets = await response.json();
      const page = targets.find(target => target.type === 'page');
      if (page?.webSocketDebuggerUrl) return page;
    } catch {}
    await delay(250);
  }
  throw new Error('Chrome DevTools endpoint did not become available.');
}

let socket;
let nextId = 1;
const pending = new Map();
const eventWaiters = new Map();

function send(method, params = {}) {
  const id = nextId++;
  socket.send(JSON.stringify({ id, method, params }));
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
}

function waitForEvent(method, timeoutMs = 30000) {
  return new Promise((resolve, reject) => {
    const timeout = setTimeout(() => {
      eventWaiters.delete(method);
      reject(new Error(`Timed out waiting for ${method}`));
    }, timeoutMs);
    eventWaiters.set(method, params => {
      clearTimeout(timeout);
      eventWaiters.delete(method);
      resolve(params);
    });
  });
}

try {
  const target = await getTarget();
  socket = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    socket.addEventListener('open', resolve, { once: true });
    socket.addEventListener('error', reject, { once: true });
  });
  socket.addEventListener('message', event => {
    const message = JSON.parse(event.data);
    if (message.id) {
      const handler = pending.get(message.id);
      if (!handler) return;
      pending.delete(message.id);
      if (message.error) handler.reject(new Error(message.error.message));
      else handler.resolve(message.result || {});
      return;
    }
    const waiter = eventWaiters.get(message.method);
    if (waiter) waiter(message.params || {});
  });

  await send('Page.enable');
  await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1440, height: 900, deviceScaleFactor: 1, mobile: false,
  });

  for (const [name, url] of Object.entries(pages)) {
    const loaded = waitForEvent('Page.loadEventFired');
    await send('Page.navigate', { url });
    await loaded;
    await delay(4500);
    await send('Runtime.evaluate', {
      expression: `(async()=>{const step=Math.max(500,Math.floor(innerHeight*.8));for(let y=0;y<document.documentElement.scrollHeight;y+=step){scrollTo(0,y);await new Promise(r=>setTimeout(r,180));}scrollTo(0,0);await new Promise(r=>setTimeout(r,600));return document.documentElement.scrollHeight})()`,
      awaitPromise: true,
      returnByValue: true,
    });
    const metrics = await send('Page.getLayoutMetrics');
    const width = Math.ceil(metrics.cssContentSize?.width || metrics.contentSize?.width || 1440);
    const height = Math.ceil(metrics.cssContentSize?.height || metrics.contentSize?.height || 900);
    const screenshot = await send('Page.captureScreenshot', {
      format: 'png',
      fromSurface: true,
      captureBeyondViewport: true,
      clip: { x: 0, y: 0, width, height, scale: 1 },
    });
    const path = new URL(`${name}.png`, outputDir);
    await writeFile(path, Buffer.from(screenshot.data, 'base64'));
    console.log(`${name}: ${width} x ${height}`);
  }
} finally {
  if (socket?.readyState === WebSocket.OPEN) socket.close();
  chrome.kill('SIGTERM');
  await delay(500);
  if (!chrome.killed) chrome.kill('SIGKILL');
  await rm(profileDir, { recursive: true, force: true });
}
