from myapp.credentials import HOSTDB, DBNAME, PORTDB, USERDB, PASSDB
import pymysql as mysql

TIMEOUT = 10
CONNECTION = mysql.connect(
    charset="utf8mb4",
    connect_timeout=TIMEOUT,
    cursorclass=mysql.cursors.DictCursor,
    db=DBNAME,
    host=HOSTDB,
    password=PASSDB,
    read_timeout=TIMEOUT,
    port=PORTDB,
    user=USERDB,
    write_timeout=TIMEOUT,
)
TABLE = "customers"
