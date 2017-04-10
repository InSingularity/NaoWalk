import vrep
import sys
import time
import numpy as np
import threading

from utils.service_scripts import *

angles = np.load('angles_nao.npy')

HeadYaw = [];
HeadPitch = [];
LHipYawPitch = [];
LHipRoll = [];
LHipPitch = [];
LKneePitch = [];
LAnklePitch = [];
LAnkleRoll = [];
RHipYawPitch = [];
RHipRoll = [];
RHipPitch = [];
RKneePitch = [];
RAnklePitch = [];
RAnkleRoll = [];
LShoulderPitch = [];
LShoulderRoll = [];
LElbowYaw = [];
LElbowRoll = [];
LWristYaw = []
RShoulderPitch = [];
RShoulderRoll = [];
RElbowYaw = [];
RElbowRoll = [];
RWristYaw = []
RH = [];
LH = [];
RHand = [];
LHand = [];
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

vrep.simxSynchronous(clientID, 1)
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
vrep.simxSynchronousTrigger(clientID)

get_all_handles(clientID, Body)

def walk():
    global angles
    _angles = angles

    while 1:
        start_position(clientID, 0, Body)

    per = [x for x in range(100)]

    # for i in range(0, len(per)):
    #     #print(i)
    #     LHipYawPitchVal = (_angles[0, 6] / len(per)) * i
    #     LHipRollVal = (_angles[0, 7] / len(per)) * i
    #     LHipPitchVal = (_angles[0, 8] / len(per)) * i
    #     LKneePitchVal = (_angles[0, 9] / len(per)) * i
    #     LAnklePitchVal = (_angles[0, 10] / len(per)) * i
    #     LAnkleRollVal = (_angles[0, 11] / len(per)) * i
    #     RHipYawPitchVal = (_angles[0, 0] / len(per)) * i
    #     RHipRollVal = (_angles[0, 1] / len(per)) * i
    #     RHipPitchVal = (_angles[0, 2] / len(per)) * i
    #     RKneePitchVal = (_angles[0, 3] / len(per)) * i
    #     RAnklePitchVal = (_angles[0, 4] / len(per)) * i
    #     RAnkleRollVal = (_angles[0, 5] / len(per)) * i
    #
    #     angles_to_script = [
    #         HeadYawVal, HeadPitchVal, LHipYawPitchVal, LHipRollVal, LHipPitchVal, LKneePitchVal, LAnklePitchVal, LAnkleRollVal,
    #         RHipYawPitchVal, RHipRollVal, RHipPitchVal, RKneePitchVal, RAnklePitchVal, RAnkleRollVal, LShoulderPitchVal,
    #         LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw, RShoulderPitch, RShoulderRoll, RElbowYaw,
    #         RElbowRoll, RWristYaw, LH, LHand, RH, RHand
    #     ];
    #
    #     Body = [],
    #     joint_move(clientID, 0, Body, angles_to_script);
    #     vrep.simxPauseCommunication(clientID, 1)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, RKneePitch3, RKneePitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, LKneePitch3, LKneePitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, LHipYawPitch3, -LHipYawPitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, LHipRoll3, LHipRoll3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, LHipPitch3, LHipPitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)  #
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, LAnklePitch, LAnklePitchVal * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, LAnkleRoll, LAnkleRollVal * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, RHipYawPitch3, RHipYawPitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, RHipRoll3, RHipRoll3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, RHipPitch3, RHipPitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)  #
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, RAnklePitch, RAnklePitchVal * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     errorCode = vrep.simxSetJointTargetPosition(clientID, RAnkleRoll, RAnkleRollVal * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #     vrep.simxPauseCommunication(clientID, 0)
    #     time.sleep(0.02)
    #
    # time.sleep(1)
    #
    # p=0
    #
    # while p < 15:
    #
    #      p=p+1;
    #
    #      for j in range(0, np.size(_angles, 0)):
    #         #print(p, j)
    #         LHipYawPitch3Val = _angles[j, 6]
    #         LHipRoll3Val = _angles[j, 7]
    #         LHipPitch3Val = _angles[j, 8]
    #         LKneePitch3Val = _angles[j, 9]
    #         LAnklePitchVal = _angles[j, 10]
    #         LAnkleRollVal = _angles[j, 11]
    #         RHipYawPitch3Val = _angles[j, 0]
    #         RHipRoll3Val = _angles[j, 1]
    #         RHipPitch3Val = _angles[j, 2]
    #         RKneePitch3Val = _angles[j, 3]
    #         RAnklePitchVal = _angles[j, 4]
    #         RAnkleRollVal = _angles[j, 5]
    #
    #         time.sleep(0.02)
    #
    #         vrep.simxPauseCommunication(clientID, 1)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, LHipYawPitch3, -LHipYawPitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, LHipRoll3, LHipRoll3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, LHipPitch3, LHipPitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)  #
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, LKneePitch3, LKneePitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, LAnklePitch, LAnklePitchVal * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, LAnkleRoll, LAnkleRollVal * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)#+
    #
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, RHipYawPitch3, RHipYawPitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, RHipRoll3, RHipRoll3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, RHipPitch3, RHipPitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)  #
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, RKneePitch3, RKneePitch3Val * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, RAnklePitch, RAnklePitchVal * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot)
    #         errorCode = vrep.simxSetJointTargetPosition(clientID, RAnkleRoll, RAnkleRollVal * 3.14 / 180,
    #                                             vrep.simx_opmode_oneshot) #+
    #         vrep.simxPauseCommunication(clientID, 0)

print(threading.enumerate())
t = threading.Thread(target=walk,  name="t1")
#t.daemon = True
t.start()
print(threading.enumerate())


# errorCode = vrep.simxSetJointTargetPosition(clientID,LHipYawPitch3,LHipYawPitch3Val*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,LHipRoll3,LHipRoll3Val*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,LHipPitch3,-LHipPitch3Val*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,LKneePitch3,LKneePitch3Val*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,LAnklePitch,LAnklePitchVal*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,LAnkleRoll,LAnkleRollVal*3.14/180, vrep.simx_opmode_oneshot)
#
# errorCode = vrep.simxSetJointTargetPosition(clientID,RHipYawPitch3,-RHipYawPitch3Val*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,RHipRoll3,-RHipRoll3Val*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,RHipPitch3,-RHipPitch3Val*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,RKneePitch3,RKneePitch3Val*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,RAnklePitch,RAnklePitchVal*3.14/180, vrep.simx_opmode_oneshot)
# errorCode = vrep.simxSetJointTargetPosition(clientID,RAnkleRoll,-RAnkleRollVal*3.14/180, vrep.simx_opmode_oneshot)



#Go back
# vrep.simxPauseCommunication(clientID, 1)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, LHipYawPitch3, -LHipYawPitch3Val * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, LHipRoll3, LHipRoll3Val * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, LHipPitch3, LHipPitch3Val * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)  #
#             errorCode = vrep.simxSetJointTargetPosition(clientID, LKneePitch3, LKneePitch3Val * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, LAnklePitch, LAnklePitchVal * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, LAnkleRoll, -LAnkleRollVal * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, RHipYawPitch3, RHipYawPitch3Val * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, RHipRoll3, RHipRoll3Val * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, RHipPitch3, RHipPitch3Val * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)  #
#             errorCode = vrep.simxSetJointTargetPosition(clientID, RKneePitch3, RKneePitch3Val * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, RAnklePitch, RAnklePitchVal * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             errorCode = vrep.simxSetJointTargetPosition(clientID, RAnkleRoll, -RAnkleRollVal * 3.14 / 180,
#                                                 vrep.simx_opmode_oneshot)
#             vrep.simxPauseCommunication(clientID, 0)