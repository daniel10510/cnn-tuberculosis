import tkinter as tk
from tkinter import messagebox
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import os

# --- CONFIGURACIÓN ---
CARPETA_IMAGENES = "FotosPrueba"
MODELO_H5 = "tuberculosis_model-99.h5"
TAMANO_IMAGEN = (256, 256)

# --- CARGAR MODELO UNA VEZ ---
model = load_model(MODELO_H5)

# --- LISTAR IMÁGENES ---
imagenes = [f for f in os.listdir(CARPETA_IMAGENES) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
indice_actual = 0

# --- PREDICCIÓN ---
def predecir_imagen(path):
    image = Image.open(path).convert('L').resize(TAMANO_IMAGEN)
    arr = img_to_array(image)
    arr = np.expand_dims(arr, axis=-1)
    arr = np.expand_dims(arr, axis=0)
    arr = arr / 255.0

    pred = model.predict(arr)[0][0]
    label = "Tuberculosis" if pred > 0.5 else "Normal"
    conf = pred if pred > 0.5 else (1 - pred)

    if label == "Tuberculosis":
        if conf > 0.9:
            stage = "Advanced stage"
        elif conf > 0.7:
            stage = "Intermediate stage"
        else:
            stage = "Early stage"
    else:
        stage = "N/A"

    return label, conf, stage

# --- ACTUALIZAR VISTA ---
def mostrar_siguiente():
    global indice_actual
    if indice_actual >= len(imagenes):
        messagebox.showinfo("Fin", "Ya no hay más imágenes.")
        return

    archivo = imagenes[indice_actual]
    ruta = os.path.join(CARPETA_IMAGENES, archivo)

    try:
        label, conf, stage = predecir_imagen(ruta)
        resultado = f"🧠 Predicción: {label} ({conf*100:.2f}%)\nEtapa: {stage}"

        img_raw = Image.open(ruta).convert('L').resize((300, 300))
        img_tk = ImageTk.PhotoImage(img_raw)

        imagen_label.configure(image=img_tk)
        imagen_label.image = img_tk

        resultado_label.config(text=f"{archivo}\n{resultado}")
        indice_actual += 1

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo procesar {archivo}\n{str(e)}")
        indice_actual += 1
        mostrar_siguiente()

# --- UI ---
root = tk.Tk()
root.title("🩺 Clasificador de Tuberculosis")
root.geometry("420x500")

titulo = tk.Label(root, text="Visor de Radiografías - Tuberculosis", font=("Arial", 14))
titulo.pack(pady=10)

imagen_label = tk.Label(root)
imagen_label.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
resultado_label.pack(pady=10)

boton_siguiente = tk.Button(root, text="➡️ Siguiente imagen", command=mostrar_siguiente, font=("Arial", 12), bg="#2196F3", fg="white")
boton_siguiente.pack(pady=20)

# Comienza mostrando la primera imagen
mostrar_siguiente()

root.mainloop()
