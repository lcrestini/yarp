#!/bin/bash
echo -e""
echo -e" ********************************************* "
echo -e" *       ROS Kinetic on Ubuntu Mate          * "
echo -e" ********************************************* "
echo -e""
echo -e" Install editor vim and change hostname "
echo -e" ______________________________________ "
echo -e""
echo -e"Setup your sources.list ..........."
echo -e""
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
echo -e""
echo -e"Set up your keys .........."
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
echo -e""
echo -e"Installation ..........."
echo -e""
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
echo -e""
echo -e"Initialize rosdep ..........."
echo -e""
sudo rosdep init
rosdep update
echo -e""
echo -e"Environment .........."
echo -e""
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
source /opt/ros/kinetic/setup.bash

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make

source devel/setup.bash
echo -e"Done !"
