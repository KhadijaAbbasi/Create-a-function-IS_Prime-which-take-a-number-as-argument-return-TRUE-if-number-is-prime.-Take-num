def IS_Prime():
    num=int(input("Enter the number: "))
    prime = 0
    for y in range(2, int(num)):
        if (num % y) == 0:
            prime = 1
    if prime == 0:
        print("TRUE")
    else:
        print("False")

def main():
    IS_Prime()
if __name__== "__main__":
    main()

