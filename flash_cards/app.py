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
    },
    {
        'question': 'When is multithreading good in Python? Can multithreading be slower than serial implementation?',
        'answer': 'MT is good for handling I/O (ex. loading 100 URIs) - in almost all cases MP is better. '
        + 'Multithreading can be slower than serial! In a threadpool only one thread is run at a time.'
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

app.run(debug=True)
