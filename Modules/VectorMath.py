'''
A Library o Vector operations
'''

import numpy as np
import math

def CreateVector(A, B):
    """Returns the AB vector for a fiven A and B points.

    AB vector: Vector which starts at A and finishen on B

    Args:
        A: Start Point represented by a List of [x, y, z] values.
        B: End Point represented by a List of [x, y, z] values.

    Returns:
        A numpy AB vector

    Raises:
        IOError: If input is incorrect.
    return
    """
    ans_list = [ B[0]-A[0], B[1]-A[1], B[2]-A[2]]
    return np.array(ans_list)

def GetLegth(A, B):
    """Returns the AB vector length.

    AB vector: Vector which starts at A and finishen on B

    Args:
        A: Start Point represented by a List of [x, y, z] values.
        B: End Point represented by a List of [x, y, z] values.

    Returns:
        A numpy AB vector length

    Raises:
        IOError: If input is incorrect.
    return
    """
    ans_vector = CreateVector(A, B)
    return math.sqrt(sum(pow(element, 2) for element in ans_vector))
