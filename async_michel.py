from playwright.async_api import async_playwright
import asyncio


async def scrap():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.ergodotisi.com/en/SearchResults.aspx")
        items = []
        i = 0
        # while i < 15:
        #     page.mouse.wheel(0, 4000)
        #     page.locator("text=More Job Posts...").click()
        #     i = i + 1

        tr = page.query_selector_all(".dxdvItem")
        # print(len(tr))
        for dt in tr:
            if ("yesterday" in dt.query_selector_all("p")[3].inner_text()):
                item = {
                    "title": dt.query_selector_all("a")[0].inner_text(),
                    "url": dt.query_selector_all("a")[1].inner_text(),
                    "city": dt.query_selector_all("p")[0].inner_text(),
                    "cmpy": dt.query_selector_all("p")[1].inner_text(),
                    "view": dt.query_selector_all("p")[2].inner_text(),
                    "date": dt.query_selector_all("p")[3].inner_text(),
                    "expire": dt.query_selector_all("p")[4].inner_text(),
                    "typeofjob": dt.query_selector_all("p")[5].inner_text()
                }
                items.append(item)
        print(len(items))
        for item in items:
            print(item['title'] + "-" + item['url'])

        browser.close()


def main():
    scrap()


if __name__ == '__main__':
    main()
