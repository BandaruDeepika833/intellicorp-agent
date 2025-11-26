#Intellicorp-Agent — Company Research Assistant (Eightfold.ai Assignment)

This project is built for the Eightfold.ai – AI Agent Building Assignment under:

#Problem Statement 1: Company Research Assistant (Account Plan Generator)

The goal is to create a conversational AI agent capable of researching companies, synthesizing insights, generating account plans, and supporting multi-turn updates. 


##🚀 Overview

Intellicorp-Agent is an AI-powered conversational system that helps users:

✔ Research any company via natural chat
✔ Gather information from multiple sources

Wikipedia lookup 

researcher

News stub generator 

researcher

LLM-driven synthesis

✔ Detect conflicting information & ask user confirmation
✔ Generate complete Enterprise Account Plans
✔ Allow updating individual sections of the plan
✔ Save and load plans for each user
✔ Adapt responses based on different user personas

The agent works through a frontend chat UI (HTML/JS) and a FastAPI backend powered by a local LLM (Llama via Ollama).

##🧠 Key Features
1. Company Research Pipeline

When the user enters:

research: <company-name>


The agent:

Scrapes Wikipedia summary using requests + BeautifulSoup

Adds latest news context (stub for extension)

Sends merged data to the LLM for synthesis

Handles conflict detection ("I'm noticing conflicting information…")

Backend implementation:

Wikipedia + news: research_company() 

researcher

LLM call: ask_llm() 

llm_client

2. Enterprise Account Plan Generator

The plan is generated via LLM with strictly enforced JSON format:
Sections include:

Company Overview

Key Opportunities

Risks & Challenges

Recommended Strategy

Tech Adoption Insights

Partnership Potential

Plan generator implementation: generate_account_plan() 

planner

Example generated plans:

Infosys (JSON) 

TCS (JSON) 


3. Updating Plan Sections

Users may update plan sections dynamically:

update: risks = new updated risks section


Backend parses update requests, finds matching keys, updates JSON, and saves changes.

Implementation: Update logic inside FastAPI route in main.py under /chat. 

main

Storage handled by: storage.py (save & load JSON) 

storage

4. User Persona Detection

The agent automatically identifies user types:

Confused → gentle guidance

Efficient → short & direct replies

Chatty → friendly but guided

Edge Case → handle invalid inputs

Logic in classify_message() inside backend. 

main

5. Frontend Chat UI

Simple responsive chat interface built using:

index.html (chat layout) 

index

styles.css (styling) 

styles

script.js (API integration) 

script

The UI sends queries to:

POST http://127.0.0.1:8000/chat

🏗 System Architecture
                ┌────────────────────────────┐
                │        Frontend UI         │
                │  (HTML + JS Chat Window)   │
                └─────────────┬──────────────┘
                              │
                              ▼
                ┌────────────────────────────┐
                │        FastAPI Backend     │
                │        (main.py)           │
                ├─────────────┬──────────────┤
                │             │               │
                ▼             ▼               ▼
      ┌────────────────┐  ┌────────────┐  ┌────────────────┐
      │ Researcher     │  │ Planner    │  │ Storage        │
      │ (Wikipedia +   │  │ (LLM JSON  │  │ Save/Load      │
      │ News + LLM)    │  │ generator) │  │ Plans          │
      └────────────────┘  └────────────┘  └────────────────┘
                              │
                              ▼
                      ┌────────────┐
                      │   LLM      │
                      │ (Ollama)   │
                      └────────────┘

##⚙️ Tech Stack
Backend

Python

FastAPI 

Requests, BeautifulSoup4

Ollama (local Llama model)

JSON-based storage

Frontend

HTML, CSS, JavaScript

Fetch API for chat

🛠 Installation & Setup
1. Clone the Repo
git clone https://github.com/BandaruDeepika833/intellicorp-agent
cd intellicorp-agent

2. Install Dependencies
pip install -r requirements.txt


(Dependencies include FastAPI, Uvicorn, Requests, BeautifulSoup4.) 


3. Start the Backend
uvicorn backend.app.main:app --reload


Server will run at:

http://127.0.0.1:8000

4. Run Frontend

Open frontend/index.html in any browser.

##🎯 How to Use the Agent
Start a research query
research: infosys

Update a specific section
update: risks = updated risks section text

Load previously saved plan (optional)
GET /plan/<user_id>/<company>

Try different personas

“idk what to do” → confused

“give quick summary” → efficient

“hi hello haha” → chatty

“asdf” or “23” → edge case

##🔍 Design Decisions
1. LLM Orchestration

LLM used only for:

Summary synthesis

JSON account plan generation

Persona-based replies

All control logic handled in Python for reliability.

2. Conflict Detection

Before generating the summary, LLM is asked to explicitly check for conflicts (required by assignment). 


3. Modular Architecture

Separated into:

llm_client.py → LLM wrapper

researcher.py → Data gathering

planner.py → Structured plan generation

storage.py → State persistence

main.py → FastAPI routes + logic

4. Lightweight Frontend

Simple JS-based chat avoids complexity and keeps focus on agent behavior.

##📦 Repository Structure
intellicorp-agent/
│
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI app logic
│   │   ├── researcher.py      # Wikipedia + news logic
│   │   ├── planner.py         # JSON account plan generator
│   │   ├── storage.py         # Save/load JSON account plans
│   │   ├── llm_client.py      # LLM communication (Ollama)
│   │   ├── utils.py           # Helper functions (if any)
│   │   └── __pycache__/       # Python cache files
│   │
│   ├── data/
│   │   ├── *.json             # Saved account plan files
│
├── frontend/
│   ├── index.html             # Chat UI
│   ├── script.js              # Frontend logic + API calls
│   └── styles.css             # Styling
│
├── requirements.txt           # Python dependencies
└── run.sh                     # Launch script (optional)


🎥 Demo Video Instructions

Per the assignment guidelines: 

✔ Show agent researching a company
✔ Show conflict detection
✔ Show persona handling
✔ Show updating account plan sections
✔ Show architecture briefly (verbally)
✔ Do NOT use slides
✔ Keep under 10 minutes

🏁 Conclusion

Intellicorp-Agent fulfills all requirements for the Eightfold AI assignment:

✔ Agentic behavior
✔ Conversational adaptability
✔ Multi-source research
✔ Account plan synthesis
✔ Section updates
✔ Persona handling
✔ Local LLM + FastAPI backend
✔ Frontend chat interface
✔ Storage & session memory

