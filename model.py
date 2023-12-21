from PIL import Image
import os
import time

#Model of MVC
class Model:

    def __init__(self):
       self.image = None
       self.images = [] # save in all images
       
       #DATA
       self.info = {}
       self.exif = {}

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
    
    def save_info(self):
        self.info = {}
        if self.image !='':
            image = Image.open(self.image)
            
            self.info['Nome file'] = os.path.basename(image.filename)
            self.info['Formato'] = image.format
            self.info['Dimensione immagine'] = image.size
            self.info['Data creazione'] = time.ctime(os.path.getctime(image.filename))
            self.info['Ultima modifica'] = time.ctime(os.path.getmtime(image.filename))
            print("INFO", self.info)
            
    def get_info(self):
        return self.info
    
    def set_info(self):
        self.save_info()