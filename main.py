import tkinter as tk
from tkinter import filedialog
import customtkinter
from neurona.perceptron import read_data, run_perceptron


class dialog(customtkinter.CTk):
     def __init__(self, parent=None, initial_weights=None, final_weights=None, learning_rate=None, permissible_error=0, num_epochs=None, bias=None, error_norms=None, weights_evolution=None):
        super().__init__()
        self.geometry("360x400")
        self.title("Resumen")
        self.resizable(False, False)

        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2 + 600
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2 - 240
        self.geometry("+%d+%d" % (x, y))

        self.LabelDialog = customtkinter.CTkLabel(self, text="Resumen",
                                                  text_color="#A980D2",
                                                  font=("Arial", 20, "bold"))
        self.LabelDialog.place(x=140, y=20)

        # Display information in the textArea
        info_text = f"Configuración:\n\n"
        info_text += f"Pesos Iniciales: {initial_weights}\n"
        info_text += f"Pesos Finales: {final_weights}\n"
        info_text += f"Tasa de Aprendizaje: {learning_rate}\n"
        info_text += f"Error Permisible: {permissible_error}\n"
        info_text += f"Número de Épocas: {num_epochs}\n"

        self.textArea = customtkinter.CTkTextbox(master=self, width=360, height=200, corner_radius=0)
        self.textArea.place(x=0, y=80)
        self.textArea.insert("0.0", info_text)


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
                                                           font=("Arial", 12, "bold"), command=self.abrir_csv)
        self.Entrada_Archivo_CSV.place(x=265, y=100)

        self.boton_Calculos = customtkinter.CTkButton(self, text="Realizar cálculos",
                                                      fg_color="#A980D2", hover_color="#8C63B5",
                                                      command=self.run,
                                                      text_color="#FFFFFF", width=200,
                                                      font=("Arial", 12, "bold"), height=30)
        self.boton_Calculos.place(x=130, y=200)

        self.boton_Dialog = customtkinter.CTkButton(self, text="Abrir resumen",
                                                    command=self.button_click_event,
                                                    fg_color="#A980D2", hover_color="#8C63B5",
                                                    text_color="#FFFFFF", width=150, font=("Arial", 12, "bold"))
        self.boton_Dialog.place(x=265, y=140)

    def button_click_event(self):
        num_epoch = int(self.entrada_Epocas.get())
        num_learning_rate = float(self.entrada_ETA.get())

        
        results = run_perceptron(self.matrix_data, self.y_desired, self.matrix_data_w0, num_epoch, num_learning_rate)

       
        dialog_instance = dialog(self, **results)
        dialog_instance.mainloop()





    def abrir_csv(self):
        root = tk.Tk()
        root.withdraw()

        ruta_archivo_csv = filedialog.askopenfilename(
            title="Selecciona un archivo CSV", filetypes=[("Archivos CSV", "*.csv")]
        )

        if ruta_archivo_csv:
            print(f"Archivo CSV seleccionado: {ruta_archivo_csv}")
            self.matrix_data, self.y_desired, self.matrix_data_w0 = read_data(ruta_archivo_csv)

    def run(self):
        num_epoch = int(self.entrada_Epocas.get())
        num_learning_rate = float(self.entrada_ETA.get())
        run_perceptron(self.matrix_data, self.y_desired, self.matrix_data_w0, num_epoch, num_learning_rate)


Ventana = Ventana()
Ventana.configure(fg_color="#EFECF3")
Ventana.mainloop()