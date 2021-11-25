#from lectuer notes, practicing if else statements 
temperature =  int(input("What is the temperature outside?"))
#we are declaring the temperature variable by asking the user to input it in the input statement, however int() is then needed to make it an integer and not a string 
if temperature > 80:
    print("turn on the AC.")
else: 
    print("Open the windows.")
