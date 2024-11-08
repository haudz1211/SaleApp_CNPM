from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route("/")
def index():
    cate_id = request.args.get("category_id")
    categories = dao.load_categories(cate_id)

    q = request.args.get("q")
    products = dao.load_products(q,cate_id)

    return render_template("index.html", categories=categories, products=products)


if __name__ == '__main__':
    app.run(debug=True)
