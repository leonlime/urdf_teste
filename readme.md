Packages:
---
To use this package you need to install all of this previous packs:

- https://github.com/leolima21/gazebo_sim For use gazebo world

- https://github.com/leolima21/360joy_teleop For joystick teleop


Launchers:
---
- roslaunch urdf_teste launch.launch 
  Rviz launch
 
- roslaunch urdf_teste spawn.launch Gazebo simulation

- roslaunch 360joy_teleop 360joy_teleop.launch 
  Xbox 360 controller teleop (Button "A" and left analog control)

- rosrun urdf_teste camera_face.py 
  Face detection. Topic: topic_camera_print

- rosrun urdf_teste camera_print.py
  Time counter and date. Topic: topic_camera_face








