numbers = []


def create_list():
    while True:
        number = int(input("Írj be egy pozitív egész számot:"))
        if number > 0:
            numbers.append(number)
        else:
            break
    numbers.reverse()
    print(numbers)


create_list()
