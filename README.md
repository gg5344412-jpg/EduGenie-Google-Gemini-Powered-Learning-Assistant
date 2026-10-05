# EduGenie - Google Gemini Powered Learning Assistant

A college-project implementation of an AI learning assistant using FastAPI, HTML/CSS/JavaScript and Google Gemini.

## Features

- Q&A: `/qna`
- Topic explanation: `/explain`
- Text summarization: `/summarize`
- 3-question MCQ quiz generation: `/quiz`
- Adaptive learning recommendations: `/learn/recommendations`
- Responsive web interface

## Requirements

- Python 3.10+
- A Gemini API key
- Internet connection

## Run locally

### Windows
```text
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

### macOS/Linux
```text
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Open `.env` and replace the placeholder with your Gemini API key.

Then start:

```text
uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000

## Important

Never upload your `.env` file or your API key to GitHub.

## Project structure

```text
EduGenie_Project/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── app.js
    └── style.css
```

## Viva explanation

Frontend -> FastAPI backend -> Gemini API -> response -> frontend.

The backend separates the five main learning functions into endpoints so each feature can be tested independently.
