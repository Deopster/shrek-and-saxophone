import winsound
from multiprocessing import Process
import sys
import time
import pyglet
import os
from threading import Thread
if 'data' in os.getcwd():
    print("Используйте Runner.bat")
    time.sleep(5)
    sys.exit()
def gif():
    animation = pyglet.resource.animation('gif.gif')
    sprite = pyglet.sprite.Sprite(animation)
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)
    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()
def sound():
    time.sleep(1)
    while True:
        winsound.PlaySound('./data/file.wav', winsound.SND_LOOP)
if __name__ == '__main__':
    p = Process(target=gif, args=())
    r = Process(target=sound, args=())
    r.start()
    p.start()
    while True:
        if p.is_alive() is False:
            r.kill()
            sys.exit()