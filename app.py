from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)

#from flask import Flask
#app = Flask(__name__)
#
#@app.route('/')
#def index():
#    # this is a comment, just like in Python
#    # note that the function name and the route argument
#    # do not need to be the same.
#    return 'Hello World!'
#
#if __name__ == '__main__':
#  app.run(port=33507)
