from flask import Flask, render_template, request, jsonify, session
import pandas as pd

# Load data
df = pd.read_excel(r"/home/ammar99/mysite/FAQ_data.xlsx") 

# make a dict for questions and answers
questions_answers = dict(zip(df['Question'], df['Answer']))  

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key to start the session

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ask for Username 
        username = request.form.get('username')
        session['username'] = username
        return render_template('index_chat.html')  

    return render_template('start_chat.html')  

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['question']
    answer = questions_answers.get(user_question, "Sorry, I don't have an answer for that.")
    return jsonify({'answer': answer})

@app.route('/suggest_questions', methods=['GET'])
def suggest_questions():
    sample_questions = df['Question'].sample(n=5).tolist()  
    return jsonify({'questions': sample_questions})

@app.route('/filter_questions', methods=['GET'])
def filter_questions():
    input_text = request.args.get('input', '').lower()
    filtered_questions = df['Question'][df['Question'].str.lower().str.contains(input_text)].tolist()
    return jsonify({'questions': filtered_questions})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  
