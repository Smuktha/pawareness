from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)
            
quizData = [
    {
        
        "question": "You receive an email claiming you've won a $1,000 gift card, but it asks for your credit card details to claim the prize. Is this phishing or legitimate?",
        "options": ["Phishing", "Legitimate"],
        "answer": "Phishing"
    },
    {
        "question": "An email from your bank asks you to confirm your account by logging in via a link provided. The email uses your full name and account number. Is this phishing or legitimate?",
        "options": ["Phishing", "Legitimate"],
        "answer": "Phishing"
    },
    {
        "question": "A newsletter email from an online store you subscribed to includes a discount code for their products. Is this phishing or legitimate?",
        "options": ["Phishing", "Legitimate"],
        "answer": "Legitimate"
    },
    {
        "question": "You receive a message from someone you don't know, claiming to be from a tech support company. They ask you to install software to fix an issue on your computer. Is this phishing or legitimate?",
        "options": ["Phishing", "Legitimate"],
        "answer": "Phishing"
    },
    {
        "question": "You receive an email with an attachment claiming to be an invoice for a purchase you never made. The sender's email address looks strange. Is this phishing or legitimate?",
        "options": ["Phishing", "Legitimate"],
        "answer": "Phishing"
    },
    {
        "question": "An email from your bank with a warning about unusual activity in your account asks you to click a link to verify your information. Is this phishing or legitimate?",
        "options": ["Phishing", "Legitimate"],
        "answer": "Phishing"
    },
    {
        "question": "A pop-up window appears while you're browsing a website, claiming your computer is infected with a virus. It asks you to download software to fix the issue. Is this phishing or legitimate?",
        "options": ["Phishing", "Legitimate"],
        "answer": "Phishing",
        "image": "D:\Phishing-Awareness-Campaign\templates\pic1.jpg" 
    }
]


# Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# Learn Page
@app.route('/learn')
def learn():
    return render_template('learn.html')

# Simulations Page
@app.route('/simulate')
def simulate():
    return render_template('simulate.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)

