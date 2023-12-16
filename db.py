import sqlite3
import os


class Database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("blackjack.db")
        self.cur = self.conn.cursor()
