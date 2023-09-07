from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json

plr = joblib.load('plr1.sav')
pnb = joblib.load('pnb1.sav')
prf = joblib.load('prf1.sav')
psg = joblib.load('psg1.sav')
ppa = joblib.load('ppa1.sav')
pst = joblib.load('pst1.sav')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api',methods=['POST'])
def get_delay():

    result=request.form
    query_title = result['title']
    query_author = result['author']
    query_text = result['maintext']
    query = get_all_query(query_title, query_author, query_text)
    user_input = {'query':query}
    pred = plr.predict(query)
    pred1 = psg.predict(query)
    pred2 = prf.predict(query)
    pred3 = pnb.predict(query)
    pred4 = ppa.predict(query)
    pred6 = pst.predict(query)
  

    count = 0
    if(pred[0] == 1):
        count += 1
    if(pred1[0] == 1):
        count += 1
    if(pred2[0] == 1):
        count += 1
    if(pred3[0] == 1):
        count += 1
    if(pred4[0] == 1):
        count += 1
    if(pred6[0] == 1):
        count += 1

    if count < 4:
        pred[0] = 0
    else:
        pred[0] = 1

    print(pred)
    print(pred1)
    print(pred2)
    print(pred3)
    print(pred4)
    print(pred6)
    dic = {0:'real',1:'fake'}
    return f'<html><body><h1>{dic[pred[0]]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'

if __name__ == '__main__':
    app.run(port=8080, debug=True)
