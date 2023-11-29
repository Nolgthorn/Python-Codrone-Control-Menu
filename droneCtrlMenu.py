from codrone_edu.drone import *
import os
from random import randint

def clear(): os.system('cls')

#define variables
running = True
menu_ops = {
    1: 'play song',
    2: 'hover',
    3: 'fly straight and return',
    4: 'roomba mode',
    5: 'set waypoints',
    6: 'move to absolute positions',
    7: 'do a backflip',
    8: 'do a spiral',
    9: 'set LED to a random colour',
    10: 'land drone',
    11: 'exit'
}

def print_menu():
    print("")
    print("""Drone Controls
    ============
    """)
    for key in menu_ops.keys():
        print(key, '--', menu_ops[key])

#establish connection to drone
drone = Drone()
drone.pair()

def playSong():
    drone.set_drone_LED(255,255,255,255)
    drone.drone_buzzer(Note.G4, 500)
    drone.drone_buzzer(Note.G4, 500)
    drone.drone_buzzer(Note.G4, 500)
    drone.drone_buzzer(Note.A4, 500)
    drone.drone_buzzer(Note.B4, 500)
    drone.drone_buzzer(Note.A4, 500)
    drone.drone_buzzer(Note.G4, 500)
    drone.drone_buzzer(Note.B4, 500)
    drone.drone_buzzer(Note.A4, 500)
    drone.drone_buzzer(Note.A4, 500)
    drone.drone_buzzer(Note.G4, 500)

def hover(time):
    drone.takeoff()
    drone.hover(time)
    drone.land()

def flyStraight():
    drone.takeoff()
    drone.hover(1)
    drone.set_waypoint()
    drone.keep_distance(7, 600)
    drone.turn_degree(180)
    drone.keep_distance(7,600)
    drone.goto_waypoint(drone.waypoint_data[0], 0.5)
    
    drone.land()
    
def roombaMode():
    drone.takeoff()
    for x in range(10):
        drone.avoid_wall(5, 50)
        drone.turn_degree(90)
    drone.land

def waypoints():
    drone.takeoff()
    drone.hover(1)
    drone.set_waypoint()
    drone.keep_distance(5, 600)
    drone.hover(1)
    drone.set_waypoint()
    
    drone.goto_waypoint(drone.waypoint_data[0], 0.5)
    drone.goto_waypoint(drone.waypoint_data[1], 0.5)
    drone.goto_waypoint(drone.waypoint_data[0], 0.5)
    
    drone.land()
    
def move2Pos():
    drone.takeoff()
    drone.send_absolute_position(0.5, 0, 1, 0.5, 0, 0)
    time.sleep(1)
    drone.send_absolute_position(0.5, 0, 1, 0.5, 0, 0)
    time.sleep(1)
    drone.land()
    
def backflip():
    drone.takeoff()

    drone.hover(3)
    drone.flip("back")  # send flip command
    time.sleep(4)  # wait for flip to complete

    drone.set_pitch(30) # move forward for 1 second
    drone.move(1)

    drone.set_pitch(-30) # move backward for 1 second
    drone.move(1)
    
    drone.land()

def doSpiral():
    drone.spiral(30, 3, 1)

def randLED():
    drone.set_drone_LED(randint(1,255), randint(1,255), randint(1,255), 100)

def landDrone():
    drone.land()

while(running == True):
    print_menu()
    selected = ''
    try: 
        print("Please enter a number to choose a command (1-7)")
        selected = int(input(">"))
    except:
        print("Error. Please enter a valid number")
    
    if selected == 1:
        playSong()
    elif selected == 2:
        try: 
            print("Please enter a length of time to hover (seconds)")
            time = int(input(">"))
            hover(time)
        except:
            print("Error. Please enter a valid number")
    elif selected == 3:
        flyStraight()
    elif selected == 4:
        roombaMode()
    elif selected == 5:
        waypoints()
    elif selected == 6:
        move2Pos()
    elif selected == 7:
        backflip()
    elif selected == 8:
        doSpiral()
    elif selected == 9:
        randLED()
    elif selected == 10:
        landDrone()
    elif selected == 11:
        running = False
    else:
        print("Please enter a number within the range (1-7)")
        
    clear()

#flyStraight()
#waypoints()
#move2Pos()
#roombaMode()

drone.land()
drone.close()

input()
