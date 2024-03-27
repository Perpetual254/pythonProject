class animals:
    limbs = 4
    eyes = 2

    def __init__(self, limbs, eyes):
        self.limbs = limbs
        self.eyes = eyes
        print("the limbs are:", self.limbs, "and eyes are:", self.eyes)

    def makesound(self):
        print("the animal makes the sound of")


class dog(animals):

    def makesound(self):
        print("the animal makes the sound of", "barking", "i am a dog")


class goat(animals):

    def makesound(self):
        print("the animal makes the sound of", "bleeting", "i am a goat")


dog1 = dog(4, 2)
dog1.makesound()

goat1 = goat(4, 2)
goat1.makesound()














