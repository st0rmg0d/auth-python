from datetime import datetime, timedelta
from re import U
from flask import Flask, request          
from flask.helpers import make_response
import jwt
from sqlalchemy.orm import session
import dbtable                    


app = dbtable.app                               
app.config['SECRET_KEY'] = 'flasksecretkey'     
 

@app.route('/login')
def login():                               
    auth = request.authorization
    id = 5                         
    dbtable.user.tablefunc(id)
    if auth and auth.username == dbtable.loginn and auth.password == dbtable.passwordd: 
        login.token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])  
        
        update_this =   dbtable.user.query.filter_by(usserid=id).first()  
        update_this.token = '''{}'''.format(login.token)                            
        dbtable.db.session.commit()
        
        return "token: " + '''{}'''.format(login.token)   
    return make_response('Could not found a user with login: ' + dbtable.loginn, 401, {'WWW-Authenticate': 'Basic realm="Login required'}) 

@app.route('/protected')
def protected():                            
    token = request.args.get('token')                 
    protected.tokenvalue = '''{}'''.format(token)        
    login.token = '''{}'''.format(login.token)         
    if login.token == protected.tokenvalue:                               
        return '<h1>Hello, token which is provided is correct </h1>'    
    else:
        return '<h1>Hello, Could not verify the token </h1>'  


if __name__ == '__main__':   
    app.run(debug=True)
