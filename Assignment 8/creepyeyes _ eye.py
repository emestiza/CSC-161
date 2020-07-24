from graphics import *
from eye import *
from button import *
import math
import time

def main():
#Draws circle for face using interactive graphics by getting a centerpoint and radius.
    win=GraphWin("face.py", 500, 500)
    Instruction=Text(Point(250,400),"The first click will be the center of the Circle that constitutes the face outline.")
    Instruction.draw(win)
    centerPoint=win.getMouse()
    centerPoint.getX()
    centerPoint.getY()
    x1=centerPoint.getX()
    y1=centerPoint.getY()
    Instruction.setText("The second click will be any point on the Cirlce that constitutes the face outline.")
    r=win.getMouse()
    r.getX()
    r.getY()
    x2=r.getX()
    y2=r.getY()
    radius= math.sqrt((x2-x1)**2+(y2-y1)**2)
    circle=Circle(centerPoint,radius)
    circle.draw(win)

#Draws eyes using interactive graphics by getting a centerpoint and Eye class.    
    Instruction.setText("The third click will be the location of one eye.")
    p1=win.getMouse()
    eyeradius1=radius/10
    Eye1=Eye(p1,eyeradius1)
    Eye1.draw(win)

    Instruction.setText("The fourth click will be the location of the other eye.")
    p2=win.getMouse()
    eyeradius2=radius/10
    Eye2=Eye(p2,eyeradius2)
    Eye2.draw(win)

#Draws mouth using interactive graphics by gettting two endpoints.
    Instruction.setText("The fifth click will be one end of the mouth.")
    EndPoint1=win.getMouse()
    Instruction.setText("The sixth click will be the other end of the mouth.")
    EndPoint2=win.getMouse()
    Mouth=Line(EndPoint1,EndPoint2)
    Mouth.setFill('red')
    Mouth.draw(win)

#Creates and activates buttons to enable the user to click a button.
    Instruction.setText("Click on a button for additional features.")
    WinkRightEye=Button(win,Point(50,480),100,100,"Wink Right Eye")
    WinkRightEye.activate()

    WinkLeftEye=Button(win,Point(150,480),100,100,"Wink Left Eye")
    WinkLeftEye.activate()

    DilatePupils=Button(win,Point(250,480),100,100,"Dilate Pupils")
    DilatePupils.activate()

    ConstrictPupils=Button(win,Point(350,480),100,100,"Constrict Pupils")
    ConstrictPupils.activate()

    Quit=Button(win,Point(450,480),100,100,"Quit")
    Quit.activate()
    click=win.getMouse()

#The while loop enables fucntions unless quit button is clicked which exits program.
    while not Quit.clicked(click):
        click=win.getMouse()

#Allows eyes to wink using functions from the Eye class.
#Winks the right eye with respect to the face.
        if WinkRightEye.clicked(click):
            Eye.wink(Eye1,win); 

#Winks the left eye with respect to the face.
        if WinkLeftEye.clicked(click):
            Eye.wink(Eye2,win);

#Increases pupil size to equal eye size using a while loop and Eye class functions and methods.
        if DilatePupils.clicked(click):
                while eyeradius1>Eye1.pupil.radius and eyeradius2>Eye2.pupil.radius:
                    size=Eye1.pupil.radius+1
                    Eye.changepupilsize(Eye1,win,size);
                    Eye.changepupilsize(Eye2,win,size);

#Decreases pupil size to its original size using a while loop and Eye class functions and methods.
        if ConstrictPupils.clicked(click):
                while Eye1.pupil.radius>eyeradius1/4 and Eye2.pupil.radius>eyeradius2/4:
                    size=Eye1.pupil.radius-1
                    Eye.changepupilsize(Eye1,win,size);
                    Eye.changepupilsize(Eye2,win,size);            

#Closes the window if Quit button is clicked.                
    else:
        win.close()
              
main()

class Eye:

    def __init__ (self,p,r):
        self.eyeradius = r
        self.pupilradius = r/4
        self.eyepoint = p
        self.outline = Circle(p,r)
        self.pupil = Circle(p,r/4)
        self.pupil.setFill("black")

#Draws the outline of the eye using the variables in __init__.
    def drawoutline(self,win):
        self.outline.draw(win)

#Draws the pupil of the eye using the variables in __init__.
    def drawpupil(self,win):
        self.pupil.draw(win)

#Draws the whole eye using functions in the class.        
    def draw(self,win):
        self.outline.draw(win)
        self.pupil.draw(win)
        self.pupil.setFill("black")

#Undraws the outline of the eye.
    def undrawoutline(self):
        self.outline.undraw()

#Undraws the pupil of the eye.       
    def undrawpupil(self):
        self.pupil.undraw()        

#Undraws the whole eye using functions in the class.
    def undraw(self):
        self.outline.undraw()
        self.pupil.undraw()
        self.pupil.setFill("")

#Makes the eye wink by turning the eye into a line and then redrawing the eye as it was before.
    def wink(self,win):
        self.outline.undraw()
        self.pupil.undraw()
        self.pupil.setFill("")
        x=self.eyepoint.getX()
        y=self.eyepoint.getY()
        wink=Line(Point(x-self.eyeradius,y),Point(x+self.eyeradius,y))
        wink.draw(win)
        time.sleep(1)
        wink.undraw()
        self.outline.draw(win)
        self.pupil.draw(win)
        self.pupil.setFill("black")

#Changes the radius of the pupil to be equal to size, undraws, and draws pupil.
    def changepupilsize(self,win,size):
        self.pupil.undraw()
        self.pupilradius=size
        self.pupil=Circle(self.eyepoint,size)
        self.pupil.draw(win)
        self.pupil.setFill("black")

