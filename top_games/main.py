from fastapi import FastAPI
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def main():
    return {"Hello": "World"}


@app.get("/title")
async def get_title():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(
            "https://store.steampowered.com/charts/mostplayed", timeout=60000
        )
        title = await page.query_selector("title")
        res = await title.inner_text()
        return {"Title": f"{res}"}


@app.get("/top_games")
async def get_games():

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(
            "https://store.steampowered.com/charts/mostplayed", timeout=60000
        )
        table = page.locator(
            '//*[@id="page_root"]/div[3]/div/div/div/div[3]/table/tbody'
        )
        result = await table.inner_html()
        await browser.close()

        soup = BeautifulSoup(result, "html.parser")

        titles = soup.find_all("div", {"_1n_4-zvf0n4aqGEksbgW9N"})
        title_texts = [text.get_text() for text in titles]

        current_pop = soup.find_all("td", {"_3L0CDDIUaOKTGfqdpqmjcy"})
        current_pop_text = [text.get_text() for text in current_pop]

        daily_top_pop = soup.find_all("td", {"yJB7DYKsuTG2AYhJdWTIk"})
        daily_top_pop_text = [text.get_text() for text in daily_top_pop]

        finals = []
        for t, cp, tp in zip(title_texts, current_pop_text, daily_top_pop_text):
            finals.append(
                {
                    f"{t}": {
                        "Current Player Count": f"{cp}",
                        "Top Daily Player Count": f"{tp}",
                    }
                }
            )

        return JSONResponse(content=finals, status_code=200)
