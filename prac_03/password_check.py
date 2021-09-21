Min_length=5
def main():
    password = input(">")
    while not is_valid_password(password):
        print("invalid password")
        for i in range(len(password)):
            print('*', end='')
        print()
        password = input(">")
    print("is valid")
    for i in range(len(password)):
        print('*', end='')
def is_valid_password(password):
    if len(password)<Min_length:
        return False
    else:
        return True
main()
