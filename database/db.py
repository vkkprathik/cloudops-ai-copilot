import sqlite3

DB_NAME = "database/chats.db"


def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent TEXT,
            role TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_message(agent, role, message):

    print(f"SAVING -> {agent} | {role}")

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_history (
            agent,
            role,
            message
        )
        VALUES (?, ?, ?)
        """,
        (
            agent,
            role,
            message
        )
    )

    conn.commit()

    print("MESSAGE SAVED")

    conn.close()


def load_messages(limit=50):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, message
        FROM chat_history
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    conn.close()

    rows.reverse()

    return rows

def get_total_messages():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM chat_history"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count
def get_agent_stats():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT agent, COUNT(*)
        FROM chat_history
        GROUP BY agent
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data