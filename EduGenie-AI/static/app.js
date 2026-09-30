const form = document.getElementById("assistantForm");
const userInput = document.getElementById("userInput");

const levelWrap = document.getElementById("levelWrap");
const countWrap = document.getElementById("countWrap");
const timelineWrap = document.getElementById("timelineWrap");
const wordsWrap = document.getElementById("wordsWrap");

const level = document.getElementById("level");
const questionCount = document.getElementById("questionCount");
const timeline = document.getElementById("timeline");
const maxWords = document.getElementById("maxWords");

const inputLabel = document.getElementById("inputLabel");
const submitBtn = document.getElementById("submitBtn");

const resultWrap = document.getElementById("resultWrap");
const result = document.getElementById("result");
const resultTitle = document.getElementById("resultTitle");
const errorBox = document.getElementById("error");

const taskButtons = document.querySelectorAll(".task");

let currentTask = "qa";


function hideAllOptions() {
    levelWrap.classList.add("hidden");
    countWrap.classList.add("hidden");
    timelineWrap.classList.add("hidden");
    wordsWrap.classList.add("hidden");
}


function setTask(task) {

    currentTask = task;

    taskButtons.forEach(function(button) {
        button.classList.remove("active");
    });

    taskButtons.forEach(function(button) {
        if (button.getAttribute("data-task") === task) {
            button.classList.add("active");
        }
    });

    hideAllOptions();

    resultWrap.classList.add("hidden");
    resultWrap.style.display = "none";

    errorBox.classList.add("hidden");
    errorBox.style.display = "none";
    errorBox.textContent = "";


    if (task === "qa") {

        inputLabel.textContent = "What would you like to know?";

        userInput.placeholder =
            "Example: Which is the largest ocean?";

        submitBtn.textContent =
            "✨ Generate Answer";
    }


    else if (task === "explain") {

        inputLabel.textContent =
            "What topic would you like explained?";

        userInput.placeholder =
            "Example: Explain photosynthesis";

        levelWrap.classList.remove("hidden");

        submitBtn.textContent =
            "✨ Explain Topic";
    }


    else if (task === "quiz") {

        inputLabel.textContent =
            "Enter the text or topic for the quiz";

        userInput.placeholder =
            "Example: Create a quiz about photosynthesis";

        countWrap.classList.remove("hidden");

        submitBtn.textContent =
            "✨ Generate Quiz";
    }


    else if (task === "summarize") {

        inputLabel.textContent =
            "Enter the text you want to summarize";

        userInput.placeholder =
            "Paste your text here...";

        wordsWrap.classList.remove("hidden");

        submitBtn.textContent =
            "✨ Summarize";
    }


    else if (task === "learn") {

        inputLabel.textContent =
            "What do you want to learn?";

        userInput.placeholder =
            "Example: I want to learn Python";

        levelWrap.classList.remove("hidden");
        timelineWrap.classList.remove("hidden");

        submitBtn.textContent =
            "✨ Create Learning Path";
    }
}


taskButtons.forEach(function(button) {

    button.addEventListener("click", function(event) {

        event.preventDefault();

        const task =
            button.getAttribute("data-task");

        setTask(task);
    });
});


form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const input = userInput.value.trim();

    if (!input) {

        errorBox.textContent =
            "Please enter something first.";

        errorBox.classList.remove("hidden");
        errorBox.style.display = "block";

        return;
    }

    errorBox.classList.add("hidden");
    errorBox.style.display = "none";

    resultWrap.classList.add("hidden");
    resultWrap.style.display = "none";


    try {

        let response;
        let data;


        if (currentTask === "qa") {

            response = await fetch("/qa", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: input
                })
            });

            data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error ||
                    data.detail ||
                    "Request failed."
                );
            }

            resultTitle.textContent = "Answer";
            result.textContent = data.answer;
        }


        else if (currentTask === "explain") {

            response = await fetch("/explain", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    topic: input,
                    level: level.value
                })
            });

            data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error ||
                    data.detail ||
                    "Request failed."
                );
            }

            resultTitle.textContent =
                "Explanation";

            result.textContent =
                data.explanation;
        }


        else if (currentTask === "quiz") {

            response = await fetch("/quiz", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    text: input,
                    question_count:
                        Number(questionCount.value)
                })
            });

            data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error ||
                    data.detail ||
                    "Request failed."
                );
            }

            ;resultTitle.textContent = "Quiz";

let quizHtml = "";

data.quiz.forEach(function(item, index) {

    quizHtml +=
        '<div class="quiz-question">' +
        '<h3>' +
        (index + 1) +
        ". " +
        item.question +
        "</h3>";

    item.options.forEach(function(option, optionIndex) {

        const letter =
            String.fromCharCode(65 + optionIndex);

        quizHtml +=
            '<div class="quiz-option">' +
            "<strong>" +
            letter +
            ".</strong> " +
            option +
            "</div>";
    });

    quizHtml +=
        '<div class="quiz-answer">' +
        "<strong>Answer:</strong> " +
        item.correct_answer +
        "</div>";

    quizHtml +=
        '<div class="quiz-explanation">' +
        "<strong>Explanation:</strong> " +
        item.explanation +
        "</div>";

    quizHtml += "</div>";
});

result.innerHTML = quizHtml;
        }


        else if (currentTask === "summarize") {

            response = await fetch("/summarize", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    text: input,
                    max_words:
                        Number(maxWords.value)
                })
            });

            data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error ||
                    data.detail ||
                    "Request failed."
                );
            }

            resultTitle.textContent =
                "Summary";

            result.textContent =
                data.summary;
        }


        else if (currentTask === "learn") {

            response = await fetch(
                "/learn/recommendations",
                {

                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        topic: input,
                        level: level.value,
                        timeline: timeline.value
                    })
                }
            );

            data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error ||
                    data.detail ||
                    "Request failed."
                );
            }

            resultTitle.textContent =
                "Learning Path";

            result.textContent =
                data.recommendations;
        }


        resultWrap.classList.remove("hidden");
        resultWrap.style.display = "block";

    }


    catch (error) {

        console.error(error);

        errorBox.textContent =
            error.message ||
            "Something went wrong.";

        errorBox.classList.remove("hidden");
        errorBox.style.display = "block";
    }

});


setTask("qa");