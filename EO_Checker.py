def evenOdd(number):
    if number%2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.") 

def main():

    number = int(input("Enter an integer: "))
    evenOdd(number)

print("Even or Odd Checker\n\n")
main()