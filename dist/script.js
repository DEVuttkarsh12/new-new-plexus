'use strict';
(() => {
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const wide = matchMedia('(min-width: 1000px) and (min-height: 700px)');
  const root = document.documentElement;
  const header = $('.site-header');
  const menu = $('.mobile-menu');
  const menuButton = $('.menu-toggle');
  let motionPaused = reduced.matches;
  try { if (sessionStorage.getItem("plexus-motion-paused") === "yes") motionPaused = true; } catch (_) {}
  let scrollFrame = false;

  function setMenu(open) {
    menu.hidden = !open;
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    header.classList.toggle('menu-open', open);
    $('main').inert = open;
    $('.site-footer').inert = open;
    $('.footer-cta').inert = open;
    document.body.classList.toggle('modal-open', open || !!$('dialog[open]'));
    if (open) $('a', menu).focus({ preventScroll: true });
    syncFilm();
  }
  menuButton.addEventListener('click', () => setMenu(menu.hidden));
  $$('a', menu).forEach(a => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', event => {
    if (menu.hidden) return;
    if (event.key === 'Escape') { setMenu(false); menuButton.focus({ preventScroll: true }); }
    if (event.key === 'Tab') {
      const items = [menuButton, ...$$('a', menu)];
      if (event.shiftKey && document.activeElement === items[0]) { event.preventDefault(); items.at(-1).focus(); }
      else if (!event.shiftKey && document.activeElement === items.at(-1)) { event.preventDefault(); items[0].focus(); }
    }
  });
  matchMedia('(min-width: 810px)').addEventListener('change', event => { if (event.matches) setMenu(false); });

  // Independent, native image preview. Source and caption always come from the clicked image.
  const photoDialog = $('.photo-dialog');
  const photoTriggers = $$('[data-photo]');
  const photoItems = [...new Map(photoTriggers.map(el => [el.dataset.photo, {file:el.dataset.photo,title:el.dataset.photoTitle,note:el.dataset.photoNote}])).values()];
  let photoIndex = 0;
  let photoTrigger = null;
  function renderPhoto() {
    const item = photoItems[photoIndex];
    if (!item) return;
    $('.photo-full').src = '/assets/' + item.file;
    $('.photo-full').alt = item.title + '. ' + item.note;
    $('#photo-title').textContent = item.title;
    $('.photo-caption > p').textContent = item.note;
    $('.photo-count').textContent = `${photoIndex + 1} / ${photoItems.length}`;
    $('[data-photo-prev]').hidden = photoItems.length < 2;
    $('[data-photo-next]').hidden = photoItems.length < 2;
  }
  photoTriggers.forEach(button => button.addEventListener('click', () => {
    photoTrigger = button;
    photoIndex = photoItems.findIndex(item => item.file === button.dataset.photo);
    renderPhoto();
    photoDialog.showModal();
    document.body.classList.add('modal-open');
    $('[data-close-photo]').focus({ preventScroll: true });
    syncFilm();
  }));
  $('[data-close-photo]').addEventListener('click', () => photoDialog.close());
  $('[data-photo-prev]').addEventListener('click', () => { photoIndex = (photoIndex - 1 + photoItems.length) % photoItems.length; renderPhoto(); });
  $('[data-photo-next]').addEventListener('click', () => { photoIndex = (photoIndex + 1) % photoItems.length; renderPhoto(); });
  photoDialog.addEventListener('keydown', event => {
    if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
    event.preventDefault();
    photoIndex = (photoIndex + (event.key === 'ArrowLeft' ? -1 : 1) + photoItems.length) % photoItems.length;
    renderPhoto();
  });
  photoDialog.addEventListener('close', () => {
    document.body.classList.remove('modal-open');
    photoTrigger?.focus({ preventScroll: true });
    syncFilm();
  });

  // Film playback is local, muted and stopped when it is not visible.
  const siteFilm = $('.site-film');
  const filmDialog = $('.film-dialog');
  const overview = $('.overview-film');
  let filmVisible = !!siteFilm && siteFilm.getBoundingClientRect().bottom > 0 && siteFilm.getBoundingClientRect().top < innerHeight;
  let filmPlayPending = false;
  let filmTrigger = null;
  function syncFilm() {
    if (!siteFilm) return;
    if (motionPaused || !filmVisible || document.hidden || filmDialog?.open || photoDialog.open || !menu.hidden) {
      siteFilm.pause(); return;
    }
    if (!siteFilm.getAttribute('src')) {
      siteFilm.src = innerWidth <= 809 ? siteFilm.dataset.mobileSrc : siteFilm.dataset.desktopSrc;
      siteFilm.load();
    }
    siteFilm.muted = true;
    if (!siteFilm.paused || filmPlayPending) return;
    filmPlayPending = true;
    siteFilm.play().catch(() => {}).finally(() => { filmPlayPending = false; });
  }
  if (siteFilm) {
    // Observe the hero itself, so a transparent video awaiting its first frame can start.
    new IntersectionObserver(entries => { filmVisible = entries[0].isIntersecting; syncFilm(); }, { threshold:.1 }).observe(siteFilm.closest('.hero'));
    siteFilm.addEventListener('playing', () => siteFilm.classList.add('has-frame'));
    siteFilm.addEventListener('error', () => siteFilm.classList.remove('has-frame'));
    document.addEventListener('visibilitychange', syncFilm);
    addEventListener('pageshow', syncFilm);
    // A gesture can unblock autoplay on browsers with stricter media policies.
    document.addEventListener('pointerdown', event => { if (!event.target.closest('.motion-preference')) syncFilm(); }, { once:true });
    // Begin fetching during the opening sequence, independently of the scroll setup.
    syncFilm();
  }
  $$('[data-open-film]').forEach(button => button.addEventListener('click', () => {
    if (!filmDialog || !overview) return;
    filmTrigger = button;
    overview.src = '/assets/plexus-overview.mp4';
    filmDialog.showModal();
    document.body.classList.add('modal-open');
    siteFilm?.pause();
    overview.play().catch(() => {});
    $('[data-close-film]').focus({ preventScroll:true });
  }));
  $('[data-close-film]')?.addEventListener('click', () => filmDialog.close());
  filmDialog?.addEventListener('close', () => {
    overview.pause(); overview.removeAttribute('src'); overview.load();
    document.body.classList.remove('modal-open');
    filmTrigger?.focus({ preventScroll:true });
    syncFilm();
  });
  $$('dialog').forEach(dialog => dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  }));

  // Expanding service panels keep collapsed content out of the tab order.
  const servicePanels = $$('.service-panel');
  function openService(index) {
    servicePanels.forEach((panel, i) => {
      const open = i === index;
      panel.classList.toggle('active', open);
      $('.service-selector', panel).setAttribute('aria-expanded', String(open));
      $('.service-content', panel).inert = !open;
    });
  }
  servicePanels.forEach((panel, i) => {
    $('.service-selector', panel).addEventListener('click', () => openService(i));
    panel.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse' && innerWidth > 809) openService(i); });
    $('.service-selector', panel).addEventListener('keydown', event => {
      if (!['ArrowLeft','ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const next = (i + (event.key === 'ArrowRight' ? 1 : -1) + servicePanels.length) % servicePanels.length;
      openService(next); $('.service-selector', servicePanels[next]).focus();
    });
  });

  // The selected projects retain their horizontal scroll on wide screens.
  const journey = $('.project-journey');
  const journeyWindow = $('.journey-window');
  const track = $('.journey-track');
  const cards = $$('.journey-card');
  const slideButtons = $$('[data-slide]');
  const mandate = $('.mandate');
  const mandateScenes = $$('[data-mandate-scene]');
  const mandateButtons = $$('[data-mandate-target]');
  const mandateCount = $('.mandate-count');
  const mandateProgress = $('.mandate-progress i');
  let journeyPinned = false;
  let mandatePinned = false;
  let currentMandateScene = -1;
  let travel = 0;
  const clamp = x => Math.max(0, Math.min(1, x));
  function activeSlide(progress) {
    const index = Math.round(progress * 2);
    slideButtons.forEach((button, i) => {
      if (i === index) button.setAttribute('aria-current', 'true'); else button.removeAttribute('aria-current');
    });
    $('.journey-progress i').style.width = `${33.333 + progress * 66.667}%`;
  }
  function measure() {
    if (journey) {
      journeyPinned = wide.matches && !motionPaused;
      journey.classList.toggle('pinned', journeyPinned);
      travel = cards[2].offsetLeft - cards[0].offsetLeft;
      if (!journeyPinned) track.style.transform = '';
      else journeyWindow.scrollLeft = 0;
      $('.journey-hint').textContent = journeyPinned ? 'Scroll to explore →' : 'Swipe to explore →';
    }
    if (architecture) {
      architecturePinned = wide.matches && !motionPaused;
      architecture.classList.toggle('perspective-pinned', architecturePinned);
    }
    if (mandate) {
      mandatePinned = wide.matches && !motionPaused;
      mandate.classList.toggle('mandate-pinned', mandatePinned);
    }
    draw();
  }
  function goToSlide(index, behavior = motionPaused ? 'auto' : 'smooth') {
    if (journeyPinned) {
      const top = scrollY + journey.getBoundingClientRect().top;
      const distance = journey.offsetHeight - innerHeight + 90;
      window.scrollTo({top:top - 90 + distance * index / 2,behavior});
    } else journeyWindow.scrollTo({left:cards[index].offsetLeft - cards[0].offsetLeft,behavior});
  }
  slideButtons.forEach(button => button.addEventListener('click', () => goToSlide(Number(button.dataset.slide))));
  cards.forEach((card,i) => card.addEventListener('focusin', () => { if (journeyPinned && !$('dialog[open]')) goToSlide(i,'auto'); }));
  journeyWindow?.addEventListener('scroll', () => { if (!journeyPinned) activeSlide(clamp(journeyWindow.scrollLeft / Math.max(1,travel))); },{passive:true});

  function renderMandate(progress) {
    if (!mandate) return;
    const index = Math.min(mandateScenes.length - 1, Math.floor(clamp(progress) * mandateScenes.length));
    if (index !== currentMandateScene) {
      mandate.dataset.scene = String(index);
      mandateScenes.forEach((scene, i) => scene.classList.toggle('active', i === index));
      mandateButtons.forEach((button, i) => {
        if (i === index) button.setAttribute('aria-current','true'); else button.removeAttribute('aria-current');
      });
      if (mandateCount) mandateCount.textContent = `0${index + 1} / 04`;
      currentMandateScene = index;
    }
    if (mandateProgress) mandateProgress.style.width = `${25 + clamp(progress) * 75}%`;
  }
  function goToMandate(index) {
    if (mandatePinned) {
      const top = scrollY + mandate.getBoundingClientRect().top;
      const distance = mandate.offsetHeight - innerHeight + 90;
      scrollTo({top:top - 90 + distance * ((index + .08) / mandateScenes.length),behavior:motionPaused?'auto':'smooth'});
    } else mandateScenes[index]?.scrollIntoView({behavior:motionPaused?'auto':'smooth',block:'center'});
  }
  mandateButtons.forEach((button, i) => {
    button.addEventListener('click', () => goToMandate(i));
    button.addEventListener('keydown', event => {
      if (!['ArrowLeft','ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const next = (i + (event.key === 'ArrowRight' ? 1 : -1) + mandateButtons.length) % mandateButtons.length;
      goToMandate(next); mandateButtons[next].focus({preventScroll:true});
    });
  });

  const hero = $('.hero');
  const heroMedia = $('.hero-media');
  const heroCopy = $('.estate-copy');
  const filmScroll = $('.film-scroll');
  const filmFrame = $('.film-frame');
  const architecture = $('.architecture');
  const buildingPlane = $('.building-plane');
  const buildingContext = $('.building-context');
  const architectureWord = $('.architecture-word');
  const architectureInterior = $('.architecture-interior');
  const perspectiveButtons = $$('[data-perspective]');
  const chapters = $$('[data-chapter]');
  let architecturePinned = false;
  let perspectiveSelection = null;
  let pointerX = 0;
  let pointerY = 0;
  let lastChapter = -1;
  const easeOut = x => 1 - Math.pow(1 - x, 3);
  function renderPerspective(progress) {
    const scene = Math.min(2, Math.floor(progress * 3));
    if (scene !== lastChapter) {
      architecture.dataset.scene = String(scene);
      chapters.forEach((chapter, i) => { chapter.hidden = i !== scene; });
      perspectiveButtons.forEach((button, i) => {
        if (i === scene) button.setAttribute('aria-current', 'true'); else button.removeAttribute('aria-current');
      });
      lastChapter = scene;
    }
    const mobile = innerWidth <= 809;
    const shift = mobile ? 0 : 105 - progress * 155;
    const scale = mobile ? .93 + progress * .08 : .86 + easeOut(clamp(progress / .65)) * .13;
    const tiltY = motionPaused ? 0 : -8 + progress * 12 + pointerX;
    const tiltX = motionPaused ? 0 : 4 - progress * 4 + pointerY;
    buildingPlane.style.transform = `translateX(${-50 + progress * 3}%) translateY(${shift}px) rotateY(${tiltY}deg) rotateX(${tiltX}deg) scale(${scale})`;
    buildingContext.style.opacity = String(clamp((progress - .18) / .32) * .65);
    architectureWord.style.transform = `translate(-50%,${-30 - progress * 48}%) scale(${1 + progress * .1})`;
    architectureWord.style.opacity = String(1 - progress * .7);
    const interior = easeOut(clamp((progress - .62) / .22));
    architectureInterior.style.opacity = String(interior);
    architectureInterior.style.transform = `translateY(${(1-interior)*80}px) rotate(${(1-interior)*6}deg)`;
    architectureInterior.style.pointerEvents = interior > .8 ? 'auto' : 'none';
    architectureInterior.inert = interior < .8;
  }
  function selectPerspective(index) {
    if (architecturePinned) {
      const top = scrollY + architecture.getBoundingClientRect().top;
      const distance = architecture.offsetHeight - innerHeight + 90;
      const progress = [.04, .48, .88][index];
      scrollTo({top:top - 90 + distance * progress, behavior:motionPaused ? 'auto' : 'smooth'});
    } else {
      perspectiveSelection = [.04, .48, .88][index];
      draw();
    }
  }
  perspectiveButtons.forEach((button, i) => {
    button.addEventListener('click', () => selectPerspective(i));
    button.addEventListener('keydown', event => {
      if (!['ArrowLeft','ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const next = (i + (event.key === 'ArrowRight' ? 1 : -1) + 3) % 3;
      selectPerspective(next); perspectiveButtons[next].focus({preventScroll:true});
    });
  });
  if (architecture) {
    architecture.addEventListener('pointermove', event => {
      if (motionPaused || event.pointerType !== 'mouse' || !architecturePinned) return;
      const r = architecture.getBoundingClientRect();
      pointerX = (event.clientX / innerWidth - .5) * 2.5;
      pointerY = (event.clientY / innerHeight - .5) * -1.5;
      if (!scrollFrame) { scrollFrame = true; requestAnimationFrame(draw); }
    },{passive:true});
    architecture.addEventListener('pointerleave', () => {pointerX=0;pointerY=0;draw();});
    architectureInterior.addEventListener('focus', () => { if (lastChapter !== 2) selectPerspective(2); });
  }
  function draw() {
    scrollFrame = false;
    header.classList.toggle('scrolled', scrollY > 45);
    if (journeyPinned) {
      const rect = journey.getBoundingClientRect();
      const progress = clamp((90 - rect.top) / Math.max(1,journey.offsetHeight - innerHeight + 90));
      track.style.transform = `translate3d(${-travel * progress}px,0,0)`;
      activeSlide(progress);
    }
    if (architecture) {
      const rect = architecture.getBoundingClientRect();
      let progress = 0;
      if (architecturePinned) progress = clamp((90 - rect.top) / Math.max(1, architecture.offsetHeight-innerHeight+90));
      else if (perspectiveSelection !== null) progress = perspectiveSelection;
      else if (!motionPaused) progress = clamp((90 - rect.top) / (architecture.offsetHeight * .75));
      renderPerspective(progress);
    }
    if (mandate) {
      const rect = mandate.getBoundingClientRect();
      const progress = mandatePinned
        ? clamp((90 - rect.top) / Math.max(1, mandate.offsetHeight - innerHeight + 90))
        : clamp((innerHeight * .7 - rect.top) / Math.max(1, mandate.offsetHeight));
      renderMandate(progress);
    }
    if (!motionPaused) {
      if (hero && heroMedia && hero.getBoundingClientRect().bottom > 0) {
        const progress = clamp(scrollY / hero.offsetHeight);
        heroMedia.style.transform = `translate3d(0,${progress * (hero.classList.contains('estate-hero') ? 28 : 130)}px,0) scale(${1+progress*.025})`;
      if (heroCopy) heroCopy.style.transform = `translateY(${-progress * 20}px)`;
      }
      if (filmScroll && innerWidth > 809) {
        const rect = filmScroll.getBoundingClientRect();
        if (rect.top < innerHeight && rect.bottom > 0) {
          const progress = clamp((innerHeight - rect.top) / (innerHeight * 1.2));
          filmFrame.style.transform = `scale(${.91 + progress * .09})`;
        }
      }
    } else {
      if (heroMedia) heroMedia.style.transform = '';
      if (heroCopy) heroCopy.style.transform = '';
      if (filmFrame) {filmFrame.style.transform='';filmFrame.style.borderRadius='';}
    }
  }
  addEventListener('scroll', () => { if (!scrollFrame) {scrollFrame=true;requestAnimationFrame(draw);} },{passive:true});
  addEventListener('resize', measure,{passive:true});
  wide.addEventListener('change',measure);
  function applyMotion() {
    root.classList.toggle('motion-paused',motionPaused);
    $('.motion-preference').textContent = motionPaused ? 'Enable motion' : 'Pause motion';
    $('.motion-preference').setAttribute('aria-pressed',String(motionPaused));
    measure();syncFilm();
  }
  $('.motion-preference').addEventListener('click', () => {motionPaused=!motionPaused;try{sessionStorage.setItem('plexus-motion-paused',motionPaused?'yes':'no');}catch(_){}applyMotion();});
  reduced.addEventListener('change', () => {motionPaused=reduced.matches;applyMotion();});

  // Reveals never gate visibility. Counters always retain the real final value as their accessible label.
  const revealObserver = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) {
      if (!motionPaused) entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  },{threshold:.08});
  $$('.reveal').forEach(el => revealObserver.observe(el));
  const countObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      countObserver.unobserve(entry.target);
      const el=entry.target,target=Number(el.dataset.count);
      if (motionPaused) return;
      el.setAttribute('aria-label',String(target));
      const start=performance.now();
      function tick(now) {
        const progress=clamp((now-start)/1000);
        el.textContent=String(Math.round(target*(1-Math.pow(1-progress,3))));
        if (progress<1&&!motionPaused) requestAnimationFrame(tick); else el.textContent=String(target);
      }
      requestAnimationFrame(tick);
    });
  },{threshold:.4});
  $$('[data-count]').forEach(el=>countObserver.observe(el));

  const search = $('#project-search');
  if (search) {
    const region=$('#filter-region'),status=$('#filter-status'),sectorButtons=$$('input[name=sector]');
    const projectCards=$$('[data-project-card]');
    const initialSector=new URLSearchParams(location.search).get('sector');
    sectorButtons.forEach(input=>{ if(input.value===initialSector) input.checked=true; });
    function filter() {
      const q=search.value.trim().toLowerCase();
      const sector=$('input[name=sector]:checked').value;
      let count=0;
      projectCards.forEach(card=>{
        const visible=(!q||card.dataset.search.includes(q))&&(!region.value||card.dataset.region===region.value)&&(!status.value||card.dataset.status===status.value)&&(!sector||card.dataset.sector===sector);
        card.hidden=!visible;if(visible)count++;
      });
      $('.result-count').textContent=`${count} ${count===1?'project':'projects'}`;
      $('.empty-state').hidden=count!==0;
    }
    search.addEventListener('input',filter);region.addEventListener('change',filter);status.addEventListener('change',filter);sectorButtons.forEach(el=>el.addEventListener('change',filter));
    $$('.clear-filters').forEach(button=>button.addEventListener('click',()=>{search.value='';region.value='';status.value='';sectorButtons[0].checked=true;filter();}));
    filter();
  }
  const form=$('.enquiry-form');
  if(form) {
    const subject=new URLSearchParams(location.search).get('subject');
    if(subject) form.elements.subject.value=subject.replaceAll('-',' ').replace(/\b\w/g,c=>c.toUpperCase());
    form.addEventListener('submit',event=>{
      event.preventDefault();
      if(!form.reportValidity())return;
      const data=new FormData(form);
      const name=String(data.get('name')).trim(), email=String(data.get('email')).trim(), message=String(data.get('message')).trim(),subject=String(data.get('subject')).trim();
      if(!name||!message){$('.form-status').textContent='Please add your name and a message.';return;}
      const body=`Hello Plexus Development Group,\n\n${message}\n\nName: ${name}\nEmail: ${email}`;
      location.href=`mailto:info@plexusdevelopmentgroup.ca?subject=${encodeURIComponent(subject||'Website enquiry from '+name)}&body=${encodeURIComponent(body)}`;
      $('.form-status').textContent='Your email app will open with your draft. Review and send it there. If it does not open, email info@plexusdevelopmentgroup.ca or call +1 902 809 9399.';
    });
  }
  // Reveal copy only after the quiet brand dissolve has completed.
  const intro = $('.page-intro');
  if (intro) {
    const introEdition = 'group-v1';
    let seen = false;
    try { seen = sessionStorage.getItem('plexus-intro-seen') === introEdition; } catch (_) {}
    let exiting = false;
    let revealed = false;
    let exitFallback;
    const revealHero = () => {
      if (revealed) return;
      revealed = true;
      clearTimeout(exitFallback);
      intro.remove();
      root.classList.remove('opening');
      root.classList.add('hero-ready');
      try { sessionStorage.setItem('plexus-intro-seen',introEdition); } catch (_) {}
    };
    const endIntro = () => {
      if (exiting || revealed) return;
      exiting = true;
      if (motionPaused || reduced.matches) { revealHero(); return; }
      intro.classList.add('done');
      const exitMs = parseFloat(getComputedStyle(intro).transitionDuration) * 1000 || 1200;
      exitFallback = setTimeout(revealHero, exitMs + 80);
    };
    intro.addEventListener('transitionend', event => {
      if (event.target === intro && event.propertyName === 'opacity' && exiting) revealHero();
    });
    intro.addEventListener('animationend', event => {
      if (event.target === intro && event.animationName === 'intro-safety') revealHero();
    });
    reduced.addEventListener('change', event => { if (event.matches) revealHero(); });
    if (motionPaused || seen) { revealHero(); }
    else {
      root.classList.add('opening');
      const started = performance.now();
      const tasks = [document.fonts.ready, new Promise(resolve => {
        const poster = new Image();poster.src = innerWidth <= 809 ? '/assets/halifax-waterfront-mobile.webp' : '/assets/halifax-waterfront.webp';
        if (poster.complete) resolve(); else {poster.onload=resolve;poster.onerror=resolve;}
      })];
      Promise.allSettled(tasks).then(() => setTimeout(endIntro, Math.max(0,2100-(performance.now()-started))));
      setTimeout(endIntro,3000);
      $('.intro-skip', intro).addEventListener('click',endIntro);
      document.addEventListener('keydown',event=>{if(event.key==='Escape')endIntro();});
    }
  }
  $$('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());
  document.fonts.ready.then(measure);
  applyMotion();
})();
