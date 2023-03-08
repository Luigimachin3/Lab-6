# Lab 6 - Luis Martinez
# Collaborator - Charleigh Walker


def encode_str(user_pw):
    res = ""
    for char in user_pw:
        if char.isdigit():
            digit = int(char) + 3
            if digit >= 10:
                digit -= 10
                res += str(digit)
            else:
                res += str(digit)
    return res


# decoded_str already exists so I changed a variable 
def decoded_str(encoded_data, user_pw):
    print(f"The encoded password is {encoded_data}, and the original password is {user_pw}\n")


def main():
    menu_continue = True
    while menu_continue:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        user_choice = input("Please enter an option: ")

        if user_choice == "1":
            user_pw = input("Please enter your password to encode: ")
            encoded_data = encode_str(user_pw)
            print("Your password has been encoded and stored!\n")
        elif user_choice == "2":
            decoded_str(encoded_data, user_pw)
        elif user_choice == "3":
            menu_continue = False


if __name__ == "__main__":
    main()
