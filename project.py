# project.py
# 
# main file for CS 122a final project

import sys
from handlers import (
    func_import,
    func_insert_agent_client,
    func_add_customized_model,
    func_delete_base_model,
    func_list_internet_service,
    func_count_customized_model,
    func_top_n_duration_config,
    func_list_base_model_keyword,
)

FUNCTION_MAPPINGS = {
    "import": func_import,
    "insertAgentClient": func_insert_agent_client,
    "addCustomizedModel": func_add_customized_model,
    "deleteBaseModel": func_delete_base_model,
    "listInternetService": func_list_internet_service,
    "countCustomizedModel": func_count_customized_model,
    "topNDurationConfig": func_top_n_duration_config,
    "listBaseModelKeyWord": func_list_base_model_keyword,
}


def parse_input(args: list[str]) -> tuple[str, list]:
    if not args:
        raise ValueError("No function name provided.")
    
    function_name = args[0]
    function_args = args[1:]
    
    if function_name not in FUNCTION_MAPPINGS:
        raise ValueError(f"Function '{function_name}' is not recognized.")
    
    return FUNCTION_MAPPINGS[function_name], function_args



if __name__ == "__main__":
    # Parse command line arguments
    func, args = parse_input(sys.argv[1:])

    # Call function with provided arguments
    func(*args)