import string
from datetime import datetime
from random import choices

from .extensions import db 

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        clist = string.digits + string.ascii_letters
        short_url = ''.join(choices(clist, k=5))

        urls = self.query.filter_by(short_url=short_url).first()

        if urls:
            return self.generate_short_url()
        
        return short_url
