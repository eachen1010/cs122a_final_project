# project.py
# 
# main file for CS 122a final project


# Functional Requirements

# 1. Import data
# Delete existing tables and create new tables. Then read the CSV files in the given folder and import data into the database. You can assume that the folder always contains all the necessary CSV files and that the files are correct. 


# 2. Insert Agent Client
# Insert a new agent client into the related tables. 

# 3. Add a customized model
# Add a new customized model to the tables.

# 4. Delete a base model
# Delete a base model from the tables.

# 5. List internet service
# Given a base model id, list all the internet services that the model is utilizing, sorted by provider’s name in ascending order. 

# 6. Count customized model
# Given a list of base model id, for each base model id, count on the numbers of customized models that build from it. Sort the results in ascending order of base model id. 

# 7. Find Top-N longest duration configuration  
# Given an agent client id, list the top-N longest duration configurations with the longest duration managed by that client. Sort the configurations by duration in descending order. 

# 8. Keyword search
# List 5 base models that are utilizing LLM services whose domain contains the keyword “video”. (If there are fewer than 5 base models that satisfy the condition, list them all.) Sort the results by bmid in ascending order. 

# 9. Experiment: Solving NL2SQL with LLM 
# NL2SQL, or text-to-SQL, is a task that translates natural language queries into SQL queries. NL2SQL is an interdisciplinary study between NLP (natural language processing) and database systems. In this project, the previously required functions also fall under the NL2SQL category — students play the role of converting natural language (NL) into SQL queries.


