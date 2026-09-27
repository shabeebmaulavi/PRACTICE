from random import randint
import os
def OTP(a):
    if type(a) is int:
        x = (10 ** (a - 1), 10 ** a - 1)
        print(randint(x[0],x[1]))
    else:
        print("wrong format")




if __name__ == "__main__":
    # os.environ.get('KEY', 'fallback_default')
    num1_str = os.environ.get("NUM1", "0")

    # Convert strings to integers
    num1 = int(num1_str)

    OTP (num1)
