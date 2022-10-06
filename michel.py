from playwright.sync_api import sync_playwright


def scrap():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.ergodotisi.com/en/SearchResults.aspx")
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

    # ***********************************************************************************
    # data = []
    # for dt in tr:
    #     data.append(dt.query_selector_all("p")[3].inner_text())

    # print(len(data))
    # page.mouse.wheel(0, 4000)
    # page.locator("text=More Job Posts...").click()
    # tr2 = page.query_selector_all(".dxdvItem")

    # for dt2 in tr2:
    #     data.append(dt2.query_selector_all("p")[3].inner_text())

    # print(len(data))
    # data = []

    # while ("yesterday" in page.query_selector(".dxdvItem").query_selector_all("p")[3].inner_text()):
    #     #     print(page.query_selector(
    #     #         ".dxdvItem").query_selector_all("p")[3].inner_text())
    #     #     page.mouse.wheel(0, 4000)
    #     #     page.locator("text=More Job Posts...").click()
    #     listing = page.query_selector_all(".dxdvItem")
    #     for item in listing:
    #         # print(item.query_selector_all("p")[3].inner_text())
    #         if ("yesterday" in item.query_selector_all("p")[3].inner_text()):
    #             print(item.query_selector_all("p")[2].inner_text())
    #             d = {
    #                 "city": item.query_selector_all("p")[0].inner_text()
    #             }
    #             data.append(item)
    #             page.mouse.wheel(0, 4000)
    #             page.locator("text=More Job Posts...").click()
    # print(listing.query_selector_all("p")[3].inner_text())
    # print(page.locator("text=posted yesterday"))
    # print(page.query_selector(search_str).inner_html)
    # while (page.locator("text=posted yesterday")):
    # print(len(data))
    # page.wait_for_timeout(2000)


if __name__ == '__main__':
    main()

# from playwright.sync_api import Playwright, sync_playwright, expect
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     # Open new page
#     page = context.new_page()
#     # Go to https://www.ergodotisi.com/en/SearchResults.aspx
#     page.goto("https://www.ergodotisi.com/en/SearchResults.aspx")
#     # Click text=More Job Posts...
#     page.locator("text=More Job Posts...").click()
#     # Click text=Οχι
#     page.locator("text=Οχι").click()
#     # Click text=More Job Posts...
#     page.locator("text=More Job Posts...").click()
#     # Click text=More Job Posts...
#     page.locator("text=More Job Posts...").click()
#     # ---------------------
#     context.close()
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)
