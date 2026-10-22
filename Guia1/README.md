# Guía N°1

El propósito de esta guía es comenzar la repo de GitHub para el resto del semestre. Además de empezar a familiarizarse con el entorno de trabajo mediante una actividad de carga y visualización de señales básicas para responder las preguntas planteadas.

# Evidencia de la lista de comprobacion 2.10

Fecha de ejecución: 2026/10/22

## Resultado:

| Comprobacion | Resultado |
| --- | --- |
| Python | `Python 3.14.6` identificado |
| VS Code / `Prueba.py` | Ejecutado correctamente; imprime versiones de las bibliotecas |
| Git | Version `2.55.0.windows.2`; repositorio en rama `main` |
| `.venv` | `sys.executable` apunta a `.venv\Scripts\python.exe` |
| Paquetes | Imports correctos y `pip check` sin conflictos |
| Jupyter | El kernel devuelve `4` para `2 + 2` |
| Carpetas y archivos | Estructura de `Guia1` registrada |
| Graficos | Notebook ejecutado; se generaron la señal 1D y la imagen 2D |
| Dependencias | Inventario completo guardado con `pip freeze` |

## Archivos

- `comprobaciones_entorno.txt`: registro textual de todos los comandos y salidas.
- `Exploracion_Inicial.ipynb`: copia ejecutada del notebook

## Actividades

La fuente seleccionada para la señal 1D es el dataset
[GTZAN music/speech collection](https://www.kaggle.com/datasets/lnicalo/gtzan-musicspeech-collection),
publicado bajo licencia CC0. La actividad utilizará la copia de trabajo
[`Datos/Senal_1D/GTZAN/trabajo/musica_bagpipe.wav`](Datos/Senal_1D/GTZAN/trabajo/musica_bagpipe.wav).
Sus metadatos, unidades, parámetros de muestreo y limitaciones están
documentados en [`Datos/Senal_1D/GTZAN/FUENTE.md`](Datos/Senal_1D/GTZAN/FUENTE.md).

La Actividad B utiliza una imagen termográfica de un sistema fotovoltaico
documentada en [`Datos/Imagen_2D/PV_Termografia/FUENTE.md`](Datos/Imagen_2D/PV_Termografia/FUENTE.md).

Los análisis reproducibles están disponibles en:

- [`Notebooks/Actividad_A.ipynb`](Notebooks/Actividad_A.ipynb): señal 1D de audio.
- [`Notebooks/Actividad_B.ipynb`](Notebooks/Actividad_B.ipynb): imagen 2D termográfica.

## Síntesis integradora

### Comparación entre las representaciones

| Aspecto | Señal 1D: audio GTZAN | Imagen 2D: termografía fotovoltaica |
| --- | --- | --- |
| Fenómeno representado | Variación temporal de una señal acústica musical | Distribución espacial de intensidades de una imagen termográfica |
| Representación numérica | Vector `x[n]` de muestras PCM enteras; se usa una copia normalizada para graficar | Arreglo NumPy `I[y, x, c]` de forma `(512, 640, 3)` |
| Ejes o coordenadas | Tiempo `t[n] = n / fs`, con `fs = 22050 [Hz]`; amplitud digital normalizada | Coordenadas `x` e `y` en píxeles; `c` identifica los canales rojo, verde y azul |
| Unidades | Segundos para el eje temporal y amplitud digital normalizada | Píxeles y valores RGB codificados entre `0` y `255` |
| Evidencia de calidad | 661.500 muestras, 30 s, mono, paso temporal constante y 0 valores no finitos | JPEG RGB, 640 × 512 píxeles, 0 valores fuera de rango, ningún canal constante y sin saturación exacta en 0 o 255 |
| Limitaciones principales | Una sola pista no permite generalizar a toda la música; la amplitud no es una medición acústica calibrada | La imagen no contiene calibración radiométrica, emisividad ni condiciones completas de adquisición; JPEG puede introducir artefactos |

La señal de audio permite estudiar cambios a lo largo del tiempo, mientras que la
imagen permite estudiar patrones distribuidos espacialmente. En ambos casos la
representación numérica es útil para visualizar y calcular, pero no debe
interpretarse como una magnitud física calibrada cuando los metadatos no la
respaldan.

### Metadatos disponibles y faltantes

Ambas fuentes tienen procedencia, licencia, formato y parámetros básicos
documentados. Para un análisis de ingeniería más confiable todavía sería
necesario conservar o recuperar:

- Para el audio: micrófono, distancia a la fuente, nivel de grabación,
  ambiente acústico y etiquetas detalladas del contenido musical.
- Para la imagen: modelo y calibración de la cámara, emisividad, distancia,
  temperatura y humedad ambiente, condiciones eléctricas del panel, fecha y
  hora de captura, y la relación exacta entre los colores almacenados y la
  temperatura.

### Posible decisión tecnológica

Una decisión razonable sería utilizar el audio para construir un sistema de
clasificación exploratorio de música frente a voz, y la imagen para investigar
la detección de anomalías visuales en paneles fotovoltaicos. Antes de desplegar
cualquiera de los dos sistemas sería necesario ampliar la muestra, conservar
las etiquetas y metadatos de adquisición, separar entrenamiento y prueba, y
validar los resultados con mediciones de referencia.

### Pregunta concreta para inteligencia artificial

**¿Puede un modelo identificar automáticamente una posible anomalía térmica en
un panel fotovoltaico a partir de una imagen, manteniendo un nivel de falsos
negativos aceptable frente a una inspección experta?**

Para responderla se necesitarían:

1. **Etiquetas:** imagen normal o anómala, tipo de anomalía, ubicación de la
   región afectada y nivel de severidad.
2. **Mediciones de referencia:** temperatura radiométrica calibrada, diferencia
   de temperatura respecto de celdas vecinas, potencia o corriente del panel y
   resultado de una inspección técnica.
3. **Condiciones experimentales:** cámara y configuración, emisividad,
   distancia, ángulo, irradiancia, temperatura ambiente, carga eléctrica,
   resolución y procedimiento de adquisición.
4. **Validación experta:** revisión independiente de las etiquetas por personal
   especializado y comparación del modelo mediante sensibilidad, especificidad,
   precisión, tasa de falsos negativos y matriz de confusión.

Con la imagen RGB disponible sólo puede hacerse una exploración visual y
estadística de intensidades. No sería correcto afirmar que el modelo está
midiendo temperatura o diagnosticando fallas sin recuperar las mediciones y
metadatos anteriores.