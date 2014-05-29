from flask import Blueprint, render_template

mod_drugsearch = Blueprint('drugsearch', __name__)

@mod_drugsearch.route('/', methods=['GET'])
def index():
    return render_template('drugsearch/index.html')
