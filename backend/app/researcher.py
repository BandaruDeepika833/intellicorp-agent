import requests
from bs4 import BeautifulSoup
from .llm_client import ask_llm

async def search_wikipedia(company):
    try:
        url = f"https://en.wikipedia.org/wiki/{company.replace(' ', '_')}"
        html = requests.get(url, timeout=5).text
        soup = BeautifulSoup(html, "html.parser")
        paragraphs = soup.find_all("p")
        return paragraphs[0].text.strip()
    except:
        return "No direct Wikipedia data found."

async def search_news(company):
    return f"Latest business news shows {company} working on digital transformation."

async def research_company(company):
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
        "news_raw": news
    
    }
