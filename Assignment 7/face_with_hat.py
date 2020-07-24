from graphics import *
import math

def main():
    win=GraphWin("face.py", 500, 500)
    Instruction=Text(Point(250,480),"The first click will be the center of the Circle that constitutes the face outline.")
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
    radius=math.sqrt((x2-x1)**2+(y2-y1)**2)
    circle=Circle(centerPoint,radius)
    circle.setFill('')
    circle.draw(win)

    Instruction.setText("The third click will be the location of one eye.")
    EyeCenter1=win.getMouse()
    EyeRadius1=radius/10
    Eye1=Circle(EyeCenter1,EyeRadius1)
    Eye1.setFill('brown')
    Eye1.draw(win)

    Instruction.setText("The fourth click will be the location of the other eye.")
    EyeCenter2=win.getMouse()
    EyeRadius2=radius/10
    Eye2=Circle(EyeCenter2,EyeRadius2)
    Eye2.setFill('brown')
    Eye2.draw(win)

    Instruction.setText("The fifth click will be one end of the mouth.")
    EndPoint1=win.getMouse()
    Instruction.setText("The sixth click will be the other end of the mouth.")
    EndPoint2=win.getMouse()
    Mouth=Line(EndPoint1,EndPoint2)
    Mouth.setFill('red')
    Mouth.draw(win)

    p1=circle.getP1()
    x=p1.getX()
    y=p1.getY()
    p2=Point(2*radius+x, y)
    p3=Point(x+radius, y-radius)
    triangle=Polygon(p1,p2,p3)
    triangle.setFill("blue")
    triangle.setOutline("green")
    triangle.draw(win)
    
    Instruction.setText("The seveneth click will close the window.")
    win.getMouse()
    win.close()

main()
