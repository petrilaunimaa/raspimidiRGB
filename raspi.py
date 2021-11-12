#!/usr/bin/python3
import mido
import pigpio
from numpy import interp
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 300)

port = mido.open_input('f_midi')  # open USB port
red = 0.0
green = 0.0
blue = 0.0
while True:
    try:
        for msg in port.iter_pending():
            if(msg.type == 'note_on'):
                out = interp(msg.velocity, [0,127],[0,255])
                if(msg.note == 60):
                    red = out
                if(msg.note == 61):
                    green = out
                if(msg.note == 62):
                    blue = out
                if(msg.note == 65):
                    red = out
                    green = out
                    blue = out
            if(msg.type == 'note_off'):
                if(msg.note == 60):
                    red = 0
                if(msg.note == 61):
                    green = 0
                if(msg.note == 62):
                    blue = 0
                if(msg.note == 65):
                    red = 0
                    green = 0
                    blue = 0
            if msg.type == 'control_change' and msg.control == 1:
                red = red * msg.value
                green = green * msg.value
                blue = blue * msg.value
            pixels.fill((red/2, green/2, blue/2))
    except AttributeError as error:
        print("Error excepted")
    pass
