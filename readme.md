Packages:
---
To use this package you need to install two previous packs:

- https://github.com/leolima21/gazebo_sim **For gazebo world**

- https://github.com/leolima21/360joy_teleop **For joystick teleop**

You can use a face image instead of an aruco picture in order to create a face model in some gazebo world:
- https://github.com/mikaelarguedas/gazebo_models


Launchers:
---
- **Rviz launch:** roslaunch urdf_teste launch.launch 
  
- **Gazebo simulation:** roslaunch urdf_teste spawn.launch 

- **Xbox 360 controller teleop (Button "A" and left analog control):** roslaunch 360joy_teleop 360joy_teleop.launch 

- **Face detection. Topic: topic_camera_print:** rosrun urdf_teste camera_face.py 
  
- **Time counter and date. Topic: topic_camera_face:** rosrun urdf_teste camera_print.py
  








