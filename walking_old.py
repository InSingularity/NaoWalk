import vrep
import sys
import time
import numpy as np
import threading

angles = np.load('angles_nao.npy')


def walk():
    global angles
    _angles = angles

    vrep.simxFinish(-1)

    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

    vrep.simxSynchronous(clientID, 1)
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
    vrep.simxSynchronousTrigger(clientID)

    if clientID != -1:
        print("Connected to remote server")
        print("Lya")
    else:
        print('Connection not successful')
        sys.exit('Could not connect')

    errorCode, LShoulderPitch3 = vrep.simxGetObjectHandle(clientID, 'LShoulderPitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)

    errorCode, RShoulderPitch3 = vrep.simxGetObjectHandle(clientID, 'RShoulderPitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)

    # 7
    errorCode, LHipYawPitch3 = vrep.simxGetObjectHandle(clientID, 'LHipYawPitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 8
    errorCode, LHipRoll3 = vrep.simxGetObjectHandle(clientID, 'LHipRoll3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 9
    errorCode, LHipPitch3 = vrep.simxGetObjectHandle(clientID, 'LHipPitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 10
    errorCode, LKneePitch3 = vrep.simxGetObjectHandle(clientID, 'LKneePitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 11
    errorCode, LAnklePitch = vrep.simxGetObjectHandle(clientID, 'LAnklePitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    #
    errorCode, LAnkleRoll = vrep.simxGetObjectHandle(clientID, 'LAnkleRoll3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 7
    errorCode, RHipYawPitch3 = vrep.simxGetObjectHandle(clientID, 'RHipYawPitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 8
    errorCode, RHipRoll3 = vrep.simxGetObjectHandle(clientID, 'RHipRoll3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 9
    errorCode, RHipPitch3 = vrep.simxGetObjectHandle(clientID, 'RHipPitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 10
    errorCode, RKneePitch3 = vrep.simxGetObjectHandle(clientID, 'RKneePitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 11
    errorCode, RAnklePitch = vrep.simxGetObjectHandle(clientID, 'RAnklePitch3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)
    # 12
    errorCode, RAnkleRoll = vrep.simxGetObjectHandle(clientID, 'RAnkleRoll3#0', vrep.simx_opmode_oneshot_wait)
    print(errorCode)

    time.sleep(1)
    errorCode = vrep.simxSetJointTargetPosition(clientID, RShoulderPitch3, 90 * 3.1416 / 180, vrep.simx_opmode_oneshot)
    errorCode = vrep.simxSetJointTargetPosition(clientID, LShoulderPitch3, 90 * 3.1416 / 180, vrep.simx_opmode_oneshot)
    time.sleep(1)

    per = [x for x in range(100)]

    file_name = 'datasets/testfile_old.txt'
    f = open(file_name, "w+")

    for i in range(0, len(per)):
        # print(i)
        LHipYawPitch3Val = (_angles[0, 6] / len(per)) * i
        LHipRoll3Val = (_angles[0, 7] / len(per)) * i
        LHipPitch3Val = (_angles[0, 8] / len(per)) * i
        LKneePitch3Val = (_angles[0, 9] / len(per)) * i
        LAnklePitchVal = (_angles[0, 10] / len(per)) * i
        LAnkleRollVal = (_angles[0, 11] / len(per)) * i
        RHipYawPitch3Val = (_angles[0, 0] / len(per)) * i
        RHipRoll3Val = (_angles[0, 1] / len(per)) * i
        RHipPitch3Val = (_angles[0, 2] / len(per)) * i
        RKneePitch3Val = (_angles[0, 3] / len(per)) * i
        RAnklePitchVal = (_angles[0, 4] / len(per)) * i
        RAnkleRollVal = (_angles[0, 5] / len(per)) * i
        print LHipYawPitch3Val
        print LHipYawPitch3Val * 3.14 / 180

        vrep.simxPauseCommunication(clientID, 1)
        errorCode = vrep.simxSetJointTargetPosition(clientID, RKneePitch3, RKneePitch3Val * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, LKneePitch3, LKneePitch3Val * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, LHipYawPitch3, -LHipYawPitch3Val * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, LHipRoll3, LHipRoll3Val * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, LHipPitch3, LHipPitch3Val * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)  #
        errorCode = vrep.simxSetJointTargetPosition(clientID, LAnklePitch, LAnklePitchVal * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, LAnkleRoll, LAnkleRollVal * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, RHipYawPitch3, RHipYawPitch3Val * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, RHipRoll3, RHipRoll3Val * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, RHipPitch3, RHipPitch3Val * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)  #
        errorCode = vrep.simxSetJointTargetPosition(clientID, RAnklePitch, RAnklePitchVal * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        errorCode = vrep.simxSetJointTargetPosition(clientID, RAnkleRoll, RAnkleRollVal * 3.14 / 180,
                                                    vrep.simx_opmode_oneshot)
        vrep.simxPauseCommunication(clientID, 0)
        time.sleep(0.02)

        f.write("%.6f " % (-LHipYawPitch3Val * 3.14 / 180))
        f.write("%.6f " % (LHipRoll3Val * 3.14 / 180))
        f.write("%.6f " % (LHipPitch3Val * 3.14 / 180))
        f.write("%.6f " % (LKneePitch3Val * 3.14 / 180))
        f.write("%.6f " % (LAnklePitchVal * 3.14 / 180))
        f.write("%.6f " % (LAnkleRollVal * 3.14 / 180))
        f.write("%.6f " % (RHipYawPitch3Val * 3.14 / 180))
        f.write("%.6f " % (RHipRoll3Val * 3.14 / 180))
        f.write("%.6f " % (RHipPitch3Val * 3.14 / 180))
        f.write("%.6f " % (RKneePitch3Val * 3.14 / 180))
        f.write("%.6f " % (RAnklePitchVal * 3.14 / 180))
        f.write("%.6f " % (RAnkleRollVal * 3.14 / 180))
        f.write("\n")

    time.sleep(1)

    p = 0

    while p < 15:

        p = p + 1;

        for j in range(0, np.size(_angles, 0)):
            # print(i)
            LHipYawPitch3Val = _angles[j, 6]
            LHipRoll3Val = _angles[j, 7]
            LHipPitch3Val = _angles[j, 8]
            LKneePitch3Val = _angles[j, 9]
            LAnklePitchVal = _angles[j, 10]
            LAnkleRollVal = _angles[j, 11]
            RHipYawPitch3Val = _angles[j, 0]
            RHipRoll3Val = _angles[j, 1]
            RHipPitch3Val = _angles[j, 2]
            RKneePitch3Val = _angles[j, 3]
            RAnklePitchVal = _angles[j, 4]
            RAnkleRollVal = _angles[j, 5]

            time.sleep(0.02)

            vrep.simxPauseCommunication(clientID, 1)
            errorCode = vrep.simxSetJointTargetPosition(clientID, LHipYawPitch3, -LHipYawPitch3Val * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)
            errorCode = vrep.simxSetJointTargetPosition(clientID, LHipRoll3, LHipRoll3Val * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)
            errorCode = vrep.simxSetJointTargetPosition(clientID, LHipPitch3, LHipPitch3Val * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)  #
            errorCode = vrep.simxSetJointTargetPosition(clientID, LKneePitch3, LKneePitch3Val * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)
            errorCode = vrep.simxSetJointTargetPosition(clientID, LAnklePitch, LAnklePitchVal * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)
            errorCode = vrep.simxSetJointTargetPosition(clientID, LAnkleRoll, LAnkleRollVal * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)  # +

            errorCode = vrep.simxSetJointTargetPosition(clientID, RHipYawPitch3, RHipYawPitch3Val * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)
            errorCode = vrep.simxSetJointTargetPosition(clientID, RHipRoll3, RHipRoll3Val * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)
            errorCode = vrep.simxSetJointTargetPosition(clientID, RHipPitch3, RHipPitch3Val * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)  #
            errorCode = vrep.simxSetJointTargetPosition(clientID, RKneePitch3, RKneePitch3Val * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)
            errorCode = vrep.simxSetJointTargetPosition(clientID, RAnklePitch, RAnklePitchVal * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)
            errorCode = vrep.simxSetJointTargetPosition(clientID, RAnkleRoll, RAnkleRollVal * 3.14 / 180,
                                                        vrep.simx_opmode_oneshot)  # +
            vrep.simxPauseCommunication(clientID, 0)

            f.write("%.6f " % (-LHipYawPitch3Val * 3.14 / 180))
            f.write("%.6f " % (LHipRoll3Val * 3.14 / 180))
            f.write("%.6f " % (LHipPitch3Val * 3.14 / 180))
            f.write("%.6f " % (LKneePitch3Val * 3.14 / 180))
            f.write("%.6f " % (LAnklePitchVal * 3.14 / 180))
            f.write("%.6f " % (LAnkleRollVal * 3.14 / 180))
            f.write("%.6f " % (RHipYawPitch3Val * 3.14 / 180))
            f.write("%.6f " % (RHipRoll3Val * 3.14 / 180))
            f.write("%.6f " % (RHipPitch3Val * 3.14 / 180))
            f.write("%.6f " % (RKneePitch3Val * 3.14 / 180))
            f.write("%.6f " % (RAnklePitchVal * 3.14 / 180))
            f.write("%.6f " % (RAnkleRollVal * 3.14 / 180))
            f.write("\n")


print(threading.enumerate())
t = threading.Thread(target=walk, name="t1")
# t.daemon = True
t.start()
print(threading.enumerate())


# errorCode = vrep.simxSetJointTargetPosition(clientID,LHipYawPitch3,LHipYawPitch3Val*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,LHipRoll3,LHipRoll3Val*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,LHipPitch3,-LHipPitch3Val*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,LKneePitch3,LKneePitch3Val*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,LAnklePitch,LAnklePitchVal*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,LAnkleRoll,LAnkleRollVal*3.14/180, vrep.simx_opmode_oneshot)
#
#     errorCode = vrep.simxSetJointTargetPosition(clientID,RHipYawPitch3,-RHipYawPitch3Val*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,RHipRoll3,-RHipRoll3Val*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,RHipPitch3,-RHipPitch3Val*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,RKneePitch3,RKneePitch3Val*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,RAnklePitch,RAnklePitchVal*3.14/180, vrep.simx_opmode_oneshot)
#     errorCode = vrep.simxSetJointTargetPosition(clientID,RAnkleRoll,-RAnkleRollVal*3.14/180, vrep.simx_opmode_oneshot)
#


# Go back
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
