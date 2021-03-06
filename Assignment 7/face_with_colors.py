from graphics import *
import math

def main():
    win=GraphWin("face.py", 500, 500)
    Instruction=Text(Point(250,450),"Click will be the center of the Circle that constitutes the face outline.")
    Instruction.draw(win)
    centerPoint=win.getMouse()
    centerPoint.getX()
    centerPoint.getY()
    x1=centerPoint.getX()
    y1=centerPoint.getY()
    Instruction.setText("Click will be any point on the Cirlce that constitutes the face outline.")
    r=win.getMouse()
    r.getX()
    r.getY()
    x2=r.getX()
    y2=r.getY()
    radius= math.sqrt((x2-x1)**2+(y2-y1)**2)
    circle=Circle(centerPoint,radius)
    circle.setFill('')
    circle.draw(win)

    EyeColorInput=Entry(Point(250,480),25)
    EyeColorInput.setText("Enter the color of one eye.")
    EyeColorInput.draw(win)
    Instruction.setText("Click anywhere to proceed.")
    win.getMouse()
    EyeColorInput.undraw()
    Eye1Color=EyeColorInput.getText()
    Instruction.setText("Click will be the location of one eye.")
    EyeCenter1=win.getMouse()
    EyeRadius1=radius/10
    Eye1=Circle(EyeCenter1,EyeRadius1)
    Eye1.setFill(Eye1Color)
    Eye1.draw(win)
    
    EyeColorInput=Entry(Point(250,480),25)
    EyeColorInput.setText("Enter the color of the other eye.")
    EyeColorInput.draw(win)
    Instruction.setText("Click anywhere to proceed.")
    win.getMouse()
    EyeColorInput.undraw()
    Eye2Color=EyeColorInput.getText()
    Instruction.setText("Click will be the location of the other eye.")
    EyeCenter2=win.getMouse()
    EyeRadius2=radius/10
    Eye2=Circle(EyeCenter2,EyeRadius2)
    Eye2.setFill(Eye2Color)
    Eye2.draw(win)

    MouthColorInput=Entry(Point(250,480),25)
    MouthColorInput.setText("Enter the color of the mouth.")
    MouthColorInput.draw(win)
    Instruction.setText("Click anywhere to proceed.")
    win.getMouse()
    MouthColorInput.undraw()
    MouthColor=MouthColorInput.getText()
    Instruction.setText("Click will be one end of the mouth.")
    EndPoint1=win.getMouse()
    Instruction.setText("Click will be the other end of the mouth.")
    EndPoint2=win.getMouse()
    Mouth=Line(EndPoint1,EndPoint2)
    Mouth.setFill(MouthColor)
    Mouth.draw(win)

    Instruction.setText("Click anywhere to close the window.")
    win.getMouse()
    win.close()

main()
