"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Owen Land.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg
window = rg.TurtleWindow()
turtle = rg.SimpleTurtle()
not_turtle = rg.SimpleTurtle()

turtle.pen = rg.Pen('pink',11)
not_turtle.pen = rg.Pen('blue',8)

turtle.speed = 10
not_turtle.speed = 10
size= 150

for k in range(8):

   turtle.draw_circle(size)
   turtle.pen_up()
   turtle.left(90)
   turtle.forward(5)
   turtle.pen_down()

   not_turtle.draw_regular_polygon(8,size)
   not_turtle.pen_up()
   not_turtle.right(45)
   not_turtle.backward(15)
   not_turtle.pen_down()
   size=size-15

window.close_on_mouse_click()



