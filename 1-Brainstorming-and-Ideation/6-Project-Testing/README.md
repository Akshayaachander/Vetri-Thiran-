# 6. Project Testing Phase

## Project Title

EduGenie – Google Gemini Powered Learning Assistant

## 1. Introduction

The Project Testing Phase focuses on testing the EduGenie application to ensure that all major features work correctly and the system responds properly to user requests.

Testing was performed on the frontend, backend APIs, AI integration, and application functionality.

## 2. Objectives of Testing

The main objectives are:

- To identify errors in the application.
- To verify that the API endpoints work correctly.
- To check frontend and backend communication.
- To verify user input validation.
- To test AI-generated responses.
- To ensure that the application handles errors properly.
- To improve the reliability of the EduGenie application.

## 3. Testing Methods

The following testing methods were used:

### Unit Testing

Individual functions and modules were tested to verify that they work correctly.

### API Testing

FastAPI endpoints were tested to check whether they return the expected responses.

### Integration Testing

The connection between the frontend, backend, and Google Gemini API was tested.

### Functional Testing

The main EduGenie features were tested to verify their functionality.

## 4. Tools Used for Testing

- Python
- Pytest
- FastAPI
- HTTPX
- Visual Studio Code
- Web Browser

## 5. Test Cases

| Test Case | Description | Expected Result | Status |
|---|---|---|---|
| TC01 | Check application health | Server returns healthy status | Passed |
| TC02 | Open the application | Home page loads successfully | Passed |
| TC03 | Submit empty topic | System rejects empty input | Passed |
| TC04 | Generate explanation | Explanation is generated | Passed |
| TC05 | Generate summary | Summary is generated | Passed |
| TC06 | Generate quiz | Quiz questions are generated | Passed |
| TC07 | Generate questions | Practice questions are generated | Passed |
| TC08 | Generate learning path | Learning steps are generated | Passed |

## 6. Automated Testing

Pytest was used to test the FastAPI application.

The test file is:

`tests/test_api.py`

The tests verify:

- Health endpoint
- Home page
- Empty input validation

The automated tests were executed successfully.

### Test Result

**5 tests passed successfully.**

## 7. Error Handling Testing

The application was tested for different types of errors, including:

- Empty user input
- Invalid requests
- Gemini API errors
- Gemini quota errors
- Invalid AI responses
- Server errors

The application displays appropriate error messages when errors occur.

## 8. AI Feature Testing

The following AI-powered features were tested:

### Explanation

The system generates simple explanations for the given topic.

### Summarization

The system generates concise summaries of educational content.

### Quiz Generation

The system generates multiple-choice questions with answers and explanations.

### Question Generation

The system generates practice questions with difficulty levels.

### Learning Path

The system generates step-by-step learning paths.

## 9. Testing Outcome

Testing helped identify and correct errors during development.

The major EduGenie features were tested and the application was verified for basic functionality.

## 10. Conclusion

The Project Testing Phase confirms that the EduGenie application has been tested using automated and functional testing methods. The testing process helped improve the reliability and functionality of the application.

**Phase 6 Status: Testing Completed**
