from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

import os
import json
import re
import time

from google import genai


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. "
        "Create a .env file and add your Gemini API key."
    )


# =========================================================
# GEMINI CLIENT
# =========================================================

client = genai.Client(api_key=API_KEY)

# Use the new Gemini model
MODEL = "gemini-3.8-flash"


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant"
)


# =========================================================
# STATIC FILES
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# =========================================================
# HTML TEMPLATES
# =========================================================

templates = Jinja2Templates(
    directory="templates"
)


# =========================================================
# GEMINI FUNCTION WITH RETRY
# =========================================================

def ask_gemini(prompt: str) -> str:

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            result = (response.text or "").strip()

            if not result:
                raise ValueError(
                    "Gemini returned an empty response."
                )

            return result

        except Exception as e:

            error_message = str(e)

            # Temporary Gemini server overload
            if (
                "503" in error_message
                or "UNAVAILABLE" in error_message
            ):

                if attempt < max_retries - 1:

                    # Wait before retrying
                    time.sleep(3)

                    continue

                raise RuntimeError(
                    "Gemini service is temporarily busy. "
                    "Please wait a few seconds and try again."
                )

            # Model not found
            if (
                "404" in error_message
                or "NOT_FOUND" in error_message
            ):

                raise RuntimeError(
                    f"Gemini model '{MODEL}' is not available. "
                    "Please check the model name and API access."
                )

            # Other Gemini/API errors
            raise RuntimeError(
                f"Gemini API error: {error_message}"
            )

    raise RuntimeError(
        "Unable to get a response from Gemini."
    )


# =========================================================
# Q&A MODULE
# =========================================================

def answer_question_with_gemini(
    question: str
) -> str:

    prompt = f"""
You are EduGenie, a friendly AI tutor.

Answer the student's question accurately and clearly.

Use simple language unless the student asks for advanced detail.

Give a useful educational answer.

Student question:
{question}
"""

    return ask_gemini(prompt)


# =========================================================
# EXPLANATION MODULE
# =========================================================

def explain_topic(
    topic: str
) -> str:

    prompt = f"""
You are EduGenie, an AI tutor.

Explain the following topic to a school or college student.

Follow this structure:

1. Simple Definition
2. Understanding the Concept
3. How It Works
4. Small Practical Example
5. Key Points

Use simple and clear language.

Topic:
{topic}
"""

    return ask_gemini(prompt)


# =========================================================
# SUMMARY MODULE
# =========================================================

def summarize_text(
    text: str
) -> str:

    prompt = f"""
You are EduGenie, a student learning assistant.

Summarize the following text in simple language.

Requirements:

- Keep the important facts.
- Remove unnecessary details.
- Use short paragraphs or bullet points.
- Make it easy for a student to revise.
- Do not add information that is not present in the original text.

Text:
{text}
"""

    return ask_gemini(prompt)


# =========================================================
# CLEAN JSON RESPONSE
# =========================================================

def clean_json_block(
    text: str
) -> str:

    text = text.strip()

    # Remove Markdown JSON code block
    text = re.sub(
        r"^```json\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^```\s*",
        "",
        text
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    return text.strip()


# =========================================================
# QUIZ MODULE
# =========================================================

def generate_quiz(
    text: str
) -> list:

    prompt = f"""
You are EduGenie, an AI quiz generator.

Create exactly 3 multiple-choice questions
from the passage below.

Return ONLY valid JSON.

Use exactly this format:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option A"
  }}
]

Rules:

- Create exactly 3 questions.
- Each question must have exactly 4 options.
- Every question must be based only on the passage.
- The answer must exactly match one of the options.
- Do not add Markdown.
- Do not add explanations.
- Return JSON only.

Passage:
{text}
"""

    raw = ask_gemini(prompt)

    raw = clean_json_block(raw)

    try:

        data = json.loads(raw)

    except json.JSONDecodeError:

        # Try to extract JSON array if Gemini added extra text
        match = re.search(
            r"\[.*\]",
            raw,
            flags=re.DOTALL
        )

        if not match:

            raise ValueError(
                "Gemini returned an invalid quiz format."
            )

        data = json.loads(
            match.group(0)
        )

    # Check list
    if not isinstance(data, list):

        raise ValueError(
            "Quiz response was not a JSON list."
        )

    # Exactly 3 questions
    if len(data) != 3:

        raise ValueError(
            "Quiz must contain exactly 3 questions."
        )

    # Validate every question
    for item in data:

        if not isinstance(item, dict):

            raise ValueError(
                "Invalid quiz question format."
            )

        if "question" not in item:
            raise ValueError(
                "Quiz question is missing."
            )

        if "options" not in item:
            raise ValueError(
                "Quiz options are missing."
            )

        if "answer" not in item:
            raise ValueError(
                "Quiz answer is missing."
            )

        if not isinstance(
            item["options"],
            list
        ):

            raise ValueError(
                "Quiz options must be a list."
            )

        if len(item["options"]) != 4:

            raise ValueError(
                "Each question must have exactly 4 options."
            )

        if item["answer"] not in item["options"]:

            raise ValueError(
                "Quiz answer must match one of the options."
            )

    return data


# =========================================================
# LEARNING RECOMMENDATION MODULE
# =========================================================

def get_learning_recommendations(
    topic: str
) -> str:

    prompt = f"""
You are EduGenie, an adaptive AI tutor.

Create a structured learning path for:

{topic}

Use these headings:

1. Beginner Level
2. Intermediate Level
3. Advanced Level
4. Practice / Resources
5. Adaptive Learning Tips

For each level:

- Give important topics in a sensible order.
- Keep explanations practical.
- Use simple language.
- Give useful study suggestions.
- Make the learning path suitable for a student.

Topic:
{topic}
"""

    return ask_gemini(prompt)


# =========================================================
# HOME PAGE
# =========================================================

@app.get(
    "/",
    response_class=HTMLResponse
)
async def home(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# =========================================================
# Q&A API
# =========================================================

@app.get("/qna")
async def qna(
    question: str = Query(
        ...,
        min_length=1
    )
):

    try:

        question = question.strip()

        answer = answer_question_with_gemini(
            question
        )

        return {
            "answer": answer
        }

    except Exception as e:

        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )


# =========================================================
# EXPLANATION API
# =========================================================

@app.post("/explain")
async def explain(
    request: Request
):

    try:

        data = await request.json()

        topic = (
            data.get("topic") or ""
        ).strip()

        if not topic:

            return JSONResponse(
                content={
                    "error": "Please provide a topic."
                },
                status_code=400
            )

        explanation = explain_topic(
            topic
        )

        return {
            "topic": topic,
            "explanation": explanation
        }

    except Exception as e:

        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )


# =========================================================
# SUMMARIZE API
# =========================================================

@app.post("/summarize")
async def summarize(
    request: Request
):

    try:

        data = await request.json()

        text = (
            data.get("text") or ""
        ).strip()

        if not text:

            return JSONResponse(
                content={
                    "error": "Please provide text to summarize."
                },
                status_code=400
            )

        summary = summarize_text(
            text
        )

        return {
            "summary": summary
        }

    except Exception as e:

        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )


# =========================================================
# QUIZ API
# =========================================================

@app.post("/quiz")
async def quiz(
    request: Request
):

    try:

        data = await request.json()

        text = (
            data.get("text") or ""
        ).strip()

        if not text:

            return JSONResponse(
                content={
                    "error": "Please provide text for the quiz."
                },
                status_code=400
            )

        quiz_data = generate_quiz(
            text
        )

        return {
            "quiz": quiz_data
        }

    except Exception as e:

        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )


# =========================================================
# LEARNING RECOMMENDATION API
# =========================================================

@app.get(
    "/learn/recommendations"
)
async def learning_recommendation(
    topic: str = Query(
        ...,
        min_length=1
    )
):

    try:

        topic = topic.strip()

        recommendation = (
            get_learning_recommendations(
                topic
            )
        )

        return {
            "topic": topic,
            "recommendation": recommendation
        }

    except Exception as e:

        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "message": "EduGenie backend is running",
        "model": MODEL
    }