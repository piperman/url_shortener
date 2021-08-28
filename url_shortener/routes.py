from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Urls

shortener = Blueprint('shortener', __name__)

@shortener.route('/<short_url>')
def redirect_to_url(short_url):
    urls = Urls.query.filter_by(short_url=short_url).first_or_404()

    urls.visits = urls.visits + 1
    db.session.commit()

    return redirect(urls.original_url) 

@shortener.route('/')
def index():
    return render_template('index.html') 

@shortener.route('/add_url', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    urls = Urls(original_url=original_url)
    db.session.add(urls)
    db.session.commit()

    return render_template('url_added.html', 
        new_link=urls.short_url, original_url=urls.original_url)

@shortener.route('/stats')
def stats():
    urls = Urls.query.all()

    return render_template('stats.html', urls=urls)

@shortener.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404