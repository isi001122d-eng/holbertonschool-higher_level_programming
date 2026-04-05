#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        }
        for row in rows
    ]


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            return render_template('product_display.html', products=[], error='Wrong source')

        if product_id:
            data = [product for product in data if str(product['id']) == product_id]
            if not data:
                return render_template('product_display.html', products=[], error='Product not found')

        return render_template('product_display.html', products=data, error=None)

    except Exception:
        return render_template('product_display.html', products=[], error='Database error')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
