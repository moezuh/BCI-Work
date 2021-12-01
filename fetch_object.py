import stretch_body.robot
import time, math

# positions in meters and radians
translate_fwd = 2.1
translate_bwd = 2.3
translate_to_init_pos = 0.2
lift_up = 0.775
wrist_fwd = 0
wrist_bwd = 3.395
gripper_open = 60
gripper_close = -60
arm_fwd = 0.17
arm_bwd = 0
rotate_error = 0.027

robot=stretch_body.robot.Robot()
robot.startup()  # opens serial ports and starts threads
robot.stow()


# Make robot sleep for 10 seconds to remove hdmi and charger cables
time.sleep(10)

print('Initial position of the robot')
status = robot.get_status()
print('x:', round(status['base']['x']), 'y:', round(status['base']['y']), round(status['base']['theta'] * 180/math.pi))

# Move the robot linearly
robot.base.translate_by(translate_fwd)
robot.push_command()
time.sleep(20)

# Lift move upwards
robot.lift.move_to(lift_up)
robot.push_command()
time.sleep(10)

# Set wrist to FWD pos
robot.end_of_arm.move_to('wrist_yaw', wrist_fwd)
time.sleep(7)

# Open the gripper
robot.end_of_arm.move_to('stretch_gripper', gripper_open)
time.sleep(7)

#Move arm forward
robot.arm.move_to(arm_fwd)
robot.push_command()
time.sleep(7)

# Close the gripper
robot.end_of_arm.move_by('stretch_gripper', gripper_close)
time.sleep(10)

# Move lift upwards
robot.lift.move_by(0.028)
robot.push_command()
time.sleep(7)

# Move the arm bwd
robot.arm.move_to(arm_bwd)
robot.push_command()
time.sleep(7)

# Set wrist to BWD pos
robot.end_of_arm.move_to('wrist_yaw', wrist_bwd)
time.sleep(10)

#rotate the robot 180
robot.base.rotate_by(math.pi + rotate_error)
robot.push_command()
time.sleep(13)

status = robot.get_status()
print('x:', round(status['base']['x']), 'y:', round(status['base']['y']), round(status['base']['theta'] * 180/math.pi))

# Move the robot back linearly
robot.base.translate_by(translate_bwd)
robot.push_command()
time.sleep(27)

# Set wrist to FWD pos
robot.end_of_arm.move_to('wrist_yaw', wrist_fwd)
time.sleep(10)

# Move arm forward
robot.arm.move_to(arm_fwd + 0.03)
robot.push_command()
time.sleep(7)

# Open the gripper
robot.end_of_arm.move_to('stretch_gripper', gripper_open)
time.sleep(10)

#Move arm Bwd
robot.arm.move_to(arm_bwd)
robot.push_command()
time.sleep(7)

# Close the gripper
robot.end_of_arm.move_to('stretch_gripper', gripper_close)
time.sleep(10)

# Set wrist to BWD pos
#robot.end_of_arm.move_to('wrist_yaw', wrist_bwd)
#time.sleep(10)

# Rotate the robot 180
robot.end_of_arm.move_to('wrist_yaw', wrist_bwd)
robot.base.rotate_by(math.pi + rotate_error) # Adjust error
robot.push_command()
time.sleep(10)

# Move robot to start position
robot.base.translate_by(translate_to_init_pos)
robot.push_command()
time.sleep(5)

status = robot.get_status()
print('x:', round(status['base']['x']), 'y:', round(status['base']['y']), round(status['base']['theta'] * 180/math.pi))

robot.stop()  # closes serial ports and closes threads


