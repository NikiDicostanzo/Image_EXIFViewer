from PIL import Image
import os
import time
from PIL.ExifTags import TAGS

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
            #print("INFO", self.info)
    
    def save_exif(self):
        self.exif={}
        img = Image.open(self.image)
        #print('Qui',self.image.format)
        if img._getexif() is None:
            print('Exif non presenti')
        else:
            if img.format == 'PNG':
                for tag, value in img.info.items():
                    decoded = TAGS.get(tag, tag)
                    self.exif[decoded] = value
            else:
                self.exif = {TAGS[k]: v
                                for k, v in img._getexif().items()
                                    if k in TAGS
                            }
            if  'GPSInfo' in self.exif.keys():
               print("GPS", len(self.exif['GPSInfo']), '\n', self.exif['GPSInfo'])
               # {1: 'N', 2: (43.0, 43.0, 37.3044), 3: 'E', 4: (11.0, 5.0, 45.8915)..}
               # degrees, minutes, and seconds
            #print("Exif data: ",self.exif)

    def get_info(self):
        return self.info
    
    def set_info(self):
        self.save_info()
    
    def get_exif(self):
        return self.exif
    
    def set_exif(self):
        self.save_exif()
    
    
        