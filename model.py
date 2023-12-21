
#Model of MVC
class Model:

    def __init__(self):
       self.image = None
       self.images = [] # save in all images

    #my current image
    def set_image(self, name):
        self.image = name[0]
    
    def get_image(self):
        return self.image
    
    def get_images(self):
        return self.images    
    
    def add_image(self, name):
        if name in self.images:
            return
        self.images.append(name)
    
    def get_image_index(self, index):
        self.image =  self.images[index]
        return self.images[index]
        