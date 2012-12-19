#!/usr/bin/env python
# File: funcs.py
# Author: Junfeng Li <li424@mcmaster.ca>
# Description: generate function finger
# Created: December 19, 2012

import matplotlib.pyplot as plt
import inspect

blacklists = ['show', ]

funcs = inspect.getmembers(plt, inspect.isfunction)

## function fingers
with open("funcs.jl", "w") as f:
    f.write("""#!/usr/bin/env julia
# File: funcs.jl
# Author: Junfeng Li <li424@mcmaster.ca>
# Description: function name of matplotlib.pyplot.
# Do not edit manully. It is generated by funcs.py
""")
    f.write('\n')
    f.write("funcs = (\n")
    for func in funcs:
        func = func[0]  # get function name
        if func[0] != '_' and not func in blacklists:
            f.write(':')
            f.write(func)
            f.write(',\n')
    f.write(")")

## export functions
with open("export.jl", "w") as f:
    f.write("""#!/usr/bin/env julia
# File: export.jl
# Author: Junfeng Li <li424@mcmaster.ca>
# Description: export wrapped functions
# Do not edit manully. It is generated by funcs.py
""")
    f.write('\n')
    f.write("export \n")
    for func in funcs:
        func = func[0]  # get function name
        if func[0] != '_' and not func in blacklists:
            f.write('\t')
            f.write(func)
            f.write(',\n')
    f.write('\t')
    f.write('plot')  # close export expr