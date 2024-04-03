'''
A Library o Vector operations

Raise doc: https://realpython.com/python-raise-exception/
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
    
    lenA = len(A)
    lenB = len(B)

    if lenA < 2 or lenA > 3 or lenB < 2 or lenB > 3:
        raise ValueError('Points with wrong dimension')        
    if lenA == 2:
        A.append(0)
    if lenB == 2:
        B.append(0)

    ans_list = [ B[0]-A[0], B[1]-A[1], B[2]-A[2]]
    return np.array(ans_list)    

def GetLegth(A, B, numofDecimals = 2):
    """Returns the AB vector length.

    AB vector: Vector which starts at A and finishen on B

    Args:
        A: Start Point represented by a List of [x, y, z] values.
        B: End Point represented by a List of [x, y, z] values.

    Returns:
        A scalar which represents the numpy AB vector length

    Raises:
        IOError: If input is incorrect.
    return
    """
    ans_vector = CreateVector(A, B)
    return round(math.sqrt(sum(pow(element, 2) for element in ans_vector)), numofDecimals)

def GetAngle(A, B, C, numofDecimals = 4):
    """Returns the angle (in radians) between the BA and BC vectors.

    BA vector: Vector which starts at B and finishes on A
    BC vector: Vector which starts at B and finishes on C

    Dot Product
    BA.BC = |BA||BC|cos(angle)

    Args:
        A: Start Point represented by a List of [x, y, z] values.
        B: Point represented by a List of [x, y, z] values where the angle is measured.
        C: End Point represented by a List of [x, y, z] values.

    Returns:
        A numpy AB vector length

    Raises:
        IOError: If input is incorrect.
    return
    """
    vectorBA = CreateVector(B, A)
    vectorBC = CreateVector(B, C)
    dotProduct = np.dot(vectorBA, vectorBC)
    angle = round(math.acos(dotProduct/(GetLegth(B,A)*GetLegth(B,C))), numofDecimals)
    return angle

def GetAngleInDegrees(A, B, C, numofDecimals = 1):
    """Returns the angle (in radians) between the BA and BC vectors.

    BA vector: Vector which starts at B and finishes on A
    BC vector: Vector which starts at B and finishes on C

    Dot Product
    BA.BC = |BA||BC|cos(angle)

    Args:
        A: Start Point represented by a List of [x, y, z] values.
        B: Point represented by a List of [x, y, z] values where the angle is measured.
        C: End Point represented by a List of [x, y, z] values.

    Returns:
        A numpy AB vector length

    Raises:
        IOError: If input is incorrect.
    return
    """
    angle_radians = GetAngle(A, B, C, 4)
    
    return round(angle_radians*180/np.pi, numofDecimals)

print(GetAngleInDegrees([1,0],[0,0],[0,1]))
