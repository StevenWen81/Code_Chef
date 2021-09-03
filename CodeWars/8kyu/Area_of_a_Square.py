import math
def square_area(A):
    # A = 1/2 pi r
    r = 2 * A / math.pi
    ans = pow(r,2)
    return float(f"{ans:.2f}")
