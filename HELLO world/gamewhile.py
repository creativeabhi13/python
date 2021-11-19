secret_number =9
guess_counter = 0
guess_limit = 3
while guess_counter < guess_limit:
    guess = int(input("Guess:"))
    guess_counter += 1
    if guess == secret_number:
        print("you won")
        break
else:
    print("sorry you may failed!")
