from graphics import *
import time

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
