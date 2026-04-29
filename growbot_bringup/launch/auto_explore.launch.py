from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    turtlebot3_gazebo_dir = get_package_share_directory('turtlebot3_gazebo')
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(turtlebot3_gazebo_dir, 'launch', 'turtlebot3_world.launch.py')
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(slam_toolbox_dir, 'launch', 'online_async_launch.py')
            ),
            launch_arguments={'use_sim_time': 'true'}.items()
        ),

        Node(
            package='growbot_bringup',
            executable='random_explorer',
            output='screen'
        ),
    ])
