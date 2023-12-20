
# Controllers interpret Model information for the View.
class Controller:

    def __init__(self, model):
        self.model = model


    def set_image(self, name): #aggiorna immagine
        self.model.set_image(name) #Richiamo il model!!!