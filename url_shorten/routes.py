from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Urls

shortener = Blueprint('shortener', __name__)

@shortener.route('/<short_url>')
def redirect_to_url(short_url):
    urls = Urls.query.filter_by(short_url=short_url).first_or_404()

    urls.visits = urls.visits + 1
    db.session.commit()

    return redirect(urls.long_url) 

@shortener.route('/')
def index():
    return render_template('index.html') 

@shortener.route('/add_url', methods=['POST'])
def add_url():
    long_url = request.form['long_url']
    urls = Urls(long_url=long_url)
    db.session.add(urls)
    db.session.commit()

    return render_template('url_added.html', 
        short_url=urls.short_url, long_url=urls.long_url)

@shortener.route('/stats')
def stats():
    urls = Urls.query.all()

    return render_template('stats.html', urls=urls)

@shortener.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404