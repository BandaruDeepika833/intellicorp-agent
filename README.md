# Intellicorp-Agent — Company Research Assistant (Eightfold.ai Assignment)

This project is built for the **Eightfold.ai – AI Agent Building Assignment** under:

### Problem Statement 1: Company Research Assistant (Account Plan Generator)

The goal of this project is to build a conversational AI agent capable of:
- Researching companies
- Synthesizing insights from multiple sources
- Generating structured account plans
- Supporting multi-turn updates
- Detecting conflicting information
- Handling different user personas

---

## Overview

Intellicorp-Agent is an intelligent research assistant that provides:
- Natural conversation–based company research
- Automatic insight generation using a local LLM (Llama via Ollama)
- JSON-based enterprise account plan creation
- Fine-grained plan section updates
- Persona-aware responses
- Full frontend + backend implementation

System Components:
- **FastAPI backend**
- **HTML/CSS/JS frontend**
- **Local LLM (Ollama)** for summarization and generation
- **JSON file storage** for saving account plans

---

## Key Features

### 1. Company Research Pipeline

Users initiate research using:

research: <company-name>


The agent:
- Scrapes Wikipedia content
- Generates lightweight “news-like” context
- Detects conflicting information between sources
- Sends merged data to the LLM for synthesis
- Returns a refined summary

Key functions:
- `research_company()`
- `ask_llm()`

---

### 2. Enterprise Account Plan Generator

The AI generates a structured JSON plan including:
- Company Overview
- Key Opportunities
- Risks & Challenges
- Recommended Strategy
- Tech Adoption Insights
- Partnership Potential

Plan creation uses:
- `generate_account_plan()`

---

### 3. Updating Plan Sections

Users can update sections after a plan is generated:

update: risks = new updated risks content


The backend:
- Identifies the correct section
- Updates that JSON field
- Saves the updated plan to `backend/data`

Handled in:
- `/chat` API route
- `storage.py`

---

### 4. User Persona Detection

The system adapts responses based on persona:
- **Confused users** → more explanation  
- **Efficient users** → short answers  
- **Chatty users** → friendly tone  
- **Edge-case users** → safe fallback  

Implemented in:
- `classify_message()` inside `main.py`

---

### 5. Frontend Chat UI

The frontend includes:
- `index.html` — chat interface  
- `styles.css` — UI styling  
- `script.js` — handles message sending & response rendering  

Messages are sent to:
POST http://127.0.0.1:8000/chat


---

## System Architecture

```text
                ┌────────────────────────────┐
                │        Frontend UI         │
                │    (HTML + JS Chat Box)    │
                └─────────────┬──────────────┘
                              │
                              ▼
                ┌────────────────────────────┐
                │        FastAPI Backend     │
                │          (main.py)         │
                ├─────────────┬──────────────┤
                │             │               │
                ▼             ▼               ▼
      ┌────────────────┐  ┌────────────┐  ┌────────────────┐
      │   Researcher   │  │   Planner  │  │    Storage     │
      │(Wikipedia +    │  │ (JSON      │  │  Save / Load   │
      │ News + LLM)    │  │  Plan)     │  │    Plans       │
      └────────────────┘  └────────────┘  └────────────────┘
                              │
                              ▼
                      ┌────────────┐
                      │    LLM     │
                      │  (Ollama)  │
                      └────────────┘

```
## Tech Stack

### Backend
- Python  
- FastAPI  
- Uvicorn  
- Requests  
- BeautifulSoup4  
- JSON storage  
- Local LLM (Ollama + Llama model)

### Frontend
- HTML  
- CSS  
- JavaScript (Fetch API)

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/BandaruDeepika833/intellicorp-agent
cd intellicorp-agent
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Run the Backend
```bash
uvicorn backend.app.main:app --reload
```
### 4. Run the Frontend

Open:
frontend/index.html

---

## How to Use

### **Research a Company**

### **Update a Plan Section**

---

## Example Personas

| Input              | Persona   |
|-------------------|-----------|
| idk what to do     | confused  |
| give quick summary | efficient |
| hi hello haha      | chatty    |
| asdf               | edge case |

---

## Design Decisions

### **1. LLM Orchestration**
- **LLM handles:** summarization, JSON plan generation, persona tone  
- **Python handles:** logic, routing, state, validation  

---

### **2. Conflict Detection**
- LLM compares sources and flags inconsistencies  
- User approves before detailed synthesis  

---

### **3. Modular Backend Architecture**
- `researcher.py` — data gathering  
- `planner.py` — JSON plan creation  
- `storage.py` — save/load  
- `main.py` — chat routing + persona detection  
- `llm_client.py` — interaction with LLM  
- `utils.py` — helpers  

---

### **4. Lightweight Frontend**
- Clean, simple chat UI  
- Easy to demonstrate and extend  

---

## Repository Structure

intellicorp-agent/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── researcher.py
│   │   ├── planner.py
│   │   ├── storage.py
│   │   ├── llm_client.py
│   │   ├── utils.py
│   │   └── __pycache__/
│   │
│   ├── data/
│   │   ├── *.json
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── styles.css
│
├── requirements.txt
└── run.sh

---

## Conclusion

Intellicorp-Agent fulfills the key requirements of the **Eightfold AI Company Research Assistant Assignment**:

- Agentic multi-step research behavior  
- LLM-powered synthesis & JSON generation  
- Section-level updates  
- Persona-aware conversation  
- FastAPI backend + simple frontend  
- Local LLM reasoning  
- Persistent storage  

