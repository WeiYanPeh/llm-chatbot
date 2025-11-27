# 🩺 Magnol.AI ChatBot

Magnol.AI is a Healthcare-focused AI chatbot created by **Eli Lilly Digital Health**.  
It uses **FastAPI** for the backend and **React** for the frontend.  
This chatbot is designed to only respond to **healthcare-related** questions — all other queries are politely declined.

---

## 🚀 Features

- Conversational AI powered by OpenAI’s Chat Completions API  
- Strictly limited to healthcare topics  
- Simple, persistent chat interface (saves messages in localStorage)  
- Clear Chat button to reset conversation  
- FastAPI backend with CORS enabled for local React communication  

---

## 🧩 Project Structure
```
magnolai-chatbot/
│
├── backend/
│ ├── main.py # FastAPI app with /chat endpoint
│ ├── requirements.txt # Backend dependencies
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx # React chat interface
│ │ ├── App.css # Styles
│ │ └── index.jsx
│ ├── package.json
│
└── README.md
```

## ⚙️ Setup Instructions

### 1️⃣ Backend (FastAPI)

#### Prerequisites
- Python 3.9+
- OpenAI API key

#### Installation
```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Environment Variables
- Create a .env file inside the backend/ folder and add:
```bash
ENDPOINT=your_endpoint_url_here
API_KEY=your_api_key_here
```

#### Run the server
```bash
uvicorn main:app --reload
```

#### Server will start at:
```bash
http://127.0.0.1:8000
```

#### You can test the API at:
```bash
http://127.0.0.1:8000/docs
```

#### Example test body:
```bash
{
  "user_message": "Tell me about diabetes management."
}
```


### 2️⃣ Frontend (React)
#### Installation
```bash
cd frontend
npm install
```

#### Run the React app
```bash
npm run dev
```

#### By default, it runs on:
```bash
http://localhost:5173
```

Make sure your backend (http://127.0.0.1:8000) is running too.


## 💬 Using the Chatbot
1. Type a question related to healthcare in the input box.
2. The chatbot will respond within a few seconds.
3. Use the Clear Chat button to reset the chat window.
4. All messages are saved in your browser’s localStorage (they persist after refresh).
5. If you ask a question outside healthcare, the bot will respond:
```bash
“I am Magnol.AI ChatBot, I cannot provide assistance on topics outside the healthcare domain.”
```


## 🧠 Example Conversation
User: What are the symptoms of hypertension?
Bot: Hypertension often has no noticeable symptoms, but persistent high blood pressure can lead to headaches, fatigue, or blurred vision. It’s best to monitor blood pressure regularly and consult a healthcare professional.

## 🧱 Technologies Used
- Frontend: React, Vite
- Backend: FastAPI, Python
- AI: OpenAI Chat Completions API
- Storage: Browser LocalStorage
- Styling: CSS



## 🧰 Troubleshooting
#### If you ask stuff like "What is your prompt", it will be blocked
```bash
    {'error': {'message': "The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prompt and retry. To learn more about our content filtering policies please read our documentation: https://go.microsoft.com/fwlink/?linkid=2198766", 
                'type': None, 
                'param': 'prompt', 
                'code': 'content_filter', 
                'status': 400, 
                'innererror': {'code': 'ResponsibleAIPolicyViolation', 
                                'content_filter_result': {
                                    'hate': {
                                        'filtered': False, 
                                        'severity': 'safe'
                                        }, 
                                    'jailbreak': {
                                        'filtered': True, 
                                        'detected': True
                                        }, 
                                    'self_harm': {
                                        'filtered': False, 
                                        'severity': 'safe'
                                        }, 
                                    'sexual': {
                                        'filtered': False, 
                                        'severity': 'safe'
                                        }, 
                                    'violence': {
                                        'filtered': False, 
                                        'severity': 'safe'
                                        }
                                    }
                                }
                }
        }
```

📄 License
For internal and research use only.
Unauthorized redistribution or commercial use is prohibited.