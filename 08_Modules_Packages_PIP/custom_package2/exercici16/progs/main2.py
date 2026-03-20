from sys import path
from pathlib import Path

# get abtsolute path and add it to libraries path
package_path = Path(__file__).parent.parent / 'package'
path.insert(0, str(package_path))

import extra.iota  # type: ignore
print(extra.iota.FunI())
import extra.good.best.tau
print(extra.good.best.tau.FunT())
