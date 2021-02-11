code_input = input("Enter the phrase you want to have encoded. ")

def secret_message_maker(code):
    original_code = list(code) # coverting string into a list and sending it variable
    new_code = []  #list to send values to 
    for i in original_code: #iterate through each item of list
        
        if i == "a":                  # takes each item through to check and cover to number
            new_code.append("01")
        elif i == "b":
            new_code.append("02")
        elif i == "c":
            new_code.append("03")
        elif i == "d":
            new_code.append("04")
        elif i == "e":
            new_code.append("05")
        elif i == "f":
            new_code.append("06")
        elif i == "g":
            new_code.append("07")
        elif i == "h":
            new_code.append("08")
        elif i == "i":
            new_code.append("09")
        elif i == "j":
            new_code.append("10")
        elif i == "k":
            new_code.append("11")
        elif i == "l":
            new_code.append("12")
        elif i == "m":
            new_code.append("13")
        elif i == "n":
            new_code.append("14")
        elif i == "o":
            new_code.append("15")
        elif i == "p":
            new_code.append("16")
        elif i == "q":
            new_code.append("17")
        elif i == "r":
            new_code.append("18")
        elif i == "s":
            new_code.append("19")
        elif i == "t":
            new_code.append("20")
        elif i == "u":
            new_code.append("21")
        elif i == "v":
            new_code.append("22")
        elif i == "w":
            new_code.append("23")
        elif i == "x":
            new_code.append("24")
        elif i == "y":
            new_code.append("25")
        elif i == "z":
            new_code.append("26")
        elif i == " ":
            new_code.append("27")

    return ".".join(new_code) #joins list together with period between each value

print(("Your encoded message is : "+ str(secret_message_maker(code_input))))  # prints new value with message
