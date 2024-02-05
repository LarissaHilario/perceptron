import tkinter as tk 
import customtkinter

class dialog(customtkinter.CTk):
    def __init__(self, parent=None):
        super().__init__()
        self.geometry("360x200")
        self.title("Resumen")
        self.transient(parent)
        self.resizable(False, False) 

        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2 + 600 
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2 - 240
        self.geometry("+%d+%d" % (x, y))

        self.LabelDialog = customtkinter.CTkLabel(self, text="Resumen",
                                                   text_color="#A980D2", 
                                                   font=("Arial", 20, "bold"))
        self.LabelDialog.place(x=140, y=20)

dialog = dialog()
dialog.configure(fg_color="#EFECF3")

class Ventana(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Neurona Artificial")
        self.geometry("460x260+100+100")

        self.label_Epocas = customtkinter.CTkLabel(self, text="Épocas", 
                                                   text_color="#A980D2", 
                                                   font=("Arial", 20, "bold"))
        self.label_Epocas.place(x=30, y=20)

        self.entrada_Epocas = customtkinter.CTkEntry(self, placeholder_text="Épocas", 
                                                     width=175, height=35)
        self.entrada_Epocas.place(x=30, y=55)

        self.label_ETA = customtkinter.CTkLabel(self, text="ETA", 
                                                text_color="#A980D2", 
                                                font=("Arial", 20, "bold"))
        self.label_ETA.place(x=30, y=100)

        self.entrada_ETA = customtkinter.CTkEntry(self, placeholder_text="Eta", 
                                                  width=175, height=35)
        self.entrada_ETA.place(x=30, y=135)

        self.label_Archivo_CSV = customtkinter.CTkLabel(self, text="Archivo CSV", 
                                                        text_color="#A980D2", 
                                                        font=("Arial", 20, "bold"))
        self.label_Archivo_CSV.place(x=280, y=65)

        self.Entrada_Archivo_CSV = customtkinter.CTkButton(self, text="Cargar CSV", 
                                                           fg_color="#A980D2", hover_color="#8C63B5", 
                                                           text_color="#FFFFFF", width=150, 
                                                           font=("Arial", 12, "bold"), command=self.abrir_csv,)
        self.Entrada_Archivo_CSV.place(x=265, y=100)

        self.boton_Calculos = customtkinter.CTkButton(self, text="Realizar cálculos", 
                                                      fg_color="#A980D2", hover_color="#8C63B5", 
                                                      text_color="#FFFFFF", width=200, 
                                                      font=("Arial", 12, "bold"), height=30)
        self.boton_Calculos.place(x=130, y=200)

        self.boton_Dialog = customtkinter.CTkButton(self, text="Abrir resumen", 
                                                   command=self.button_click_event,
                                                   fg_color="#A980D2", hover_color="#8C63B5",
                                                   text_color="#FFFFFF", width=150, font=("Arial", 12, "bold"))
        self.boton_Dialog.place(x=265, y=140)

    def button_click_event(self):
       dialog.mainloop()
        
    def abrir_csv(self):
        root = tk.Tk()
        root.withdraw()

        ruta_archivo_csv = tk.filedialog.askopenfilename(
            title="Selecciona un archivo CSV", filetypes=[("Archivos CSV", "*.csv")]
        )

        if ruta_archivo_csv:
            print(f"Archivo CSV seleccionado: {ruta_archivo_csv}")

Ventana = Ventana()
Ventana.configure(fg_color="#EFECF3")
Ventana.mainloop()