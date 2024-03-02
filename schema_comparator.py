# schema_comparator.py

import sqlite3
import difflib

def compare_schema(connection_string, table_name, sqlite_db_path):
    """
    Compares the current schema of a table with a stored schema in a SQLite database.
    """
    import pandas as pd
    
    # Read current schema
    source_conn = sqlite3.connect(connection_string)
    query = f"SHOW CREATE TABLE {table_name}"
    df = pd.read_sql_query(query, source_conn)
    current_create_statement = df.iloc[0, 1]  # Assuming the create statement is in the first row, second column
    source_conn.close()

    # Read stored schema
    sqlite_conn = sqlite3.connect(sqlite_db_path)
    cursor = sqlite_conn.cursor()
    cursor.execute('''SELECT create_statement FROM schema_history WHERE table_name = ?''', (table_name,))
    row = cursor.fetchone()
    stored_create_statement = row[0] if row else ""
    sqlite_conn.close()

    # Compare schemas
    diff = difflib.unified_diff(
        stored_create_statement.splitlines(keepends=True),
        current_create_statement.splitlines(keepends=True),
        fromfile='stored_schema',
        tofile='current_schema',
    )
    return '\n'.join(diff)
