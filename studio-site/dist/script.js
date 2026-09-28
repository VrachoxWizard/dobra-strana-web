(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Naslov: svaka riječ ulazi zasebno, naglasak u <em> ostaje cjelina.
  const h1 = document.querySelector('[data-split]');
  if (h1) {
    let i = 0;
    const word = (content) => { const s = document.createElement('span'); s.className = 'w'; s.style.setProperty('--i', i++); s.append(content); return s; };
    [...h1.childNodes].forEach((node) => {
      if (node.nodeType !== 3) return node.replaceWith(word(node.cloneNode(true)));
      const frag = document.createDocumentFragment();
      node.textContent.split(/(\s+)/).forEach((p) => frag.append(p.trim() ? word(p) : p));
      node.replaceWith(frag);
    });
  }
  requestAnimationFrame(() => requestAnimationFrame(() => document.documentElement.classList.add('is-loaded')));

  // Zaglavlje se sužava nakon početka skrolanja.
  const header = document.getElementById('zaglavlje');
  const onScroll = () => header.classList.toggle('is-scrolled', scrollY > 12);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Paralaksa snimki u heroju prati miš (samo precizni pokazivač, bez smanjenog pokreta).
  const hero = document.querySelector('.hero');
  const stage = document.querySelector('.hero-stage');
  if (reduce || !hero || !stage || !matchMedia('(pointer: fine)').matches) return;
  hero.addEventListener('pointermove', (e) => {
    const r = hero.getBoundingClientRect();
    stage.style.setProperty('--mx', ((e.clientX - r.left) / r.width - .5).toFixed(3));
    stage.style.setProperty('--my', ((e.clientY - r.top) / r.height - .5).toFixed(3));
  });
  hero.addEventListener('pointerleave', () => { stage.style.setProperty('--mx', 0); stage.style.setProperty('--my', 0); });
})();
