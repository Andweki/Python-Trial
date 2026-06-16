import time

password = "126"

print("Cracking Password.....")

for i in range(1000):
    guess = str(i).zfill(3)
    print("Trying", guess)
    time.sleep(0.05)

    if guess == password:
        print("Password found")
        print("Password is :", guess)
        break
    