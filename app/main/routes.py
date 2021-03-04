from flask import render_template, Blueprint

bp_main = Blueprint('main', __name__, template_folder="templates", static_folder="static")


@bp_main.route('/')
def index():
    return render_template('index.html')


@bp_main.route('/docs')
def docs():
    return render_template('docs.html')


