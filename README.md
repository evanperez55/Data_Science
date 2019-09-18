# matrices_multiplcation
Using different data types as well as different multiplication algorithms to see difference in runtime speed.

This program has four different algorithms that multiply matrices in different ways using loops:

1)Multiply using doubles
2)Multiply using ints
3)Multiply with doubles using rows inside of the inner loop instead of columns
4)Multiply with doubles using rows inside of the inner loop instead of columns


After running the program 7 times I came up with these statistics:

1) 15.61s ± 0.30
2) 14.97  ± 0.25
3) 15.64  ± 0.25
4) 15.12  ± 0.16

From the data above I can assume that of the data types, integers process faster than doubles when multiplying. Also, multiplying the matrices when looping through the rows on the outside loop with integers ended up being the fastest method. 

