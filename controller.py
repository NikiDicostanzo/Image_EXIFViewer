
# Controllers interpret Model information for the View.
class Controller:

    def __init__(self, model):
        self.model = model #Richiamo il model!!!


    def set_image(self, name): #aggiorna immagine
        self.model.set_image(name) 
        self.model.save_exif()
    
    def get_image(self):
        return self.model.get_image()
    
    def get_length(self):
        return len(self.get_images())
    
    def get_images(self):
        return self.model.get_images()
    
    def add_image(self, name):
        self.model.add_image(name)
        self.set_image(name)
    
    def get_image_index(self, index):
        image = self.model.get_image_index(index)
        self.model.set_image(image)

    def get_info(self):
       return self.model.save_info()
    
    def set_info(self):
        self.model.save_info()
    
    def set_exif(self):
        self.model.save_exif()
    