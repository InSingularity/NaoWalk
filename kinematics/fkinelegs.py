# File:        kineLegs.py
# Description: Contains Forward kinematics for Nao legs

from numpy import *
from math import *
from numpy.linalg import inv


def fkineLegs(*args):
    # fkineLegs(chain, pChain, pBody, hipYawPitch)

    # Return position kinematics from joint angles for Nao legs
    # chain = 'LLeg' or 'RLeg'
    # pChain = Position6D description of end effector
    # pBody = Position6D description of Nao wait
    # hipYawPitch = [] or set position of hipYawPitch motor


    chain = args[0]
    jAngles = args[1]
    pBody = args[2]

    if args < 3:
        pBody = zeros((6, 1))

    chainU = chain[0]

    if chainU.upper() == 'L':
        left = 1
    else:
        left = 0

    hipOffsetY = .050
    hipOffsetZ = .085
    thighLength = .1001
    tibiaLength = .1027
    footHeight = .046

    A0 = np.array([[1, 0, 0, 0],[0, 1, 0, y_s],[0, 0, 1, z_s],[0, 0, 0, 1]])
    T01 = np.array([[np.cos(q1), -np.sin(q1), 0, 0], [np.sin(q1), np.cos(q1), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    T12 = np.array([[1, 0, 0, 0], [0, 0, -1, -d2], [0, 1, 0, 0], [0, 0, 0, 1]])
    T23 = np.array([[np.cos(q3), -np.sin(q3), 0, 0], [0, 0, 1, 0], [-np.sin(q3), -np.cos(q3), 0, 0], [0, 0, 0, 1]])
    T34 = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, d4], [0, 0, 0, 1]])
    T45 = np.array([[np.cos(q5), -np.sin(q5), 0, 0], [0, 0, -1, 0], [np.sin(q5), np.cos(q5), 0, 0], [0, 0, 0, 1]])
    R5 = np.array([[-1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    A5 = np.array([[1, 0, 0, x_off], [0, 1, 0, y_off], [0, 0, 1, z_off], [0, 0, 0, 1]])
    TBody = np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(A0, T01), T12), T23), T34), T45), R5), A5)

    return q
