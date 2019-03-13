from flask import Flask, render_template, request

app = Flask("flash_cards")

questions = [
    {
    'question': 'What is the difference between concurrent and parallel?',
    'answer': 'Concurrent means different tasks carried out in seemingly parallel run,'
        + ' whereas parallel means to run tasks exactly at the same time',
    },
    {
        'question': 'What is multiprocessing and multithreading?',
        'answer': 'Multiprocessing is creating a seperate space in memory for the application run some task'
            + 'Multithreading differs in that it uses the same memory space as a process, whereas processes are seperate from each other',
    }
]

@app.route("/")
def display_home():
    return render_template("index.html")

@app.route("/quiz")
def display_quiz():
    return render_template("index.html", title="quiz", questions=questions)

@app.route("/tutorials")
def display_videos():
    return render_template("tutorials.html", title="Flask Tutorials")

if __name__ == '__main__':
    app.run(debug=True)
