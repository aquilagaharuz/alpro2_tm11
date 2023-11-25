from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, template_folder='templates')

default_messages = [
    "Makan patty itu spongebob",
    "Berdansalah, Patrick",
    "Ayo kita ke Jellyfish Fields!",
    "Saya suka krabby patty!",
    "Bikini Bottom sangat menyenangkan!",
    "Saya ingin memiliki rumah karang!",
    "Squidward adalah seniman!",
    "Mrs. Puff, saya sudah siap!",
    "Gary, jangan diam saja!",
    "Saya ingin menjadi Goofy Goober!"
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('nama')
        if name:
            welcome_message = f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib"
            return render_template(welcome_message=welcome_message)
        else:
            return render_template(welcome_message="Parameter 'nama' pada permintaan POST tidak ditemukan.")

    return render_template('nama.html')

@app.route('/PujaKerangAjaib', methods=['GET', 'POST'])
def pujakerangajaib():
    if request.method == 'GET':
        name = request.args.get('nama')
        if name:
            message = f"{name}, {random.choice(default_messages)}"
            return jsonify({"message": message})
        else:
            message = random.choice(default_messages)
            return jsonify({"message": message})

    elif request.method == 'POST':
        name = request.form.get('nama')
        if name:
            message = f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib"
            return jsonify({"message": message})
        else:
            return jsonify({"message": "Parameter 'nama' pada permintaan POST tidak ditemukan."})

if __name__ == '__main__':
    app.run(debug=True)