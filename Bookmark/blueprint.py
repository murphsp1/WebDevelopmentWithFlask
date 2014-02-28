'''
https://gist.github.com/coleifer/d55324a3406a11661c50
This file comes from a gist and a blog that I did not write
but decided to implement for practice
'''
import datetime
 
from flask import request, redirect, url_for, render_template, Blueprint
from peewee import *
 
#from flask.ext.rest import RestResource
from flask.extutils import get_object_or_404, object_list
 
from app import app, db
from auth import auth
 
 
class Bookmark(db.Model):
    url = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
 
    class Meta:
        ordering = (('created_date', 'desc'),)
 
    def __unicode__(self):
        return self.url
 
bookmarks = Blueprint('bookmarks', __name__, template_folder='templates')
 
@bookmarks.route('/')
@auth.login_required
def list():
    qr = Bookmark.select()
    return object_list('bookmarks/index.html', qr)
 
@bookmarks.route('/add/')
@auth.login_required
def add():
    url = request.args.get('url')
    if url:
        Bookmark.get_or_create(url=url)
    return redirect(url or url_for('bookmarks.list'))
 
@bookmarks.route('/<pk>/delete/')
@auth.login_required
def delete(pk):
    bookmark = get_object_or_404(Bookmark, id=pk)
    bookmark.delete_instance()
    return redirect(url_for('bookmarks.list'))
 
 
class BookmarkResource(RestResource):
    pass