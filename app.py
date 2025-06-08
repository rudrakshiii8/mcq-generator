from flask import Flask, render_template, request
from mcq_data import mcq_bank

app = Flask(__name__)

@app.route('/')
def home():
    topics = list(mcq_bank.keys())
    return render_template('index.html', topics=topics)

@app.route('/quiz', methods=['POST'])
def quiz():
    selected_topic = request.form.get('topic')
    if selected_topic not in mcq_bank:
        return "Invalid Topic", 400
    questions = mcq_bank[selected_topic]
    return render_template('quiz.html', topic=selected_topic, questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form.get('topic')
    questions = mcq_bank.get(topic, [])
    score = 0
    results = []

    for i, q in enumerate(questions):
        selected = request.form.get(f'q{i}')
        correct = q['answer']
        is_correct = (selected == correct)
        if is_correct:
            score += 1
        results.append({
            'question': q['question'],
            'selected': selected,
            'correct': correct,
            'is_correct': is_correct,
            'options': q['options']
        })

    return render_template('result.html', score=score, total=len(questions), topic=topic, results=results)

if __name__ == '__main__':
    app.run(debug=True)
