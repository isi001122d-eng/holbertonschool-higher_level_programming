#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def get_json_products():
    with open('products.json', 'r') as file:
        return json.load(file)


def get_csv_products():
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


def get_sql_products():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()

    conn.close()

    products = []

    for row in rows:
        products.append({
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        })

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None

    if source == 'json':
        products = get_json_products()
    elif source == 'csv':
        products = get_csv_products()
    elif source == 'sql':
        try:
            products = get_sql_products()
        except Exception:
            return render_template(
                'product_display.html',
                products=[],
                error='Database error'
            )
    else:
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    if product_id is not None:
        products = [p for p in products if str(p['id']) == product_id]

        if len(products) == 0:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=products,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True)
