from sys import path
from pathlib import Path

# Obtener la ruta absoluta del directorio package
package_path = Path(__file__).parent.parent / 'package'
path.insert(0, str(package_path))

import extra.iota  # type: ignore
print(extra.iota.FunI())
