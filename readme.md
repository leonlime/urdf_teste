Packages:
---
To use this package you need to install two previous packs:

- https://github.com/leolima21/gazebo_sim **For use gazebo world**

- https://github.com/leolima21/360joy_teleop **For joystick teleop**


To create a face model in gazebo world you can use this repository and use a face image instead a aruco pic: 
---
- https://github.com/mikaelarguedas/gazebo_models


Launchers:
---
- **Rviz launch:** roslaunch urdf_teste launch.launch 
  
- **Gazebo simulation:** roslaunch urdf_teste spawn.launch 

- **Xbox 360 controller teleop (Button "A" and left analog control):** roslaunch 360joy_teleop 360joy_teleop.launch 

- **Face detection. Topic: topic_camera_print:** rosrun urdf_teste camera_face.py 
  
- **Time counter and date. Topic: topic_camera_face:** rosrun urdf_teste camera_print.py
  








