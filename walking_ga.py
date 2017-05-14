import math

from utils.vrep_scripts import *
#from ga.evo import *

filename = 'datasets/ga.txt'
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
#226-476
def walk():
    global Body
    #len(dataset[0])

    file_name = 'log/com_ga_unlim.csv'
    f = open(file_name, "w+")
    t = 1

    while t < 600:
            move = []
            for data in dataset:
                move += [data[t]]
            joint_move_short(clientID, Body, move)
            # get the motor joint handle
            e, lleg = vrep.simxGetObjectHandle(clientID, 'LHipYawPitch3#0', vrep.simx_opmode_oneshot_wait)
            e, lJointPosition = vrep.simxGetObjectPosition(clientID, lleg, -1, vrep.simx_opmode_streaming)
            e, rleg = vrep.simxGetObjectHandle(clientID, 'RHipYawPitch3#0', vrep.simx_opmode_oneshot_wait)
            e, rJointPosition = vrep.simxGetObjectPosition(clientID, rleg, -1, vrep.simx_opmode_streaming)
            #print lJointPosition
            #print rJointPosition

            f.write("%.6f," % ((lJointPosition[0]+rJointPosition[0])/2))
            f.write("%.6f," % ((lJointPosition[1]+rJointPosition[1])/2))
            f.write("%.6f" % ((lJointPosition[2]+rJointPosition[2])/2))
            f.write("\n")
            t = t + 1
            if t == 477:
                t = 226
    f.close()

reset_simulation()
get_all_handles(clientID, Body)
start_position(clientID, Body)
get_data()
walk()
vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)

