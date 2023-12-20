
#Model of MVC
class Model:

    def __init__(self):
       self.image = None


    #my current image
    def set_image(self, name):
        self.image = name[0]
    
    def get_image(self):
        return self.image