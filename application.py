from flask import Flask, render_template, request, redirect

app = Flask(__name__)

filleName = 'titles.txt'
news = []

@app.route('/', methods=["POST", "GET"])

def index():
    return render_template('index.html', ranndom_number=ranndom_number)

@app.route('/news/create', methods=["GET"])

def news_create():
    return render_template('news-create-form.html')

@app.route('/news', methods=["POST"])

def news_store():
    title = request.form.get('title')
    news.append(title)
    file = open('titles.txt', 'a')
    file.write(title + '\n')
    return redirect('/')