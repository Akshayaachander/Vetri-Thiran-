async function generateContent(type) {

    const topicElement = document.getElementById("topic");
    const resultElement = document.getElementById("result");
    const loadingElement = document.getElementById("loading");

    const topic = topicElement.value.trim();

    if (!topic) {
        resultElement.textContent = "Please enter a topic first.";
        return;
    }

    loadingElement.classList.remove("hidden");
    resultElement.innerHTML = "";

    try {

        const response = await fetch(`/${type}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                topic: topic
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }

        displayResult(type, data);

    } catch (error) {

        resultElement.textContent =
            "Error: " + error.message;

    } finally {

        loadingElement.classList.add("hidden");
    }
}


function displayResult(type, data) {

    const resultElement = document.getElementById("result");

    if (type === "explain") {

        resultElement.textContent =
            data.explanation || "No explanation received.";

        return;
    }


    if (type === "summarize") {

        resultElement.textContent =
            data.summary || "No summary received.";

        return;
    }


    if (type === "quiz") {

        resultElement.innerHTML = "";

        data.quiz.forEach((item, index) => {

            const card = document.createElement("div");
            card.className = "quiz-card";

            const question = document.createElement("h3");
            question.textContent =
                `${index + 1}. ${item.question}`;

            card.appendChild(question);

            item.options.forEach(option => {

                const optionElement =
                    document.createElement("div");

                optionElement.className = "option";

                optionElement.textContent = option;

                card.appendChild(optionElement);
            });

            const answer =
                document.createElement("p");

            answer.innerHTML =
                `<strong>Answer:</strong> ${item.correct_answer}`;

            card.appendChild(answer);

            const explanation =
                document.createElement("p");

            explanation.innerHTML =
                `<strong>Explanation:</strong> ${item.explanation}`;

            card.appendChild(explanation);

            resultElement.appendChild(card);
        });

        return;
    }


    if (type === "questions") {

        resultElement.innerHTML = "";

        data.questions.forEach((item, index) => {

            const card = document.createElement("div");

            card.className = "question-card";

            card.innerHTML = `
                <h3>${index + 1}. ${item.question}</h3>
                <p><strong>Answer:</strong> ${item.answer}</p>
                <p><strong>Difficulty:</strong> ${item.difficulty}</p>
            `;

            resultElement.appendChild(card);
        });

        return;
    }


    if (type === "learning-path") {

        resultElement.innerHTML = "";

        const title = document.createElement("h3");

        title.textContent =
            data.topic || "Learning Path";

        resultElement.appendChild(title);

        data.steps.forEach(step => {

            const card = document.createElement("div");

            card.className = "path-card";

            card.innerHTML = `
                <h3>Step ${step.step}: ${step.title}</h3>
                <p>${step.description}</p>
            `;

            resultElement.appendChild(card);
        });

        return;
    }
}
