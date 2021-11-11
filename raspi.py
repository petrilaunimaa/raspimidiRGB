#!/usr/bin/python3
import mido
import pigpio
from numpy import interp
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 300)

port = mido.open_input('f_midi')  # open USB port
while True:
    try:  # This filters out all non-note data
        for msg in port.iter_pending():  # if there is a message pending
            if msg.type == 'pitchwheel':  # of type pitchwheel
                print("PITCH: ", msg.pitch)
                out = interp(msg.pitch, [-8192, 8192], [0, 255])
                pixels.fill((0, out, 0))
                if msg.type == 'control_change' and msg.control == 1:
                    print("MOD: ", msg.value)
    except AttributeError as error:
        print("Error excepted")
    pass
