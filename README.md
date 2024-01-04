# Image*EXIFViewer*
Questo progetto ha lo scopo di implementare una semplice applicazione di visualizzazione delle immagini e dei dati EXIF associati. Utilizza *Python* come linguaggio di programmazione e *PyQt5* come toolkit della GUI. Il progetto adotta il modello Model-View-Controller (MVC) per separare le responsabilità relative ai dati (Model), all'interfaccia utente (View) e alla logica di controllo (Controller).

## Installazione
Per installare le dipendenze necessarie per eseguire il progetto digitare i seguenti comandi:
```
    conda create -n viewer python=3.9
    conda activate viewer
    pip install pyqt5-tools
    conda install -c anaconda pillow
```
## Funzionalità
* **Visualizzazione delle immagini**: l'interfaccia utente supporta la visualizzazione di immagini JPEG (una alla volta). Le immagini sono state ridimensionate per avere una dimensione massima (altezza o larghezza) di 512 pixel.

* **Visualizzazione dei dati EXIF dell'immagine**: l'interfaccia utente elenca tutti i tag EXIF codificati nel file JPEG. Quando il numero di tag è troppo grande per essere visualizzato nella finestra dell'applicazione, l'interfaccia utente fornisce un widget di scorrimento per visualizzarli tutti.

* **Ridimensionamento**: la finestra principale dell'interfaccia utente supporta il ridimensionamento. Quando l'utente ridimensiona l'applicazione, tutta l'interfaccia utente viene ridimensiona.

* **Rotazione dell'immagine**: l'interfaccia utente supporta la rotazione dell'immagine. Per accedere alla rotazione, supporta sia un'interfaccia di pulsanti sia un'interfaccia di tasti di scelta rapida.

* **Geolocalizzazione**: se un'immagine ha tag di geolocalizzazione GPS nel suo set di tag EXIF, il visualizzatore implementa una funzione che consente agli utenti di fare clic sul pulsante e aprire un browser con Google Maps centrato sulla posizione GPS dell'immagine.

* **Visualizzazione di più immagini**: l'interfaccia permette all'utente di aggiungere più di un'immagine e implementa controlli per passare all'immagine precedente/successiva  nell'elenco.
* **Hotkeys**: sono stati inserite delle *keyboard shortcuts*:
  *  *Left* per uno shift verso sinistra
  *  *Right* per uno shift verso destra
  *  *Q* per una rotazione verso sinistra
  *  *W* per una rotazione verso destra
  
## Utilizzo
Per eseguire il progetto, usa il seguente comando:
```
    python main.py
```
  
## Struttura del progetto

* **Model**: contiene tutte le informazioni necessarie per elaborare l'immagine e i suoi dati EXIF (se disponibili), include l'immagine corrente e la lista di tutte le immagini presenti. 

* **View**: definisce l'aspetto della finestra principale e collega i suoi pulsanti alle funzioni del Controller. La View è stata creata utilizzando *Qt Designer*. Il comando usato per generare il codice Python da un file `.ui` è il seguente:
```
    pyuic5 -x nome.ui -o nome.py
```
* **Controller**: carica e salva l'immagine (gestisce l'I/O). Interpreta le informazioni del Model per la View.

## File
* main.py: inizializza le classi Model, Controller e View e avvia l'event loop dell'applicazione.
* model.py: contiene il Model dei dati e la business logic dell'applicazione. 
* view.py: gestisce l'interfaccia utente dell'applicazione. Ha metodi per visualizzare le immagini, gestire le interazioni dell'utente e aggiornare la visualizzazione.
* view_ui.py: contiene l'implementazione dell'interfaccia utente. Utilizza PyQt5 per definire il layout della finestra principale.
* controller.py: definisce il Controller, che agisce come intermediario tra il Model e la View. 

## Screen

