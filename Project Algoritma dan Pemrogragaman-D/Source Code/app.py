from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Diperlukan untuk flash message

@app.route("/", methods=["GET", "POST"])
def index():
    # Data soal, pilihan, dan jawaban
    bank_soal = [
        "Pulau Komodo terletak di provinsi?",
        "Siapa Presiden Indonesia ketiga?",
        "Apa singkatan dari MPR?",
        "Pada tanggal berapakah Hari Lahir Pancasila diperingati?",
        "Apa julukan terkenal dari negara Korea Selatan?"
    ]

    pilihan_soal = [
        ["A. Bali", "B. NTT", "C. NTB", "D. Jawa Timur", "E. Jawa Barat"],
        ["A. B.J Habibie", "B. Jokowi", "C. Soekarno", "D. Abdurahman Wahid", "E. Prabowo Subianto"],
        ["A. Majelis Perwakilan Rakyat", "B. Majelis Permusyawaratan Rakyat", "C. Majelis Perhimpunan Rakyat", "D. Majelis Perserikatan Rakyat", "E. Majelis Perkumpulan Rakyat"],
        ["A. 17 Agustus", "B. 1 Maret", "C. 1 Juni", "D. 1 Desember", "E. 1 Januari"],
        ["A. Negeri Tirai Bambu", "B. Negeri Gingseng", "C. Zamrud Khatulistiwa", "D. Negeri Kincir Angin", "E. Lumbung Padi Dunia"]
    ]

    jawaban = ["B", "A", "B", "C", "B"]

    if request.method == "POST":
        jawaban_user = []
        skor = 0
        is_complete = True

        # Ambil jawaban dari formulir
        for i in range(len(bank_soal)):
            user_jawaban = request.form.get(f"jawaban{i}")  # None jika kosong
            if not user_jawaban:
                is_complete = False
                flash("Harap jawab semua soal sebelum mengirim!", "danger")
                break
            jawaban_user.append(user_jawaban)
            if user_jawaban == jawaban[i]:
                skor += 1

        if is_complete:
            skor = int(skor / len(bank_soal) * 100)  # Hitung skor dalam persen
            return render_template("index.html", skor=skor, jawaban=jawaban, jawaban_user=jawaban_user, bank_soal=bank_soal, pilihan_soal=pilihan_soal)

    # GET atau jika ada kesalahan
    return render_template("index.html", skor=None, bank_soal=bank_soal, pilihan_soal=pilihan_soal)
