# 02 — First Xacro / URDF Model

This document records the first ROS 2 robot-description test created for the ECNG 3020 robotic prosthesis project.

The purpose of this stage was not to create the final prosthetic geometry. It was to verify that the ROS 2 workspace could:

- load a Xacro / URDF robot description;
- represent a parent-child link structure;
- define a revolute joint;
- publish the robot state;
- visualize the model in RViz;
- move the first test finger joint using the joint-state publisher GUI.

## 1. Create the First Xacro File

Open the robot-description file:

```bash
cd ~/prosthetic_ws/src/prosthetic_description
nano urdf/prosthetic_hand.urdf.xacro
```

The first model used simple box geometry for a palm and one index-finger link:

```xml
<?xml version="1.0"?>

<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="prosthetic_hand">

  <link name="palm_link">
    <visual>
      <geometry>
        <box size="0.08 0.02 0.10"/>
      </geometry>
    </visual>
  </link>

  <link name="index_proximal_link">
    <visual>
      <geometry>
        <box size="0.018 0.018 0.05"/>
      </geometry>
    </visual>
  </link>

  <joint name="index_mcp_joint" type="revolute">
    <parent link="palm_link"/>
    <child link="index_proximal_link"/>

    <origin xyz="0.025 0 0.075" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>

    <limit lower="0"
           upper="1.57"
           effort="2"
           velocity="2"/>
  </joint>

</robot>
```

Save in Nano using:

```text
Ctrl + O
Enter
Ctrl + X
```

## 2. Validate the Xacro File

Move to the workspace root:

```bash
cd ~/prosthetic_ws
```

Convert the Xacro file to URDF:

```bash
xacro src/prosthetic_description/urdf/prosthetic_hand.urdf.xacro > /tmp/prosthetic_hand.urdf
```

An XML parsing error was encountered during the first attempt. The file was reopened, the XML formatting was corrected, and the command was rerun successfully.

The corrected model was then checked with:

```bash
check_urdf /tmp/prosthetic_hand.urdf
```

If the URDF checking tool is not available:

```bash
sudo apt install liburdfdom-tools -y
```

The purpose of this test was to verify that ROS could successfully parse the robot link and joint structure before adding real CAD geometry.

## 3. Create the RViz Launch File

Create:

```bash
nano ~/prosthetic_ws/src/prosthetic_description/launch/display.launch.py
```

The launch file used was:

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_path = get_package_share_directory('prosthetic_description')

    xacro_file = os.path.join(
        pkg_path,
        'urdf',
        'prosthetic_hand.urdf.xacro'
    )

    robot_description = ParameterValue(
        Command(['xacro ', xacro_file]),
        value_type=str
    )

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
```

This launches three main components:

- `robot_state_publisher` to publish the robot transforms;
- `joint_state_publisher_gui` to provide a slider for the revolute joint;
- `rviz2` to visualize the robot model.

## 4. Update CMakeLists.txt

Open:

```bash
nano ~/prosthetic_ws/src/prosthetic_description/CMakeLists.txt
```

Add the following block above `ament_package()`:

```cmake
install(
  DIRECTORY
    urdf
    launch
    meshes
    rviz
  DESTINATION share/${PROJECT_NAME}
)
```

This ensures that the URDF, launch, mesh, and RViz resources are copied into the installed ROS package.

## 5. Rebuild the Workspace

```bash
cd ~/prosthetic_ws
colcon build
source install/setup.bash
```

Launch the model:

```bash
ros2 launch prosthetic_description display.launch.py
```

## 6. RViz Configuration

RViz initially opened without the model being visible.

The following settings were used:

```text
Fixed Frame = palm_link
```

A `RobotModel` display was added if not already present.

The robot-description topic was set to:

```text
/robot_description
```

The initial RViz camera distance was much larger than the approximately 0.1 m test model. Reducing the view distance / zooming in allowed the model to become visible.

## 7. Result of the First Model

The first model appeared as simple rectangular blocks rather than a realistic prosthetic hand. This was intentional.

The test successfully demonstrated the basic pipeline:

```text
Xacro / URDF
      ↓
robot_state_publisher
      ↓
joint states
      ↓
RViz RobotModel
```

It also confirmed that the `index_mcp_joint` could act as a revolute joint between the palm and first index-finger link.

This placeholder model is not intended to represent the final mechanical design. The next development stage is to replace the box geometry with CAD meshes from the OpenBionics prosthetic hand repository and evaluate their orientation, scale, segmentation, and joint compatibility.
