from flask import Flask

app = Flack(__name__)

@app.route('/')
def index():
    return <h1>Deployed to Heroku!</h1

#https://www.youtube.com/watch?v=skc-ZEU9kO8