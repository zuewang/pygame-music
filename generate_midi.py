import pygame.midi
import time
pygame.midi.init()
output = pygame.midi.Output(pygame.midi.get_default_output_id())

#output.note_on(60,127)
#time.sleep(2)
#output.note_off(60,127)
#1st line: instrument, pitch
#middle: time sleep, pitch
f = open('evaop.txt')
firstline = True
pitch=-1
for line in f.readlines():
    if line == '\n':
        continue
    #print(tuple(line.split(',')))
    slp, offset= tuple(line.split(','))
    if firstline:
        output.set_instrument(int(slp))
        pitch = int(offset)
        firstline = False
    else:
        pitch += int(offset)
        output.note_on(pitch,127)
        time.sleep(float(slp))
        output.note_off(pitch,127)

f.close()

output.close()
pygame.midi.quit()

