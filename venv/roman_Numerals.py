s = input()
roman_l = "IVXLCDM" #  All of the roman numerals
roman_I = "VX" #  "I" will substract these
roman_X = "LC" #  So on so forth
roman_C = "DM"
roman_n = [1, 5, 10, 50, 100, 500, 1000] #  total number in same location as roman_l
test = False
count = 0
total = 0

if 15 >= len(s) >= 1: #  checks if character is greater than 1 or less than 15
    while count < len(s):
        if s[count] in roman_l: #  checks if string input is part of roman numerals
            count += 1
            test = True
        else:
            test = False
            count += 1
            break

count = 0
while count < len(s) and test: #  if conditions above true, executes
    if count < len(s):
        if count < len(s) - 1 and s[count] == "I" and s[count + 1] in roman_I: #  I substraction
            total += roman_n[roman_l.index(s[count + 1])] - 1 #substract 1 from number after the number being compared
            # Letters retrieved by going to current s position which position is then searched in roman_l letter
            # position which is then searched within position of roman_n which represents numerical roman letter value
            count += 2 #  Increments two because you substract one, move 2 position
        elif count < len(s) - 1 and s[count] == "X" and s[count + 1] in roman_X: # X substraction
            total += roman_n[roman_l.index(s[count + 1])] - 10
            count += 2
        elif count < len(s) - 1 and s[count] == "C" and s[count + 1] in roman_C:
            total += roman_n[roman_l.index(s[count + 1])] - 100
            count += 2
        elif count < len(s):
            total += roman_n[roman_l.index(s[count])] # if not substracting, add one by one
            count += 1

print(total)