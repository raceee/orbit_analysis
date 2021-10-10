"""
Chapter 8
For each of the following functions, modifyu the program in Appendix B to compute the corresponding orbit diagram for the given lambda and x intervals.
Be sure to sue the critical point that lies in the given x-interval to plot the diagram

Methodology
for each chosen c, we will record the ultimate fate of the orbit of 0 sa follows. If the orbit of 0 under Qc1 is attracted to a fixed point p1 then we plot (c1 p1)
if the orbit of Qc2 is attracted to a 2 cycle then we plot c2, q1) and (c2, q2).
"""


import numpy as np
import matplotlib.pyplot as plt

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
        else:
            return False
    except:
        return False

def two_cycle_check(orbital):
    "returns tuple"
    try:
        if orbital[len(orbital) - 1] == orbital[len(orbital) - 3] and orbital[len(orbital) - 2] == orbital[len(orbital) - 4]: 
            print("two cycle found")
            return orbital[len(orbital) - 1], orbital[len(orbital) - 2]
        else: 
            return False
    except:
        return False

def vis(graph):
    fig = plt.figure()
    ax = fig.add_subplot(projection="2d")
    for pair in graph:
        ax.scatter(pair[0], pair[1])
    plt.show()
    

def make_orbit(func, lambda_int, interval):
    all_points = []
    for l in lambda_int:
        for x in interval:
            orbital_of_x = [x]
            a = func(x,l)
            orbital_of_x.append(a)
            for _ in range(500):
                a = func(a, l)
                orbital_of_x.append(a)
                # check orbit
                fp = fp_check(orbital_of_x)
                ppone, pptwo = two_cycle_check(orbital_of_x)
                if fp:
                    # points to plot (c, x)
                    all_points.append([l,fp])
                if ppone:
                    all_points.append([l,ppone])
                    all_points([l,pptwo])
    vis(all_points)



def func_one(l, x):
    return l * np.sin(x)


if __name__ == "__main__":

    range()
    make_orbit(func_one, lambda_int=lambda_interval_one, interval=interval_one)



