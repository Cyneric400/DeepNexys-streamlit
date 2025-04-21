import pdfreader
import sqlite3


def read_uploaded_files(uid):
    with sqlite3.connect("VTI64_db/vti64.db") as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT contents FROM Documents WHERE user_id={uid};")
        return cursor.fetchall()


def add_uploaded_file(file):
    text = pdfreader.read_file(file)
    uid = 0
    with sqlite3.connect("VTI64_db/vti64.db") as conn:
        cursor = conn.cursor()
        # need to upgrade id
        cursor.execute("SELECT Max(file_id) FROM Documents")
        max_raw = cursor.fetchone()[0]
        curr_max_id = int(max_raw) if max_raw else 0
        new_fid = curr_max_id + 1
        cursor.execute(f"INSERT INTO Documents VALUES ({new_fid}, {uid}, 'f'); UPDATE DOCUMENTS SET USER_ID=0;--');")
        
        conn.commit()