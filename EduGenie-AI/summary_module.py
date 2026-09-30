import re


def local_summary(text: str, max_words: int = 120) -> str:
    text = text.strip()

    if not text:
        return "Please provide some text to summarize."

    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    selected = []
    word_count = 0

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        words = sentence.split()

        if word_count + len(words) <= max_words:
            selected.append(sentence)
            word_count += len(words)
        else:
            remaining = max_words - word_count

            if remaining > 0:
                selected.append(
                    " ".join(words[:remaining]) + "..."
                )

            break

    if not selected:
        words = text.split()
        return " ".join(words[:max_words]) + "..."

    return " ".join(selected)


async def summarize_text(
    text: str,
    max_words: int = 120
) -> str:

    return local_summary(
        text,
        max_words
    )