from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

app.config['DEBUG'] - False

# Daftar gambar dan jawaban
images = [
    {
        'url': 'https://images.unsplash.com/photo-1518717758536-85ae29035b6d?auto=format&fit=crop&w=400&h=400&q=80',
        'answer': 'anjing'
    },
    {
        'url': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&h=400&q=80',
        'answer': 'gunung'
    },
    {
        'url': 'https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=400&h=400&q=80',
        'answer': 'burung'
    },
    {
        'url': 'https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=400&h=400&q=80',
        'answer': 'kelinci'
    },
    {
        'url': 'https://images.unsplash.com/photo-1470770903676-69b98201ea1c?auto=format&fit=crop&w=400&h=400&q=80',
        'answer': 'gajah'
    }
]

@app.route('/')
def index():
    return render_template('index.html', image=images[0], index=0)

@app.route('/next/<int:index>')
def next_image(index):
    if index + 1 < len(images):
        return jsonify(images[index + 1])
    else:
        return jsonify({'message': 'Terima kasih sudah bermain!', 'image': None})


@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    guess = data['guess'].strip().lower()
    index = data['index']
    correct_answer = images[index]['answer'].lower()

    if guess == correct_answer:
        return jsonify({'result': 'correct', 'message': '🎉 Benar! Selamat!'})
    else:
        return jsonify({'result': 'incorrect', 'message': 'Salah! Coba lagi.'})


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=8000)