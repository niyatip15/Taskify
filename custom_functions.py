FILE_PATH = 'todos.txt'

def read_todos(filepath=FILE_PATH):
    '''Read a text file and returns the list of to-do items.'''
    with open(filepath,"r") as file:
            todos =  file.readlines()
    return todos

def write_todos(todos_arg,filepath=FILE_PATH):
    '''Writes the to-do items in the text file.'''
    with open(filepath,"w") as file:
        todos = file.writelines(todos_arg)
    return todos