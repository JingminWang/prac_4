Min_length=5
def main():
    password = get_password()
    while not is_valid_password(password):
        print("invalid password")
        Print_asterisks(password)
        print()
        password = input(">")
    print("is valid")
    Print_asterisks(password)
def get_password():
   return input(">")


def Print_asterisks(password):
    for i in range(len(password)):
        print('*', end='')
def is_valid_password(password):
    if len(password)<Min_length:
        return False
    else:
        return True
main()
