I am hoping to build a robot that watches birds.

I want to put it all on a pi thats just watching a bird feeder.

Maybe it will record the types of birds it sees or something.


List of things I need to get:
- Raspberry pi 4
- PIR (motion) sensor
- Camera
- Sim Card
- Sim Card HAT for Pi
- Battery pack
- Solar panels

List of things I need to do:
- Program ROS2 node for sensor
- Figure out how to read PIR sensor data
- Decide what data I am keeping
- Program ROS2 service for data recording
- Figure out how to SSH into it using the SIM card
- design the case in on shape
- Print the case
- Figure out how to get the power bank to charge and power at the same time


About Power:
So With the the waveshare SIM HAT, a camera, and the pi 4 I think it would be safe to assume that it needs to be able to handle
up to 5A draw of power. 5A and 5V should mean that its using 25 WATTs of power. So whatever power solution I go with Ineed to be
able to charge it with at least 25 Watts of power.

