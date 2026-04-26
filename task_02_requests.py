#!/usr/bin/env python3
"""Fetch posts from JSONPlaceholder and print/save them."""

import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print the response status code and each post title."""
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        # Network/DNS/timeout/etc.
        return

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts and save id/title/body fields to posts.csv."""
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    posts = response.json()
    rows = [
        {"id": p.get("id"), "title": p.get("title"), "body": p.get("body")}
        for p in posts
    ]

    fieldnames = ["id", "title", "body"]
    with open("posts.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
