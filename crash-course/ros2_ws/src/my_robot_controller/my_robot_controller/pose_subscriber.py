#!/usr/bin/env python3
from typing import Any
import rclpy 
from rclpy.node import Node
from turtlesim.msg import Pose
class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        self.get_logger().info('Pose Subscriber has been started')

    def pose_callback(self,msg:Pose):
        self.get_logger().info('Received Pose: x=%f, y=%f, theta=%f, linear_velocity=%f, angular_velocity=%f' % (msg.x,msg.y,msg.theta,msg.linear_velocity,msg.angular_velocity))

def main(args=None):
    # init connection
    rclpy.init(args=args)

    node= PoseSubscriberNode()

    rclpy.spin(node)
    
    
    # end connection
    rclpy.shutdown()

if __name__=='__main__':

    main()