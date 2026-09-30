
from gemini_client import generate_text


SYSTEM_PROMPT = """
You are EduGenie, a helpful educational assistant.

Your job is to help students understand academic
and general educational questions.

Rules:

- Give accurate answers.
- Use simple language.
- Keep answers reasonably concise.
- Explain difficult terms.
- Use examples when useful.
- Do not invent facts.
- If a question is ambiguous, mention the ambiguity.
"""


def fallback_answer(question: str) -> str:

    question_lower = question.lower()

    if "photosynthesis" in question_lower:
        return (
            "Photosynthesis is the process by which green plants "
            "make their own food using sunlight, carbon dioxide, "
            "and water. It mainly takes place in the leaves using "
            "chlorophyll.\n\n"
            "Key points:\n"
            "• Sunlight provides energy.\n"
            "• Carbon dioxide comes from the air.\n"
            "• Water is absorbed by the roots.\n"
            "• Glucose is produced as food.\n"
            "• Oxygen is released into the atmosphere."
        )

    if "python" in question_lower:
        return (
            "Python is a high-level, general-purpose programming "
            "language. It is known for its simple and readable "
            "syntax.\n\n"
            "It is commonly used for web development, data science, "
            "artificial intelligence, automation, and education."
        )

    if "computer" in question_lower:
        return (
            "A computer is an electronic device that accepts data, "
            "processes it according to instructions, stores it, "
            "and produces useful information.\n\n"
            "The basic functions of a computer are:\n"
            "• Input\n"
            "• Processing\n"
            "• Storage\n"
            "• Output"
        )

    if "array" in question_lower:
        return (
            "An array is a collection of elements of the same data "
            "type stored in consecutive memory locations.\n\n"
            "For example, an integer array can store several integer "
            "values under one variable name.\n\n"
            "Arrays are useful when we need to store and process "
            "multiple related values."
        )

    if "recursion" in question_lower:
        return (
            "Recursion is a programming technique in which a function "
            "calls itself to solve a smaller version of the same problem.\n\n"
            "A recursive function normally contains:\n"
            "• A base condition\n"
            "• A recursive call\n\n"
            "Example: calculating the factorial of a number."
        )

    return (
        f"Here is a simple explanation of your question:\n\n"
        f"{question}\n\n"
        "This topic can be understood by identifying its definition, "
        "main concepts, working process, and practical examples.\n\n"
        "For a detailed AI-generated answer, Gemini can provide "
        "additional information when the API quota is available."
    )


async def answer_question(
    question: str
) -> str:

    prompt = f"""
{SYSTEM_PROMPT}

Student question:

{question}

Give a direct educational answer.

When useful, use:

- short headings
- bullet points
- examples
- simple explanations
"""

    try:

        return await generate_text(
            prompt,
            temperature=0.3,
            max_output_tokens=1000,
        )

    except RuntimeError as exc:

        error_message = str(exc)

        if (
            "GEMINI_QUOTA_EXCEEDED" in error_message
            or "GEMINI_TEMPORARILY_UNAVAILABLE" in error_message
        ):

            return fallback_answer(question)

        raise

