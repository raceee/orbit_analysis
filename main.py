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


interval_one = [0, 3.14]
lambda_interval_one = [1, 3.14]
interval_two = []
lambda_interval_two = []
interval_three = []
lambda_interval_three = []

def fp_check(orbital):
    "returns single val"
    try:
        if orbital[len(orbital) - 1] == orbital[len(orbital) - 2]:
            # print("fp found")
            return orbital[len(orbital) - 1]
        else:
            return False
    except:
        return False


def two_cycle_check(orbital):
    "returns tuple"
    try:
        if orbital[len(orbital) - 1] == orbital[len(orbital) - 3] and orbital[len(orbital) - 2] == orbital[len(orbital) - 4]: 
            # print("two cycle found")
            return orbital[len(orbital) - 1], orbital[len(orbital) - 2]
        else: 
            return False
    except:
        return False


def vis(graph):
    fig = plt.figure()
    ax = fig.add_subplot()
    for pair in graph:
        print(pair)
        ax.scatter(pair[0], pair[1])
    plt.show()
    

def make_orbit(func, lambda_int, interval):
    all_points = []
    for l in lambda_int:
        for x in interval:
            orbital_of_x = [x]
            a = func(l,x)
            orbital_of_x.append(a)
            for _ in range(50):
                print("lambda: {} x: {} iter: {}".format(l,x,_))
                a = func(l, a)
                orbital_of_x.append(a)
                # check orbit

                fp = fp_check(orbital_of_x)
                print("fp: ", fp)
                if fp != False:
                    all_points.append([l,fp])
                else:
                    period = two_cycle_check(orbital_of_x)
                    print("period: ", period)
                    if period != False:
                        all_points.append([l,period[0]])
                        all_points.append([l,period[1]])
                    else:
                        pass
        if l == 1.2:
            break
    print("len of all points: ", len(all_points))
    vis(all_points)

# TODO critial point of func lol

def func_one(l, x):
    return l * np.sin(x) # maybe this 


def func_two(l,x):
    return l * np.cos(x)


def func_three(l, x):
    d = (x - x ** 3)/3
    f = l * d
    return f

if __name__ == "__main__":
    interval_one = [num/10 for num in range(31)] + [3.14]
    print(interval_one)
    lambda_one = [1]+[(num/10)+1 for num in range(1,215)]
    lambda_one = lambda_one[:22]+[3.14]
    print("---------------------------------------------------------")
    print(lambda_one)
    make_orbit(func_one, lambda_int=lambda_one, interval=interval_one)
    # make_orbit(func_one, lambda_int=lambda_interval_one, interval=interval_one)
