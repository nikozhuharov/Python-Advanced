import os
command = input()
while True:
    if command == "End":
        break
    command_list = command.split("-")
    choice = command_list[0]
    file_name = command_list[1]
    if choice == "Create":
        open(file_name, 'w').close()
    elif choice == "Add":
        content = command_list[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")
    elif choice == "Replace":
        if os.path.exists(file_name):
            old_string = command_list[2]
            new_string = command_list[3]
            with open(file_name, "r+") as file:
                new_content = file.read().replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(new_content)
        else:
            print("An error occurred")
    elif choice == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")






    command = input()