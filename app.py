from playwright.sync_api import sync_playwright
from flask import Flask
import json
import time


def my_function(x):
    return 5 * x


def scrap():
    items = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.ergodotisi.com/en/SearchResults.aspx")

        i = 0
        # while i < 15:
        #     page.mouse.wheel(0, 4000)
        #     page.locator("text=More Job Posts...").click()
        #     i = i + 1

        tr = page.query_selector_all(".dxdvItem")
        # print(len(tr))
        for dt in tr:
            if ("today" in dt.query_selector_all("p")[3].inner_text()):
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
        # print(len(items))
        # for item in items:
        #     print(item['title'] + "-" + item['url'])

        browser.close()
    return items


app = Flask(__name__)


@app.route('/')
def home():
    # for item in items:
    #     print(item['title'] + "-" + item['url'])
    # data = {"Page": "home", "Data": scrap(), "Timestamp": time.time()}
    json_dump = json.dumps(scrap())
    return json_dump
    # return render_template("index.html")


app.run(debug=True)
