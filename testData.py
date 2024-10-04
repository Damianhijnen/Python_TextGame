import travel
print("Game start\n")

def constructSession():
    class session:
        location = travel.construct()
        msg = "You are on the main square.\n 1. Go to Town Hall 2. Go to Forest: "
        state = "travel"
        character = constructCharacter()
    return session

    
def constructCharacter():
    class character:
        strength = 1
        speed = 1
        accuracy = 1
        endurance = 1
        hp = 100
    return character
sess = constructSession()
print(sess.character.hp)