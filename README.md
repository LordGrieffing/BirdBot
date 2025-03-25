I am hoping to build a robot that watches birds.

I want to put it all on a pi thats just watching a bird feeder.

Maybe it will record the types of birds it sees or something.


List of things I need to get:
- [Completed] Raspberry pi 4
- [Completed] PIR (motion) sensor
- [Completed] Camera
- Sim Card
- Sim Card HAT for Pi
- Battery pack
- Solar panels
- Wires

List of things I need to do:
- Program ROS2 node for sensor
- Figure out how to read PIR sensor data
- [Completed]Decide what data I am keeping
- Program ROS2 service for data recording
- Figure out how to SSH into it using the SIM card
- design the case in on shape
- Print the case
- Figure out how to get the power bank to charge and power at the same time
- [Completed]Annotate Bird images for object detection (BirdSnap Data set is already annoted)
- Build a YOLO object detection model
- Learn how to use Google Collab
- [Completed]Download all the images from images.txt
- Get better data stretching
- Turn yolos .pt file into .hef file


About Power:
So With the the waveshare SIM HAT, a camera, and the pi 4 I think it would be safe to assume that it needs to be able to handle
up to 5A draw of power. 5A and 5V should mean that its using 25 WATTs of power. So whatever power solution I go with Ineed to be
able to charge it with at least 25 Watts of power.

About Models:
There seems to be no mapping at all to the data in birdsnap that you can find from the parquet files to the images.txt files.
This doesn't make the data unusable since the parquet files are indeed labeled for spieces. What it means Is I guess I will need to
either train two models, one for object detection and a second for object classification. Or just download every image from the 
images.txt file.

About Training:
So my GPU (gtx 1070) is way to underpowered to train this model. A friend who has a 3070 offered to let me use their device
However I learned CUDA doesn't worrk on windows 11 which is what they use. So now I am planning on moving to google collab
to train this model.

I may need to train in python instead of CLI. Python would let me set up more data manipulation to stretch my data.
