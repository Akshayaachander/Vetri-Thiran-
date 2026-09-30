from quiz_module import clean_json_block


def test_clean_json_block():
    raw = """```json
[
    {
        "question": "What is Python?",
        "options": [
            "Language",
            "Animal",
            "Database",
            "Browser"
        ],
        "correct_answer": "Language",
        "explanation": "Python is a programming language."
    }
]
```"""

    cleaned = clean_json_block(raw)

    assert cleaned.startswith("[")
    assert cleaned.endswith("]")