
from flask import Flask, request, abort
from flask_bcrypt import Bcrypt
from config import ApplicationConfig
from models import db, User

app = Flask(__name__)
app.config.from_object(ApplicationConfig)


db.init_app(app)

with app.app_context():    
    db.create_all()
    
@app.route("/register", method=["POST"])
def register_user():
    email = request.json["email"]
    password = request.json["password"]
    
    user_exists = User.query.filter_by(email=email).first() is not None
    if user_exists:
        abort(409)
        
    new_user = User(email=email, password=password)

    
    
    
    
    
    

if __name__=="__main__":
    app.run(debug=True)