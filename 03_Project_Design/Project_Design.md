# PHASE 3 – PROJECT DESIGN

## EDU GENIE – GOOGLE GEMINI POWERED LEARNING ASSISTANT

---

## 1. Introduction

The Project Design Phase defines the overall technical structure, architecture, modules, user interface, data flow, and system components of the EduGenie application.

EduGenie is a web-based AI educational assistant designed to provide learning support to students. The application uses Google Gemini to generate educational responses based on the user's input.

The system provides multiple learning features such as:

- Question and Answer
- Concept Explanation
- Content Summarization
- Quiz Generation
- Learning Recommendations

The system is designed using a frontend-backend architecture. The frontend provides the user interface, while the FastAPI backend processes requests and communicates with the Google Gemini API.

---

# 2. Project Title

**EduGenie – Google Gemini Powered Learning Assistant**

---

# 3. Design Objectives

The main objectives of the system design are:

1. To create a simple and user-friendly educational interface.
2. To integrate Google Gemini for AI-powered learning assistance.
3. To design separate modules for different learning activities.
4. To provide quick responses to student requests.
5. To maintain a clear separation between frontend and backend.
6. To securely manage the Gemini API key.
7. To create a maintainable and extensible project structure.
8. To provide a foundation for future educational features.

---

# 4. Overall System Architecture

EduGenie follows a web-based client-server architecture.

The system consists of the following major components:

1. Student/User
2. Web Browser
3. Frontend
4. FastAPI Backend
5. Gemini API
6. AI Generated Response

The overall architecture is:

```text
                         +----------------------+
                         |       Student        |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |     Web Browser      |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |   EduGenie Frontend  |
                         |    HTML/CSS/JS       |
                         +----------+-----------+
                                    |
                                    | HTTP Request
                                    v
                         +----------------------+
                         |   FastAPI Backend    |
                         |       main.py        |
                         +----------+-----------+
                                    |
                                    | API Request
                                    v
                         +----------------------+
                         |    Google Gemini     |
                         |         API          |
                         +----------+-----------+
                                    |
                                    | AI Response
                                    v
                         +----------------------+
                         |   FastAPI Backend    |
                         +----------+-----------+
                                    |
                                    | HTTP Response
                                    v
                         +----------------------+
                         |   EduGenie Frontend  |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |       Student        |
                         +----------------------+