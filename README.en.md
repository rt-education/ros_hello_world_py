[English](README.en.md) | [Japanese](README.md)

# ROS tutorial
This tutorial is provided from the ROS wiki [page](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) which is provided by [Open Source Robotics Foundation](http://www.osrfoundation.org/) under the [CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/) license and editted by Shuhei Kozasa\<kozasa@rt-net.jp\>

## Install
Execute the commands listed below to install this repository.
```shell
$ cd ~/<ROS_WORKSPACE>/src
$ git clone https://github.com/rt-education/ros_hello_world_py
$ catkin build
$ source ~/.bashrc
```

## Usage
```shell
# Terminal 1
$ roscore
# Terminal 2
$ rosrun hello_world_py talker.py
# Terminal 3
$ rosrun hello_world_py listener.py
``` 

## License
(C) 2020 RT Corporation \<edu@rt-net.jp\>
If a file has a license written within it, it is released under that license. Otherwise, each file is licensed under the Apache-2.0 license.

The full text of the license is written in the [LICENSE](LICENSE) file or [here](http://www.apache.org/licenses/LICENSE-2.0).

*This software is released __AS IS__ as an open source software.  
This software is provided during a seminar, and will only be supported during that seminar.  
For detailed about the seminar, please refer to [here](https://rt-net.jp/service/for-companies/).