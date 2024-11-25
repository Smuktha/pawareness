// Placeholder for the email simulation check
function checkEmail() {
    alert("Check the sender's address and the URL in the email for signs of phishing.");
}

// Placeholder for the website simulation check
function checkWebsite() {
    alert("Ensure the URL matches the official domain and look for HTTPS encryption.");
}

// Quiz form submission (example)
document.getElementById('quiz-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var score = 0;
    var answer = document.querySelector('input[name="q1"]:checked');
    if (answer && answer.value === "A") {
        score += 1;
    }
    document.getElementById('score').innerText = "Your score: " + score + "/1";
});

// Report form submission (example)
document.getElementById('report-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert("Thank you for reporting. Your submission has been received.");
});
