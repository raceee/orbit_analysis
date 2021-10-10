"""
Chapter 8
For each of the following functions, modifyu the program in Appendix B to compute the corresponding orbit diagram for the given lambda and x intervals.
Be sure to sue the critical point that lies in the given x-interval to plot the diagram

Methodology
for each chosen c, we will record the ultimate fate of the orbit of 0 sa follows. If the orbit of 0 under Qc1 is attracted to a fixed point p1 then we plot (c1 p1)
if the orbit of Qc2 is attracted to a 2 cycle then we plot c2, q1) and (c2, q2).

"""


import numpy
import matplotlib

interval_one = []
lambda_interval_one = []
interval_two = []
lambda_interval_two = []
interval_three = []
lambda_interval_three = []

def fp_check(orbital):
    "returns single val"
    try:
        if orbital[len(orbital) - 1] == orbital[len(orbital) - 2]:
            print("fp found")
            return orbital[len(orbital) - 1]
    except:
        pass

def two_cycle_check(orbital):
    "returns tuple"
    try:
        if orbital[len(orbital) - 1] == orbital[len(orbital) - 3]:
            print("fp found")
            return orbital[len(orbital) - 1] , orbital[len(orbital) - 3]
    except:
        pass



def func_one(lambda_int, interval):
    for l in lambda_int:


    pass

def func_two():
    pass

def func_three():
    pass



