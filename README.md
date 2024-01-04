# Image and EXIF Metadata Viewer
Questo progetto ha lo scopo di implementare una semplice applicazione di visualizzazione delle immagini e dei dati EXIF associati. Utilizza *Python* come linguaggio di programmazione insieme alla libreria *PyQt5*. 
<br>Il progetto adotta il pattern *Model-View-Controller*(MVC) per separare le responsabilità relative ai dati (Model), all'interfaccia utente (View) e alla logica di controllo (Controller).

## Installazione
Per installare le dipendenze necessarie per eseguire il progetto digitare i seguenti comandi:
```
    conda create -n viewer python=3.9
    conda activate viewer
    pip install pyqt5-tools
    conda install -c anaconda pillow
```
## Funzionalità dell'interfaccia utente
* **Visualizzazione delle immagini**: supporta la visualizzazione di immagini(una alla volta). Le immagini sono state ridimensionate per avere una dimensione massima (altezza o larghezza) di 512 pixel.
* **Visualizzazione dei dati EXIF dell'immagine**: elenca tutti i tag EXIF codificati nell'immagine.
* **Ridimensionamento**: la finestra dell'interfaccia utente supporta il ridimensionamento.
* **Rotazione dell'immagine**: supporta la rotazione dell'immagine. 
* **Geolocalizzazione**: Se un'immagine possiede il tag di geolocalizzazione GPS nel suo set di tag EXIF, permette agli utenti di fare clic su un pulsante per aprire un browser con Google Maps, che mostra la posizione GPS dell'immagine. Questa funzionalità sfrutta il modulo *webbrowser* di Python che consente l'apertura di una pagina web in un browser.
* **Visualizzazione di più immagini**: permette all'utente di aggiungere più immagini e implementa controlli per passare all'immagine precedente/successiva nell'elenco.
* **Hotkeys**: sono presenti delle *keyboard shortcuts*:
  *  *left* per uno shift verso sinistra
  *  *right* per uno shift verso destra
  *  *q* per una rotazione verso sinistra
  *  *w* per una rotazione verso destra
  
## Utilizzo
Per eseguire il progetto si deve digitare il seguente comando:
```
    python main.py
```
  
## Struttura del progetto
Il progetto adotta il pattern Model-View-Controller (MVC):
* **Model**: contiene tutte le informazioni necessarie per elaborare l'immagine e i suoi dati EXIF(se disponibili), include l'immagine corrente e la lista di tutte le immagini presenti. 
* **View**: definisce l'aspetto della finestra principale e collega i suoi pulsanti alle funzioni del Controller. La View è stata creata utilizzando *Qt Designer*. Il comando usato per generare il codice Python da un file `.ui` è il seguente:
```
    pyuic5 -x nome.ui -o nome.py
```
* **Controller**: Interpreta le informazioni del Model per la View. Ad esempio carica e salva l'immagine (gestisce l'I/O). 

## File
* main.py: inizializza le classi Model, Controller e View e avvia l'event loop dell'applicazione.
* model.py: contiene il Model dei dati e la business logic dell'applicazione. 
* view.py: gestisce l'interfaccia utente dell'applicazione. Ha metodi per visualizzare le immagini, gestire le interazioni dell'utente e aggiornare la visualizzazione.
* view_ui.py: contiene l'implementazione dell'interfaccia utente. Utilizza PyQt5 per definire il layout della finestra principale.
* controller.py: definisce il Controller, che agisce come intermediario tra il Model e la View. 

## Screen
<img width="320" alt="4_general_info" src="https://github.com/NikiDicostanzo/Image_EXIFViewer_/assets/32903530/9d8766b4-0326-4083-93fc-9e51e3c92454">
<img  width="220" alt="10_scale_window" src="https://github.com/NikiDicostanzo/Image_EXIFViewer_/assets/32903530/4f9ed415-69fa-4017-a3ad-693b8577ea8f"></div>
<img width="320" alt="6_right_rotation" src="https://github.com/NikiDicostanzo/Image_EXIFViewer_/assets/32903530/2416effd-0d8f-4036-b0c6-51226a393c14">
<img width="320" alt="5_left_rotation" src="https://github.com/NikiDicostanzo/Image_EXIFViewer_/assets/32903530/3374f73a-5c16-4709-b0b0-f99126a0ce8f">
<img width="320" alt="9_exif_data" src="https://github.com/NikiDicostanzo/Image_EXIFViewer_/assets/32903530/483d5d38-b532-430b-bcfa-4aa882c7195f">
<img width="320" alt="8_no_gpsData" src="https://github.com/NikiDicostanzo/Image_EXIFViewer_/assets/32903530/8c4d0274-5dd0-450f-8f48-173b6614725b">



