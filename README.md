# file info
This code is the sample code for the hypharos_minibot and the turtlebot. It includes:

* collect the laser scan

# How to use
To using this code in different robots, you need to input different name as different "type" arg.
## turtlebot3
    roslaunch python_sample python_sample.py type:=turtlebot3
## hypharos minibot
    roslaunch python_sample python_sample.py type:=minibot
## for simulator
    roslaunch python_sample python_sample.py type:=a
"a" can be replaced to any other words except the word used above. Because the simulator is already open the robots setting, it has no need to open twice.

# Exception
If there is something wrong, please check
* the script/main.py is executable or not
