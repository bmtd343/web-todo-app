FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Reads each line of the designated file with to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    # No 'return' b/c it is a procedure that doesn't require storage of a value --> just writing to a file, not storing


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
