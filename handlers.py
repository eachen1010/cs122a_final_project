# handlers.py
# 
# handler functions for CS 122a final project

import csv
import os
import mysql.connector

IMPORT_CSV_FILENAMES = {
    "User": "User.csv",
    "AgentClient": "AgentClient.csv",
    "AgentCreator": "AgentCreator.csv",
    "BaseModel": "BaseModel.csv",
    "Configuration": "Configuration.csv",
    "InternetService": "InternetService.csv",
    "DataStorage": "DataStorage.csv",
    "LLMService": "LLMService.csv",
    "CustomizedModel": "CustomizedModel.csv",
    "ModelConfigurations": "ModelConfigurations.csv",
    "ModelServices": "ModelServices.csv",
}
DB_HOST = "localhost"
DB_USER = "test"
DB_PASS = "password"  

# DB_HOST = "127.0.0.1"
# DB_USER = "root"
# DB_PASS = "YourPasswordHere" 


# Connects to db and returns the connectino and cursor
def connect_db():
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database="cs122a"
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
                # if cursor.with_rows:
                #     print(cursor.fetchall())
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                print(f"Failed SQL Command: {cmd}")
    
    db.commit()
    
    # Import data from CSV files in folder_name
    for table, filename in IMPORT_CSV_FILENAMES.items():
        file_path = os.path.join(folder_name, filename)
        # print(file_path)
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")
        
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            column_names = reader.fieldnames
            
            query = f'INSERT INTO cs122a.{table}({", ".join(column_names)}) VALUES ({", ".join(["%s" for _ in column_names])});'
            # print(query)
            for row in reader:
                values = tuple(row[col] for col in column_names)
                # print(values)

                cursor.execute(query, values)

    db.commit()
    close_db(db, cursor)
    return "Success"


# 2. Insert Agent Client
# Insert a new agent client into the related tables.
# Use: python3 project.py insertAgentClient [uid:int] [username:str] [email:str] [card_number:int] [card_holder:str] [expiration_date:date] [cvv:int] [zip:int] [interests:str]
def func_insert_agent_client(uid: int, username: str, email: str, card_number: int, card_holder: str, expiration_date: str, cvv: int, zip_code: int, interests: str) -> None:
    db, cursor = connect_db()
    
    # Insert a new agent client into the table
    # f'INSERT INTO User (uid, username, email) VALUES ({uid}, \'{username}\', \'{email}\');',
    commands = [
        f'INSERT INTO AgentClient (uid, cardno, cardholder, expire, cvv, zip, interests) VALUES ({uid}, {card_number}, \'{card_holder}\', \'{expiration_date}\', {cvv}, {zip_code}, \'{interests}\');']

    for cmd in commands:
        try:
            # print(cmd)
            cursor.execute(cmd)
        except mysql.connector.Error as err:
            close_db(db, cursor)
            return "Fail"

    db.commit()
    close_db(db, cursor)
    return "Success"

# 3. Add a customized model
# Add a new customized model to the tables.
# Use: python3 project.py addCustomizedModel [mid:int] [bmid:int]
def func_add_customized_model(mid: int, bmid: int) -> None:
    db, cursor = connect_db()
    
    # Insert a new agent client into the table
    commands = [f'INSERT INTO CustomizedModel (mid, bmid) VALUES ({mid}, {bmid});']

    for cmd in commands:
        try:
            cursor.execute(cmd)
            if cursor.with_rows:
                print(cursor.fetchall())
        except mysql.connector.Error as err:
            # print(f"Error: {err}")
            # print(f"Failed SQL Command: {cmd}")
            close_db(db, cursor)
            return "Fail"

    db.commit()
    close_db(db, cursor)
    return "Success"

# 4. Delete a base model
# Delete a base model from the tables.
# Use: python3 project.py deleteBaseModel [bmid:int]
def func_delete_base_model(bmid: int) -> None:
    return "Fail"

# 5. List internet service
# Given a base model id, list all the internet services that the model is utilizing, sorted by provider’s name in ascending order. 
# Use python3 project.py listInternetService [bmid:int]
def func_list_internet_service(bmid: int) -> None:
    return "Fail"

# 6. Count customized model
# Given a list of base model id, for each base model id, count on the numbers of customized models that build from it. Sort the results in ascending order of base model id. 
# Use: python3 project.py countCustomizedModel [bmid1:int] [bmid2:int] [bmid3:int]
def func_count_customized_model(bmid_list: list[int]) -> None:
    return "Fail"

# 7. Find Top-N longest duration configuration  
# Given an agent client id, list the top-N longest duration configurations with the longest duration managed by that client. Sort the configurations by duration in descending order. 
# Use: python3 project.py topNDurationConfig [uid:int] [N:int]
def func_top_n_duration_config(uid: int, N: int) -> None:
    return "Fail"

# 8. Keyword search
# List 5 base models that are utilizing LLM services whose domain contains the keyword “video”. (If there are fewer than 5 base models that satisfy the condition, list them all.) Sort the results by bmid in ascending order. 
# Use: python3 project.py listBaseModelKeyWord [keyword:str]
def func_list_base_model_keyword(keyword: str) -> None:
    return "Fail"

# 9. Experiment: Solving NL2SQL with LLM 
# NL2SQL, or text-to-SQL, is a task that translates natural language queries into SQL queries. NL2SQL is an interdisciplinary study between NLP (natural language processing) and database systems. In this project, the previously required functions also fall under the NL2SQL category — students play the role of converting natural language (NL) into SQL queries.
