from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/getvalue', methods=['POST'])
# def data():
#   df = pd.read_excel('/home/runner/GFGHack/assets/toughestsport.xlsx')
#   return df
# def check(l,sport,df):
#   sport = sport[0].upper()+sport[1:].lower()
#   s=(df.loc[df['SPORT'] == s])
#   p=['END',	'STR',	'PWR',	'SPD',	'AGI',	'FLX',	'NER',	'DUR',	'HAN',	'ANA']
#   s = s[p].values
#   o=[]
#   for i in range(10):
#     if l[i]< s[0][i]:
#       o.append(p[i])
#   return o
def getvalue():
    # df = data()
    df = pd.read_excel('/home/runner/GFGHack/assets/toughestsport.xlsx')
    feed = [request.form['feedback_text'],request.form['feedback_text1'],request.form['feedback_text2'],request.form['feedback_text3'],request.form['feedback_text4'],request.form['feedback_text5'],request.form['feedback_text6'],request.form['feedback_text7'],request.form['feedback_text8'],request.form['feedback_text9']]
    print(feed)
    
    sport = request.form['sport']
    # o=check(feed,sport,df)
    sport = sport[0].upper()+sport[1:].lower()
    s=(df.loc[df['SPORT'] == sport])
    p=['END',	'STR',	'PWR',	'SPD',	'AGI',	'FLX',	'NER',	'DUR',	'HAN',	'ANA']
    s = s[p].values
    o=[]
    for i in range(10):
      if int(feed[i])< int(s[0][i]):
        o.append(p[i])
    
    
    
    return render_template("output.html", f=feed,s=o)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug=True)
