import random
import argparse

parser = argparse.ArgumentParser(
                    prog='skibidigame',
                    description='number game',
                    epilog='input ANY number 1-50. try getting it first try!')
parser.add_argument('--max_number', type=int,help='max number')

def gfu():
    number = int(input("Guess the number!: "))
    return number

def cn():
    return random.randint(1, 2)
def dd(n1, n2):
    return abs(n1 - n2)

def dr(user_number, created_number, d):
    if user_number == created_number:
        print("YOUR DID IT1!1!onejuan")
    print(f"Your guess: {user_number}, Generated Number: {created_number}. Difference: {d}")


if __name__ == '__main__':
    args = parser.parse_args()
    n1 = gfu()
    n2 = cn()
    difference = dd(n1, n2)
    print(f"This try was good! You were *POSSIBLY* {difference + random.randint(-10, 10)} away.")
    if difference == 0:
      dr(n1, n2, difference)
    else:
        for _ in range(10):
            n1 = gfu()
            difference = dd(n1, n2)
            print(f"This try was so close. You were {difference} away.")
            if difference == 0:
                dr(n1, n2, difference)
                break
