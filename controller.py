
# Controllers interpret Model information for the View.
class Controller:

    def __init__(self, model):
        self.model = model #Richiamo il model!!!


    def set_image(self, name): #aggiorna immagine
        self.model.set_image(name) 
    
    def get_image(self):
        return self.model.get_image()