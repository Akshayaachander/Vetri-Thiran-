from typing import Any, Dict, List


def fallback_quiz(
    text: str,
    question_count: int = 3
) -> List[Dict[str, Any]]:

    text_lower = text.lower()

    if "photosynthesis" in text_lower:

        questions = [
            {
                "question": "What is the main purpose of photosynthesis?",
                "options": [
                    "To make food for the plant",
                    "To absorb oxygen",
                    "To produce soil",
                    "To cool the plant"
                ],
                "correct_answer": "To make food for the plant",
                "explanation": "Photosynthesis allows green plants to make their own food using sunlight."
            },
            {
                "question": "Which substance provides energy for photosynthesis?",
                "options": [
                    "Sunlight",
                    "Oxygen",
                    "Soil",
                    "Protein"
                ],
                "correct_answer": "Sunlight",
                "explanation": "Sunlight provides the energy needed for photosynthesis."
            },
            {
                "question": "Which gas do plants take in during photosynthesis?",
                "options": [
                    "Carbon dioxide",
                    "Oxygen",
                    "Nitrogen",
                    "Hydrogen"
                ],
                "correct_answer": "Carbon dioxide",
                "explanation": "Plants take carbon dioxide from the air during photosynthesis."
            },
            {
                "question": "Where does photosynthesis mainly take place?",
                "options": [
                    "Leaves",
                    "Roots",
                    "Flowers",
                    "Seeds"
                ],
                "correct_answer": "Leaves",
                "explanation": "Photosynthesis mainly takes place in the leaves of green plants."
            },
            {
                "question": "Which substance is released during photosynthesis?",
                "options": [
                    "Oxygen",
                    "Carbon dioxide",
                    "Nitrogen",
                    "Salt"
                ],
                "correct_answer": "Oxygen",
                "explanation": "Oxygen is released during photosynthesis."
            }
        ]

    elif "python" in text_lower:

        questions = [
            {
                "question": "What type of language is Python?",
                "options": [
                    "High-level programming language",
                    "Machine language",
                    "Assembly language",
                    "Markup language"
                ],
                "correct_answer": "High-level programming language",
                "explanation": "Python is a high-level programming language."
            },
            {
                "question": "What is Python known for?",
                "options": [
                    "Readable syntax",
                    "Binary instructions",
                    "Hardware wiring",
                    "Machine code only"
                ],
                "correct_answer": "Readable syntax",
                "explanation": "Python is known for its simple and readable syntax."
            },
            {
                "question": "Which field commonly uses Python?",
                "options": [
                    "Artificial intelligence",
                    "Brick manufacturing",
                    "Road construction",
                    "Metal cutting"
                ],
                "correct_answer": "Artificial intelligence",
                "explanation": "Python is widely used in artificial intelligence."
            }
        ]

    else:

        questions = [
            {
                "question": "What is the main purpose of studying a topic?",
                "options": [
                    "To understand the concepts",
                    "To avoid learning",
                    "To remove information",
                    "To stop practicing"
                ],
                "correct_answer": "To understand the concepts",
                "explanation": "Studying helps learners understand important concepts."
            },
            {
                "question": "Which method helps improve understanding?",
                "options": [
                    "Practice",
                    "Ignoring the topic",
                    "Avoiding examples",
                    "Skipping revision"
                ],
                "correct_answer": "Practice",
                "explanation": "Regular practice helps strengthen understanding."
            },
            {
                "question": "Why are examples useful when learning?",
                "options": [
                    "They make concepts easier to understand",
                    "They remove concepts",
                    "They prevent learning",
                    "They replace studying completely"
                ],
                "correct_answer": "They make concepts easier to understand",
                "explanation": "Examples connect ideas with clear situations."
            }
        ]

    return questions[:question_count]


async def generate_quiz(
    text: str,
    question_count: int = 3
) -> List[Dict[str, Any]]:

    return fallback_quiz(
        text,
        question_count
    )