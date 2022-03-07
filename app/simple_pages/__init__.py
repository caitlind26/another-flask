from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_pages', __name__,
                        template_folder='templates',static_folder='static')


@simple_pages.route('/', defaults={'page': 'index'})
@simple_pages.route('/<page>')
@simple_pages.route('/index')
@simple_pages.route('/cicd')
@simple_pages.route('/docker')
@simple_pages.route('/pyflask')
@simple_pages.route('/git')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
