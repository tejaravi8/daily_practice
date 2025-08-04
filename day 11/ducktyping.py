class hen:
    def sound(self):
        return "cocok"

class cock:
    def sound(self):
        return "kokkurok"
    
def speak(bird):
    print(bird.sound())
    
c=cock()
speak(c)