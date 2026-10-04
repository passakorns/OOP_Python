import sqlite3
from flask import flash, session

def init_db(db_name):
    with get_db(db_name) as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS members(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL,
            gender TEXT NOT NULL, 
            password TEXT NOT NULL, 
            isAgree BOOLEAN, 
            province TEXT, 
            address TEXT
        );
        """)

def get_db(db_name):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    
    return conn

def login_required():
    if "member_id" not in session:
        flash("กรุณาเข้าสู่ระบบก่อน")
        return False
    return True