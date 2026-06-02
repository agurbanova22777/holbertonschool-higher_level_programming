#!/usr/bin/env python3
"""Fetch posts from JSONPlaceholder and print/save them."""

import requests
import csv

def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder and writes them into csv file"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        structured_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts       
        ]
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)
