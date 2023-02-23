FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as loc_file:
        loc_todos = loc_file.readlines()

    return loc_todos

def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
