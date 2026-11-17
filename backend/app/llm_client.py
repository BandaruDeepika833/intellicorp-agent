import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"
REQUEST_TIMEOUT = 60.0


async def ask_llm(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
    }

    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
        response = await client.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()

    return data.get("response", "")
