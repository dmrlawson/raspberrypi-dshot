import dshot

"""
This sends a 0 throttle (value 48) to pins 5, 7, 19 and 20 for a little
while, then 51 (value 99) which should start the motors turning, then 151
(199) which should make them turn a little faster.

These pins worked for me with the Sense HAT attached.
"""

for _ in range(10000):
    dshot.send(48, 5)
    dshot.send(48, 7)
    dshot.send(48, 19)
    dshot.send(48, 20)

for _ in range(20000):
    dshot.send(99, 5)
    dshot.send(99, 7)
    dshot.send(99, 19)
    dshot.send(99, 20)

for _ in range(10000):
    dshot.send(199, 5)
    dshot.send(199, 7)
    dshot.send(199, 19)
    dshot.send(199, 20)

