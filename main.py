from flask import Flask
from flask_cors import CORS


#creates the Flask app object, contains data about the app and methods (object functions)
#functions tell the app to do certain actions
app = Flask(__name__)
CORS(app)



#starts the debugger -- if code is malformed an error will appear
app.config["DEBUG"] = True
    

@app.route('/')
def home():
    return '<p>Hola</p>'


#@app.route('/test')
#def test():
#    return render_template('historical.html')


app.run()
