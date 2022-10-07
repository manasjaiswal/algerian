import pickle
from flask import Flask,request,jsonify,render_template,url_for
import numpy as np
import pandas as pd

app=Flask(__name__)

model=pickle.load(open('algeria_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    data=[x for x in request.form.values()]
    new_data=[data]
    output=model.predict(new_data)[0]
    text=''
    if output==1:
        text='There are chances of forest fire wrt to above parameters'
    else:
        text='There are no chances of fire'
    return render_template('home.html',prediction_text=text)

if __name__=='__main__':
    app.run(debug=True)