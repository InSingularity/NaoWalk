import vrep
import time


# Moving joints
def joint_move(client_id, i, body, command_angles):
    vrep.simxPauseCommunication(client_id, 1)

    vrep.simxSetJointTargetPosition(client_id, body[0][i], command_angles[0], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[1][i], command_angles[1], vrep.simx_opmode_oneshot)
    # Left Leg
    vrep.simxSetJointTargetPosition(client_id, body[2][i], command_angles[8], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[3][i], command_angles[9], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[4][i], command_angles[10], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[5][i], command_angles[11], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[6][i], command_angles[12], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[7][i], command_angles[13], vrep.simx_opmode_oneshot)
    # Right Leg
    vrep.simxSetJointTargetPosition(client_id, body[8][i], command_angles[14], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[9][i], command_angles[15], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[10][i], command_angles[16], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[11][i], command_angles[17], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[12][i], command_angles[18], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[13][i], command_angles[19], vrep.simx_opmode_oneshot)
    # Left Arm
    vrep.simxSetJointTargetPosition(client_id, body[14][i], command_angles[2], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[15][i], command_angles[3], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[16][i], command_angles[4], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[17][i], command_angles[5], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[18][i], command_angles[6], vrep.simx_opmode_oneshot)
    # Right Arm
    vrep.simxSetJointTargetPosition(client_id, body[19][i], command_angles[20], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[20][i], command_angles[21], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[21][i], command_angles[22], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[22][i], command_angles[23], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[23][i], command_angles[24], vrep.simx_opmode_oneshot)

    vrep.simxPauseCommunication(client_id, 0)
    time.sleep(0.02)


# Moving joints
def start_position(client_id, i, body):
    vrep.simxPauseCommunication(client_id, 1)
    angle = 90 * 3.1416 / 180
    errorCode = vrep.simxSetJointTargetPosition(client_id, body[14][i], angle, vrep.simx_opmode_oneshot)
    errorCode = vrep.simxSetJointTargetPosition(client_id, body[19][i], angle, vrep.simx_opmode_oneshot)

    vrep.simxPauseCommunication(client_id, 0)
    time.sleep(0.02)


def get_all_handles(clientID, Body):
    print '-> Head for NAO : ' + str(1)
    Body[0].append(vrep.simxGetObjectHandle(clientID, 'HeadYaw#', vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(clientID, 'HeadPitch#', vrep.simx_opmode_oneshot_wait)[1])
    # Left Leg
    print '-> Left Leg for NAO : ' + str(1)
    Body[2].append(vrep.simxGetObjectHandle(clientID, 'LHipYawPitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(clientID, 'LHipRoll3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[4].append(vrep.simxGetObjectHandle(clientID, 'LHipPitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(clientID, 'LKneePitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(clientID, 'LAnklePitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(clientID, 'LAnkleRoll3#', vrep.simx_opmode_oneshot_wait)[1])
    # Right Leg
    print '-> Right Leg for NAO : ' + str(1)
    Body[8].append(vrep.simxGetObjectHandle(clientID, 'RHipYawPitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(clientID, 'RHipRoll3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(clientID, 'RHipPitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(clientID, 'RKneePitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(clientID, 'RAnklePitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(clientID, 'RAnkleRoll3#', vrep.simx_opmode_oneshot_wait)[1])
    # Left Arm
    print '-> Left Arm for NAO : ' + str(1)
    Body[14].append(vrep.simxGetObjectHandle(clientID, 'LShoulderPitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(clientID, 'LShoulderRoll3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(clientID, 'LElbowYaw3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(clientID, 'LElbowRoll3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(clientID, 'LWristYaw3#', vrep.simx_opmode_oneshot_wait)[1])
    # Right Arm
    print '-> Right Arm for NAO : ' + str(1)
    Body[19].append(vrep.simxGetObjectHandle(clientID, 'RShoulderPitch3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(clientID, 'RShoulderRoll3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(clientID, 'RElbowYaw3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(clientID, 'RElbowRoll3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(clientID, 'RWristYaw3#', vrep.simx_opmode_oneshot_wait)[1])
    # Left fingers
    print '-> Left Fingers for NAO : ' + str(1)
    Body[24].append(vrep.simxGetObjectHandle(clientID, 'NAO_LThumbBase#', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint8#', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID, 'NAO_LLFingerBase#', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint12#', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint14#', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID, 'NAO_LRFinger_Base#', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint11#', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint13#', vrep.simx_opmode_oneshot_wait)[1])
    Body[25].append(Body[24][0:8])
    # Right Fingers
    print '-> Right Fingers for NAO : ' + str(1)
    Body[26].append(vrep.simxGetObjectHandle(clientID, 'NAO_RThumbBase#', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint0#', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID, 'NAO_RLFingerBase#', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint5#', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint6#', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID, 'NAO_RRFinger_Base#', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint2#', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID, 'Revolute_joint3#', vrep.simx_opmode_oneshot_wait)[1])
    Body[27].append(Body[26][0:8])
