# Introduction
This project was moved to [MRL organization account](https://github.com/NcuMathRoboticsLab/hypharos_minibot_turtlebot_python_sample) now.

This code is the sample code for the hypharos_minibot and the turtlebot. It includes:

* collect the laser scan

# How to use

## Installation

```shell
# Run following command on your robot but don't copy $ mark.
$ cd ~/catkin_ws/src
$ git clone https://github.com/MathRoboticsLab/hypharos_minibot_turtlebot_python_sample.git python_sample
$ cd ..
$ catkin_make
```

## Run code
To using this code in different robots, you need to input different name as different "type" arg.

* For turtlebot3, you should run `roslaunch python_sample python_sample.launch type:=turtlebot3` on your robot.
* For minibot, you should run `roslaunch python_sample python_sample.launch type:=minibot` on your robot.
* For other simulator, you should run `roslaunch python_sample python_sample.launch type:=a` on your computer, `a` can be replaced to any other words except the word used above. Because the simulator is already open the robots setting, it has no need to open twice.

## Get errors
If there is something wrong, please check the `script/main.py` is executable or not.
