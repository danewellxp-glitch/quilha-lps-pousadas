// Coleta fotos HD de um perfil do Instagram (rodar com javascript_tool na aba do perfil logado: https://www.instagram.com/<user>/)
// Guarda os blobs no IndexedDB 'qd_ig' (origem instagram.com). Progresso: JSON.stringify(window.__qd)
// MINPX: lado mínimo aceito (1080 padrão; use 720 para perfis antigos com poucas fotos). MAXPOSTS: limite de posts.
window.scrollTo(0,0); (async (MINPX = 1080, MAXPOSTS = 120) => {
  const USER = location.pathname.split('/').filter(Boolean)[0];
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const A='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
  const sid=sc=>{let n=0n; for(const c of sc) n=n*64n+BigInt(A.indexOf(c)); return n.toString();};
  const csrf=(document.cookie.match(/csrftoken=([^;]+)/)||[])[1];
  const H={'X-IG-App-ID':'936619743392459','X-CSRFToken':csrf,'X-Requested-With':'XMLHttpRequest'};
  const db = await new Promise((res, rej) => { const q = indexedDB.open('qd_ig', 1); q.onupgradeneeded = () => q.result.createObjectStore('f'); q.onsuccess = () => res(q.result); q.onerror = () => rej(q.error); });
  const put = (k, v) => new Promise((res, rej) => { const t = db.transaction('f', 'readwrite'); t.objectStore('f').put(v, k); t.oncomplete = res; t.onerror = () => rej(t.error); });
  window.__qd = { user: USER, status: 'scrolling', posts: 0, done: 0, imgs: 0, skipped: 0, err: 0 };
  const codes = new Set();
  for (let s = 0; s < 30; s++) { if (codes.size >= MAXPOSTS) break;
    document.querySelectorAll('main a[href*="/p/"]').forEach(a => { const h = a.getAttribute('href'); if (h.startsWith('/' + USER + '/p/') || h.startsWith('/p/')) { const m = h.match(/\/p\/([^/]+)/); if (m) codes.add(m[1]); } });
    window.scrollBy(0, 1400); await sleep(1600);
  }
  window.__qd.posts = codes.size; window.__qd.status = 'fetching';
  const meta = [];
  for (const sc of codes) {
    try {
      const r = await fetch('/api/v1/media/' + sid(sc) + '/info/', { credentials: 'include', headers: H });
      if (r.status === 429) { window.__qd.status = 'ratelimited'; await sleep(30000); }
      const j = await r.json(); const it = j.items[0];
      const cap = (it.caption && it.caption.text || '').slice(0, 300);
      const list = it.carousel_media ? it.carousel_media : [it];
      let k = 0;
      for (const c of list) {
        k++;
        if (c.media_type !== 1 || !c.image_versions2) { window.__qd.skipped++; continue; }
        const best = c.image_versions2.candidates.slice().sort((a, b) => b.width - a.width)[0];
        if (best.width < MINPX && best.height < MINPX) { window.__qd.skipped++; continue; }
        const b = await (await fetch(best.url)).blob();
        const name = `${USER}/ig/${sc}_${String(k).padStart(2,'0')}.jpg`;
        await put(name, b);
        meta.push({ name, sc, w: best.width, h: best.height, likes: it.like_count, taken: it.taken_at, cap });
        window.__qd.imgs++;
      }
    } catch (e) { window.__qd.err++; }
    window.__qd.done++;
    await sleep(1200);
  }
  await put(`${USER}/ig/_meta.json`, new Blob([JSON.stringify(meta, null, 1)], { type: 'application/json' }));
  window.__qd.status = 'done';
})(); 'started';
