# AI Lab Mini Project Report

## Title
**Student AI Virtual Assistant**

## 1. Introduction
A virtual assistant is a software application that interacts with users and provides useful information or performs simple tasks. This project develops a student-focused virtual assistant using Python and Streamlit. It provides basic academic information, calculations, study guidance, motivational quotes, date/time and task management through a web interface.

## 2. Objectives
- To understand the basic working of a virtual assistant.
- To create an interactive web interface using Streamlit.
- To provide quick answers to common student questions.
- To implement a safe arithmetic calculator.
- To help students organise tasks using a to-do list.

## 3. Tools and Technologies
- **Python:** Main programming language.
- **Streamlit:** Creates the web application interface.
- **AST, operator:** Safely parse and evaluate supported arithmetic expressions.
- **datetime:** Displays current date and time.
- **random:** Selects a motivational quote.

## 4. System Modules
1. **Chat module:** Accepts user messages and displays assistant responses.
2. **Knowledge module:** Provides predefined explanations about AI, ML, Python, NLP and Data Science.
3. **Calculator module:** Evaluates supported arithmetic expressions.
4. **Motivation module:** Displays a random motivational quote.
5. **Date and time module:** Shows the current system date and time.
6. **To-do module:** Adds, completes and deletes student tasks.

## 5. Working
The user enters a message in the Streamlit chat box. The application sends the message to the `get_response()` function. The function identifies the intent using simple keyword matching and returns a relevant response. Streamlit displays that response. The to-do list uses session state to keep tasks while the current session is active.

## 6. Sample Test Cases

| Test input | Expected output |
|---|---|
| Hello | Greeting message |
| What is Artificial Intelligence? | AI definition and example |
| Explain Machine Learning | ML explanation and types |
| calculate 10 + 5 | Result: 15 |
| Give me study tips | Study tips |
| motivate me | Motivational quote |
| help | List of available features |

## 7. Advantages
- Easy to use.
- Beginner-friendly implementation.
- Combines multiple useful student tools in one interface.
- Can be extended with a larger knowledge base or an AI API.

## 8. Limitations
- Uses predefined responses and keyword matching.
- Cannot answer every possible question.
- Tasks are not permanently stored.
- Requires Python and Streamlit to run locally.

## 9. Future Scope
- Add speech-to-text and text-to-speech.
- Connect an AI language model API for more flexible answers.
- Save tasks in a database.
- Add user login and subject-wise notes.
- Deploy the app online.

## 10. Conclusion
The Student AI Virtual Assistant demonstrates how Python and Streamlit can be used to build a simple interactive assistant. It combines academic question answering, calculations, study tips, motivation and task management in one application. The project provides a foundation for developing more advanced AI assistants.

## 11. GitHub Repository
Paste your actual GitHub repository URL here after uploading the project:

`https://github.com/YOUR-USERNAME/student-ai-virtual-assistant`
