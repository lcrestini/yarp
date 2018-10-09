#! /usr/bin/env python
print("")
print(" ********************************************* ")
print(" *       ROS Kinetic on Ubuntu Mate          * ")
print(" ********************************************* ")
print("")
print(" Install editor vim and change hostname ")
print(" ______________________________________ ")
print("")

print("Setup your sources.list ...........")
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

print("Set up your keys ..........")
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

print("Installation ...........")
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full

print("Initialize rosdep ...........")
sudo rosdep init
rosdep update

print("Environment ..........")
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
source /opt/ros/kinetic/setup.bash

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make

source devel/setup.bash
print("Done !")

sudo raspi-config
