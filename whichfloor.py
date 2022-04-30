maximumn_stories = 25
position = int(input("On what floor of the building is your office?"))

while(position > maximumn_stories):
    print("You entered: ", position, "there are only", maximumn_stories, "in the building. Please, try again")
    position =int(input("On what floor of the building is your office?"))

print("Congratulation! You work on", position, "floor.")