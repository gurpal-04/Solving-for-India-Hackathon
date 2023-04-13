from flask import Flask, render_template, request
import pandas as pd

df = pd.read_excel('toughestsport.xlsx')

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")


@app.route('/getvalue', methods=['POST'])
def getvalue():

  feed = [
    request.form['parameter1'], request.form['parameter2'],
    request.form['parameter3'], request.form['parameter4'],
    request.form['parameter5'], request.form['parameter6'],
    request.form['parameter7'], request.form['parameter8'],
    request.form['parameter9'], request.form['parameter10']
  ]
  # print(feed)

  sport = request.form['sport']

  sport = sport[0].upper() + sport[1:].lower()
  s = (df.loc[df['SPORT'] == sport])
  p = ['END', 'STR', 'PWR', 'SPD', 'AGI', 'FLX', 'NER', 'DUR', 'HAN', 'ANA']
  P = [
    'Endurance', 'Strength', 'Power', 'Speed', 'Agility', 'Flexibility',
    'Nerve', 'Drability', 'Hand-Eye Coordination', 'Analitic Aptitude'
  ]
  s = s[p].values
  o = []
  for i in range(10):
    if int(feed[i]) < int(s[0][i]):
      o.append(P[i])

  return render_template("output.html", f=feed, s=o)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug=True)
