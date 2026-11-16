# Student AI Virtual Assistant

**AI Lab Mini Project**  
**Selected assistant topic:** Student AI Virtual Assistant

A beginner-friendly virtual assistant built using Python and Streamlit. It helps students with basic academic questions, arithmetic calculations, study tips, motivational quotes, date/time and a simple to-do list.

## Features

- Chat interface with greetings and help responses
- Built-in explanations for Artificial Intelligence, Machine Learning, Python, NLP and Data Science
- Safe basic arithmetic calculator
- Study and exam preparation tips
- Motivational quotes
- Current date and time
- Interactive student to-do list with completion tracking and delete option

## Technologies used

- Python
- Streamlit
- Python standard libraries: `datetime`, `random`, `ast`, `operator`

## Project files

```text
Student_AI_Virtual_Assistant/
├── app.py
├── assistant.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── .gitignore
```

## Run locally

1. Install Python 3.9 or later.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. (Recommended) Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Start the application:
   ```bash
   streamlit run app.py
   ```
7. Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser.

## Example inputs

| Input | Expected behaviour |
|---|---|
| `Hello` | Displays a greeting |
| `What is AI?` | Explains Artificial Intelligence |
| `Explain machine learning` | Explains Machine Learning |
| `What is NLP?` | Explains NLP |
| `calculate 25 * (4 + 2)` | Displays the result |
| `Give me study tips` | Displays study tips |
| `motivate me` | Displays a motivational quote |
| `help` | Lists assistant capabilities |

Use the To-Do List panel to add tasks, mark them complete or delete them.

## How it works

1. `app.py` creates the Streamlit user interface and manages chat/task state using `st.session_state`.
2. User messages are passed to `get_response()` in `assistant.py`.
3. The assistant checks greetings, date/time, calculator commands and a small built-in knowledge base.
4. The response is displayed in the chat window.
5. The calculator parses arithmetic expressions with Python's `ast` module and permits only selected arithmetic operators.

## Limitations

- This is a rule-based educational assistant, not a large language model.
- It responds to topics included in its built-in knowledge base.
- Chat and task data are stored in the current Streamlit session; they are not saved permanently.
- The calculator supports basic arithmetic only.

## GitHub upload

Create a new public repository on GitHub, for example `student-ai-virtual-assistant`. Then run these commands in the project folder (replace `YOUR-USERNAME` with your GitHub username):

```bash
git init
git add .
git commit -m "Initial Student AI Virtual Assistant project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-ai-virtual-assistant.git
git push -u origin main
```

Your repository URL will be:

`https://github.com/YOUR-USERNAME/student-ai-virtual-assistant`

Do not submit the placeholder URL. Submit your actual repository URL after pushing the project.
