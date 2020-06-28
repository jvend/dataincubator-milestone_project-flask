from flask import Flask, render_template, request, redirect, url_for
from scrape_stocks.get_yahoo_finance_data import *

app = Flask(__name__)
app.vars = {}

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def get_ticker():
    if request.method == 'GET':
        return render_template('ticker.html')
    else:
        app.vars['name_ticker'] = request.form['name_ticker']
        return redirect(url_for('plot_stock_data'))

@app.route('/plot_stock_data',methods=['GET','POST'])
def plot_stock_data():
    from bokeh.plotting import figure
    from bokeh.resources import CDN
    from bokeh.embed import file_html
    
    
    ticker = app.vars['name_ticker']
    url = build_url(ticker) 
    page = requests.get(url)
    if page.status_code == 200:
        html = page.content.decode('utf-8')
        data = json.loads(html)['chart']['result'][0]
        datetimes   = list(map(datetime.fromtimestamp,data['timestamp']))
        close_data  = data['indicators']['quote'][0]['close']
        close_data  = [ el if el is not None else float("nan") for el in close_data ]

        #return str(close_data)

        # prepare some data
        y = close_data
        x = list(range(len(y)))

        # Get new days for x-ticks
        prev_day = -1; new_days = []
        for i in range(len(datetimes)):
            if datetimes[i].day != prev_day:
                prev_day = datetimes[i].day
                new_days.append(i)
            else: pass

        labels = [datetimes[i].strftime('%b %d') for i in new_days]

        plt_title = ticker + ' stock price for the past month' 
        # create a new plot with a title and axis labels
        p = figure(title=plt_title, x_axis_label='Day', y_axis_label='Stock Price (US$)')
        
        # add a line renderer with legend and line thickness
        p.line(x, y, legend_label="Close Price", line_width=2)
        p.xaxis.major_label_overrides = dict(zip(new_days, labels))
        p.xaxis.major_label_orientation = 'vertical'
        p.xaxis.ticker = new_days  
        
        # show the results
        html = file_html(p, CDN, "my plot")
        return html
    else:
        return 'Invalid ticker'
    #return render_template('stock_price.html')
    #  #return 'Plot data for ' + app.vars['name'] 


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
