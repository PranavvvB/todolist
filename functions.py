FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Reads items from file and returns them as a list."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes a list to to-do list file. (to-do.txt)"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    """ These will only run if this file is opened directly
     it will not run if this is imported elsewhere
     """
    print(get_todos())
