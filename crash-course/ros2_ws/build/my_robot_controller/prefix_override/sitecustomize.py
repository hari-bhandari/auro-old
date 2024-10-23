import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hari/projects/auro/crash-course/ros2_ws/install/my_robot_controller'
