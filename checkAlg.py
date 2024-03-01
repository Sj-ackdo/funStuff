import hashlib
import keyboard

def algType(num):
    switch={
      '1':"sha256",
      '2':"sha1",
      '3':"md5",
      '4':"sha512",
      }
    return switch.get(num,"Invalid input")

class algCalculate:
    def algorithmChoice(num, input):
        match num:
            case "1":
                result = hashlib.sha256(input.encode())
            case "2":
                result = hashlib.sha1(input.encode())
            case "3":
                result = hashlib.md5(input.encode())
            case "4":
                result = hashlib.sha512(input.encode())
        print("----------", algType(num), "----------\n", result.hexdigest(), "\n----------", algType(num), "----------\n")

comAlg = input("compare or calculate Algorithm?\n")  
match comAlg:
    case "calculate":      
        num = input("What Algorithm?\nPress 'L' for a full list.\n")
        if num == "L":
            print("1. sha256 / 2. sha1 / 3. md5 / 4. sha512")
            num = input("What Algorithm?\n")     
        input = input("Input:\n")
        algCalculate.algorithmChoice(num, input)
        keyboard.wait("enter")
    case "compare":
        hash1 = input("hash1:\n")
        hash2 = input("hash2\n")
        if hash1 == hash2:
            print("-----------------------\n", "hash 1 & 2 are the same")
            keyboard.wait("enter")
        else:
            print("----------!!!----------\n", "these hashes are not the same!")
            keyboard.wait("enter")
    case _:
        print("Invalid answer, retry\n")
        keyboard.wait("enter")