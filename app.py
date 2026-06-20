import random

def guess_number():
    number = random.randint(1, 5)
    print("Guess a number between 1 and 5!")
    guess = int(input("Your guess: "))
    if guess == number:
        return "🎉 Correct!"
    else:
        return f"❌ Wrong! The number was {number}"

if __name__ == "__main__":
    print(guess_number())
