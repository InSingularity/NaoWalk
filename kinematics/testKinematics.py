from ikinelegs import *

iterations = 15

slength = 0.10
sheight = 0.025


class RobotController():
    def __init__(self):
        self.sa = 0
        self.sb = 0
        self.sc = 0

        self.timeStep = 40
        self.bodyHeight = 0.28
        self.dHeight = 0.00
        self.bodyRoll = 0
        self.bodyTilt = 0
        self.tPhase = 0.
        self.phShift = 0.
        self.tStep = 0.5

        self.phBody = self.tPhase / self.tStep
        self.bodyHeight += self.dHeight * cos(2 * pi * self.phBody)
        self.bodyTilt = self.bodyTilt
        self.bodyRoll = 0

        self.uLeft = array([0, 0, 0.])
        self.pLeft = array([self.uLeft[0], self.uLeft[1], 0, 0, 0, self.uLeft[2]])
        self.uRight = array([0, 0, 0.])
        self.pRight = array([self.uRight[0], self.uRight[1], 0, 0, 0, self.uRight[2]])
        self.uBody = array([0., 0., 0.])
        self.pBody = [self.uBody[0], self.uBody[1], self.bodyHeight, self.bodyRoll, self.bodyTilt, self.uBody[2]]

    def get_coefficients(self):
        self.sa = -4 * sheight / slength**2
        self.sb = 4 * sheight / slength
        self.sc = 0

    def get_position(self, x):
        z = self.sa * x ** 2 + self.sb * x + self.sc
        #y = (0.0242 + 0.44 * x) / 0.075
        y = 0
        return [x, y, z]


    # Step Cycle Functions
    def run(self):
        self.get_coefficients()
        length = slength / iterations
        file_name = '../datasets/testfile.txt'
        f = open(file_name, "w+")

        for i in xrange(iterations):
            self.uLeft = self.get_position(length * i)
            self.pLeft = array([self.uLeft[0], self.uLeft[1], 0, 0, 0, self.uLeft[2]])
            pos = ikineLegs('LLeg', self.pLeft, self.pBody, ())
            for j in pos:
                f.write("%.6f " % j)
            f.write("\n")

        for i in xrange(iterations):
            self.uRight = self.get_position(length * i)
            self.pRight = array([self.uRight[0], self.uRight[1], 0, 0, 0, self.uRight[2]])
            #    pos = ikineLegs('RLeg', self.pRight, self.pBody, ())

        f.close()

controller = RobotController()

controller.run()
