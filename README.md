# Information Entropy-assisted Hierarchical Framework for Unknown Environments Exploration

## Introduction


### 1. Related Paper

### 2. Authors

### 3. Cite

## How to use

Note: This project has been tested in `Ubuntu 20.04 (ROS Noetic)`, and following dependencies are based on `ROS Noetic`. If your ROS version is not `ROS Noetic`, replace `noetic` with your ROS version name.

### 1. Basic Dependency

```bash
sudo apt-get install ros-noetic-navigation \
ros-noetic-octomap-*
```

```bash
pip3 install pyquaternion opencv-python
```
### 2. Simulation Environment

The project is run under the autonomous exploration framework provided by Robotics Institute from Carnegie Mellon University.

```bash
sudo apt update
sudo apt install libusb-dev
```

```bash
git clone https://github.com/HongbiaoZ/autonomous_exploration_development_environment.git
cd autonomous_exploration_development_environment
git checkout noetic
catkin_make
```
