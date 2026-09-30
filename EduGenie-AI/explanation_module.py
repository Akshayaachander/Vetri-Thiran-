from gemini_client import generate_text


def fallback_explain(topic: str, level: str) -> str:

    topic_lower = topic.lower()

    if "photosynthesis" in topic_lower:
        return (
            "Photosynthesis\n\n"
            "Simple definition:\n"
            "Photosynthesis is the process by which green plants "
            "make their own food using sunlight, water, and carbon dioxide.\n\n"
            "How it works:\n"
            "Plants use chlorophyll to capture sunlight. "
            "The energy from sunlight helps the plant convert "
            "water and carbon dioxide into glucose.\n\n"
            "Key points:\n"
            "• Sunlight provides energy.\n"
            "• Chlorophyll absorbs sunlight.\n"
            "• Carbon dioxide comes from the air.\n"
            "• Water is absorbed through the roots.\n"
            "• Oxygen is released.\n\n"
            "Example:\n"
            "A green plant uses sunlight to produce food in its leaves.\n\n"
            "Memory tip:\n"
            "Think: Sunlight + Water + Carbon dioxide → Food + Oxygen."
        )

    if "python" in topic_lower:
        return (
            "Python\n\n"
            "Simple definition:\n"
            "Python is a high-level programming language known "
            "for its simple and readable syntax.\n\n"
            "How it works:\n"
            "We write Python instructions, and the Python interpreter "
            "executes them.\n\n"
            "Key points:\n"
            "• Easy to learn\n"
            "• Simple syntax\n"
            "• Used in many fields\n\n"
            "Example:\n"
            "Python can be used to create programs, websites, "
            "automation tools, and AI applications.\n\n"
            "Memory tip:\n"
            "Python = simple syntax + many applications."
        )

    if "computer" in topic_lower:
        return (
            "Computer\n\n"
            "Simple definition:\n"
            "A computer is an electronic device that accepts data, "
            "processes it, stores it, and produces information.\n\n"
            "Key points:\n"
            "• Input\n"
            "• Processing\n"
            "• Storage\n"
            "• Output\n\n"
            "Example:\n"
            "When you type on a keyboard, the computer receives "
            "the input, processes it, and displays the result.\n\n"
            "Memory tip:\n"
            "Remember IPO: Input → Processing → Output."
        )

    return (
        f"Explanation of {topic}\n\n"
        "Simple definition:\n"
        f"{topic} is an important educational topic that can be "
        "understood by learning its basic meaning and main ideas.\n\n"
        "How it works / main idea:\n"
        f"Start by understanding the basic concept of {topic}, "
        "then learn its important parts and how they are connected.\n\n"
        "Key points:\n"
        "• Learn the basic definition.\n"
        "• Understand the main concepts.\n"
        "• Practice with examples.\n\n"
        "Example:\n"
        f"An example related to {topic} can help connect the concept "
        "with a real-world situation.\n\n"
        "Memory tip:\n"
        f"Remember the definition, main ideas, and one example of {topic}."
    )


async def explain_topic(
    topic: str,
    level: str = "beginner"
) -> str:

    prompt = f"""
You are EduGenie's concept explanation tutor.

Explain this topic for a {level} learner:

{topic}

Use:

1. Simple definition
2. How it works
3. Three key points
4. One easy example
5. One memory tip

Use simple student-friendly language.
"""

    try:

        return await generate_text(
            prompt,
            temperature=0.35,
            max_output_tokens=1000,
        )

    except RuntimeError as exc:

        error_message = str(exc)

        if (
            "GEMINI_QUOTA_EXCEEDED" in error_message
            or "GEMINI_TEMPORARILY_UNAVAILABLE" in error_message
        ):
            return fallback_explain(topic, level)

        raise