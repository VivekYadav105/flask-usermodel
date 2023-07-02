from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), unique=False, nullable=False)
    rollNo = db.Column(db.String(20), unique=True, nullable=False)
    mobileNo = db.Column(db.String(10), unique=False, nullable=False)
    date_of_birth = db.Column(db.Date)

    def __repr__(self):
        return f'<User {self.userName}>'

    def __str__(self):  
        return f'UserName:{self.userName}\nrollNo:{self.rollNo}\nmobile no:{self.mobileNo}\ndate of birth:{self.date_of_birth}'

db.create_all()