from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

try:
    import stackless
except ImportError:
    stackless = None

import timeit
import gc

results = dict()
RANGE = range(0, 100000, 10000)[1:]
if stackless:
    libs = ["stacklessb", "fibrab", "kamaeliab"]
else:
    libs = ["fibrab", "kamaeliab"]

for lib in libs:
    print lib
    for i in RANGE:
        print i 
        t = timeit.Timer(setup="import %s.hackysack"%lib, stmt="%s.hackysack.runit(%d, 1000, dbg=0)"%(lib, i))
        v = t.timeit(1)
        gc.collect()
        results.setdefault(lib, []).append(v)

for lib, v in results.items():
    open("%s.results"%lib, "w").write(repr(v))

