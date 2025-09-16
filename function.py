
def get_file():
    with open("todo.txt", "r") as file:
        file_read = file.readlines()
    return file_read

def write_to_file(todos):
    with open("todo.txt", "w") as file:
        file.writelines(todos)

