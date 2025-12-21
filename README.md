# 🤖 Agentic AI-Based Travel Planner (Agentic AI System)

The **Agentic AI-Based Travel Planner** is an intelligent AI assistant built using an **agentic workflow**.  
It can generate complete travel plans using **natural language user queries**, with all reasoning and tool execution handled locally — **no API keys, no paid services, no cloud dependency**.

This project uses:

- **LangChain** for agent orchestration  
- **Ollama (LLaMA 3)** for local LLM inference  
- **Streamlit** for a clean ChatGPT-style interactive UI  

---

## ✨ Features

-  Understands natural language travel queries  
-  Extracts source and destination cities automatically  
-  Searches flights between cities  
-  Recommends hotels based on budget  
-  Discovers tourist places  
-  Provides weather information  
-  Estimates total travel budget  
-  Fully local execution (no API keys)  
-  Modular and production-ready code  

---

## 📁 Project Structure
```
AGENTIC_AI_TRAVEL_PLANNER
├── agent/
│ └── travel_agent.py 
│
├── tools/
│ ├── flight_tool.py 
│ ├── hotel_tool.py 
│ ├── places_tool.py 
│ ├── weather_tool.py 
│ └── budget_tool.py 
│
├── app/
│ └── streamlit_app.py 
│
├── requirements.txt 
└── README.md 
```

---

## Requirements

### Python Version  
**Python 3.10+** recommended

### Install Dependencies

After cloning repo, run:

```bash
pip install -r requirements.txt
