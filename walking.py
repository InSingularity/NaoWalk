from utils.vrep_scripts import *
from utils.service_scripts import *

#filename = 'datasets/training_data_my.txt'
filename = 'datasets/training_data_my_test.txt'
#filename = 'datasets/head_training_data.txt'
#filename = 'datasets/training_data_only_first_moves.txt'
#filename = 'datasets/training_data2.txt'
#filename = 'datasets/training_data_1_2999_sample_0.1s.txt'
#filename = 'datasets/training_data_1_9999_sample_0.1s.txt'
#filename = 'datasets/verification_training_data.txt'
#filename = 'datasets/start_moviment_my.txt'
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
    END = 3000

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
    #len(dataset[0])
    for t in xrange(1):
        print t
        move = []
        for data in dataset:
            move += [data[t]]
        joint_move(clientID, Body, move)
        time.sleep(0.07)


reset_simulation()
get_all_handles(clientID, Body)
start_position(clientID, Body)
get_data()
walk()
