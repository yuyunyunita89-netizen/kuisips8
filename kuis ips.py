# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print()
# IPS - Pulau Jawa
print("🌏 Selamat datang di pembelajaran IPS Artventure!")
print("Hari ini kita akan belajar tentang Pulau Jawa, salah satu wilayah penting di Indonesia.\n")

# Materi
print("📘 Materi IPS: Pulau Jawa")
print("""
Pulau Jawa adalah salah satu pulau terbesar dan terpadat penduduknya di Indonesia.
Ibu kota negara, Jakarta, terletak di pulau ini. Pulau Jawa terdiri dari 6 provinsi:
1. DKI Jakarta
2. Jawa Barat
3. Banten
4. Jawa Tengah
5. DI Yogyakarta
6. Jawa Timur

Ciri khas Pulau Jawa:
- Pusat pemerintahan dan ekonomi Indonesia.
- Mayoritas masyarakat bekerja di sektor pertanian, perdagangan, dan industri.
- Budaya Jawa terkenal dengan wayang, batik, gamelan, serta berbagai upacara adat.
- Gunung berapi aktif banyak terdapat di Jawa, contohnya Gunung Merapi dan Gunung Bromo.
- Pulau Jawa menjadi pusat perkembangan sejarah kerajaan-kerajaan besar seperti Majapahit dan Mataram.
""")

print("\nSekarang, coba jawab pertanyaan berikut!\n")
score = 0

# Pertanyaan
questions = [
    ("Provinsi manakah yang termasuk bagian dari Pulau Jawa?", 
     {"a": "Sumatera Utara", "b": "Jawa Tengah", "c": "Kalimantan Timur"}, "b"),

    ("Gunung berapi terkenal yang ada di Jawa adalah...", 
     {"a": "Merapi", "b": "Kerinci", "c": "Rinjani"}, "a"),

    ("Kerajaan besar yang pernah berdiri di Pulau Jawa adalah...", 
     {"a": "Sriwijaya", "b": "Majapahit", "c": "Kutai"}, "b"),

    ("Ibu kota Indonesia, Jakarta, terletak di provinsi...", 
     {"a": "Jawa Barat", "b": "DKI Jakarta", "c": "Banten"}, "b"),

    ("Budaya Jawa yang menggunakan boneka kulit disebut...", 
     {"a": "Wayang", "b": "Reog", "c": "Kuda Lumping"}, "a"),

    ("Batik Indonesia diakui UNESCO sebagai warisan budaya dunia pada tahun...", 
     {"a": "2005", "b": "2009", "c": "2013"}, "b"),

    ("Gunung Bromo berada di provinsi...", 
     {"a": "Jawa Tengah", "b": "DI Yogyakarta", "c": "Jawa Timur"}, "c"),

    ("Bahasa utama yang digunakan mayoritas masyarakat Jawa adalah...", 
     {"a": "Bahasa Sunda", "b": "Bahasa Jawa", "c": "Bahasa Betawi"}, "b"),

    ("Tari tradisional yang berasal dari Yogyakarta adalah...", 
     {"a": "Tari Saman", "b": "Tari Bedhaya", "c": "Tari Piring"}, "b"),

    ("Candi Borobudur yang terkenal berada di provinsi...", 
     {"a": "Jawa Tengah", "b": "Jawa Timur", "c": "Banten"}, "a"),
]

# Loop pertanyaan
for i, (q, opts, correct) in enumerate(questions, 1):
    print(f"{i}. {q}")
    for key, val in opts.items():
        print(f"{key}. {val}")
    answer = input("Your answer: ").lower()

    if answer == correct or answer == opts[correct].lower():
        print("✅ Benar!\n")
        score += 1
    else:
        print(f"❌ Salah! Jawaban yang benar adalah {opts[correct]}.\n")

# Hasil
print("🎉 Quiz selesai! Skor kamu:", score, "/", len(questions))
if score == 10:
    print("🔥 Perfect! Kamu master IPS tentang Pulau Jawa! 👑")
elif score >= 7:
    print("Keren! Kamu paham banget materi ini. 👏")
elif score >= 4:
    print("Not bad! Masih perlu belajar lagi 😎")
else:
    print("Tetap semangat belajar IPS ya! 🌏")