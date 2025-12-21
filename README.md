# 🤖 Agentic AI-Based Travel Planner (Agentic AI System)

The **Agentic AI-Based Travel Planner** is an intelligent AI assistant built using an **agentic workflow**.  
It can generate complete travel plans using **natural language user queries**, with all reasoning and tool execution handled locally — **no API keys, no paid services, no cloud dependency**.

This project uses:

- **LangChain** for agent orchestration  
- **Ollama (LLaMA 3)** for local LLM inference  
- **Streamlit** for a clean ChatGPT-style interactive UI  

---

## ✨ Features

- 🧠 Understands natural language travel queries  
- 📍 Extracts source and destination cities automatically  
- ✈️ Searches flights between cities  
- 🏨 Recommends hotels based on budget  
- 📍 Discovers tourist places  
- 🌦️ Provides weather information  
- 💰 Estimates total travel budget  
- 🔐 Fully local execution (no API keys)  
- 🗂️ Modular and production-ready code  

---

## 📁 Project Structure

AGENTIC_AI_TRAVEL_PLANNER
├── agent/
│ └── travel_agent.py # Main agent orchestration logic
│
├── tools/
│ ├── flight_tool.py # Flight search tool
│ ├── hotel_tool.py # Hotel recommendation tool
│ ├── places_tool.py # Places discovery tool
│ ├── weather_tool.py # Weather information tool
│ └── budget_tool.py # Budget estimation tool
│
├── app/
│ └── streamlit_app.py # Streamlit UI
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Requirements

### Python Version  
**Python 3.10+** recommended

### Install Dependencies

After cloning repo, run:

```
pip install -r requirements.txt
