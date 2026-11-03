"""Teste do fluxo de reserva do template casa (home -> reservas -> checkout -> WhatsApp).
uso: python scripts/flow_test.py out/<slug>
Saída esperada: url com ?checkin=..., alert True, errs [] (o 'wa' abre chrome-error sem internet, normal)."""
import asyncio, sys, os
from playwright.async_api import async_playwright
D = os.path.abspath(sys.argv[1]) + '/'
async def main():
  async with async_playwright() as p:
    b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1440, 'height': 900})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    await pg.goto('file://' + D + 'index.html'); await pg.wait_for_timeout(800)
    await pg.fill('#bkIn', '2030-12-10'); await pg.fill('#bkOut', '2030-12-14')
    await pg.click('#bookingForm button'); await pg.wait_for_timeout(1200)
    print('url', pg.url.split('/')[-1])
    await pg.click('.room-card:nth-child(1) .pick'); await pg.wait_for_timeout(800)
    await pg.fill('input[name=name]', 'Teste'); await pg.fill('input[name=phone]', '48999999999')
    async with pg.context.expect_page() as np:
      await pg.click('button.wa')
    print('wa', (await np.value).url[:60])
    pg2 = await b.new_page(viewport={'width': 390, 'height': 844}); await pg2.goto('file://' + D + 'reservas.html'); await pg2.wait_for_timeout(500)
    await pg2.click('.room-card:nth-child(1) .pick'); await pg2.wait_for_timeout(600)
    print('alert', await pg2.evaluate("dateAlert.classList.contains('show')"))
    print('errs', errs); await b.close()
asyncio.run(main())
