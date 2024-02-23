import json
from card import *
from decode import *
if __name__ == "__main__":
    with open('1040250010.json', 'r') as file:
        a = pCardDecode(file)
    print(a)