num_to_name = {1: "one",
          2: "two",
          3: "three",
          4: "four",
          5: "five",
          6: "six",
          7: "seven",
          8: "eight",
          9: "nine",
          10: "ten",
          11: "eleven",
          12: "twelve",
          13: "thirteen",
          14: "fourteen",
          15: "fifteen",
          16: "sixteen",
          17: "seventeen",
          18: "eighteen",
          19: "nineteen",
          20: "twenty",
          30: "thirty",
          40: "forty",
          50: "fifty",
          60: "sixty",
          70: "seventy",
          80: "eighty",
          90: "ninety",
          100: "hundred",
          1000: "thousand"}

def addTens():
    for i in range(20, 100, 10):
        for j in range(1, 10):
            num_to_name[i + j] = num_to_name[i] + num_to_name[j]

def addHundreds():
    num_to_name[100] = "hundred"
    for i in range(2, 10):
        num_to_name[i * 100] = num_to_name[i] + num_to_name[100]
    for i in range(200, 1000, 100):
        for j in range(1, 100):
            num_to_name[i + j] = num_to_name[i] + "and" + num_to_name[j]
    num_to_name[100] = "onehundred"
    for i in range(1, 100):
        num_to_name[100 + i] = num_to_name[100] + "and" + num_to_name[i]

def addThousands():
    num_to_name[1000] = "onethousand"

def initialize():
    addTens()
    addHundreds()
    addThousands()

def translate(num):
    initialize()
    thousands = 0
    numeral = []
    while num:
        triplet = num % 1000
        numeral.append(num_to_name[triplet] + (thousands * "thousand"))
        thousands += 1
        num //= 1000
        print(numeral)
    return list(reversed(numeral))

initialize()

through_one_thousand = [num_to_name[i] for i in range(1, 1001)]

def toCharacters():
    letters = ""
    for numeral in through_one_thousand:
        letters += numeral
    return letters

len(toCharacters()) # 21124
