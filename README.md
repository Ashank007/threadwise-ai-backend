![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

# Thread AI - Backend

This is the **backend service** for **Thread AI - Smart Email Reply Generator**.  
It acts as a unified **LLM router** to handle multiple AI providers (**OpenAI**, **Gemini**, and **Ollama**) and generate context-aware, high-quality email replies.


## 🚀 Features
- **Multi-LLM Support** – OpenAI, Gemini, and Ollama in one place.
- **Dynamic Provider Selection** – Switch AI providers via API.
- **Prompt Engineering** – Centralized and optimized prompts for better responses.
- **FastAPI Backend** – Lightweight and high-performance.
- **Easy Deployment** – Works locally or on cloud.

## 📂 Project Structure
```
├── llm_router.py # Routes requests to the correct LLM provider
├── main.py # FastAPI app entry point
├── prompt.py # Contains the system & user prompt templates
├── providers/
│ ├── gemini_provider.py # Google Gemini integration
│ ├── ollama_provider.py # Ollama local LLM integration
│ └── openai_provider.py # OpenAI API integration
├── requirements.txt # Python dependencies
```

## ⚙️ Installation

### 1 Clone the Repository
```
git clone https://github.com/Ashank007/threadwise-ai-backend.git
cd thread-ai-backend
```
### 2 Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```
### 3 Install Dependencies
```
pip install -r requirements.txt
```

## ▶️ Running the Server
```
uvicorn main:app --reload
```
Server will start at:
```
http://127.0.0.1:8000
```

## 📡 API Endpoints
```
Method	Endpoint	Description
POST	/generate	Generate an AI email reply
GET	    /providers	List available AI providers
POST	/switch	    Switch active AI provider
```

## 📝 License

This project is licensed under the MIT License.
