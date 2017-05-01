from numpy.matlib import matrix, identity, zeros

import math

import string

HipOffsetY = 50.0
HipOffsetZ = 85.0
FootHeight = 45.19
ThighLength = 100.0
TibiaLength = 102.9

# class InverseKinematicsAgent:
'''
    def __init__(self, effector_name,targetpoint):
        #super(InverseKinematicsAgent, self).__init__()
        self.transforms = {n: identity(4) for n in self.joint_names}
	self.targetpoint = targetpoint
        # chains defines the name of chain and joints of the chain
        self.chains = {'Head': ['HeadYaw', 'HeadPitch']
                       # YOUR CODE HERE
		       'RArm': ['RShoulderRoll', 'RShoulderPitch', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand']
		       'LArm': ['LShoulderRoll', 'LShoulderPitch', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand']
		       'RLeg': ['RHipYawPitch', 'RHipPitch', 'RHipRoll', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll']
		       'LLeg': ['LHipYawPitch', 'LHipPitch', 'LHipRoll', 'LKneePitch', 'LAnklePitch', 'LAnkleRoll']
                       }
	self.predef = {'HipOffsetY': 50.0, 'HipOffsetZ': 85.0, 'FootHeight': 45.19, 'ThighLength': 100.0, 'TibiaLength': 102.9}
    def think(self, perception):
        self.inverse_kinematics(perception.joint)
        return super(InverseKinematicsAgent, self).think(perception)
'''


def Translation(x, y, z):
    Tl = identity(4)
    Tl = matrix([[1, 0, 0, x],
                 [0, 1, 0, y],
                 [0, 0, 1, z],
                 [0, 0, 0, 1]])
    return Tl


def RotationZ(joint_angle):
    Tz = identity(4)
    c = math.cos(joint_angle)
    s = math.sin(joint_angle)
    Tz = matrix([[c, -s, 0, 0],
                 [s, c, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])
    return Tz


def RotationY(joint_angle):
    Ty = identity(4)
    c = math.cos(joint_angle)
    s = math.sin(joint_angle)
    Ty = matrix([[c, 0, s, 0],
                 [0, 1, 0, 0],
                 [-s, 0, c, 0],
                 [0, 0, 0, 1]])
    return Ty


def RotationX(joint_angle):
    Tx = identity(4)
    c = math.cos(joint_angle)
    s = math.sin(joint_angle)
    Tx = matrix([[1, 0, 0, 0],
                 [0, c, -s, 0],
                 [0, s, c, 0],
                 [0, 0, 0, 1]])
    return Tx


def RotationXYZ(joint_angle_x, joint_angle_y, joint_angle_z):
    Txyz = RotationX(joint_angle_x)
    Txyz = Txyz * RotationY(joint_angle_y)
    Txyz = Txyz * RotationZ(joint_angle_z)
    return Txyz


def RotationZYX(joint_angle_x, joint_angle_y, joint_angle_z):
    Tzyx = RotationZ(joint_angle_z)
    Tzyx = Tzyx * RotationY(joint_angle_y)
    Tzyx = Tzyx * RotationX(joint_angle_x)
    return Tzyx


def DHTransformation(a, alpha, d, theta):
    Tdh = zeros(4)
    ca = math.cos(alpha)
    ct = math.cos(theta)
    sa = math.sin(alpha)
    st = math.sin(theta)
    Tdh = matrix([[ct, -st, 0, a],
                  [st * ca, ct * ca, -sa, -sa * d],
                  [st * sa, ct * sa, ca, ca * d],
                  [0, 0, 0, 1]])
    return Tdh


def fast_invert(A):
    B = []
    B = A.getI()
    return B


def prints(s):
    print s


def inverseLeftLeg(targetpoint):
    returnResult = [0, 0, 0, 0, 0, 0]
    HipOffsetY = 50.0
    HipOffsetZ = 85.0
    FootHeight = 45.19
    ThighLength = 100.0
    TibiaLength = 102.9
    TtempTheta5 = identity(4)
    T4i = identity(4)
    T5i = identity(4)
    T6i = identity(4)
    Ttemp = identity(4)
    Ttemp2 = identity(4)
    T = targetpoint
    Tinit = T
    base = Translation(0.0, HipOffsetY, -HipOffsetZ)
    base = fast_invert(base)
    base *= T
    base *= Translation(0.0, 0.0, -FootHeight)
    Rot = RotationXYZ(math.pi / 2, 0.0, 0.0)
    Rot *= base
    Tstart = Rot
    Rot = fast_invert(Rot)
    T = Rot

    side1 = ThighLength
    side2 = TibiaLength

    distancesqrd = math.pow(T[0, 3], 2) + math.pow(T[1, 3], 2) + math.pow(T[3, 3], 2)

    theta4 = math.pi - math.acos((math.pow(side1, 2) + math.pow(side2, 2) - distancesqrd) / (2 * side1 * side2))
    theta6 = math.atan(T[1, 3] / T[2, 3])
    T6i = DHTransformation(0.0, -math.pi / 2, 0.0, theta6)
    T6i *= RotationZYX(math.pi, -math.pi / 2, 0.0)
    T6i = fast_invert(T6i)
    Tstart *= T6i
    TtempTheta5 = Tstart
    TtempTheta5 = fast_invert(TtempTheta5)
    T4i = DHTransformation(-ThighLength, 0.0, 0.0, theta4)

    up = TtempTheta5[1, 3] * (TibiaLength + ThighLength * math.cos(theta4)) + ThighLength * TtempTheta5[
        0, 3] * math.sin(theta4)
    down = math.pow(ThighLength, 2) * math.pow(math.sin(theta4), 2) + TibiaLength + ThighLength * math.cos(theta4)

    theta5 = math.asin(-up / down - 1)
    T5i = DHTransformation(-TibiaLength, 0.0, 0.0, theta5)
    Ttemp = T4i
    Ttemp *= T5i
    Ttemp = fast_invert(Ttemp)
    Ttemp2 = Tstart
    Ttemp2 *= Ttemp
    temptheta2 = math.acos(Ttemp2[1, 2])
    theta2 = temptheta2 - math.pi / 4
    theta3 = math.asin(Ttemp2[1, 1] / math.sin(theta2 + math.pi / 4))
    temptheta1 = math.acos(Ttemp2[0, 2] / math.sin(theta2 + math.pi / 4))
    theta1 = temptheta1 + math.pi / 2
    returnResult[0] = theta1
    returnResult[1] = theta2
    returnResult[2] = theta3
    returnResult[3] = theta4
    returnResult[4] = theta5
    returnResult[5] = theta6
    print returnResult
    return returnResult


'''
    def inverseRightLeg(targetpoint):
	res = []
	targetPoint(0,1) = -targetPoint(0,1)
	targetPoint(1,0) = -targetPoint(1,0)
	targetPoint(1,2) = -targetPoint(1,2)
	targetPoint(2,1) = -targetPoint(2,1)
	targetPoint(1,3) = -targetPoint(1,3)
	res = inverseLeftLeg(targetpoint)
	for i in range (res.size):
		(res[i])[HIP_ROLL]=-(res[i])[HIP_ROLL]
		(res[i])[ANKLE_ROLL]=-(res[i])[ANKLE_ROLL]
	return res
'''
'''if __name__ == '__main__':
    agent = InverseKinematicsAgent()
    agent.run()'''