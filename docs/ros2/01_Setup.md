# 01 — ROS 2 and Gazebo Setup

This document records the development environment setup used for the ECNG 3020 project:

**Design, Simulation, and Development of a Deep-Learning-Assisted Robotic Prosthesis with Haptic Tactile Feedback**

The setup was completed on a Windows HP Pavilion x360 using WSL2 with Ubuntu 24.04 LTS.

## 1. Install WSL

Open **PowerShell as Administrator**:

```powershell
wsl --install
```

If WSL2 reports that required virtualization components are unavailable, enable the required Windows features:

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl.exe --update
```

Restart Windows after enabling these features.

## 2. Install Ubuntu 24.04 LTS

The default Ubuntu installation initially installed a newer Ubuntu release. Ubuntu 24.04 LTS was then installed specifically for the ROS 2 Jazzy / Gazebo Harmonic environment:

```powershell
wsl --install -d Ubuntu-24.04
```

To manually launch the correct distribution:

```powershell
wsl -d Ubuntu-24.04
```

A UNIX username and password were created during first launch.

## 3. Move to the Linux Home Directory

When Ubuntu was first launched from PowerShell, the terminal opened inside the Windows System32 directory. Move to the Linux home directory with:

```bash
cd ~
```

Check the current location:

```bash
pwd
```

Expected result:

```text
/home/ansarah_mohammed
```

Check the Ubuntu version:

```bash
lsb_release -a
```

The selected environment was Ubuntu 24.04 LTS (Noble).

## 4. Update Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

## 5. Basic Development Tools

Check Python:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

Install repository utilities:

```bash
sudo apt install software-properties-common curl -y
sudo add-apt-repository universe
sudo apt update
```

## 6. Configure Locale for ROS 2

```bash
sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

## 7. Add the ROS 2 Repository

Install required tools:

```bash
sudo apt install curl gnupg lsb-release -y
```

Add the ROS signing key:

```bash
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
-o /usr/share/keyrings/ros-archive-keyring.gpg
```

Add the ROS 2 package repository:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

Update package information:

```bash
sudo apt update
```

## 8. Install ROS 2 Jazzy Desktop

```bash
sudo apt install ros-jazzy-desktop -y
```

Activate ROS 2 in the current terminal:

```bash
source /opt/ros/jazzy/setup.bash
```

Confirm that ROS 2 is available:

```bash
ros2 --help
```

## 9. Test ROS 2 Communication

Run the C++ talker:

```bash
ros2 run demo_nodes_cpp talker
```

In a second Ubuntu 24.04 terminal:

```bash
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_py listener
```

Successful operation was confirmed when the listener received the talker's `Hello World` messages.

Stop a running ROS node using:

```text
Ctrl + C
```

## 10. Automatically Source ROS 2

Add ROS 2 to the shell startup file:

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```

Reload the shell configuration:

```bash
source ~/.bashrc
```

## 11. Install Gazebo / ROS Integration

Install the ROS-Gazebo integration package:

```bash
sudo apt install ros-jazzy-ros-gz -y
```

Test Gazebo:

```bash
gz sim
```

Gazebo opened successfully through WSL.

## 12. Create the ROS 2 Workspace

Create the project workspace:

```bash
mkdir -p ~/prosthetic_ws/src
cd ~/prosthetic_ws
```

Check the workspace path:

```bash
pwd
```

Expected result:

```text
/home/ansarah_mohammed/prosthetic_ws
```

## 13. Create the Prosthetic Description Package

```bash
cd ~/prosthetic_ws/src
ros2 pkg create --build-type ament_cmake prosthetic_description
```

This package is intended to contain the prosthetic robot description, meshes, launch files, and RViz configuration.

## 14. Install Colcon

The first attempt to run `colcon build` showed that Colcon was not yet installed.

Install the Colcon extensions:

```bash
sudo apt install python3-colcon-common-extensions -y
```

Build the workspace:

```bash
cd ~/prosthetic_ws
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

Verify that ROS can find the package:

```bash
ros2 pkg list | grep prosthetic_description
```

## 15. Create the Package Folder Structure

```bash
cd ~/prosthetic_ws/src/prosthetic_description
mkdir -p urdf meshes launch rviz
```

The working structure is:

```text
prosthetic_description/
├── launch/
├── meshes/
├── rviz/
├── urdf/
├── CMakeLists.txt
└── package.xml
```

## 16. Install Robot Description Tools

```bash
sudo apt install ros-jazzy-xacro ros-jazzy-joint-state-publisher-gui -y
```

## Setup Notes

- A WSL `systemd-binfmt.service` warning was observed and the system reported a degraded systemd state. The Ubuntu environment remained usable for the ROS 2 workflow.
- Ubuntu 24.04 should be used for this project environment rather than accidentally launching the separate Ubuntu 26.04 distribution.
- The active ROS workspace is stored in the Linux filesystem at `~/prosthetic_ws`.
