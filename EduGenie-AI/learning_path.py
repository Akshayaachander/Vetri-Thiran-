def local_learning_path(
    topic: str,
    level: str = "beginner",
    timeline: str = "6 weeks"
) -> str:

    topic = topic.strip()

    if not topic:
        return "Please enter a topic you want to learn."

    return (
        f"Learning Path: {topic}\n\n"

        f"Level: {level}\n"
        f"Timeline: {timeline}\n\n"

        "Stage 1 — Basics\n"
        "• Learn the basic meaning and important terms.\n"
        f"• Understand the fundamentals of {topic}.\n"
        "• Make short notes while studying.\n\n"

        "Stage 2 — Core Concepts\n"
        "• Study the main concepts step by step.\n"
        "• Understand how the concepts are connected.\n"
        "• Practice simple examples.\n\n"

        "Stage 3 — Practice\n"
        "• Solve exercises related to the topic.\n"
        "• Practice regularly.\n"
        "• Identify and correct your mistakes.\n\n"

        "Stage 4 — Mini Project\n"
        f"• Create a small project related to {topic}.\n"
        "• Apply the concepts you learned.\n"
        "• Try to complete the project independently.\n\n"

        "Stage 5 — Revision\n"
        "• Review the important concepts.\n"
        "• Practice questions and exercises.\n"
        "• Revise your difficult areas.\n\n"

        "Suggested Activities\n"
        "• Read study material.\n"
        "• Watch educational videos.\n"
        "• Practice examples.\n"
        "• Make short notes.\n"
        "• Complete a mini project.\n\n"

        "Revision Checkpoints\n"
        "• Review after each stage.\n"
        "• Test yourself with questions.\n"
        "• Revisit topics you find difficult.\n\n"

        "Goal\n"
        f"By the end of {timeline}, you should have a clear understanding "
        f"of the fundamentals of {topic} and some practical experience."
    )


async def get_learning_recommendations(
    topic: str,
    level: str = "beginner",
    timeline: str = "6 weeks"
) -> str:

    return local_learning_path(
        topic,
        level,
        timeline
    )