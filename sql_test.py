import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="YourPasswordHere"
)

cursor = mydb.cursor(buffered=True)

with open("create_schema.sql", 'r') as f:
    sql_cmds = f.read()

    # Split commands by semicolon and strip whitespace
    commands = [cmd.strip() for cmd in sql_cmds.split(';') if cmd.strip()]

    for cmd in commands:
        try:
            cursor.execute(cmd)
            if cursor.with_rows:
                print(cursor.fetchall())
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print(f"Failed SQL Command: {cmd}")

mydb.commit()
cursor.close()
mydb.close()