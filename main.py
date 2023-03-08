# Lab 6 - Luis Martinez

def encode_str(data_string):
    res = ""
    for char in data_string:
        if char.isdigit():
            digit = int(char) + 3
            if digit >= 10:
                digit -= 10
                res += str(digit)
            else:
                res += str(digit)
    return res


def main():
    menu_continue = True
    while menu_continue:
        print("Menu\n"
              "_____________\n"
              "\n1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        user_choice = input("Please enter an option: ")

        if user_choice == "1":
            data_string = input("Please enter your password to encode: ")
            encoded_data = encode_str(data_string)
            print("Your password has been encoded and stored!\n")
        elif user_choice == "2":
            print(f"The encoded password is {encoded_data}, and the original password is {data_string}\n")
        elif user_choice == "3":
            menu_continue = False


if __name__ == "__main__":
    main()

