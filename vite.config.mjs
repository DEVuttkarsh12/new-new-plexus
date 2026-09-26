import { defineConfig } from 'vite';

export default defineConfig({
  root: 'dist',
  server: { host: '0.0.0.0', allowedHosts: ['terminal.local'] },
  plugins: [{
    name: 'responsive-review',
    apply: 'serve',
    transformIndexHtml(html) {
      return html.replace('</body>', '<a class="dev-review-link" href="/__qa" style="position:fixed;bottom:8px;right:8px;z-index:1000;font:12px Arial;padding:8px 12px;background:#fff;color:#253a36;border:1px solid #bbc2b5">Responsive review</a><script>if(new URLSearchParams(location.search).has("review-intro")){try{sessionStorage.removeItem("plexus-intro-seen")}catch(e){}}if(window.self!==window.top)document.querySelector(".dev-review-link").remove();</script></body>');
    },
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        const url = new URL(req.url, 'http://terminal.local:4173');
        if (url.pathname !== '/__qa') return next();
        const widths = [320, 390, 430, 1280, 1920];
        const requested = Number(url.searchParams.get('width'));
        const width = widths.includes(requested) ? requested : 390;
        res.setHeader('Content-Type', 'text/html; charset=utf-8');
        res.end(`<!doctype html><html><head><title>Plexus responsive review</title><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0;background:#dfe5dc;font:14px Arial;color:#253a36}nav{display:flex;gap:20px;padding:18px}a{color:inherit}iframe{display:block;width:${width}px;height:850px;margin:0 20px 20px;border:1px solid #bbc2b5;background:white}h1{font-size:16px;margin:0 20px 15px}</style></head><body><nav>${widths.map(w=>`<a href="/__qa?width=${w}">${w>=1280?`${w}px desktop`:`${w}px phone`}</a>`).join('')}<a href="/">Full website</a><a href="/?review-intro=1">Opening animation</a></nav><h1>${width}px responsive viewport</h1><iframe id="site-frame" title="Plexus website" src="/"></iframe></body></html>`);
      });
    }
  }]
});
