from app import app
from flask import render_template, url_for, redirect
from app.forms import TitleForm, PostForm


#create posts global variable, only for placement before implementing database
#once database is created, get rid of this variables
tweets = [
    {
        'post_id': 0,
        'tweet': 'Suck it Sauron!',
        'date_posted': 'February 14th, 2019'
    }
]

@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])
def index(header= ''):
    products = {
        1001: {
            'title': 'Soap',
            'price': 3.98,
            'desc': 'Cleaner than faker himself'
        },
        1002: {
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'Straight from the vine'
        },
        1003: {
            'title': 'Pickles',
            'price': 5.67,
            'desc': 'Hey, why not?'
        },
        1004: {
            'title': 'Juice',
            'price': 2.68,
            'desc': 'Do you even tren brah?'
        }
    }
    return render_template('index.html', header=header, products=products, title='Home')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    form = PostForm()

    #when form is submitted append to posts list, re-render posts page
    if form .validate_on_submit():
        tweet = form.tweet.data
        tweets.append({
        'post_id': len(tweets),
        'tweet': tweet,
        'date_posted': 'February 14th, 2019'
        })


    return render_template('posts.html', title='Posts', form=form, tweets=tweets)

@app.route('/title', methods=['GET', 'POST'])
def title():
    form = TitleForm()

    #when form is submitted, redirect to home page, and pass title to change what the h1 tag says
    if form.validate_on_submit():
        header = form.title.data
        return redirect(url_for('index', header=header))

    return render_template('title.html', title='Title', form=form)
