import os

def menu(user_input):
    print("Choose from one of the options below: ")

    print("P: Print your friends list")
    print("U: <name>: Unfriend someone")
    print("F <name>: Friend someone")
    print("Q: Quit")
    option = input().title()
    return option


def read_file(facebook):
    try:
        filename = "dwarves.txt"
        #if os.path.isdir(filename):
        file = open(filename, "r")
        for line in file:
            split_line = line.strip().split(" ")
            facebook[split_line[0]] = split_line[1:]
        file.close()
    except FileNotFoundError:
        print("File not found")
        return


def write_file(facebook):
    try:
        filename = "dwarves.txt"
        file = open(filename, 'w')
        for user_name, friend_list in facebook.items():
            file.write(str(user_name))
            for friend in friend_list:
                file.write(" " + str(friend))
            file.write("\n")
    except FileNotFoundError:
        print("File not found")


def main():

    facebook = {}
    read_file(facebook)
    print(facebook)

    user_name = ''
    while user_name not in facebook:
        user_name = input("Type user name: ")
    option = (menu(user_name)).split(' ')
    while option[0] != "Q":
        if option[0] == "P":
            print("Your friends: " + str(facebook[user_name]))
        elif option[0] == "U":
            friend_list = facebook[user_name]
            if option[1] in friend_list:
                friend_list.remove(option[1])
            facebook[user_name] = friend_list

            friend_list = facebook[option[1]]
            if user_name in friend_list:
                friend_list.remove(user_name)
            facebook[option[1]] = friend_list
            print(" Unfriending: " + str(option[1]))

        elif option[0] == "F":
            friend_list = facebook[user_name]
            if option[1] not in friend_list:
                friend_list.append(option[1])
            facebook[user_name] = friend_list

            friend_list = facebook[option[1]]
            if user_name not in friend_list:
                friend_list.append(user_name)
            facebook[option[1]] = friend_list
            print("Adding friends with: " + str(option[1]))
        else:
            print("Input is invalid")
        option = (menu(user_name)).split(' ')
    write_file(facebook)
















if __name__ == "__main__":
    main()
