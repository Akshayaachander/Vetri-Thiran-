# 7. Project Documentation Phase

## Project Title

EduGenie – Google Gemini Powered Learning Assistant

## 1. Introduction

EduGenie is a web-based AI learning assistant developed to help students understand educational topics and improve their learning experience.

The application uses Google Gemini API to provide AI-powered educational assistance.

## 2. Purpose of the Project

The main purpose of EduGenie is to provide students with a single platform for learning, revision, practice, and personalized guidance.

## 3. Technologies Used

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- Google Gemini API
- Pytest
- HTTPX
- GitHub
- Visual Studio Code

## 4. System Features

### AI Explanation

Provides simple explanations for difficult educational topics.

### Summarization

Summarizes lengthy educational content into shorter and easier-to-understand information.

### Quiz Generation

Creates multiple-choice questions for practice.

### Question Generation

Generates practice questions with answers and difficulty levels.

### Learning Path

Creates a step-by-step learning plan for a selected topic.

## 5. System Architecture

The basic working flow of EduGenie is:

User  
↓  
Frontend  
↓  
FastAPI Backend  
↓  
Google Gemini API  
↓  
FastAPI Backend  
↓  
Frontend  
↓  
User

## 6. Installation Requirements

The following software is required:

- Python
- Visual Studio Code
- Internet connection
- Modern web browser
- Google Gemini API key

## 7. Installation Steps

### Step 1

Clone or download the EduGenie project from GitHub.

### Step 2

Open the project in Visual Studio Code.

### Step 3

Install the required Python packages:

```bash
pip install -r requirements.txt
Step 4

Create a .env file and add the Gemini API key:
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash
Step 5

Start the FastAPI server:
uvicorn main:app --reload
Step 6

Open the application in a web browser.

8. Usage

1. Open the EduGenie application.
2. Enter a topic or educational content.
3. Select a feature.
4. Wait for the AI-generated response.
5. Read and use the generated learning content.
9. API Endpoints
Method

Endpoint

Description

GET

/

Opens the EduGenie application

GET

/health

Checks server health

POST

/explain

Generates an explanation

POST

/summarize

Generates a summary

POST

/quiz

Generates a quiz

POST

/questions

Generates practice questions

POST

/learning-path

Generates a learning path
10. Security

The Gemini API key must be kept private.

The .env file containing the actual API key should not be uploaded to GitHub.

Only .env.example should be included in the repository.

11. Testing

The project uses Pytest for automated testing.

The test file is located at:

tests/test_api.py

The automated tests were successfully executed.

Test Result: 5 tests passed.

12. Project Limitations

* AI responses depend on the availability of the Gemini API.
* Internet access is required.
* AI-generated content may require verification.
* API quota limitations may affect usage.

13. Future Enhancements

Future versions may include:

* User accounts and login.
* Learning progress tracking.
* Database integration.
* More educational tools.
* Improved quiz scoring.
* Personalized recommendations.
* Voice-based learning assistance.

14. Conclusion

The Project Documentation Phase provides the technical and usage information required to understand, install, run, and use EduGenie.

The documentation supports users and developers in understanding the system and its features.
