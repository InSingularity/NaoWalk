from utils.vrep_scripts import *
from utils.service_scripts import *

#filename = 'datasets/testfile.txt'
#filename = 'datasets/testfile_old_one_step.txt'
filename = 'datasets/training_custom.txt'
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
    END = 30

    f = file(filename)

    count = 0
    functions = []

    for i in xrange(12):
        functions += [[]]

    for line in f:
        split_line = line.split(' ')
        if float(split_line[0]) < BEGIN:
            continue
        if float(split_line[0]) > END:
            break

        print split_line
        to_float = [float(x) for x in split_line[0:12]]
        for i in xrange(len(to_float)):
            functions[i] += [to_float[i]]
        count += 1

    dataset = functions
    print dataset

def walk():
    global Body
    #len(dataset[0])

    for t in xrange(600):
        move = []
        for data in dataset:
            move += [data[t]]
        joint_move_short(clientID, Body, move)


reset_simulation()
get_all_handles(clientID, Body)
start_position(clientID, Body)
get_data()
walk()
vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)

