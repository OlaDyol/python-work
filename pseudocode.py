# write a for loop that iterates through this dictionary and prints the key followed by the value using f shorthand
# write a while loop that prints out while_num, decrements it by 1, and continues this pattern until it reaches \

csx = {
    "mp1": "hardware",
      "mp2": "skinny py",
      "mp3": "python basics",
      "mp4": "advanced OOP"
}
for mpx in csx:
    print (f"The key is {mpx}"),
    print (f"The value is {csx[mpx]}")
#new 
while_num = 10
while (while_num):
    print (while_num),
    while_num -=1