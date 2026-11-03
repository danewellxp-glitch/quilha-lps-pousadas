// Coleta TUDO de uma pousada no Google Maps numa chamada (rodar na aba do Maps, ?hl=pt-BR):
// info (nome, nota, endereço, telefone, horários, site), comodidades, avaliações e fotos (>=1500px, =s2400).
// Guarda no IndexedDB 'qd_gm' da origem: <SLUG>/info.json e <SLUG>/gm/*.jpg. Progresso: JSON.stringify(window.__st)
// Se a aba estiver numa lista de resultados, clica no card cujo nome contém NAME.
(async (SLUG, NAME, MINPX = 1500) => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const st = window.__st = { slug: SLUG, status: 'start', rev: 0, n: 0, kept: 0 };
  const main = () => [...document.querySelectorAll('div[role=main]')].pop();
  const card = [...document.querySelectorAll('a.hfpxzc')].find(a => (a.getAttribute('aria-label') || '').toLowerCase().includes(NAME.toLowerCase()));
  if (card) { card.click(); await sleep(4000); }
  const tab = re => [...main().querySelectorAll('button[role="tab"]')].find(b => re.test(b.textContent));
  const info = { slug: SLUG };
  const tx = main().innerText;
  info.name = main().querySelector('h1')?.textContent?.trim();
  info.rating = (tx.match(/\n(\d,\d)\n\((\d[\d.]*)\)/) || []).slice(1).join(' ');
  info.kind = (tx.match(/\)·([^\n]+)/) || [])[1];
  info.address = (tx.split('\n').find(l => / - SC|SC, \d{5}/.test(l)) || '').trim();
  info.phone = (tx.match(/\(\d\d\) \d{4,5}-\d{4}/) || [])[0];
  info.checkin = (tx.match(/check-in: ([\d:]+)/i) || [])[1];
  info.checkout = (tx.match(/check-out: ([\d:]+)/i) || [])[1];
  info.no_site = /Adicionar website/.test(tx);
  info.site = [...main().querySelectorAll('a[data-item-id="authority"]')].map(a => a.href)[0] || '';
  info.unclaimed = /Reivindicar esta empresa/.test(tx);
  info.prices = (tx.match(/R\$ ?\d+/) || [])[0] || '';
  let t = tab(/Sobre/);
  if (t) { t.click(); await sleep(2500); info.amen = [...main().querySelectorAll('[aria-label]')].map(e => e.getAttribute('aria-label')).filter(x => / dispon/i.test(x)); info.about = main().innerText.slice(0, 1500); }
  st.status = 'reviews';
  t = tab(/Avalia/);
  if (t) {
    t.click(); await sleep(2500);
    for (let i = 0; i < 16; i++) { const sc = [...document.querySelectorAll('div')].filter(d => d.scrollHeight > d.clientHeight + 200 && /(auto|scroll)/.test(getComputedStyle(d).overflowY) && d.getBoundingClientRect().left < 220); sc.forEach(s => s.scrollTop += 2500); await sleep(800); }
    document.querySelectorAll('button.w8nwRe').forEach(b => b.click()); await sleep(800);
    info.reviews = [...document.querySelectorAll('div.jftiEf')].map(c => ({
      a: c.querySelector('.d4r55')?.textContent?.trim(), s: (c.querySelector('.kvMYJc')?.getAttribute('aria-label') || '').slice(0, 1),
      w: c.querySelector('.rsqaWe')?.textContent?.trim(), t: (c.querySelector('.wiI7pd')?.textContent || '').trim().replace(/\s+/g, ' ')
    })).filter(r => r.t);
    st.rev = info.reviews.length;
  }
  const db = await new Promise((res, rej) => { const q = indexedDB.open('qd_gm', 1); q.onupgradeneeded = () => q.result.createObjectStore('f'); q.onsuccess = () => res(q.result); q.onerror = () => rej(q.error); });
  const put = (k, v) => new Promise((res, rej) => { const x = db.transaction('f', 'readwrite'); x.objectStore('f').put(v, k); x.oncomplete = res; x.onerror = () => rej(x.error); });
  await put(`${SLUG}/info.json`, new Blob([JSON.stringify(info, null, 1)], { type: 'application/json' }));
  st.status = 'photos';
  t = tab(/Visão/); if (t) { t.click(); await sleep(2000); }
  const btn = [...document.querySelectorAll('button[aria-label]')].find(b => /^(Photo of|Foto de|Fotos de)/i.test(b.getAttribute('aria-label')));
  if (btn) { btn.click(); await sleep(3500); }
  for (let i = 0; i < 30; i++) { const sc = [...document.querySelectorAll('div')].filter(d => d.scrollHeight > d.clientHeight + 200 && /(auto|scroll)/.test(getComputedStyle(d).overflowY) && d.getBoundingClientRect().left < 220); sc.forEach(s => s.scrollTop += 1600); await sleep(650); }
  const urls = new Set();
  document.querySelectorAll('[style*="googleusercontent"], img[src*="googleusercontent"]').forEach(e => { const m = (e.getAttribute('style') || '').match(/url\("?([^")]+)/); const u = m ? m[1] : e.src; if (u && !/\/a\/|\/a-\/|\/proxy\//.test(u)) urls.add(u.split('=')[0]); });
  st.total = urls.size; let i = 0;
  for (const u of urls) {
    i++; st.n = i;
    try {
      const im = new Image(); im.src = u + '=s0'; await im.decode();
      const w = im.naturalWidth, h = im.naturalHeight;
      if (Math.max(w, h) < MINPX) continue;
      const b = await (await fetch(u + '=s2400')).blob();
      await put(`${SLUG}/gm/gm_${String(i).padStart(3, '0')}_${w}x${h}.jpg`, b);
      st.kept++;
    } catch (e) { }
  }
  st.status = 'done';
})
