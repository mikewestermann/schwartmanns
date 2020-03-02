from flask import Flask, render_template, request, redirect, url_for, make_response
import hashlib
import uuid
from models.user import User
from models.settings import db

app = Flask(__name__)

db.create_all()

@app.route("/")
def index():
    session_token = request.cookies.get("session_token")

    print(session_token)

    user = db.query(User).filter_by(session_token=session_token).first()

    return render_template("index.html", user=user)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        Vorname = request.form.get("Vorname")
        Nachname = request.form.get("Nachname")
        Name_des_Unternehmens = request.form.get("Name_des_Unternehmens")
        Position_im_Unternehmen = request.form.get("Position_im_Unternehmen")
        Email_Adresse = request.form.get("Email_Adresse")
        Passwort = request.form.get("Passwort")
        Passwort_wiederholen = request.form.get("Passwort_wiederholen")

        if Passwort != Passwort_wiederholen:
            return "Passwords do not match! Go back and try again."

        print(Email_Adresse)
        print(Passwort)
        print(Passwort_wiederholen)

        user = User(Vorname=Vorname, Nachname=Nachname, Name_des_Unternehmens=Name_des_Unternehmens, Position_im_Unternehmen=Position_im_Unternehmen, Email_Adresse=Email_Adresse, password_hash=hashlib.sha256(Passwort.encode()).hexdigest(), session_token=str(uuid.uuid4()) )
        db.add(user)
        db.commit()

        response = make_response(redirect(url_for("index")))
        response.set_cookie("session_token", user.session_token, httponly=True, samesite="Strict")

        return response

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        Email_Adresse = request.form.get("Email_Adresse")
        Passwort = request.form.get("Passwort")

        password_hash = hashlib.sha256(Passwort.encode()).hexdigest()

        user = db.query(User).filter_by(Email_Adresse=Email_Adresse).first()

        if not user:
            return "This user does not exist"
        else:
            if password_hash == user.password_hash:
                user.session_token = str(uuid.uuid4())
                db.add(user)
                db.commit()

                response = make_response(redirect(url_for("index")))
                response.set_cookie("session_token", user.session_token, httponly=True, samesite="Strict")

                return response
            else:
                return "Your password is incorrect"

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "GET":
        return render_template("dashboard.html")    
    elif request.method == "POST":
        name = db.query(Machine_models).filter_by(name=name).first()

                    
if __name__ == "__main__":
    app.run()