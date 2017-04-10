import vrep
import time


# Moving joints
def joint_move(client_id, body, command_angles):
    vrep.simxPauseCommunication(client_id, 1)

    vrep.simxSetJointTargetPosition(client_id, body[0][0], command_angles[0], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[1][0], command_angles[1], vrep.simx_opmode_oneshot)
    # Left Leg
    vrep.simxSetJointTargetPosition(client_id, body[2][0], command_angles[8], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[3][0], command_angles[9], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[4][0], command_angles[10], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[5][0], command_angles[11], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[6][0], command_angles[12], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[7][0], command_angles[13], vrep.simx_opmode_oneshot)
    # Right Leg
    vrep.simxSetJointTargetPosition(client_id, body[8][0], command_angles[14], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[9][0], command_angles[15], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[10][0], command_angles[16], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[11][0], command_angles[17], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[12][0], command_angles[18], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[13][0], command_angles[19], vrep.simx_opmode_oneshot)
    # Left Arm
    vrep.simxSetJointTargetPosition(client_id, body[14][0], command_angles[2], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[15][0], command_angles[3], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[16][0], command_angles[4], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[17][0], command_angles[5], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[18][0], command_angles[6], vrep.simx_opmode_oneshot)
    # Right Arm
    vrep.simxSetJointTargetPosition(client_id, body[19][0], command_angles[20], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[20][0], command_angles[21], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[21][0], command_angles[22], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[22][0], command_angles[23], vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(client_id, body[23][0], command_angles[24], vrep.simx_opmode_oneshot)

    vrep.simxPauseCommunication(client_id, 0)
    time.sleep(0.02)


# Start position of joints
def start_position(client_id, body):
    vrep.simxPauseCommunication(client_id, 1)
    angle = 90 * 3.1416 / 180
    print body[14]
    errorCode = vrep.simxSetJointTargetPosition(client_id, body[14][0], angle, vrep.simx_opmode_oneshot)
    errorCode = vrep.simxSetJointTargetPosition(client_id, body[19][0], angle, vrep.simx_opmode_oneshot)

    vrep.simxPauseCommunication(client_id, 0)
    time.sleep(0.02)


def get_all_handles(client_id, Body):
    print '-> Head for NAO : ' + str(1)
    Body[0].append(vrep.simxGetObjectHandle(client_id, 'HeadYaw#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(client_id, 'HeadPitch#0', vrep.simx_opmode_oneshot_wait)[1])
    # Left Leg
    print '-> Left Leg for NAO : ' + str(1)
    Body[2].append(vrep.simxGetObjectHandle(client_id, 'LHipYawPitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(client_id, 'LHipRoll3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[4].append(vrep.simxGetObjectHandle(client_id, 'LHipPitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(client_id, 'LKneePitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(client_id, 'LAnklePitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(client_id, 'LAnkleRoll3#0', vrep.simx_opmode_oneshot_wait)[1])
    # Right Leg
    print '-> Right Leg for NAO : ' + str(1)
    Body[8].append(vrep.simxGetObjectHandle(client_id, 'RHipYawPitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(client_id, 'RHipRoll3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(client_id, 'RHipPitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(client_id, 'RKneePitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(client_id, 'RAnklePitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(client_id, 'RAnkleRoll3#0', vrep.simx_opmode_oneshot_wait)[1])
    # Left Arm
    print '-> Left Arm for NAO : ' + str(1)
    Body[14].append(vrep.simxGetObjectHandle(client_id, 'LShoulderPitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(client_id, 'LShoulderRoll3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(client_id, 'LElbowYaw3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(client_id, 'LElbowRoll3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(client_id, 'LWristYaw3#0', vrep.simx_opmode_oneshot_wait)[1])
    # Right Arm
    print '-> Right Arm for NAO : ' + str(1)
    Body[19].append(vrep.simxGetObjectHandle(client_id, 'RShoulderPitch3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(client_id, 'RShoulderRoll3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(client_id, 'RElbowYaw3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(client_id, 'RElbowRoll3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(client_id, 'RWristYaw3#0', vrep.simx_opmode_oneshot_wait)[1])
    # Left fingers
    print '-> Left Fingers for NAO : ' + str(1)
    Body[24].append(vrep.simxGetObjectHandle(client_id, 'NAO_LThumbBase#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint8#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(client_id, 'NAO_LLFingerBase#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint12#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint14#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(client_id, 'NAO_LRFinger_Base#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint11#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint13#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[25].append(Body[24][0:8])
    # Right Fingers
    print '-> Right Fingers for NAO : ' + str(1)
    Body[26].append(vrep.simxGetObjectHandle(client_id, 'NAO_RThumbBase#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint0#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(client_id, 'NAO_RLFingerBase#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint5#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint6#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(client_id, 'NAO_RRFinger_Base#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint2#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(client_id, 'Revolute_joint3#0', vrep.simx_opmode_oneshot_wait)[1])
    Body[27].append(Body[26][0:8])

