import traceback
import mysql.connector
import config

db = mysql.connector.connect(
    host=config.host,
    database=config.database,
    user=config.user,
    passwd=config.passwd)


cursor = db.cursor()

try:
    cursor.execute("CREATE TABLE leads (lead_id int(100), source text(200), name text(200), message int(100))")
except Exception:
    print("ERROR: ERROR while trying to create table leads")
    traceback.print_exc()

cursor.execute("SHOW TABLES")