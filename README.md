# 🩺 Implementación de un Modelo de Deep Learning para la Detección de Tuberculosis en Imágenes Médicas

Este proyecto implementa un modelo de *Deep Learning* basado en redes neuronales convolucionales (**CNN**) para la detección automática de **tuberculosis pulmonar** a partir de imágenes de rayos X.  
El desarrollo se realizó en **Google Colab** utilizando TensorFlow y técnicas de aumentación de datos. El objetivo es asistir en la evaluación temprana de tuberculosis a través de herramientas automatizadas de diagnóstico.

---

## 📂 Estructura del Proyecto

El código fuente se organiza en bloques funcionales, cubriendo todo el pipeline de desarrollo:

### 1️⃣ Carga y Visualización Básica del Dataset
- Montaje de Google Drive
- Carga del dataset desde la carpeta `DS`
- Visualización de imágenes y clases detectadas

### 2️⃣ Exploración Técnica del Dataset
- Conteo de imágenes por clase
- Análisis de balance de clases
- Identificación de tipos de archivos
- Visualización gráfica de la distribución del dataset

### 3️⃣ Definición del Modelo CNN con Aumentación de Datos
- Red convolucional personalizada
- Capas de normalización y aumentación de datos
- Capas de extracción y clasificación
- Compilación del modelo

### 4️⃣ Entrenamiento del Modelo
- Aplicación de pesos para clases desbalanceadas
- Entrenamiento con validación
- Gráfica de evolución de precisión y pérdida

### 5️⃣ Evaluación del Modelo
- Generación de matriz de confusión
- Reporte de métricas de clasificación: *precision*, *recall*, *F1-score*

### 6️⃣ Prueba con Imágenes Manuales
- Inferencia sobre imágenes nuevas contenidas en la carpeta `Prueba`
- Reporte detallado por imagen con nivel de confianza

---

## 🛠️ Tecnologías Utilizadas

- [Google Colab](https://colab.research.google.com/)
- [TensorFlow 2.x](https://www.tensorflow.org/)
- Python 3.x
- Scikit-learn
- Matplotlib
- Seaborn
- Pandas

---

## 📊 Resultados Esperados

- Clasificación automática en 2 categorías:
  - **Normal**
  - **Tuberculosis**
- Matriz de confusión para evaluar desempeño
- Precisión esperada en validación superior al 90% (dependiendo del dataset)

---

## 📁 Dataset

- Las imágenes se encuentran en la carpeta al interior del archivo ZIP `DS.zip` con subcarpetas por clase.
- Las imágenes de prueba se ubican en la carpeta `Prueba`.

> ⚠️ Nota: El dataset se incluye en este repositorio. Deberás cargarlo en Google Drive siguiendo la misma estructura.

---

## 🚀 Cómo Ejecutar

1. Clona este repositorio en tu entorno local o Google Colab:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```

2. Sube el código `ProyectoFinal_RASS.ipynb` a Google Colab.

3. Carga el archivo `DS.zip` al mismo nivel que el archivo `ProyectoFinal_RASS.ipynb`
   
4. Monta Google Drive y ajusta las rutas de `DS` y `Prueba` según tu Drive.

5. Ejecuta cada bloque secuencialmente:

    - Bloques 1 y 2 → Exploración
    - Bloque 3 → Definición de la red
    - Bloque 4 → Entrenamiento
    - Bloque 5 → Evaluación
    - Bloque 6 → Inferencias manuales

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
