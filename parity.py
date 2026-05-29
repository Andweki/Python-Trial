def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")


def is_even(n):
    return true if n % 2 == 0 else False

if __name__ == "__main__":
    main()


name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Luna":
        print("Ravenclaw")
    case _:
        print("who?")
        