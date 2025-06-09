# 🩺 Implementación de un Modelo de Deep Learning para la Detección de Tuberculosis en Imágenes Médicas

Este proyecto implementa un modelo de *Deep Learning* basado en redes neuronales convolucionales (**CNN**) para la detección automática de **tuberculosis pulmonar** a partir de imágenes de rayos X.  
El desarrollo se realizó en **Google Colab** utilizando TensorFlow y técnicas de aumentación de datos. El objetivo es asistir en la evaluación temprana de tuberculosis a través de herramientas automatizadas de diagnóstico.

---

## 📂 Contenido del Repositorio

| Archivo / Carpeta          | Descripción                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `archivos-pruebas-modelo/`                  | Carpeta que contiene archivos para pruebas a partir del modelo H5 generado                            |
| `dataset/`                      | Carpeta que contiene el dataset de imágenes                                  |
| `video-desarrollo-implementacion-pruebas/`                  | Carpeta que contiene el video de desarrollo, implementacion y pruebas                            |
| `proyecto-final.ipynb`     | Notebook de Google Colab con todo el código fuente del proyecto             |
| `README.md`                | Documento actual con la descripción del proyecto                             |

---

## 📌 Descripción

El modelo fue entrenado utilizando un conjunto de imágenes de tórax clasificadas como:

- **Normal** 🫁
- **Tuberculosis (TB)** 🦠

Se implementaron las siguientes etapas:

✅ Preprocesamiento de imágenes  
✅ Balanceo de clases mediante **SMOTE**  
✅ Construcción de una arquitectura **CNN**  
✅ Entrenamiento y evaluación del modelo  
✅ Desarrollo de una interfaz interactiva con **ipywidgets** para predicción en línea  

---

## 🛠️ Tecnologías Utilizadas

- **Python 3**
- **TensorFlow / Keras**
- **OpenCV**
- **NumPy**
- **imbalanced-learn** (SMOTE)
- **scikit-learn**
- **matplotlib**
- **ipywidgets**
- **Google Colab**

---

## 🏗️ Arquitectura del Modelo

- 3 capas convolucionales (**Conv2D**) con activación **ReLU**
- Capa de **MaxPooling** después de cada capa convolucional
- Capa **Flatten** para conectar con capas densas
- Capa densa con 64 neuronas y activación **ReLU**
- Capa de **Dropout** para evitar sobreajuste
- Capa de salida con activación **sigmoid** para clasificación binaria (Normal / Tuberculosis)

---

## 📁 Dataset

- Las imágenes se encuentran en la carpeta al interior del archivo ZIP `dataset/Dataset of Tuberculosis Chest X-rays Images.zip` con subcarpetas por clase.

> ⚠️ Nota: El dataset se incluye en este repositorio. Deberás cargarlo en Google Drive siguiendo la misma estructura.

---

## 🚀 Cómo Ejecutar

1. Clona este repositorio en tu entorno local o Google Colab:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```

2. Sube el código `proyecto-final.ipynb` a Google Colab.

3. Carga el archivo `dataset/Dataset of Tuberculosis Chest X-rays Images.zip` al repositorio colab.
   
4. Monta Google Drive y ajusta las rutas del `dataset` según tu Drive.

5. Ejecuta cada bloque secuencialmente:

---

## 📜 Licencia

Este proyecto es de uso académico.  
Puedes utilizarlo y modificarlo para fines educativos y de investigación.

---

## ✏️ Autores

- **Enrique Miranda**
- **Daniel Herrera**
- **Ivan Davalos**
- **Roy Sillerico**
- **Rumy Mamani** 
- Estudiantes del Módulo "Modelamiento de Datos I"  
- Proyecto de la Maestría en Inteligencia Artificial y Ciencia de Datos  
- Universidad Mayor de San Andrés

---

## 🤝 Agradecimientos

- Al docente del módulo "Modelamiento de datos I", Msc. Edwin Salcedo.
- A la comunidad de [TensorFlow](https://www.tensorflow.org/community) por la documentación.

---
