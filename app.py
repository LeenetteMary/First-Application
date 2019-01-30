from flask import Flask, render_template
app = Flask(__name__)

#@app.route('/')

#def sample():
    #a,b = 0,1
    #while a < 10:
      #  print(a)
       # a,b = b,a+b

#@app.route('/web')
#def web():
#       return render_template('index.html')

@app.route('/index') 
def index():
  return render_template('index.html')


if __name__=='__main__':
  app.run(debug=True) 