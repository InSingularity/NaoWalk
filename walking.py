import numpy as np

from utils.vrep_scripts import *
from utils.service_scripts import *

#filename = 'datasets/training_data.txt'
filename = 'datasets/head_training_data.txt'
#filename = 'datasets/training_data_only_first_moves.txt'
#filename = 'datasets/training_data2.txt'
#filename = 'datasets/training_data_1_2999_sample_0.1s.txt'
#filename = 'datasets/training_data_1_9999_sample_0.1s.txt'
#filename = 'datasets/verification_training_data.txt'
#filename = 'datasets/start_moviment.txt'
dataset = []

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


def get_data():
    global dataset
    BEGIN = 0
    END = 999
    INTERVAL = 0.001

    f = file(filename)

    print(file_len(filename))

    count = 0
    functions = []

    for i in xrange(26):
        functions += [[]]

    for line in f:
        count += 1
        split_line = line.split(' ')
        if float(split_line[0]) < BEGIN:
            continue
        if float(split_line[0]) > END:
            break
        to_float = [float(x) for x in split_line[1:]]
        for i in xrange(len(to_float)):
            functions[i] += [to_float[i]]

    dataset = functions
    print count


def walk():
    global Body

    for t in xrange(len(dataset[0])):
        print t
        move = []
        for data in dataset:
            move += [data[t]]
        joint_move(clientID, Body, move)
        time.sleep(0.07)


def walk_old():
    global angles
    global Body
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
start_position(clientID, Body)
get_data()
walk()

# print(threading.enumerate())
# t = threading.Thread(target=walk, name="t1")
# # t.daemon = True
# t.start()
# print(threading.enumerate())
