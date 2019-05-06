from svg_draw import *
import math

print("Sujit Neupane")
print("Oct 24, 2018")
print("Assignment_4")
print("---------------------------")

width = 1200
height = 800
create_plot(width, height, True)
eye_color = "(0, 0, 0)"
nose_color = "(0, 0, 200)"
mouth_color = "(255, 200, 200)"

L = [[[-80, 120], 20], [[80, 120], 20], [[0, 55], 10], [[0, 45], 10], [[0, 35], 10],
     [[-6, 30], 10], [[6, 30], 10], [[-70, -25], 10], [[-55, -45], 10], [[-35, -52], 10],
     [[-15, -55], 10], [[0, -55], 10], [[70, -25], 10], [[55, -45], 10], [[35, -52], 10],
     [[15, -55], 10]]


def draw_face(L):
    for i in range(len(L)):
        if i < 2:
            color = eye_color
        elif i < 7:
            color = nose_color
        else:
            color = mouth_color
        draw_point(L[i][0], L[i][1], color)
        

def pause():
    input("Type 'Enter' to proceed: ")
    print("\n")


def scale_point(point, alpha):
    return [point[0]*alpha, point[1]*alpha]


def scale_pointList(listOfPoints, alpha):
    return [[scale_point(i[0], alpha), i[1]*alpha] for i in listOfPoints]


def frame_animation(frame):
    for i in range(1, frame, 1):
        clear_plot(True)
        scaled_points = scale_pointList(L, i/frame)        
        draw_face(scaled_points)


def translate_point(point, delta):
    return [point[0]+delta[0], point[1]+delta[1]]


def translate_pointList(listOfPoints, delta):
    return [[translate_point(i[0], delta), i[1]] for i in listOfPoints]


def translate_face(step):
    a = []
    b = []
    c = []
    print("Probem C: ")
    for i in range(0, 300, step):
        a = translate_pointList(L, [i, i])
        clear_plot(True)
        draw_face(a)
    pause()

    print("Problem D: ")
    for i in range(0, -600, -step):
        b = translate_pointList(a, [i, -step])
        clear_plot(True)
        draw_face(b)
    pause()

    print("Problem E: ")
    for i in range(0, 300, step):
        c = translate_pointList(b, [i+step, -i])
        clear_plot(True)
        draw_face(c)
    pause()

    shrink_face(c)
   

def shrink_face(listOfPoints):
    print("Problem F: ")
    a = scale_pointList(listOfPoints, 1/5)
    b = []
    for i in range(30, 1, -1):
        if (a != b):
            b = scale_pointList(listOfPoints,i/30)
            clear_plot(True)
            draw_face(b)


def tracing_sineFunction():
    print("Problem G: ")
    a = scale_pointList(L, 30/100)
    amplitude = 400
    period = 300
    k = 0
    l = 1200
    interval = 5
    oscillation = 3
    for i in range(oscillation):
        for x in range(k, l, interval):
            y = amplitude * (1 + math.sin((math.pi * x)/150))
            c = translate_pointList(a, [x-(period * 2), y-amplitude])
            clear_plot(True)
            draw_face(c)

        if i%2 == 0:
            k = 1200
            l = 0
            interval = -5
        else:
            k = 0
            l = 1200
            interval = 5
        

def main():
    print("Problem A: ")
    draw_face(L)
    pause()

    print("Problem B: ")
    frame_animation(30)
    pause()

    translate_face(20)
    pause()

    tracing_sineFunction()
   

main()
