# A "simple" time conversion code
# This is my attempt at writing a code as long as possible.

loopOnOff = bool(True)
statement = "quit()"

# Header
print("  _____  _                                                             _               ")
print(" |_   _|(_) _ __ ___    ___    ___  ___   _ __ __   __ ___  _ __  ___ (_)  ___   _ __  ")
print("   | |  | || '_ ` _ \  / _ \  / __|/ _ \ | '_ \\ \ / // _ \| '__|/ __|| | / _ \ | '_ \ ")
print("   | |  | || | | | | ||  __/ | (__| (_) || | | |\ V /|  __/| |   \__ \| || (_) || | | |")
print("   |_|  |_||_| |_| |_| \___|  \___|\___/ |_| |_| \_/  \___||_|   |___/|_| \___/ |_| |_|\n")
print("### Written by Sj-ackdo, with an unnecessary amount of lines ###\n")





while loopOnOff == True: 
    convertedNumber = int()
    print('Do you want to convert (s)econds, (m)inutes, (h)ours, (d)ays, (w)eeks, (M)onths or (y)ears?')
    print('type "quit()" to leave prompt')
    convertAnswer = str(input())
    
    if convertAnswer == statement:
        loopOnOff == False
        break

    if convertAnswer == "s":
        print('to what unit? Valid options are:(m)inutes, (h)ours, (d)ays, (w)eeks, (M)onths or (y)ears')
        convertUnit = str(input())
        if convertUnit == "m":
            print("How many seconds do you want to convert?")
            amountTime = int(input())
            convertedNumber = amountTime / 60
            print( amountTime, "seconds are", convertedNumber, "minutes.")
        elif convertUnit == "h":
            print("How many seconds do you want to convert?")
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 60 
            print( amountTime, "seconds are", convertedNumber, "hours.")
        elif convertUnit == "d":
            print("How many seconds do you want to convert?")
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 60 
            convertedNumber = convertedNumber / 24
            print( amountTime, "seconds are", convertedNumber, "days.")
        elif convertUnit == "w":
            print("How many seconds do you want to convert?")
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 60 
            convertedNumber = convertedNumber /24
            convertedNumber = convertedNumber / 7
            print( amountTime, "seconds are", convertedNumber, "weeks.")
        elif convertUnit == "M":
            print("How many seconds do you want to convert?")
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 60 
            convertedNumber = convertedNumber /24
            convertedNumber = convertedNumber / 7
            convertedNumber = convertedNumber / 4
            print( amountTime, "seconds are", convertedNumber, "months.")
        elif convertUnit == "y":
            print("How many seconds do you want to convert?")
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 60 
            convertedNumber = convertedNumber /24
            convertedNumber = convertedNumber / 7
            convertedNumber = convertedNumber / 4
            convertedNumber = convertedNumber / 12
            print( amountTime, "seconds are", convertedNumber, "years.")

    if convertAnswer == "m":
        print('to what unit? Valid options are:(s)econds, (h)ours, (d)ays, (w)eeks, (M)onths or (y)ears')
        convertUnit = str(input())
        if convertUnit == "s":
            print('how many minutes do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            print( amountTime, "minutes are", convertedNumber, "seconds.")     
        elif convertUnit == "h":
            print('how many minutes do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 60
            print( amountTime, "minutes are", convertedNumber, "hours.")  
        elif convertUnit == "d":
            print('how many minutes do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 24
            print( amountTime, "minutes are", convertedNumber, "days.")  
        elif convertUnit == "w":
            print('how many minutes do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 24
            convertedNumber = convertedNumber / 7
            print( amountTime, "minutes are", convertedNumber, "weeks.")
        elif convertUnit == "M":
            print('how many minutes do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 24
            convertedNumber = convertedNumber / 7 
            convertedNumber = convertedNumber / 4
            print( amountTime, "minutes are", convertedNumber, "months.")    
        elif convertUnit == "y":
            print('how many minutes do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 60
            convertedNumber = convertedNumber / 24
            convertedNumber = convertedNumber / 7 
            convertedNumber = convertedNumber / 4
            convertedNumber = convertedNumber / 12
            print( amountTime, "minutes are", convertedNumber, "years.") 
    
    if convertAnswer == "h":
        print('to what unit? Valid options are:(s)econds, (m)inutes, (d)ays, (w)eeks, (M)onths or (y)ears')
        convertUnit = str(input())
        if convertUnit == "s":
            print('how many hours do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 60
            print( amountTime, "hours are", convertedNumber, "seconds.")     
        elif convertUnit == "m":
            print('how many hours do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            print( amountTime, "hours are", convertedNumber, "minutes.")  
        elif convertUnit == "d":
            print('how many hours do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 24
            print( amountTime, "hours are", convertedNumber, "days.")  
        elif convertUnit == "w":
            print('how many hours do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 24
            convertedNumber = convertedNumber / 7
            print( amountTime, "hours are", convertedNumber, "weeks.")
        elif convertUnit == "M":
            print('how many hours do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 24
            convertedNumber = convertedNumber / 7 
            convertedNumber = convertedNumber / 4
            print( amountTime, "hours are", convertedNumber, "months.")    
        elif convertUnit == "y":
            print('how many hours do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 24
            convertedNumber = convertedNumber / 7 
            convertedNumber = convertedNumber / 4
            convertedNumber = convertedNumber / 12
            print( amountTime, "hours are", convertedNumber, "years.")

    if convertAnswer == "d":
        print('to what unit? Valid options are:(s)econds, (m)inutes, (h)ours, (w)eeks, (M)onths or (y)ears')
        convertUnit = str(input())
        if convertUnit == "s":
            print('how many days do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 60
            convertedNumber = convertedNumber * 24
            print( amountTime, "days are", convertedNumber, "seconds.")     
        elif convertUnit == "m":
            print('how many days do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 60
            print( amountTime, "days are", convertedNumber, "minutes.")  
        elif convertUnit == "h":
            print('how many days do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            print( amountTime, "days are", convertedNumber, "hours.")  
        elif convertUnit == "w":
            print('how many days do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 7
            print( amountTime, "days are", convertedNumber, "weeks.")
        elif convertUnit == "M":
            print('how many days do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 7 
            convertedNumber = convertedNumber / 4
            print( amountTime, "days are", convertedNumber, "months.")    
        elif convertUnit == "y":
            print('how many days do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 7 
            convertedNumber = convertedNumber / 4
            convertedNumber = convertedNumber / 12
            print( amountTime, "days are", convertedNumber, "years.")

    if convertAnswer == "w":
        print('to what unit? Valid options are:(s)econds, (m)inutes, (h)ours, (d)ays, (M)onths or (y)ears')
        convertUnit = str(input())
        if convertUnit == "s":
            print('how many weeks do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 60
            convertedNumber = convertedNumber * 24
            convertedNumber = convertedNumber * 7
            print( amountTime, "weeks are", convertedNumber, "seconds.")     
        elif convertUnit == "m":
            print('how many weeks do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 24
            convertedNumber = convertedNumber * 7
            print( amountTime, "weeks are", convertedNumber, "minutes.")  
        elif convertUnit == "h":
            print('how many weeks do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 24
            convertedNumber = convertedNumber * 7
            print( amountTime, "weeks are", convertedNumber, "hours.")  
        elif convertUnit == "d":
            print('how many weeks do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 7
            print( amountTime, "weeks are", convertedNumber, "days.")
        elif convertUnit == "M":
            print('how many weeks do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 4
            print( amountTime, "weeks are", convertedNumber, "months.")    
        elif convertUnit == "y":
            print('how many weeks do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 4
            convertedNumber = convertedNumber / 12
            print( amountTime, "weeks are", convertedNumber, "years.")

    if convertAnswer == "M":
        print('to what unit? Valid options are:(s)econds, (m)inutes, (h)ours, (d)ays, (w)eeks or (y)ears')
        convertUnit = str(input())
        if convertUnit == "s":
            print('how many months do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 60
            convertedNumber = convertedNumber * 24
            convertedNumber = convertedNumber * 7
            convertedNumber = convertedNumber * 4
            print( amountTime, "months are", convertedNumber, "seconds.")     
        elif convertUnit == "m":
            print('how many months do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 24
            convertedNumber = convertedNumber * 7
            convertedNumber = convertedNumber * 4
            print( amountTime, "months are", convertedNumber, "minutes.")  
        elif convertUnit == "h":
            print('how many months do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 24
            convertedNumber = convertedNumber * 7
            convertedNumber = convertedNumber * 4
            print( amountTime, "months are", convertedNumber, "hours.")  
        elif convertUnit == "d":
            print('how many months do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 7
            convertedNumber = convertedNumber * 4
            print( amountTime, "months are", convertedNumber, "days.")
        elif convertUnit == "w":
            print('how many months do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 4
            print( amountTime, "months are", convertedNumber, "weeks.")    
        elif convertUnit == "y":
            print('how many months do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime / 12
            print( amountTime, "months are", convertedNumber, "years.")

    if convertAnswer == "y":
        print('to what unit? Valid options are:(s)econds, (m)inutes, (h)ours, (d)ays, (w)eeks or (M)onths')
        convertUnit = str(input())
        if convertUnit == "s":
            print('how many years do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 60
            convertedNumber = convertedNumber * 24
            convertedNumber = convertedNumber * 7
            convertedNumber = convertedNumber * 4
            convertedNumber = convertedNumber * 12
            print( amountTime, "years are", convertedNumber, "seconds.")     
        elif convertUnit == "m":
            print('how many years do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 60
            convertedNumber = convertedNumber * 24
            convertedNumber = convertedNumber * 7
            convertedNumber = convertedNumber * 4
            convertedNumber = convertedNumber * 12
            print( amountTime, "years are", convertedNumber, "minutes.")  
        elif convertUnit == "h":
            print('how many months do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 24
            convertedNumber = convertedNumber * 7
            convertedNumber = convertedNumber * 4
            convertedNumber = convertedNumber * 12
            print( amountTime, "years are", convertedNumber, "hours.")  
        elif convertUnit == "d":
            print('how many years do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 7
            convertedNumber = convertedNumber * 4
            convertedNumber = convertedNumber * 12
            print( amountTime, "years are", convertedNumber, "days.")
        elif convertUnit == "w":
            print('how many years do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 4
            convertedNumber = convertedNumber * 12
            print( amountTime, "years are", convertedNumber, "weeks.")    
        elif convertUnit == "M":
            print('how many years do you want to convert?')
            amountTime = int(input())
            convertedNumber = amountTime * 12
            print( amountTime, "years are", convertedNumber, "months.")

print("If you actually use this for time conversion, cudo's.")
print("~Sj-ackdo")




    
    
