from gpiozero import MotionSensor

pir = MotionSensor(23)

while True:
    print("Waiting for Motion...")
    pir.wait_for_active()

    print("Moition detected")
    pir.wait_for_inactive()

    print("Moition no longer detected")