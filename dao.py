import json


def load_categories(que=None):
    with open("data/categories_json.json", encoding="utf-8") as f:

        categories = json.load(f)

        return categories


def load_products(q=None, cate_id=None):
    with open("data/products.json", encoding="utf-8") as f:

        products = json.load(f)
        if q:
            products = [p for p in products if p['name'].find(q) >= 0]
        if cate_id:
            products = [p for p in products if p['category_id'] == cate_id]
        return products



