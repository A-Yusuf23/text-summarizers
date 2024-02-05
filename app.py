from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_word', methods=['POST'])
def predict_word():
    data = request.get_json()
    word = data['word']
    
    # Use bigram model to predict the next word
    next_word = predict_next_word_bigram(word)

    return jsonify({'next_word': next_word})

@app.route('/suggest_emoticons', methods=['POST'])
def suggest_emoticons_route():
    data = request.get_json()
    tokens = data['tokens']

    # Use the suggest_emoticons function to get emoticon suggestions
    emoticons = suggest_emoticons(tokens)

    return jsonify({'emoticons': emoticons})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
