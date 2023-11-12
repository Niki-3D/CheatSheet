# from . import db

# class Title(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)

# class Detail(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title_id = db.Column(db.Integer, db.ForeignKey('title.id'), nullable=False)
#     info = db.Column(db.Text, nullable=False)

#     title = db.relationship('Title', backref=db.backref('details', lazy=True))
