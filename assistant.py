import ast
import operator
import random

KNOWLEDGE = {
    "artificial intelligence": (
        "**Artificial Intelligence (AI)** is a branch of computer science that makes "
        "machines perform tasks that normally require human intelligence, such as learning, "
        "reasoning and problem-solving.\n\n**Example:** Voice assistants and recommendation systems."
    ),
    "machine learning": (
        "**Machine Learning (ML)** is a subset of AI in which computers learn patterns from data "
        "and use those patterns to make predictions or decisions without being explicitly programmed "
        "for every task.\n\n**Types:** Supervised, unsupervised and reinforcement learning."
    ),
    "python": (
        "**Python** is a high-level, interpreted, general-purpose programming language. "
        "It is popular because its syntax is readable and it has libraries for AI, data science, "
        "web development and automation."
    ),
    "nlp": (
        "**Natural Language Processing (NLP)** is a field of AI that helps computers understand, "
        "interpret and generate human language.\n\n**Examples:** Chatbots, translation and speech recognition."
    ),
    "data science": (
        "**Data Science** combines statistics, programming and domain knowledge to extract useful "
        "information from data. A typical workflow includes collecting, cleaning, analysing and visualising data."
    ),
    "study tips": (
        "**Study tips:**\n"
        "1. Set a small daily goal.\n"
        "2. Study in focused 25–30 minute sessions.\n"
        "3. Practise questions instead of only rereading.\n"
        "4. Revise topics regularly.\n"
        "5. Take short breaks and sleep properly."
    ),
    "exam": (
        "**Exam preparation tips:** Make a topic checklist, revise important concepts, solve previous "
        "questions, practise writing answers within a time limit and keep the final day for revision."
    )
}

QUOTES = [
    "The secret of getting ahead is getting started.",
    "Small progress every day adds up to big results.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Believe you can and you are halfway there."
]

# Safe calculator: only arithmetic operators and numeric constants are accepted.
_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def _eval_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 8:
            raise ValueError("Exponent is too large.")
        return _ALLOWED_OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
        return _ALLOWED_OPERATORS[type(node.op)](_eval_node(node.operand))
    raise ValueError("Only basic arithmetic is allowed.")

def safe_calculate(expression):
    try:
        tree = ast.parse(expression, mode="eval")
        result = _eval_node(tree.body)
        return f"Result: **{result}**"
    except ZeroDivisionError:
        return "You cannot divide by zero."
    except Exception:
        return "I could not calculate that. Try an expression like `25 * (4 + 2)`."

def get_quote():
    return "🌟 **Motivational quote:** " + random.choice(QUOTES)

def get_response(message):
    text = message.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! 👋 How can I help you with your studies today?"
    if "your name" in text or "who are you" in text:
        return "I am **Student AI Virtual Assistant**, a mini project built with Python and Streamlit."
    if "time" in text or "date" in text:
        from datetime import datetime
        return "Current date and time: **" + datetime.now().strftime("%d %B %Y, %I:%M:%S %p") + "**"
    if "quote" in text or "motivat" in text:
        return get_quote()

    if text.startswith("calculate "):
        return safe_calculate(message[10:].strip())
    if text.startswith("solve "):
        return safe_calculate(message[6:].strip())

    for keyword, answer in KNOWLEDGE.items():
        if keyword in text:
            return answer

    if "thank" in text:
        return "You're welcome! 😊 Keep learning and practising."
    if "help" in text:
        return (
            "I can help with:\n"
            "- AI, Machine Learning, Python, NLP and Data Science explanations\n"
            "- Basic calculations (write `calculate 12 * (5 + 2)`)\n"
            "- Study and exam tips\n"
            "- Motivational quotes\n"
            "- Date and time\n"
            "- A to-do list in the panel on the right"
        )

    return (
        "I am still learning. I can answer questions about AI, Machine Learning, Python, NLP "
        "and Data Science. You can also ask for study tips or type `calculate 10 + 5`.\n\n"
        "Try typing **help** to see what I can do."
    )
