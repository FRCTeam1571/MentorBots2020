#!/usr/bin/env python3
"""
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    a single joystick
"""

import wpilib
from wpilib.drive import DifferentialDrive
import ptvsd


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot initialization function"""

        self.frontLeft = wpilib.Spark(1)
        self.rearLeft = wpilib.Spark(2)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

        self.frontRight = wpilib.Spark(3)
        self.rearRight = wpilib.Spark(4)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

        self.drive = DifferentialDrive(self.left, self.right)
        # object that handles basic drive operations
        #self.myRobot = wpilib.Drive.DifferentialDrive(0, 1)
        #self.myRobot.setExpiration(0.1)

        # joystick #0
        self.stick = wpilib.Joystick(0)

    def disabledInit(self):
        self.drive.setSafetyEnabled(False)
    def disabledPeriodic(self):
        self.drive.setSafetyEnabled(False)
    def robotPeriodic(self):
        self.drive.setSafetyEnabled(False)

    def testInit(self):
        print("Test Init")
    def testPeriodic(self):
        if(self.stick.getRawButtonPressed(1) == True):
            print("Test Button 1 Pressed.")

    def autonomousInit(self):
        self.drive.setSafetyEnabled(False)

    def autonomousPeriodic(self):
        """Called when autonomous mode is enabled"""

        while self.isAutonomous() and self.isEnabled():
            #wpilib.Timer.delay(0.01)
            self.drive.arcadeDrive(0.20, 0.1)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        
        self.drive.setSafetyEnabled(False)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        
        # timer = wpilib.Timer()
        # timer.start()

        while self.isOperatorControl() and self.isEnabled():
            # Move a motor with a Joystick
            #wpilib.Timer.delay(0.02)
            self.drive.arcadeDrive(self.stick.getRawButton(1), True)


# if __name__ == "__main__":
#     wpilib.run(MyRobot)

if __name__ == "__main__":
    # Allow other computers to attach to ptvsd at this IP address and port.
    #ptvsd.enable_attach(address=('10.15.71.2', 22), redirect_output=True)
    # Pause the program until a remote debugger is attached
    #ptvsd.wait_for_attach()

    wpilib.run(MyRobot)





#!/usr/bin/env python3

# """
#     The SampleRobot class is the base of a robot application that will
#     automatically call your Autonomous and OperatorControl methods at
#     the right time as controlled by the switches on the driver station
#     or the field controls.
    
#     WARNING: While it may look like a good choice to use for your code
#     if you're inexperienced, don't. Unless you know what you are doing,
#     complex code will be much more difficult under this system. Use
#     IterativeRobot or Command-Based instead if you're new.
# """


# import wpilib
# from wpilib.drive import DifferentialDrive


# class MyRobot(wpilib.SampleRobot):
#     """Main robot class"""

#     def robotInit(self):
#         """Robot-wide initialization code should go here"""

#         self.lstick = wpilib.Joystick(0)
#         self.motor = wpilib.Jaguar(0)

#     def disabled(self):
#         """Called when the robot is disabled"""
#         while self.isDisabled():
#             wpilib.Timer.delay(0.01)

#     def autonomous(self):
#         """Called when autonomous mode is enabled"""

#         while self.isAutonomous() and self.isEnabled():
#             wpilib.Timer.delay(0.01)
#             self.motor.set(0.20)

#     def operatorControl(self):
#         """Called when operation control mode is enabled"""

#         timer = wpilib.Timer()
#         timer.start()

#         while self.isOperatorControl() and self.isEnabled():

#             # Move a motor with a Joystick
#             self.motor.set(self.lstick.getY())

#             # if timer.hasPeriodPassed(1.0):
#             #     print("Analog 8: %s" % self.ds.getBatteryVoltage())

#             wpilib.Timer.delay(0.02)


# if __name__ == "__main__":
#     wpilib.run(MyRobot)

#     #wpilib.run(MyRobot, a="test")
