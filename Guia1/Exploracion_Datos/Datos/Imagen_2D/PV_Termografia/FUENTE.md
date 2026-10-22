# Fuente de la imagen 2D

## Identificación

- **Dataset:** Photovoltaic system thermography
- **URL** <https://www.kaggle.com/datasets/marcosgabriel/photovoltaic-system-thermography>
- **Autor/a:** `marcosgabriel`
- **Versión de Kaggle:** 3
- **Fecha de actualización indicada por Kaggle:** 2023-08-19
- **Fecha de consulta:** 2026-10-22
- **Licencia indicada por Kaggle:** CC0: Public Domain
- **Fuente declarada:** imágenes del artículo sobre detección automática de anomalías en sistemas fotovoltaicos y un repositorio de GitHub indicado en la ficha de Kaggle
- **Archivo de trabajo:** `trabajo/termografia_panel_001R.jpg`

## Representación

La imagen de trabajo es JPEG RGB de 640 x 512 píxeles. Sus tres canales son
componentes de color de la imagen termográfica almacenada. El arreglo NumPy se usa para inspección y visualización, mientras
el JPEG original se conserva sin modificar.

La imagen incluye una anotación JSON asociada en la carpeta `trabajo`. Esa
anotación no se usa para alterar ni recortar la imagen en esta actividad.

## Limitaciones

La imagen no proporciona por sí sola una calibración radiométrica en grados
Celsius, emisividad, distancia, humedad, temperatura ambiente ni condiciones
de adquisición completas. Por tanto, el histograma describe la distribución
de valores RGB codificados, no una distribución física de temperaturas. La
compresión JPEG y la ausencia de metadatos de cámara pueden afectar la
interpretación de bordes, contraste y valores extremos.
