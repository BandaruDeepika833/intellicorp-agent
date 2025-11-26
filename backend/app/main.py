from fastapi import FastAPI
from pydantic import BaseModel

from .researcher import research_company
from .planner import generate_account_plan
from .storage import Storage
from .llm_client import ask_llm

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
storage = Storage("data")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_sessions = {}

class ChatRequest(BaseModel):
    user_id: str
    message: str


# ======================================================
# USER BEHAVIOR CLASSIFICATION
# ======================================================
async def classify_message(msg: str):
    text = msg.lower().strip()

    # Confused User
    if text in ["idk", "i dont know", "not sure", "help", "confused"]:
        reply = await ask_llm(
            f"The user is confused. Give simple guidance. User said: '{msg}'"
        )
        return {"type": "confused", "response": reply}

    # Efficient User
    if any(w in text for w in ["quick", "fast", "short"]):
        reply = await ask_llm(
            f"User wants fast results. Reply concisely. User said: '{msg}'"
        )
        return {"type": "efficient", "response": reply}

    # Chatty User
    if any(w in text for w in ["hi", "hello", "lol", "haha", "bro", "how are you"]):
        reply = await ask_llm(
            f"User is chatty. Be friendly but guide them to the right format. User said: '{msg}'"
        )
        return {"type": "chatty", "response": reply}

    # Edge Case User
    if len(text) < 3 or text.isnumeric() or "asdf" in text:
        reply = await ask_llm(
            f"Invalid input. Politely guide them. User said: '{msg}'"
        )
        return {"type": "edgecase", "response": reply}

    return {"type": "normal"}


# ======================================================
# CHAT ENDPOINT
# ======================================================
@app.post("/chat")
async def chat(request: ChatRequest):
    msg = request.message
    user = request.user_id

    if user not in user_sessions:
        user_sessions[user] = {
            "company": None,
            "summary": None,
            "plan": None
        }

    session = user_sessions[user]

    # 1) Detect user type
    behavior = await classify_message(msg)
    if behavior["type"] != "normal":
        return behavior

    msg = msg.lower().strip()

    # ========== RESEARCH ==========
    if msg.startswith("research:"):
        company = msg.replace("research:", "").strip()

        session["company"] = company

        findings = await research_company(company)
        session["summary"] = findings["summary"]

        plan = await generate_account_plan(findings["summary"])
        session["plan"] = plan

        storage.save(user, company, plan)

        return {
            "mode": "research",
            "company": company,
            "summary": findings["summary"],
            "plan": plan
        }

    # ========== UPDATE ==========
    if msg.startswith("update:"):
        if session["plan"] is None:
            return {"error": "Run Research first."}

        try:
            section, new_text = msg.replace("update:", "").split("=", 1)
        except:
            return {"error": "Use format: update: risks=new value"}

        section = section.strip()
        new_text = new_text.strip()

        matched_key = None
        for key in session["plan"].keys():
            if section.lower() in key.lower():
                matched_key = key
                break

        if matched_key is None:
            return {"error": f"No matching section for '{section}'"}

        session["plan"][matched_key] = new_text
        storage.save(user, session["company"], session["plan"])

        return {
            "mode": "update",
            "status": f"Updated {matched_key}",
            "plan": session["plan"]
        }

    # ========== DEFAULT ==========
    fallback = await ask_llm(
        f"User asked: '{msg}'. Explain how to use Research: <company> or Update: <section>=<text>."
    )
    return {"response": fallback}


@app.get("/plan/{user_id}/{company}")
def load_plan(user_id: str, company: str):
    return storage.load(user_id, company)


