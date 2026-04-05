#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', products=[], error='Wrong source')

    if product_id:
        filtered = [product for product in data if str(product['id']) == product_id]
        if not filtered:
            return render_template('product_display.html', products=[], error='Product not found')
        data = filtered

    return render_template('product_display.html', products=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
