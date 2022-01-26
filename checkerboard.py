from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('checkerboard.html', x=8,y=8)

@app.route('/<int:x>') #NOTE: could put in the return statement: x=int(x)
def changeNum1(x):
    return render_template('checkerboard.html', x=x, y=8)

@app.route('/<int:x>/<int:y>')
def changeXY(x,y):
    return render_template('checkerboard.html', x=x, y=y)

@app.route('/<int:x>/<int:y>/<color1>')
def colorChange(x,y,color1):
    return render_template('checkerboard.html', x=x, y=y, color1=color1)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def colorChanges(x, y, color1, color2):
    
    return render_template('checkerboard.html', x=x, y=y, color1=color1, color2=color2)


if __name__=='__main__':  #Ensure this file is being run directly and not from a different module.
    app.run(debug=True)   #Run the app in 'DEBUG' mode. this should be the last statement in our files. 
