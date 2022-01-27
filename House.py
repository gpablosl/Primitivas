from OpenGL.GL import *
from glew_wish import *
from math import *
import math
import glfw

def grass():
    glBegin(GL_QUADS)
    glColor3f(.2,.45,0)
    glVertex3f(-1.0,-1.0,0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(1.0,-0.5,0.0)
    glVertex3f(-1.0,-0.5,0)
    glEnd()

def house():
    glBegin(GL_QUADS)
    glColor3f(.95,.90,0.75)
    glVertex3f(-0.5,0.4,0)
    glVertex3f(0.5,0.4,0)
    glVertex3f(0.5,-0.5,0.0)
    glVertex3f(-0.5,-0.5,0)
    glEnd()

def door():
    glBegin(GL_QUADS)
    glColor3f(.39,.26,0.12)
    glVertex3f(-0.15,-0.1,0)
    glVertex3f(0.15,-0.1,0)
    glVertex3f(0.15,-0.5,0.0)
    glVertex3f(-0.15,-0.5,0)
    glEnd()

    posx, posy,sides,radius = 0.1,-0.3,8,0.01
    glBegin(GL_POLYGON)
    glColor3f(0,0,0)
    for i in range(sides):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def clowds():
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(1,359,5):
        glVertex3f(0.09*math.cos(angulo * math.pi / 180) + 0.61, 0.05*math.sin(angulo * math.pi / 180) + 0.7, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(1,359,5):
        glVertex3f(0.2*math.cos(angulo * math.pi / 180) + 0.6, 0.11*math.sin(angulo * math.pi / 180) + 0.6, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(1,359,5):
        glVertex3f(0.09*math.cos(angulo * math.pi / 180) - 0.42, 0.05*math.sin(angulo * math.pi / 180) + 0.8, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(1,359,5):
        glVertex3f(0.22*math.cos(angulo * math.pi / 180) - 0.45, 0.09*math.sin(angulo * math.pi / 180) + 0.9, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(1,359,5):
        glVertex3f(0.09*math.cos(angulo * math.pi / 180) + 0.2, 0.05*math.sin(angulo * math.pi / 180) + 0.84, 0)
    glEnd()
    glBegin(GL_POLYGON)
    for angulo in range(1,359,5):
        glVertex3f(0.15*math.cos(angulo * math.pi / 180) + 0.2, 0.1*math.sin(angulo * math.pi / 180) + 0.75, 0)
    glEnd()
   

def windows():
    glBegin(GL_QUADS)
    glColor3f(0.88,0.92,0.89)
    glVertex3f(-0.4,0.1,0)
    glVertex3f(-0.1,0.1,0)
    glVertex3f(-0.1,0.3,0.0)
    glVertex3f(-0.4,0.3,0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex3f(-0.4,0.2,0)
    glVertex3f(-0.1,0.2,0)
    glVertex3f(-0.25,0.1,0)
    glVertex3f(-0.25,0.3,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.88,0.92,0.89)
    glVertex3f(0.4,0.1,0)
    glVertex3f(0.1,0.1,0)
    glVertex3f(0.1,0.3,0.0)
    glVertex3f(0.4,0.3,0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex3f(0.4,0.2,0)
    glVertex3f(0.1,0.2,0)
    glVertex3f(0.25,0.1,0)
    glVertex3f(0.25,0.3,0)
    glEnd()

def roof():
    glBegin(GL_TRIANGLES)
    glColor3f(.16,.16,0.20)
    glVertex3f(-0.55,0.4,0)
    glVertex3f(0.55,0.4,0)
    glVertex3f(0.0,0.6,0.0)
    glEnd()

def sun():
    glBegin(GL_LINES)
    glColor3f(.97,.99,0.0)
    glVertex3f(-0.7,0.42,0.0)
    glVertex3f(-0.7,0.98,0.0)
    glVertex3f(-0.98,0.7,0.0)
    glVertex3f(-0.42,0.7,0.0)
    glVertex3f(-0.95,.47,0.0)
    glVertex3f(-0.45,0.93,0.0)
    glVertex3f(-.95,.95,0.0)
    glVertex3f(-0.49,0.48,0.0)
    glEnd()

    posx, posy,sides,radius = -0.7,0.7,32,0.20
    glBegin(GL_POLYGON)
    glColor3f(.97,.84,0.10)
    for i in range(sides):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def tree():
    glBegin(GL_QUADS)
    glColor3f(.55,.30,0.13)
    glVertex3f(0.8,0.2,0)
    glVertex3f(0.9,0.2,0)
    glVertex3f(0.8,-0.6,0)
    glVertex3f(0.9,-0.6,0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0.5, 0)
    for angulo in range(1,359,5):
        glVertex3f(0.2*math.cos(angulo * math.pi / 180) + 0.75, 0.2*math.sin(angulo * math.pi / 180) + 0.2, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0.5, 0)
    for angulo in range(1,359,5):
        glVertex3f(0.2*math.cos(angulo * math.pi / 180) + 0.85, 0.2*math.sin(angulo * math.pi / 180) + 0.25, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0.5, 0)
    for angulo in range(1,359,5):
        glVertex3f(0.2*math.cos(angulo * math.pi / 180) + 0.8, 0.2*math.sin(angulo * math.pi / 180) + 0.10, 0)
    glEnd()

def main():
    width = 1000
    height = 1000
    if not glfw.init():
        return
    window = glfw.create_window(width, height, "Mi ventana", None, None)
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glewExperimental = True
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return
    version = glGetString(GL_VERSION)
    print(version)

    while not glfw.window_should_close(window):
        glClearColor(0.52,0.80,0.92,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

        grass()
        house()
        roof()
        door()
        windows()
        sun()
        clowds()
        tree()

        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
