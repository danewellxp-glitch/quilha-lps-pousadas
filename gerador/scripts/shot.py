import sys, asyncio
from playwright.async_api import async_playwright
async def main(path, out, w=1440, h=900, full=True, scrolls=True):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.goto('file://' + path)
        await pg.wait_for_timeout(2500)
        if scrolls:
            H = await pg.evaluate('document.body.scrollHeight')
            for y in range(0, H, 400):
                await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(120)
            await pg.evaluate('document.querySelectorAll("[data-reveal]").forEach(e=>e.classList.add("in"))')
            await pg.evaluate('window.scrollTo(0,0)'); await pg.wait_for_timeout(1500)
        await pg.screenshot(path=out, full_page=full)
        await b.close()
w = int(sys.argv[3]) if len(sys.argv) > 3 else 1440
asyncio.run(main(sys.argv[1], sys.argv[2], w=w, h=900 if w > 600 else 844))
