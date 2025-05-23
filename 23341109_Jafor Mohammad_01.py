#Task 1

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

win_w, win_h = 600, 600

rain_particles = []
for i in range(1000):
    rain_particles.append([random.randint(0, win_w), random.randint(0, win_h), 2, 18])

wind_offset = 0
fall_speed = 3
background_intensity = 0.85
brightness_step = 0.04

def draw_structure():
    #house base
    glColor3f(0.3, 0.2, 0.6)
    glBegin(GL_TRIANGLES)
    glVertex2d(150, 50)
    glVertex2d(150, 300)
    glVertex2d(450, 300)
    glEnd()

    glColor3f(0.3, 0.2, 0.6)
    glBegin(GL_TRIANGLES)
    glVertex2d(150, 50)
    glVertex2d(450, 50)
    glVertex2d(450, 300)
    glEnd()

    #Roof
    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex2d(150, 300)
    glVertex2d(300, 450)
    glVertex2d(450, 300)
    glEnd()
    
    #Door
    glColor3f(0.4, 0.2, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2d(250, 50)
    glVertex2d(250, 180)
    glVertex2d(350, 180)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2d(250, 50)
    glVertex2d(350, 50)
    glVertex2d(350, 180)
    glEnd()

    #Window
    glColor3f(0.1, 0.7, 0.9)
    glBegin(GL_TRIANGLES)
    glVertex2d(370, 200)
    glVertex2d(370, 270)
    glVertex2d(440, 270)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2d(370, 200)
    glVertex2d(440, 200)
    glVertex2d(440, 270)
    glEnd()

    #window crossbar
    glColor3f(0, 0, 0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2d(370, 235)
    glVertex2d(440, 235)
    glEnd()

    glBegin(GL_LINES)
    glVertex2d(405, 200)
    glVertex2d(405, 270)
    glEnd()

def draw_raindrops():
    global rain_particles, wind_offset
    for drop in rain_particles:
        glColor3f(0.4, 0.1, 1.0)
        glLineWidth(drop[2])
        glBegin(GL_LINES)
        glVertex2f(drop[0] - wind_offset, drop[1])
        glVertex2f(drop[0], drop[1] - drop[3])
        glEnd()

def keyboard_input(key, x, y):
    global background_intensity
    if key == b'd':
        if background_intensity < 0.85:
            background_intensity += brightness_step
    elif key == b'n':
        if background_intensity > 0.15:
            background_intensity -= brightness_step
    glutPostRedisplay()

def special_keys(key, x, y):
    global wind_offset
    if key == GLUT_KEY_LEFT: 
        wind_offset -= 1
    if key == GLUT_KEY_RIGHT:
        wind_offset += 1
    glutPostRedisplay()

def render_scene():
    global background_intensity
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(background_intensity, background_intensity, background_intensity, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_raindrops()
    draw_structure()

    glutSwapBuffers()

def animate():
    global rain_particles, win_w, win_h, fall_speed, wind_offset
    for drop in rain_particles:
        drop[1] = (drop[1] - fall_speed) % win_h
        drop[0] = (drop[0] + wind_offset) % win_w
    glutPostRedisplay()

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, win_w, 0, win_h, -1, 1)

glutInit()
glutInitWindowSize(win_w, win_h)
glutInitWindowPosition(150, 150)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

win = glutCreateWindow(b"House with Rain")
init()

glutDisplayFunc(render_scene)
glutIdleFunc(animate)
glutKeyboardFunc(keyboard_input)
glutSpecialFunc(special_keys)

glutMainLoop()



#task 2


# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random
# import time

# W_Width, W_Height = 500, 500
# boundary = 200  

# points = []  
# speed_factor = 0.01  
# blinking = False  
# frozen = False 

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.vx = random.choice([-1, 1]) * random.uniform(0.5, 1.5)  
#         self.vy = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
#         self.r = random.random()
#         self.g = random.random()
#         self.b = random.random()
#         self.blink_state = True  

#     def move(self):
#         if frozen:
#             return

#         self.x += self.vx * speed_factor
#         self.y += self.vy * speed_factor

#         if self.x >= boundary or self.x <= -boundary:
#             self.vx *= -1  
#         if self.y >= boundary or self.y <= -boundary:
#             self.vy *= -1  

#     def toggle_blink(self):
#         if blinking:
#             self.blink_state = not self.blink_state  

# def draw_boundary():
#     glColor3f(1, 1, 1)  
#     glBegin(GL_LINES)

#     # Bottom Edge
#     glVertex2f(-boundary, -boundary)
#     glVertex2f(boundary, -boundary)

#     # Right Edge
#     glVertex2f(boundary, -boundary)
#     glVertex2f(boundary, boundary)

#     # Top Edge
#     glVertex2f(boundary, boundary)
#     glVertex2f(-boundary, boundary)

#     # Left Edge
#     glVertex2f(-boundary, boundary)
#     glVertex2f(-boundary, -boundary)

#     glEnd()


# def draw_points():
#     for p in points:
#         if blinking and not p.blink_state:
#             continue  
        
#         glColor3f(p.r, p.g, p.b)
#         glPointSize(5)
#         glBegin(GL_POINTS)
#         glVertex2f(p.x, p.y)
#         glEnd()

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
    
#     draw_boundary() 
#     draw_points()  

#     glutSwapBuffers()

# def animate():
#     if not frozen:
#         for p in points:
#             p.move()
#         if blinking:
#             for p in points:
#                 p.toggle_blink()
    
#     glutPostRedisplay()

# def keyboardListener(key, x, y):
#     global frozen, speed_factor, blinking

#     if key == b' ':  
#         frozen = not frozen

#     glutPostRedisplay()

# def specialKeyListener(key, x, y):
#     global speed_factor

#     if frozen:
#         return

#     if key == GLUT_KEY_UP:  
#         speed_factor *= 1.5
       

#     elif key == GLUT_KEY_DOWN:  
        
#         speed_factor /= 1.5

#     glutPostRedisplay()

# def mouseListener(button, state, x, y):
#     global blinking

#     if frozen:
#         return

#     if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
#         gl_x = (x - W_Width / 2)  
#         gl_y = (W_Height / 2 - y)  
        
#         if -boundary <= gl_x and gl_x <= boundary and -boundary <= gl_y and gl_y <= boundary:
#             new_point = Point(gl_x, gl_y)
#             points.append(new_point)

#     elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
#         blinking = not blinking

#     glutPostRedisplay()

# def init():
#     glClearColor(0, 0, 0, 1)  
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluOrtho2D(-W_Width / 2, W_Width / 2, -W_Height / 2, W_Height / 2)  
#     glMatrixMode(GL_MODELVIEW)  

# glutInit()
# glutInitWindowSize(W_Width, W_Height)
# glutInitWindowPosition(0, 0)
# glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

# wind = glutCreateWindow(b"Task 2")
# init()

# glutDisplayFunc(display)
# glutIdleFunc(animate)
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)

# glutMainLoop()