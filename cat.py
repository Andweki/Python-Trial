def main ():
    number = get_number()
    meaow(number)


def get_number():
    while True:
        n = int(input("what is n?: "))
        if n > 0:
            break
    return n

def meaow (n):
    for _ in range(n):
        print("meaow")



main()