sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY, 
            username varchar(255), 
            text TEXT
    );""",
    """CREATE TABLE IF NOT EXISTS answers (
            id SERIAL PRIMARY KEY, 
            username varchar(255), 
            question_id INTEGER,
            text TEXT,
            FOREIGN KEY (question_id) REFERENCES questions (id)
    );""",
    
    ]

def migrate_db(con):
    cur = con.cursor()

    for stmt in sql_statements:
        cur.execute(stmt)

    con.commit()