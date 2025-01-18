from detect import *

detector = BallnetPose()
path = "imgs"
locations = detector.detect(path)

print(locations)