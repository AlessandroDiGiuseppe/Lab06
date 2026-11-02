import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_strumenti(self, e):
        self._view.lista_strumenti.controls.clear()
        strumenti = self._model.get_strumenti()

        if strumenti is None:
            self._view.show_alert("Errore durante la lettura dal database.")
            return

        if len(strumenti) == 0:
            self._view.lista_strumenti.controls.append(ft.Text("Nessuno strumento presente nel deposito."))
        else:
            for s in strumenti:
                self._view.lista_strumenti.controls.append(ft.Text(str(s)))

        self._view.update()

    def cerca_strumento(self, e):
        self._view.lista_strumenti_ricerca.controls.clear()
        tipo_cercato = self._view.input_tipo_strumento.value.strip()

        if not tipo_cercato:
            self._view.show_alert("Inserire un tipo di strumento per effettuare la ricerca!")
            return

        strumenti = self._model.cerca_strumenti_per_tipo(tipo_cercato)

        if strumenti is None:
            self._view.show_alert("Errore durante la ricerca nel database.")
            return

        if len(strumenti) == 0:
            self._view.lista_strumenti_ricerca.controls.append(
                ft.Text(f"Nessuno strumento trovato per il tipo: {tipo_cercato}")
            )
        else:
            for s in strumenti:
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))

        self._view.update()