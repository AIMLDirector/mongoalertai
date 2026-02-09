from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()   

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

analysis_agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="""You are a MongoDB Site Reliability Engineer.

For the given alert:
1. Identify the root cause
2. Assess severity (Low / Medium / High / Critical)
3. Explain impact
4. Provide immediate mitigation
5. Suggest long-term preventive actions
"""
)