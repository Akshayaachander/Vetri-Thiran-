# 3. Project Design Phase

## Project Title
EduGenie – Google Gemini Powered Learning Assistant

## 1. Introduction

The Project Design Phase describes the overall structure, modules, user interaction, and technical design of the EduGenie system.

## 2. System Architecture

EduGenie follows a simple web-based architecture:

User → Frontend → Backend API → Google Gemini API → Backend → Frontend → User

The user interacts with the frontend. The frontend sends requests to the FastAPI backend. The backend communicates with Google Gemini to generate the required learning content and sends the response back to the user.

## 3. Main Modules

### 3.1 Explanation Module
Generates simple and understandable explanations for educational topics.

### 3.2 Summarization Module
Converts lengthy educational content into short and useful summaries.

### 3.3 Quiz Module
Generates multiple-choice quizzes based on the selected topic or content.

### 3.4 Question Generation Module
Generates practice questions to help students prepare for examinations.

### 3.5 Learning Path Module
Creates a structured learning path to help students study a topic step by step.

### 3.6 AI Learning Assistant
Provides AI-powered assistance for students' learning needs.

## 4. User Flow

1. User opens the EduGenie application.
2. User enters a topic or learning content.
3. User selects the required learning feature.
4. The frontend sends the request to the backend.
5. The backend processes the request.
6. Google Gemini generates the required response.
7. The backend returns the response.
8. The result is displayed to the user.

## 5. Technology Design

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI

### AI Integration
- Google Gemini API

### Development Tool
- Visual Studio Code

## 6. Database Design

The initial version of EduGenie does not require a complex database. The application mainly processes user input and generates AI-based responses.

## 7. Security Design

- API keys should be stored securely.
- Sensitive configuration values should not be uploaded to GitHub.
- Environment variables should be used for secret credentials.
- User inputs should be validated before processing.

## 8. Expected Design Outcome

The design provides a simple and modular structure that allows the different EduGenie features to work together efficiently.

## 9. Conclusion

The Project Design Phase defines the architecture, modules, user flow, technologies, and security considerations required for developing EduGenie.

**Phase 3 Status: Completed**
