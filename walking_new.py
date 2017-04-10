import numpy as np
import threading

from utils.service_scripts import *

angles = np.load('angles_nao.npy')

HeadYaw = []
HeadPitch = []
LHipYawPitch = []
LHipRoll = []
LHipPitch = []
LKneePitch = []
LAnklePitch = []
LAnkleRoll = []
RHipYawPitch = []
RHipRoll = []
RHipPitch = []
RKneePitch = []
RAnklePitch = []
RAnkleRoll = []
LShoulderPitch = []
LShoulderRoll = []
LElbowYaw = []
LElbowRoll = []
LWristYaw = []
RShoulderPitch = []
RShoulderRoll = []
RElbowYaw = []
RElbowRoll = []
RWristYaw = []
RH = []
LH = []
RHand = []
LHand = []

Body = [HeadYaw, HeadPitch, LHipYawPitch, LHipRoll, LHipPitch, LKneePitch, LAnklePitch, LAnkleRoll,
        RHipYawPitch, RHipRoll, RHipPitch, RKneePitch, RAnklePitch, RAnkleRoll, LShoulderPitch,
        LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw, RShoulderPitch, RShoulderRoll, RElbowYaw,
        RElbowRoll, RWristYaw, LH, LHand, RH, RHand]

print ('Program started')

vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID == -1:
    exit(10)

print ('Connected to remote API server')


def reset_simulation():
    vrep.simxSynchronous(clientID, 1)
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
    vrep.simxSynchronousTrigger(clientID)


def walk(Body):
    global angles
    _angles = angles

    start_position(clientID, Body)

    per = [x for x in range(100)]

    for i in range(0, len(per)):
        LHipYawPitchVal = (_angles[0, 6] / len(per)) * i * 3.14 / 180
        LHipRollVal = (_angles[0, 7] / len(per)) * i * 3.14 / 180
        LHipPitchVal = (_angles[0, 8] / len(per)) * i * 3.14 / 180
        LKneePitchVal = (_angles[0, 9] / len(per)) * i * 3.14 / 180
        LAnklePitchVal = (_angles[0, 10] / len(per)) * i * 3.14 / 180
        LAnkleRollVal = (_angles[0, 11] / len(per)) * i * 3.14 / 180
        RHipYawPitchVal = (_angles[0, 0] / len(per)) * i * 3.14 / 180
        RHipRollVal = (_angles[0, 1] / len(per)) * i * 3.14 / 180
        RHipPitchVal = (_angles[0, 2] / len(per)) * i * 3.14 / 180
        RKneePitchVal = (_angles[0, 3] / len(per)) * i * 3.14 / 180
        RAnklePitchVal = (_angles[0, 4] / len(per)) * i * 3.14 / 180
        RAnkleRollVal = (_angles[0, 5] / len(per)) * i * 3.14 / 180

        # new_angels = [HeadYawVal, HeadPitchVal, LHipYawPitchVal, LHipRollVal, LHipPitchVal, LKneePitchVal,
        #               LAnklePitchVal, LAnkleRollVal, RHipYawPitchVal, RHipRollVal, RHipPitchVal, RKneePitchVal,
        #               RAnklePitchVal, RAnkleRollVal, LShoulderPitchVal, LShoulderRollVal, LElbowYawVal,
        #               LElbowRollVal, LWristYawVal, RShoulderPitchVal, RShoulderRollVal, RElbowYawVal,
        #               RElbowRollVal, RWristYawVal, LHVal, LHandVal, RHVal, RHandVal]
        new_angels = [0, 0, LHipYawPitchVal, LHipRollVal, LHipPitchVal, LKneePitchVal,
                      LAnklePitchVal, LAnkleRollVal, RHipYawPitchVal, RHipRollVal, RHipPitchVal, RKneePitchVal,
                      RAnklePitchVal, RAnkleRollVal, 0, 0, 0,
                      0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0]

        joint_move(clientID, Body, new_angels)


reset_simulation()
get_all_handles(clientID, Body)
walk(Body)
# print(threading.enumerate())
# t = threading.Thread(target=walk, name="t1")
# # t.daemon = True
# t.start()
# print(threading.enumerate())
