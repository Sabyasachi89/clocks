
from logging import getLogger

def clockAngle(hour,minute):
    """
    clockAngle method to calculate the angle between hour and minute hand at a particular time.

    Parameters
    ----------
    hour: int
        should be positive and less than 24.

    minute: int
        should be positive and less than 60.


    Returns
    -------
    angle : int
        angle between the hour and minute hand.
    """

    if hour<0 or minute<0 or minute>60 or hour>24:
        return 'invalid input'

    if hour == 12:
        hour = 0
    elif hour>12:
        hour = hour-12
    if minute == 60:
        minute = 0

    hourAngle = hour*30
    minuteAngle = minute*6

    angle = abs(hourAngle - minuteAngle)
    angle2 = 360-angle

    if angle2<angle:
        return angle2
    return angle

log = getLogger()
angle = clockAngle(1,50)
log.info(angle)

print(clockAngle(1,50))