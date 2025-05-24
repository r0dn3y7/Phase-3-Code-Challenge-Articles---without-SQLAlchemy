from lib.db.connection import CONN, CURSOR
from lib.models.article import Article
from lib.models.magazine import Magazine

class Author:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def save(self):
        CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        self.id = CURSOR.lastrowid
        CONN.commit()

    def articles(self):
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        return [Article(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]

    def magazines(self):
        CURSOR.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = CURSOR.fetchall()
        return [Magazine(row[1], row[2], id=row[0]) for row in rows]
