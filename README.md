# DSHOT on Raspberry Pi

This is a *very* quick and dirty python module for sending DSHOT frames to ESCs via a Raspberry Pi 3B's GPIO pins.

The signal timings are tuned (and could probably be fine tuned further) to my Raspberry Pi 3B and will most likely not work on other models due to the use a of busy loop (and so it depends on the processor frequency).

See `run_motors.py` for an example of how to use it.

## Installation
`python setup.py install`

*Usage note: you will need to run your python script as root as the C code directly accesses /dev/mem.*


