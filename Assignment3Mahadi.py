from graphics import *

def rectangle():
    win = GraphWin("MY Rectangle", 600, 450)

    win.setCoords(0.0, 0.0, 10.0, 20.0)
    message = Text(Point(5, 3), "Please Click on two points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rct = Rectangle(p1, p2)
    rct.setOutline("Purple")
    rct.draw(win)

    win.getMouse()
    win.close()

rectangle()