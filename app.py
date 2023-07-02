from flask import Flask,request,render_template
import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

@app.route("/",methods=['GET','POST'])
def student_page():
    from models.user import User
    data = User.query.all()
    print(data)
    if request.method=="POST":
        name = request.form.get("userName")
        rollNo = request.form.get("rollNo")
        mobileNo = request.form.get("mobileNo")
        dob = request.form.get("DoB")
        parsed_dob = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
        new_user = User(userName=name, rollNo=rollNo, mobileNo=mobileNo, date_of_birth=parsed_dob)
        db.session.add(new_user)
        db.session.commit()
        data = User.query.all()
    return render_template('index.html',data=data)



if __name__ == "__main__":
    app.run(debug=True,static_folder='/static')

