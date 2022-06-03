from crypt import methods
import os
from turtle import title
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods= ['POST', 'GET'])
def movie_prediction():
    df = pd.read_csv('movie1.csv')
    title = df['Title']
    if request.method == 'POST':
        movie = request.form['movie']
        print(df[df['Title'] == movie]["Success"].iloc[0])
        res = df[df['Title'] == movie]["Success"].iloc[0]
        result = ""
        if res == 0:
            result = "Failed"
        else:
            result = "Success"
        return render_template("prediction.html", data=title, res=result)
    return render_template("prediction.html", data=title)



if __name__ == '__main__':
    app.run(debug=True)