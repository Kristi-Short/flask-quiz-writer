## Steps to depoly to heroku

1. `virtualenv env`
1. `pip install flash`
1. `pip install gunicorn`
1. `git init`
1. add .gitignore with env
1. add Procfile with web: gunicorn deploy:app
1. run `pip3 freeze > requirements.txt`
1. `git commit -m"...`
1. `heroku login`
1. `heroku create`
1. `git push heroku master`
1. `heroku open`
