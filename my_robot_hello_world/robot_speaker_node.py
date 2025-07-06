import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotSpeaker(Node):

    def __init__(self):
        super().__init__('robot_speaker_node')
        # Declare a parameter for speaking rate
        self.declare_parameter('speaking_rate_sec', 2.0) # Default to 2.0 seconds

        self.publisher_ = self.create_publisher(String, 'robot_chatter', 10)

        # Get the parameter value
        timer_period = self.get_parameter('speaking_rate_sec').get_parameter_value().double_value
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.get_logger().info('RobotSpeaker node initialized and speaking at %f second intervals.' % timer_period)

    def timer_callback(self):
        # ... (rest of your timer_callback remains the same)
        msg = String()
        if self.i % 5 == 0: # Say goodbye every 5th message
            msg.data = f'Goodbye, world! ({self.i})'
        else:
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
