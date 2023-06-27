def determineFavColor():
    userInput = input('Which color do you prefer - Red or Green?: ')
    return userInput

def determineFavoriteTeam():
    userInput2 = input('What is your favorite sports team? :')
    return userInput2

def retColorAndTeam():
    print(f"You prefer the color {usersFavColor}, and your favorite sports team is the {usersFavTeam}")

usersFavColor = determineFavColor()
usersFavTeam = determineFavoriteTeam()
retColorAndTeam()
