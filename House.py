from OpenGL.GL import *
from glew_wish import *
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


def window1():
    glBegin(GL_QUADS)
    glColor3f(0.5,.90,0.75)
    glVertex3f(-0.3,0.2,0)
    glVertex3f(0.3,0.2,0)
    glVertex3f(0.1,0.1,0)
    glVertex3f(-0.1,0.1,0.0)
    glEnd()

def roof():
    glBegin(GL_TRIANGLES)
    glColor3f(.16,.16,0.20)
    glVertex3f(-0.55,0.4,0)
    glVertex3f(0.55,0.4,0)
    glVertex3f(0.0,0.6,0.0)
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
        glClearColor(0.67,0.84,0.9,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

        grass()
        house()
        roof()
        window1()

        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
