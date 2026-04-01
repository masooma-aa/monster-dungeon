# Name: Masooma Fatima
# NSID: mbq567
# Student number: 11438127
# Course: CMPT 140
# Instructor Name: Sandra Kumi

import turtle
import random
import math

screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("#404040")
screen.title("Monster Dungeon")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

radius = 30
max_attempts = 870
canvas_min = -200
canvas_max = 200

monsters = []
is_full = False

def can_place_monster(x, y, existing_monsters, radius):
    for (mx, my) in existing_monsters:
        distance = math.sqrt((x - mx) ** 2 + (y - my) ** 2)
        if distance < 2 * radius:
            return False
    return True

def draw_monster(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.pencolor("red")
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()
    
def draw_full_message():
    pen.penup()
    pen.goto(0, 20)
    pen.pendown()
    pen.pencolor("white")
    pen.write("ALL FULL!", align="center", font=("Garamond", 30, "bold"))
    pen.penup()
    pen.goto(0, -20)
    pen.pendown()
    pen.write("NO MORE MONSTERS!", align="center", font=("Garamond", 22, "bold"))
    pen.penup()
    
def on_click(x, y):
    global is_full
    
    if is_full:
        return
    
    placed = False
    for _ in range(max_attempts):
        rx = random.randint(canvas_min, canvas_max)
        ry = random.randint(canvas_min, canvas_max)
        if can_place_monster(rx, ry, monsters, radius):
            monsters.append((rx, ry))
            draw_monster(rx, ry, radius)
            placed = True
            break
        
    if not placed:
        is_full = True
        draw_full_message()
    screen.update()
    
screen.update()
screen.onclick(on_click)
screen.listen()

turtle.done()