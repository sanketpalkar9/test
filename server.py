from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

year = datetime.now().year

def get_age(name):
    response = requests.get(url="https://api.agify.io/", params={"name":name})
    data = response.json()
    age = data.get("age")
    return age

def get_gender(name):
    response = requests.get(url="https://api.genderize.io/", params={"name": "sanket"})
    data = response.json()
    gender = data.get("gender")
    return gender


@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html",num = random_number,year = year)

@app.route('/guess/<name>')
def guess(name):
    age=get_age(name)
    gender=get_gender(name)
    return render_template("agify.html",age=age,gender=gender,name=name)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return  render_template("blog.html",posts = all_posts)


if __name__ == "__main__":
    app.run(debug=True)