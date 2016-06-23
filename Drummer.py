class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
# Extend the example code to add a Drummer class. Drummers should be able to solo, 
# count to four, and spontaneously combust. Then add a Band class. Bands should be 
# able to hire and fire musicians, and have the musicians play their solos after 
# the drummer has counted time.

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Thump", "Bump", "Droll"])
        
    def count(self):
        print("One, two, three, four")
        
    def combust(self):
        print("Foosh! Aaaah!")
        
class Band(Musician):
    def hire(self):
        print("You're hired!")
        
    def fire(self):
        print("You're fired!")
        
    def play(self):
        Drummer.count()
        Drummer.solo(6)
        Bassist.solo(8)
        Guitarist.solo(6)

if __name__== "__main__":
    Band.play()