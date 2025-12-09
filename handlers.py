# handlers.py
# 
# handler functions for CS 122a final project

import mysql.connector

INSERT_AGENT_CLIENT_QUERY = "INSERT INTO AgentClient (uid, username, email, card_number, card_holder, expiration_date, cvv, zip, interests) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
ADD_CUSTOMIZED_MODEL_QUERY = "INSERT INTO CustomizedModel (mid, bmid) VALUES (%s, %s);"
DELETE_BASE_MODEL_QUERY = "DELETE FROM BaseModel WHERE bmid = %s;"
LIST_INTERNET_SERVICE_QUERY = "SELECT * FROM InternetService WHERE bmid = %s ORDER BY provider_name ASC;"
COUNT_CUSTOMIZED_MODEL_QUERY = "SELECT bmid, COUNT(*) FROM CustomizedModel WHERE bmid IN (%s) GROUP BY bmid ORDER BY bmid ASC;"
TOP_N_DURATION_CONFIG_QUERY = "SELECT * FROM Configuration WHERE uid = %s ORDER BY duration DESC LIMIT %s;"
LIST_BASE_MODEL_KEYWORD_QUERY = "SELECT * FROM BaseModel WHERE llm_service_domain LIKE %s ORDER BY bmid ASC LIMIT 5;"   


# Connects to db and returns the connectino and cursor
def connect_db():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="YourPasswordHere"
    )

    cursor = db.cursor(buffered=True)

    return db, cursor

def close_db(db, cursor):
    cursor.close()
    db.close()




# 1. Import data
# Delete existing tables and create new tables. Then read the CSV files in the given folder and import data into the database. You can assume that the folder always contains all the necessary CSV files and that the files are correct.
# Use: python3 project.py import [folderName:str]
def func_import(folder_name: str) -> None:
    db, cursor = connect_db()
    
    # Remake tables
    with open("create_schema.sql", 'r') as f:
        sql_cmds = f.read()
        commands = [cmd.strip() for cmd in sql_cmds.split(';') if cmd.strip()]

        for cmd in commands:
            try:
                cursor.execute(cmd)
                if cursor.with_rows:
                    print(cursor.fetchall())
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                print(f"Failed SQL Command: {cmd}")
    
    # Import data from CSV files in folder_name

    db.commit()
    close_db(db, cursor)


# 2. Insert Agent Client
# Insert a new agent client into the related tables.
# Use: python3 project.py insertAgentClient [uid:int] [username:str] [email:str] [card_number:int] [card_holder:str] [expiration_date:date] [cvv:int] [zip:int] [interests:str]
def func_insert_agent_client(uid: int, username: str, email: str, card_number: int, card_holder: str, expiration_date: str, cvv: int, zip_code: int, interests: str) -> None:
    pass

# 3. Add a customized model
# Add a new customized model to the tables.
# Use: python3 project.py addCustomizedModel [mid:int] [bmid:int]
def func_add_customized_model(mid: int, bmid: int) -> None:
    pass

# 4. Delete a base model
# Delete a base model from the tables.
# Use: python3 project.py deleteBaseModel [bmid:int]
def func_delete_base_model(bmid: int) -> None:
    pass

# 5. List internet service
# Given a base model id, list all the internet services that the model is utilizing, sorted by provider’s name in ascending order. 
# Use python3 project.py listInternetService [bmid:int]
def func_list_internet_service(bmid: int) -> None:
    pass

# 6. Count customized model
# Given a list of base model id, for each base model id, count on the numbers of customized models that build from it. Sort the results in ascending order of base model id. 
# Use: python3 project.py countCustomizedModel [bmid1:int] [bmid2:int] [bmid3:int]
def func_count_customized_model(bmid_list: list[int]) -> None:
    pass

# 7. Find Top-N longest duration configuration  
# Given an agent client id, list the top-N longest duration configurations with the longest duration managed by that client. Sort the configurations by duration in descending order. 
# Use: python3 project.py topNDurationConfig [uid:int] [N:int]
def func_top_n_duration_config(uid: int, N: int) -> None:
    pass

# 8. Keyword search
# List 5 base models that are utilizing LLM services whose domain contains the keyword “video”. (If there are fewer than 5 base models that satisfy the condition, list them all.) Sort the results by bmid in ascending order. 
# Use: python3 project.py listBaseModelKeyWord [keyword:str]
def func_list_base_model_keyword(keyword: str) -> None:
    pass

# 9. Experiment: Solving NL2SQL with LLM 
# NL2SQL, or text-to-SQL, is a task that translates natural language queries into SQL queries. NL2SQL is an interdisciplinary study between NLP (natural language processing) and database systems. In this project, the previously required functions also fall under the NL2SQL category — students play the role of converting natural language (NL) into SQL queries.
