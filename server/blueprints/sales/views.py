from flask import Blueprint

sales = Blueprint('sales', __name__, template_folder="templates/sales", url_prefix="/sales")

@sales.route("/")
def home():
    context={'title': 'Sales'}
    return render_template('home.html', context=context)
