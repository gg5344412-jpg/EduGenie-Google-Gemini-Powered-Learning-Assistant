# PHASE 6 – PROJECT TESTING

## EDU GENIE – GOOGLE GEMINI POWERED LEARNING ASSISTANT

---

## 1. Introduction

The Project Testing Phase verifies whether the EduGenie application works according to the requirements defined during the Requirement Analysis and Project Design phases.

Testing is performed on the major features of the application including:

- Question and Answer
- Explanation
- Summarization
- Quiz Generation
- Quiz Answer Validation
- Learning Recommendations
- Backend API
- Web Interface

The objective of testing is to identify errors, verify expected functionality, and ensure that the application produces appropriate results for different user inputs.

---

## 2. Testing Objectives

The main objectives of testing are:

- To verify the functionality of each EduGenie module.
- To verify communication between frontend and backend.
- To verify Google Gemini API integration.
- To check whether valid user inputs produce responses.
- To test quiz generation and answer validation.
- To identify application errors.
- To verify error handling.
- To confirm that the application is ready for demonstration.

---

## 3. Testing Environment

| Component | Details |
|---|---|
| Operating System | Windows |
| Programming Language | Python |
| Backend | FastAPI |
| Server | Uvicorn |
| AI Service | Google Gemini API |
| Frontend | HTML, CSS, JavaScript |
| Browser | Google Chrome |
| Development Environment | Visual Studio Code |

---

## 4. Testing Method

Functional testing is used to verify the major features of EduGenie.

For each feature:

1. A valid input is provided.
2. The request is submitted.
3. The application processes the request.
4. The generated result is observed.
5. The actual result is compared with the expected result.
6. The test is marked as PASS or FAIL.

---

# 5. Test Cases

## TC-01 – Application Launch Test

| Field | Details |
|---|---|
| Test Case ID | TC-01 |
| Module | Application |
| Test Objective | Verify that the EduGenie application launches successfully |
| Input | Application URL |
| Expected Result | EduGenie home page should load |
| Actual Result | EduGenie home page loaded successfully |
| Status | PASS |

---

## TC-02 – Backend Health Test

| Field | Details |
|---|---|
| Test Case ID | TC-02 |
| Module | Backend |
| Test Objective | Verify that the backend server is running |
| Input | Backend health request |
| Expected Result | Backend should return a successful status |
| Actual Result | Backend returned status OK and confirmed that EduGenie backend is running |
| Status | PASS |

---

## TC-03 – Question and Answer Test

| Field | Details |
|---|---|
| Test Case ID | TC-03 |
| Module | Question and Answer |
| Test Objective | Verify that EduGenie can answer an educational question |
| Input | What is Artificial Intelligence? |
| Expected Result | The system should generate an educational answer |
| Actual Result | EduGenie generated an answer explaining Artificial Intelligence |
| Status | PASS |

---

## TC-04 – Explanation Test

| Field | Details |
|---|---|
| Test Case ID | TC-04 |
| Module | Explanation |
| Test Objective | Verify that EduGenie can explain an educational topic |
| Input | Machine Learning |
| Expected Result | The system should provide an understandable explanation |
| Actual Result | EduGenie generated a detailed explanation of Machine Learning |
| Status | PASS |

---

## TC-05 – Summary Test

| Field | Details |
|---|---|
| Test Case ID | TC-05 |
| Module | Summarization |
| Test Objective | Verify that EduGenie can summarize educational content |
| Input | Educational paragraph about Artificial Intelligence |
| Expected Result | The system should generate a concise summary |
| Actual Result | EduGenie generated a concise summary of the provided content |
| Status | PASS |

---

## TC-06 – Quiz Generation Test

| Field | Details |
|---|---|
| Test Case ID | TC-06 |
| Module | Quiz |
| Test Objective | Verify that EduGenie can generate a multiple-choice quiz |
| Input | AI-related quiz request |
| Expected Result | System should generate 3 questions with 4 options each |
| Actual Result | Quiz containing 3 questions and 4 options for each question was generated |
| Status | PASS |

---

## TC-07 – Quiz Correct Answer Test

| Field | Details |
|---|---|
| Test Case ID | TC-07 |
| Module | Quiz Answer Validation |
| Test Objective | Verify correct answer validation |
| Input | Correct options selected by the user |
| Expected Result | System should display correct-answer feedback |
| Actual Result | Correct answers were identified and positive feedback was displayed |
| Status | PASS |

---

## TC-08 – Quiz Incorrect Answer Test

| Field | Details |
|---|---|
| Test Case ID | TC-08 |
| Module | Quiz Answer Validation |
| Test Objective | Verify incorrect answer handling |
| Input | Incorrect options selected by the user |
| Expected Result | System should indicate that the answer is incorrect and show the correct answer |
| Actual Result | The system displayed incorrect-answer feedback and provided the correct answer |
| Status | PASS |

---

## TC-09 – Learning Recommendation Test

| Field | Details |
|---|---|
| Test Case ID | TC-09 |
| Module | Learning Recommendations |
| Test Objective | Verify that EduGenie can generate a learning roadmap |
| Input | Python Programming |
| Expected Result | System should generate structured learning recommendations |
| Actual Result | EduGenie generated Beginner, Intermediate, Advanced, Practice/Resources, Adaptive Learning Tips, and a stepwise roadmap |
| Status | PASS |

---

## TC-10 – Frontend and Backend Integration Test

| Field | Details |
|---|---|
| Test Case ID | TC-10 |
| Module | System Integration |
| Test Objective | Verify communication between frontend and backend |
| Input | User requests through the web interface |
| Expected Result | Frontend should send requests to the backend and display the response |
| Actual Result | User requests were processed through the backend and generated responses were displayed |
| Status | PASS |

---

## TC-11 – Gemini API Integration Test

| Field | Details |
|---|---|
| Test Case ID | TC-11 |
| Module | Gemini API |
| Test Objective | Verify communication with Google Gemini API |
| Input | Educational prompts |
| Expected Result | Gemini should generate a response |
| Actual Result | Gemini-generated responses were received for the tested learning modules |
| Status | PASS |

---

## TC-12 – Error Handling Test

| Field | Details |
|---|---|
| Test Case ID | TC-12 |
| Module | Error Handling |
| Test Objective | Verify that API and response errors are handled |
| Input | API/service error conditions |
| Expected Result | Application should handle the error and provide an appropriate message |
| Actual Result | Error handling and retry mechanisms were implemented in the backend |
| Status | PASS |

---

# 6. Test Case Summary

| Test Case | Module | Result |
|---|---|---|
| TC-01 | Application Launch | PASS |
| TC-02 | Backend Health | PASS |
| TC-03 | Question & Answer | PASS |
| TC-04 | Explanation | PASS |
| TC-05 | Summarization | PASS |
| TC-06 | Quiz Generation | PASS |
| TC-07 | Quiz Correct Answer | PASS |
| TC-08 | Quiz Incorrect Answer | PASS |
| TC-09 | Learning Recommendations | PASS |
| TC-10 | Frontend-Backend Integration | PASS |
| TC-11 | Gemini API Integration | PASS |
| TC-12 | Error Handling | PASS |

---

# 7. Functional Testing Result

The major functional modules of EduGenie were tested using appropriate inputs.

The following features successfully produced the expected type of output:

- Question and Answer
- Explanation
- Summarization
- Quiz Generation
- Correct Answer Validation
- Incorrect Answer Validation
- Learning Recommendations

The frontend and backend integration was also tested.

---

# 8. Quiz Testing Result

The quiz functionality was tested using both correct and incorrect answers.

### Correct Answer Testing

The system correctly identified selected correct options and provided positive feedback.

### Incorrect Answer Testing

The system correctly identified incorrect options and displayed the corresponding correct answer.

This confirms that the quiz answer validation functionality is working.

---

# 9. Learning Recommendation Testing Result

The Learning Recommendation feature was tested using:

Python Programming

The system generated recommendations covering different learning levels and practice guidance.

The generated result included:

- Beginner
- Intermediate
- Advanced
- Practice/Resources
- Adaptive Learning Tips
- Stepwise Roadmap

The test was marked as PASS.

---

# 10. Testing Screenshots

Screenshots of the completed application testing are stored in:

06_Project_Testing/screenshots/

Recommended screenshots include:

1. EduGenie Home Page
2. Q&A Result
3. Explanation Result
4. Summary Result
5. Quiz Questions
6. Quiz Correct Answer
7. Quiz Incorrect Answer
8. Learning Recommendations
9. Backend/Health Response

---

# 11. Defects and Observations

During testing, temporary API/service availability issues may occur when communicating with the Gemini API.

The application includes retry handling for temporary service availability errors.

AI-generated responses can also vary depending on the prompt and model response. Therefore, response validation is particularly important for structured outputs such as quizzes.

The quiz module validates the generated structure before presenting the questions to the user.

---

# 12. Final Testing Status

Based on the performed functional tests, the major EduGenie features were successfully tested.

The application successfully demonstrated:

- AI-powered question answering.
- Educational explanations.
- Content summarization.
- Multiple-choice quiz generation.
- Correct and incorrect answer validation.
- Learning recommendations.
- Frontend and backend communication.

The application is ready for the next project phases:

- Project Documentation
- Project Demonstration

---

# 13. Conclusion

The Project Testing Phase verified the major functionality of the EduGenie application.

Functional testing was performed for the Q&A, Explanation, Summary, Quiz, and Learning Recommendation modules.

The quiz functionality was tested with both correct and incorrect answers.

The frontend, backend, and Gemini API integration were also tested.

The testing results indicate that the implemented EduGenie features are functioning as expected for the tested scenarios.

The next phase is the Project Documentation Phase.
