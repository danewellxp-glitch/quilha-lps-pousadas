// Coleta fotos do Google Maps de UMA pousada (rodar na aba do Maps já aberta no local, ?hl=pt-BR).
// Troque SLUG pelo slug da pousada. Guarda no IndexedDB 'qd_gm' (origem google.com). Progresso: JSON.stringify(window.__gm)
// ATENÇÃO: o Maps também carrega miniaturas de "hotéis semelhantes"; elas entram na coleta e precisam ser descartadas na escolha.
(async (SLUG, MINPX = 1500) => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  window.__gm = { slug: SLUG, status: 'opening', n: 0, kept: 0 };
  const btn = [...document.querySelectorAll('button[aria-label]')].find(b => /^(Photo of|Foto de|Fotos de)/i.test(b.getAttribute('aria-label')));
  if (btn) { btn.click(); await sleep(3500); }
  window.__gm.status = 'scrolling';
  for (let i = 0; i < 30; i++) {
    const sc = [...document.querySelectorAll('div')].filter(d => d.scrollHeight > d.clientHeight + 200 && /(auto|scroll)/.test(getComputedStyle(d).overflowY) && d.getBoundingClientRect().left < 60);
    sc.forEach(s => s.scrollTop += 1600); await sleep(650);
  }
  const urls = new Set();
  document.querySelectorAll('[style*="googleusercontent"], img[src*="googleusercontent"]').forEach(e => { const m = (e.getAttribute('style') || '').match(/url\("?([^")]+)/); const u = m ? m[1] : e.src; if (u && !/\/a\/|\/a-\/|\/proxy\//.test(u)) urls.add(u.split('=')[0]); });
  const db = await new Promise((res, rej) => { const q = indexedDB.open('qd_gm', 1); q.onupgradeneeded = () => q.result.createObjectStore('f'); q.onsuccess = () => res(q.result); q.onerror = () => rej(q.error); });
  const put = (k, v) => new Promise((res, rej) => { const t = db.transaction('f', 'readwrite'); t.objectStore('f').put(v, k); t.oncomplete = res; t.onerror = () => rej(t.error); });
  window.__gm.status = 'fetching'; window.__gm.total = urls.size;
  let i = 0;
  for (const u of urls) {
    i++; window.__gm.n = i;
    try {
      const im = new Image(); im.src = u + '=s0'; await im.decode();
      const w = im.naturalWidth, h = im.naturalHeight;
      if (Math.max(w, h) < MINPX) continue;
      const b = await (await fetch(u + '=s2400')).blob();
      await put(`${SLUG}/gm/gm_${String(i).padStart(3, '0')}_${w}x${h}.jpg`, b);
      window.__gm.kept++;
    } catch (e) { }
  }
  window.__gm.status = 'done';
})('SLUG'); 'started';
