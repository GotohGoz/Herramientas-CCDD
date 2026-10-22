print('Holaaaaaaaaaaaaaaaaaa')

import importlib.metadata as metadata
import numpy, pandas, scipy, matplotlib, plotly, PIL, skimage, jupyter, ipykernel
for paquete in ("numpy", "pandas", "scipy", "matplotlib", "plotly",
"pillow", "scikit-image", "jupyter", "ipykernel"):
    print(paquete, metadata.version(paquete))