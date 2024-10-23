#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('first_node')
        self._counter=0
        self.get_logger().info('Hello From ROS2 python1')

        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello' + str(self._counter))
        self._counter+=1
    

def main(args=None):
    # init connection
    rclpy.init(args=args)

    node= MyNode()

    rclpy.spin(node)
    
    
    # end connection
    rclpy.shutdown()

if __name__=='__main__':
    main()


    