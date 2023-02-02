import sqlite3

def execute_query(sql_query):
    with sqlite3.connect("Data.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result

def add_content(content_name,content_qn):
    sql_query = "INSERT INTO Data(content_name,content_qn) VALUES('%s','%s')" %(content_name,content_qn)
    execute_query(sql_query)
    
def get_content_name():
    sql_query = "SELECT content_name FROM Data"
    content = execute_query(sql_query)
    return [content_name[0] for content_name in content.fetchall()]

def get_content_qn():
    sql_query = "SELECT content_qn FROM Data"
    content = execute_query(sql_query)
    return [content_qn[0] for content_qn in content.fetchall()]


    


