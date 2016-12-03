## code_examples_project_euler

Here are my solutions to some of the coding challenges on https://projecteuler.net/

I use the Linux command "time" to check the speed of programs
    time python3 hello.py

I use cProfile and pyprof2calltree to profile code.
    python3 -m cProfile -o myscript.cprof p12_highly_divisible_triangular_number.py 
    pyprof2calltree -k -i myscript.cprof
