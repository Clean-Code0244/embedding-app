from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TextEmbedding(db.Model):
    __tablename__ = 'text_embeddings'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    embedding_vector = db.Column(db.Text, nullable=False)  # JSON formatında
