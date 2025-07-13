import os
import json
from flask import Flask, render_template, request, redirect, url_for
from models import db, TextEmbedding
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını oku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text']
        if text_input.strip():
            embedding = model.encode(text_input).tolist()  
            record = TextEmbedding(text=text_input, embedding_vector=json.dumps(embedding))
            db.session.add(record)
            db.session.commit()
        return redirect(url_for('index'))

    all_records = TextEmbedding.query.all()
    return render_template('index.html', records=all_records)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
