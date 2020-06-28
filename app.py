from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.vars = {}

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def get_ticker():
    if request.method == 'GET':
        return render_template('ticker.html')
    else:
        app.vars['name'] = request.form['name_ticker']
        return redirect(url_for('plot_stock_data'))

@app.route('/plot_stock_data',methods=['GET','POST'])
def plot_stock_data():
   return 'Plot data for ' + app.vars['name'] 


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
