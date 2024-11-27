from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.jinja_env.globals['enumerate'] = enumerate

# Bank soal dan jawaban
questions = [
    {
        "question": "Pulau Komodo terletak di provinsi?",
        "options": ["A. Bali", "B. NTT", "C. NTB", "D. Jawa Timur"],
        "answer": "B"
    },
    {
        "question": "Siapa Presiden Indonesia ketiga?",
        "options": ["A. B.J Habibie", "B. Jokowi", "C. Soekarno", "D. Abdurahman Wahid"],
        "answer": "A"
    },
    {
        "question": "Apa singkatan dari MPR?",
        "options": [
            "A. Majelis Perwakilan Rakyat",
            "B. Majelis Permusyawaratan Rakyat",
            "C. Majelis Perhimpunan Rakyat",
            "D. Majelis Perserikatan Rakyat"
        ],
        "answer": "B"
    },
    {
        "question": "Pada tanggal berapakah Hari Lahir Pancasila diperingati?",
        "options": ["A. 17 Agustus", "B. 1 Maret", "C. 1 Juni", "D. 1 Desember"],
        "answer": "C"
    },
    {
        "question": "Apa julukan terkenal dari negara Korea Selatan?",
        "options": ["A. Negeri Tirai Bambu", "B. Negeri Ginseng", "C. Zamrud Khatulistiwa", "D. Negeri Kincir Angin"],
        "answer": "B"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answers = request.form
        score = 0
        correct_answers = [q["answer"] for q in questions]
        
        for i, answer in enumerate(correct_answers):
            if user_answers.get(f"question-{i}") == answer:
                score += 1

        return render_template("result.html", score=score, total=len(questions))
    return render_template("quiz.html", questions=questions)

