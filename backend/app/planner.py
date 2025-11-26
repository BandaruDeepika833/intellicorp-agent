import json
from .llm_client import ask_llm

async def generate_account_plan(summary):
    prompt = f"""
Create a detailed enterprise account plan.

Return ONLY a valid JSON object with these sections:

1. Company Overview
2. Key Opportunities
3. Risks & Challenges
4. Recommended Strategy
5. Tech Adoption Insights
6. Partnership Potential

Base on this summary:

{summary}
"""

    response = await ask_llm(prompt)

    # Parse JSON
    try:
        return json.loads(response)
    except:
        return {
            "error": "JSON parse failed",
            "raw": response
        }
