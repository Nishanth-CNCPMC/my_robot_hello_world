import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotSpeaker(Node):

    def __init__(self):
        super().__init__('robot_speaker_node')
        self.publisher_ = self.create_publisher(String, 'robot_chatter', 10)
        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.get_logger().info('RobotSpeaker node started!')

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, world! ({self.i})'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    robot_speaker = RobotSpeaker()
    rclpy.spin(robot_speaker)
    robot_speaker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
