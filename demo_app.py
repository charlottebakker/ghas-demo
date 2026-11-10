"""Deliberately insecure, non-deployed sample for a CodeQL demonstration."""

import sqlite3

from flask import Flask, request


app = Flask(__name__)


@app.get("/books")
def books():
    author = request.args.get("author", "")
    with sqlite3.connect(":memory:") as connection:
        connection.execute("CREATE TABLE books (author TEXT, title TEXT)")
        connection.execute(
            "INSERT INTO books (author, title) VALUES (?, ?)",
            ("Demo author", "Demo book"),
        )
        rows = connection.execute(
            f"SELECT title FROM books WHERE author = '{author}'"
        ).fetchall()
    return {"books": [row[0] for row in rows]}
