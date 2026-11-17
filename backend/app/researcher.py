import httpx
from bs4 import BeautifulSoup

from .llm_client import ask_llm


async def search_wikipedia(company: str) -> str:
    url = f"https://en.wikipedia.org/wiki/{company.replace(' ', '_')}"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
    except httpx.HTTPError:
        return "No direct Wikipedia data found."

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    if not paragraphs:
        return "No direct Wikipedia data found."

    return paragraphs[0].text.strip()


async def search_news(company: str) -> str:
    return f"Latest business news shows {company} working on digital transformation."


async def research_company(company: str) -> dict:
    wiki = await search_wikipedia(company)
    news = await search_news(company)

    prompt = f"""
Combine this data into a summarized company research report:

Wikipedia:
{wiki}

News:
{news}

Identify conflicts. If any conflicts exist say:
"I'm noticing conflicting information about X. Should I dig deeper?"

Then provide a clean summary.
"""

    summary = await ask_llm(prompt)

    return {
        "company": company,
        "summary": summary,
        "wiki_raw": wiki,
        "news_raw": news,
    }
