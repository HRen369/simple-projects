# 3 % 0 == Fizz
# 5 % 0 == Buzz
# 3 % 0 and 5 % 0 == FizzBuzz

def fizzbuzzSol1(num):
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def fizzbuzzSol2(num):
    for i in range(1,num+1):
        numStr = ""
        if i % 3 == 0:
            numStr += "Fizz"
        if i % 5 == 0:
            numStr += "Buzz"
        
        if numStr == "":
            print(i)
        else:
            print(numStr)


def main():
    fizzbuzzSol2(20)

if __name__ == "__main__":
    main()