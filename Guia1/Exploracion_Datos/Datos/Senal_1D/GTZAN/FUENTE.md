# Fuente de la señal 1D

## Identificación

- **Dataset:** GTZAN music/speech collection
- **URL:** <https://www.kaggle.com/datasets/lnicalo/gtzan-musicspeech-collection>
- **Autor/a:** `lnicalo`
- **Versión de Kaggle:** 1
- **Fecha de actualización indicada por Kaggle:** 2017-10-24
- **Fecha de consulta:** 2026-10-22
- **Licencia indicada por Kaggle:** CC0: Public Domain
- **Formato:** WAV, PCM entero de 16 bits
- **Frecuencia de muestreo:** 22.050 Hz
- **Canales:** mono
- **Duración declarada:** 30 segundos por pista

## Señal seleccionada

La copia de trabajo es `trabajo/musica_bagpipe.wav`, tomada de la carpeta
musical del dataset. La señal de amplitud se representa como `x[n]`, donde
`n` es el índice de muestra y el tiempo se calcula con `t[n] = n / fs`, usando
`fs = 22050 Hz`.

La señal conserva sus muestras originales. Para visualizarla se convierte una
copia a punto flotante y se normaliza por el máximo valor absoluto del tipo
`int16`; esa transformación sólo afecta la representación gráfica y se
mantiene separada de los datos PCM originales.

## Alcance y limitaciones

El dataset fue creado para discriminar música y voz. La muestra seleccionada
permite estudiar una señal de audio musical real, pero no representa toda la
música ni permite concluir propiedades generales del género.

El paquete descargado completo se mantiene fuera del seguimiento mediante
`.gitignore`; la copia de trabajo es el único archivo que se incorpora al
análisis.
