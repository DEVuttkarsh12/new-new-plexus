'use strict';
(() => {
  const $ = (s, root=document) => root.querySelector(s);
  const $$ = (s, root=document) => [...root.querySelectorAll(s)];
  const menuButton=$('.menu-button'), menu=$('.mobile-nav');
  function closeMenu(){if(!menu)return;menu.hidden=true;menuButton.setAttribute('aria-expanded','false');menuButton.setAttribute('aria-label','Open menu');document.body.classList.remove('nav-open')}
  menuButton?.addEventListener('click',()=>{let open=menu.hidden;menu.hidden=!open;menuButton.setAttribute('aria-expanded',String(open));menuButton.setAttribute('aria-label',open?'Close menu':'Open menu');document.body.classList.toggle('nav-open',open)});
  $$('.mobile-nav a').forEach(a=>a.addEventListener('click',closeMenu));
  document.addEventListener('keydown',ev=>{if(ev.key==='Escape')closeMenu()});
  matchMedia('(min-width:901px)').addEventListener('change',ev=>{if(ev.matches)closeMenu()});

  const video=$('.hero-video');
  if(video&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
    const start=()=>video.play().then(()=>video.classList.add('playing')).catch(()=>{});
    new IntersectionObserver(entries=>{if(entries[0].isIntersecting&&!document.hidden)start();else video.pause()},{threshold:.15}).observe(video);
    document.addEventListener('visibilitychange',()=>{if(document.hidden)video.pause();else if(video.getBoundingClientRect().top<innerHeight)start()});
  }

  const cards=$$('[data-project]'), type=$('#type-filter'), stage=$('#stage-filter'), search=$('#project-search'), count=$('.results-count');
  if(cards.length&&type&&stage&&search){
    const params=new URLSearchParams(location.search);let requested=params.get('type');if(requested&&[...type.options].some(o=>o.value===requested||o.textContent===requested))type.value=requested;
    function filter(){const text=search.value.trim().toLowerCase();let visible=0;cards.forEach(card=>{const yes=(type.value==='all'||card.dataset.type===type.value)&&(stage.value==='all'||card.dataset.stage===stage.value)&&(!text||card.dataset.search.includes(text));card.hidden=!yes;if(yes)visible++});count.textContent=`${visible} project profile${visible===1?'':'s'}`;$('.no-results').hidden=visible!==0}
    [type,stage,search].forEach(el=>el.addEventListener(el===search?'input':'change',filter));$('#clear-filters').addEventListener('click',()=>{type.value='all';stage.value='all';search.value='';history.replaceState({},'',location.pathname);filter()});filter();
  }

  $$('[data-mail-form]').forEach(form=>form.addEventListener('submit',ev=>{
    ev.preventDefault();if(!form.reportValidity())return;
    const data=new FormData(form);if(data.get('website'))return;
    const subject=form.dataset.subject||'Plexus enquiry';const lines=[...data.entries()].filter(([key])=>key!=='website'&&key!=='consent').map(([key,value])=>`${key.replaceAll('_',' ').replace(/\b\w/g,c=>c.toUpperCase())}: ${value}`);
    const body=`${lines.join('\n')}\n\nPlease attach any supporting documents before sending.\n\nSent from the Plexus website preview.`;
    const href=`mailto:info@plexusdevelopmentgroup.ca?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    $('.form-status',form).textContent='Your email app is opening. Review the draft, attach any documents, and send it to complete your enquiry.';
    location.href=href;
  }));

  const query=$('#site-query'), results=$('.search-results');
  if(query&&results){
    fetch('/search-index.json').then(response=>response.json()).then(entries=>{
      const params=new URLSearchParams(location.search);query.value=params.get('q')||'';
      const draw=()=>{
        const term=query.value.trim().toLowerCase();
        const matching=term?entries.filter(item=>(item.title+' '+item.description).toLowerCase().includes(term)):entries.slice(0,8);
        results.replaceChildren(...matching.map(item=>{
          const link=document.createElement('a'), title=document.createElement('strong'), text=document.createElement('span');
          link.href=item.url;title.textContent=item.title;text.textContent=item.description;
          link.append(title,text);return link;
        }));
        $('.search-count').textContent=term?`${matching.length} result${matching.length===1?'':'s'}`:'Suggested pages';
      };
      query.addEventListener('input',draw);draw();
    }).catch(()=>{$('.search-count').textContent='Search is temporarily unavailable.'});
  }
})();
