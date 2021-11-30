def name(firstname):
    if firstname == "Gyula" :
        return "Hi Gyula"
    elif firstname == "Pascal" : 
        return "Hi Pascal, Grüße nach Saarbrücken" 
    else:
        return "I don't know you"

user_input = (input("Enter firstname:"))
print(name(user_input))