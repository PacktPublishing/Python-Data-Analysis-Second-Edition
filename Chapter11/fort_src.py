from numpy import f2py
fsource = b'''
       subroutine sumarray(A, N)
       REAL, DIMENSION(N) :: A
       INTEGER :: N
       RES = 0.1 * SUM(A, MASK = A .GT. 0)
       RES2 = -0.025 * SUM(A, MASK = A .LT. 0)
       print*, RES + RES2
       end 
 '''
f2py.compile(fsource,modulename='fort_sum',verbose=0)
