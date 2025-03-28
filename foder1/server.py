from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a pre-trained conversational model
chatbot = pipeline('conversational', model='facebook/blenderbot-400M-distill')

# College-specific knowledge base
college_info = {
    "about": "Sumathi Reddy Institute of Technology for Women (SRITW) is a premier engineering college for women, offering various undergraduate and postgraduate programs.",
    "courses": "SRITW offers B.Tech in CSE, ECE, EEE, and IT, along with M.Tech programs in various specializations.",
    "admissions": "Admissions are based on merit and entrance exam scores. Visit https://sritw.org/admissions for more details.",
    "facilities": "The college has state-of-the-art labs, a well-stocked library, sports facilities, and modern classrooms.",
    "contact": "You can contact SRITW at +91-123-4567890 or email info@sritw.org. Address: Hyderabad, Telangana, India."
}

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message'].lower()
    
    # Check for college-specific queries
    for keyword, response in college_info.items():
        if keyword in user_message:
            return jsonify({'response': response})
    
    # Use AI model for general conversation
    result = chatbot(user_message)
    return jsonify({'response': result[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
