from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql   
from sqlalchemy.sql import text
from sqlalchemy import create_engine

app = Flask(__name__)     
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:st0rmg0d@localhost/webserver'  
db = SQLAlchemy(app)  

engine = create_engine('postgresql://postgres:st0rmg0d@localhost/webserver') 

class user(db.Model):          
    __tablename__ = 'user'
    usserid = db.Column('usserid', db.Integer, primary_key=True)   
    login = db.Column('login', db.Unicode)
    password = db.Column('password', db.Unicode)
    token = db.Column('token', db.Unicode)

    def __init__(self,usserid,login,password, token):  
        self.usserid = usserid
        self.login = login
        self.password = password
        self.token = token

    login = ''     
    password = ''  

    def tablefunc(id):                       
        with engine.connect() as connection:
            result = connection.execute(text("select login, password from usser where usser.usserid = "+str(id)))
            for row in result:
                global loginn, passwordd
                loginn = row['login']
                passwordd = row['password']
        connection.close()   
