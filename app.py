from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)
app.secret_key = "tubes45-01_BENGPRO"

@app.route("/line")
def index():
	flash("Ketikkan truth atau dare")
	return render_template("index.html")

def indexx():
	flash("Hukuman kamu adalah")
	return render_template("indexx.html")

def indexxx():
	flash("Keren banget!!")
	return render_template("indexxx.html")

t = {'Kalau kamu bisa jadi tidak terlihat, apa hal pertama yang akan kamu lakukan?':1, 
        'Apa rahasia yang kamu sembunyikan dari orangtuamu?':2,
        'Siapa orang yang diam-diam kamu sukai?' :3,
        'Siapa orang terakhir yang kamu kepoin di media sosial?':4,
        'Kalau ada jin yang memberikanmu tiga permohonan, apa yang kamu inginkan?':5,
        'Jika kamu kembali ke masa lalu, apa yang akan kamu lakukan?':6,
        'Apa tontonan favoritmu saat masih kecil?': 7,
        'Siapa orang yang paling sering kamu chat?':8,
        'Apa kebohongan terbesar yang pernah kamu katakan kepada orangtuamu?':9,
        'Apa mimpi paling aneh yang pernah kamu alami?':10,
        'Ceritakan detail ciuman pertamamu…':11,
        'Kapan terakhir kali kamu ngompol atau eek di celana?':12,
        'Menurutmu, hewan apa yang terlihat paling mirip denganmu?':13,
        'Di antara temanmu, siapa orang yang paling kamu suka dalam konteks romantis?':15,
        'Di antara temanmu, siapa orang yang menurutmu paling baik dan paling buruk sifatnya?':16,
        'Siapa mantan terindahmu?':16,
        'Siapa orang yang ingin kamu jadikan istri/suami?':17,
        'Apakah kamu pernah melakukan ghosting?':18,
        'Apa aib yang kamu sembunyikan dari teman-temanmu?':19,
        'Berapa jumlah mantanmu? sebutkan!':20,
        }
tth = random.choice(list(t.keys()))
	
d = {'Lakukan rap gaya bebas selama 3 menit!':1, 
        'Biarkan orang lain membuat status menggunakan akun sosial mediamu!':2,
        'Berikan ponselmu kepada salah satu di antara kita dan biarkan orang tersebut mengirim satu pesan kepada siapapun yang dia mau!' :3,
        'Cium salah satu kaus kaki di antara temanmu!':4,
        'Makan satu gigitan kulit pisang!':5,
        'Peragakan salah satu orang di antara kita sampai ada yang bisa menebak siapa orang yang diperagakan!':6,
        'Nyanyikanlah salah lagu lagu dari Rossa!': 7,
        'Tirukan seorang selebriti sampai ada yang bisa menebak!':8,
        'Bertingkahlah seperti Hotman Paris selama 2 menit!':9,
        'Biarkan satu orang menggambar tato di wajahmu!':10,
        'Tutuplah mata lalu raba muka salah satu di antara kita sampai kamu bisa menebak siapa orang itu!':11,
        'Ungkapkan persaanmu kepada gebetanmu!':12,
        'Push up 20 kali!':13,
        'Kayang selama satu menit!':15,
        'Plank selama satu menit!.':16,
        'Coba teriak “aku sayang kamu” sekarang juga!':16,
        'Baca dengan lantang pesan yang terakhir kali kamu kirim ke gebetanmu!':17,
        'Telepon seorang teman dan katakan selamat ulang tahun sambil menyanyikan lagu!':18,
        'Tunjukkan gerakan dance terbaikmu!':19,
        'Parodikan adegan di film India kesukaanmu!':20,
        }
dare = random.choice(list(d.keys()))

h = {'Push up 20 kali sambil nyanyi lagu Bagimu Negeri':1, 
        'Sit up 30 kali':2,
        'Teriak Aku sayang dia sekarang' :3,
        'Beliin teman kamu permen':4,
        'Gendong salah satu temanmu':5,
        'Lompat-lompat selama 2 menit':6,
        'Ngerap selama 2 menit': 7,
        'Nyanyikan sebuah lagu anak-anak':8,
        'Bertingkahlah seperti Hotman Paris selama 2 menit!':9,
        'Kayang selama 30 detik':10,
        }
hukuman = random.choice(list(h.keys()))

@app.route("/mulai", methods=['POST', 'GET'])
def truthordare():
	if (request.form['name_input']=="truth"):
		flash("Jawab jujur ya...."+ tth)
		flash("\n") 
		flash("Apakah bisa menjawabnya? Ketik 'bisa' jika bisa menjawab dan ketik 'gabisa' jika tidak mampu melakukannya")
		return render_template("index.html")

	if (request.form['name_input']=="dare"):
		flash("Lakukan tantangannya dengan benar ya...."+ dare)
		flash("\n") 
		flash("Apakah bisa melakukannya? Ketik 'bisa' jika mampu melakukannya dan ketik 'gabisa' jika tidak mampu melakukannya")
		return render_template("index.html")
		
	if (request.form['name_input']=="gabisa"):
		flash(hukuman)
		flash("\n")
		flash("Semangat ngejalanin hukumannya!! Untuk melanjutkan games ini ke temanmu, silahkan ketik 'lanjut' dan jika keluar dari games ketik 'selesai'")
		return render_template("indexx.html")
	
	if (request.form['name_input']=="bisa"):
		flash("Wahh hebat lho kamu bisa menjawab pertanyaannya!!")
		flash("\n")
		flash("Untuk melanjutkan games ini ke temanmu, silahkan ketik 'lanjut' dan jika keluar dari games ketik 'selesai'")
		return render_template("indexxx.html")
	
	if (request.form['name_input']=="lanjut"):
		index()
