print("")
print(" ****************************************** ")
print(" *       ROS Kinetic on Rasbpian          * ")
print(" ****************************************** ")
print("")
print(" Install editor vim and change hostname ")
print(" ______________________________________ ")
print("")
sudo apt-get install vim
sudo hostname rpi
print("")
print("fix the hosts file ")
print("__________________ ")
print("")
[[ -e /etc/hosts ]] && sudo mv /etc/hosts /etc/hosts.bak
echo "127.0.0.1  localhost" | sudo tee /etc/hosts
echo "127.0.1.1  $(</etc/hostname)" | sudo tee -a /etc/hosts
print("")
print("     Install ROS Kinetic ")
print(" ____________________________ ")
print("")
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-
latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake
sudo apt install dirmngr
sudo rosdep init
rosdep update
rosinstall_generator ros_comm --rosdistro kinetic --deps --wet-only --tar > kinetic-ros_comm-wet.rosinstall
wstool init src kinetic-ros_comm-wet.rosinstall
rosdep install -y --from-paths src --ignore-src --rosdistro kinetic -r --os=debian:stretch
sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/kinetic -j2
source /opt/ros/kinetic/setup.bash
echo 'source /opt/ros/kinetic/setup.bash' >> ~/.bashrc
print("")
print("    Install di catkin ")
print(" _______________________ ")
print("")
mkdir -p ~/catkin_ws/src
cd catkin_ws/src
catkin_init_ws
cd ~/catkin_ws/
catkin_make
source ~/catkin_ws/devel/setup.bash
echo 'source ~/catkin_workspace/devel/setup.bash' >> ~/.bashrc
export | grep ROS
print("")
print(" Enable SSH access and PI camera ")
print(" _______________________________ ")
print("")
sudo raspi-config
