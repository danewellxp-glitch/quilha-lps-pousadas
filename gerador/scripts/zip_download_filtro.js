// Igual ao zip_download.js, mas só inclui chaves que começam com um dos prefixos em KEEP
// (o IndexedDB guarda lotes antigos também). Rodar na mesma origem da coleta.
const DBN = 'qd_gm', OUT = 'fotos-gm-lote4.zip', KEEP = ['chalesbeach/', 'ilhadosanjos/'];
const db = await new Promise((res) => { const q = indexedDB.open(DBN, 1); q.onsuccess = () => res(q.result); });
const all = await new Promise(res => { const out = []; const t = db.transaction('f'); const c = t.objectStore('f').openCursor(); c.onsuccess = e => { const cur = e.target.result; if (cur) { if (KEEP.some(k => cur.key.startsWith(k))) out.push([cur.key, cur.value]); cur.continue(); } else res(out); }; });
const T = new Uint32Array(256); for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; T[n] = c >>> 0; }
const crc = u => { let c = 0xFFFFFFFF; for (let i = 0; i < u.length; i++) c = T[(c ^ u[i]) & 255] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; };
const enc = new TextEncoder(); const parts = []; const central = []; let off = 0;
for (const [name, blob] of all) {
  const data = new Uint8Array(await blob.arrayBuffer()); const nm = enc.encode(name); const c = crc(data);
  const h = new DataView(new ArrayBuffer(30)); h.setUint32(0, 0x04034b50, true); h.setUint16(4, 20, true); h.setUint16(6, 0x800, true); h.setUint32(14, c, true); h.setUint32(18, data.length, true); h.setUint32(22, data.length, true); h.setUint16(26, nm.length, true);
  parts.push(h.buffer, nm, data);
  const ce = new DataView(new ArrayBuffer(46)); ce.setUint32(0, 0x02014b50, true); ce.setUint16(4, 20, true); ce.setUint16(6, 20, true); ce.setUint16(8, 0x800, true); ce.setUint32(16, c, true); ce.setUint32(20, data.length, true); ce.setUint32(24, data.length, true); ce.setUint16(28, nm.length, true); ce.setUint32(42, off, true);
  central.push(ce.buffer, nm); off += 30 + nm.length + data.length;
}
let csize = 0; central.forEach(b => csize += b.byteLength);
const e = new DataView(new ArrayBuffer(22)); e.setUint32(0, 0x06054b50, true); e.setUint16(8, all.length, true); e.setUint16(10, all.length, true); e.setUint32(12, csize, true); e.setUint32(16, off, true);
const zip = new Blob([...parts, ...central, e.buffer], { type: 'application/zip' });
const a = document.createElement('a'); a.href = URL.createObjectURL(zip); a.download = OUT; document.body.appendChild(a); a.click();
'files ' + all.length + ' MB ' + (zip.size / 1048576).toFixed(1)
