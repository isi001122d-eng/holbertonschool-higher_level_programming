#!/usr/bin/python3
"""
API-dən məlumat çəkmək və emal etmək üçün modul
"""
import requests
import csv


def fetch_and_print_posts():
    """
    JSONPlaceholder-dən postları çəkir və başlıqlarını çap edir
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Postları çəkir və onları posts.csv faylına yazır
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        
        # CSV üçün lazım olan məlumatları strukturlaşdırırıq
        # id, title və body sütunları tələb olunur
        data_to_save = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # CSV faylına yazırıq
        with open('posts.csv', 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data_to_save)
