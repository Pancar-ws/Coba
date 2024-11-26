

bank_soal = ("Pulau Komodo terletak di provinsi?",
        "Siapa Presiden Indonesia ketiga Indonesia?",
        "Apa singkatan dari MPR?",
        "Pada tanggal berapakah Hari Lahir Pancasila diperingati?",
        "Apa julukan terkenal dari negara Korea Selatan?")

pilihan = (("A. Bali", "B. NTT", "C. NTB", "D. Jawa Timur", "E. Jawa Barat"),
           ("A. B.J Habibie ", "B. Jokowi", "C. Soekarno", "D. Abdurahman Wahid", "E. Prabowo Subianto"),
           ("A. Majelis Perwakilan Rakyat", "B. Majelis Permusyawaratan Rakyat", "C. Majelis Perhimpunan Rakyat", "D. Majelis Perserikatan Rakyat", "E. Majelis Perkumpulan Rakyat"),
           ("A. 17 Agustus", "B. 1 Maret", "C. 1 Juni ", "D. 1 Desember", "E. 1 Januari"),
           ("A. Negeri Tirai Bambu", "B. Negeri Gingseng", "C. Zamrud Khatulistiwa", "D. Negeri Kincir Angin", "E. Lumbung Padi Dunia"))

jawaban = ("B", "A", "B", "C", "B")
jawaban_user = []
skor = 0
nomor_soal = 0

for i in bank_soal:
    print("----------------------------")
    print(i)
    for j in pilihan[nomor_soal]:
        print(j)

    jawab = input("Masukkan (A, B, C, D, Ea): ").upper()
    jawaban_user.append(jawab)
    if jawab == jawaban[nomor_soal]:
        skor += 1
        print("Jawaban Anda BENAR!")
    else:
        print("Jawaban Anda SALAH!")
        print(f"Jawaban yang benar adalah {jawaban[nomor_soal]}")
    nomor_soal += 1

print("----------------------------")
print("           HASIL            ")
print("----------------------------")

print("kunci: ", end="")
for a in jawaban:
    print(a, end=" ")
print()

print("jawabanmu: ", end="")
for b in jawaban_user:
    print(b, end=" ")
print()

skor = int(skor / len(bank_soal) * 100)
print(f"Skor Anda adalah {skor}%")