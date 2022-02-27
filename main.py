from tkinter import *
import time
import random

winner = False
redhorse_x = 0
redhorse_y = 0

bluehorse_x = -7
bluehorse_y = 110

def startGame():
    global bluehorse_x
    global redhorse_x
    global winner

    while winner == False :
        time.sleep(0.05)
        random_move_blue_horse = random.randint(0,20)
        random_move_red_horse = random.randint(0,20)
        
        #update the x position of horses
        bluehorse_x += random_move_blue_horse
        redhorse_x += random_move_red_horse
        
        moveHorse(random_move_red_horse,random_move_blue_horse)
        main_screen.update()
        
        winner = checkWinner()
    
    if winner == "tie":
        Label(main_screen,text=winner,fg='green').place(x=200,y=450)
    else:
        Label(main_screen, text=winner +' WINS', fg='green').place(x=250, y=100)


def moveHorse(red_horse_random_move,blue_horse_random_move):
    canvas.move(red_horse,red_horse_random_move,0)
    canvas.move(blue_horse,blue_horse_random_move,0)


def checkWinner():
    if bluehorse_x >= 550   and redhorse_x >= 550 :
        return "Tie"
    if bluehorse_x >= 550 :
        return "Blue Horse"
    if redhorse_x >= 550:
        return "Red Horse"
    return False




#initi the screen
main_screen = Tk()
main_screen.title('Horse Race')
main_screen.geometry('600x500')
main_screen.config(background = 'white')

#setting the canvas
canvas = Canvas(main_screen, width = 600 , height = 200, bg = 'white') 
#The Canvas is a rectangular area intended for drawing pictures
# or other complex layouts. You can place graphics, text, widgets or frames on a Canvas.

canvas.pack(pady=20)

#import images
redhorse =PhotoImage(file='images/images.png')
bluehorse =PhotoImage(file='images/images (1).png')

#resizing images
redhorse = redhorse.zoom(15)
redhorse = redhorse.subsample(50)
#Return a new PhotoImage based on the same image as this widget but use only every Xth or Yth pixel.
bluehorse = bluehorse.zoom(15)
bluehorse = bluehorse.subsample(60)

#adding images to canvas
red_horse = canvas.create_image(redhorse_x,redhorse_y,anchor=NW,image=redhorse)
blue_horse = canvas.create_image(bluehorse_x,bluehorse_y,anchor=NW,image=bluehorse)


#adding labels to screen
l1 = Label(main_screen,text='Choose your Horse ',font=("Times", "24", "bold italic"),bg='white')
l1.place(x=190,y=300)
l2 = Label(main_screen,text='Click to Start',font=("Times", "24", "bold italic"),bg='white')
l2.place(x=220,y=430)

#adding the button
b1 = Button(main_screen,height=2,width=15,text="PLAY",bg='gray',command=startGame  )
b1.place(x=220,y=360)

main_screen.mainloop()
