// Lê as avaliações do Google Maps (rodar na aba do local com ?hl=pt-BR para vir o texto original).
// Depois leia em partes (o retorno do javascript_tool trunca ~900 chars): window.__r.slice(0,3).join('\n'), slice(3,6)...
const sleep = ms => new Promise(r => setTimeout(r, ms));
const tab = [...document.querySelectorAll('button[role="tab"]')].find(b => /Avalia|Reviews/.test(b.textContent));
if (tab) { tab.click(); await sleep(2500); }
for (let i = 0; i < 14; i++) {
  const sc = [...document.querySelectorAll('div')].filter(d => d.scrollHeight > d.clientHeight + 200 && /(auto|scroll)/.test(getComputedStyle(d).overflowY) && d.getBoundingClientRect().left < 60);
  sc.forEach(s => s.scrollTop += 2500); await sleep(900);
}
document.querySelectorAll('button.w8nwRe').forEach(b => b.click()); await sleep(800);
window.__r = [...document.querySelectorAll('div.jftiEf')].map(c => {
  const a = c.querySelector('.d4r55')?.textContent?.trim();
  const t = c.querySelector('.wiI7pd')?.textContent?.trim();
  return t ? (a + ' | ' + t.replace(/\n/g, ' ').slice(0, 300)) : null;
}).filter(Boolean);
window.__r.length
