import turtle as trtl

painter = trtl.Turtle()

#draws body of rocket ship
painter.forward(100)
painter.right(90)
painter.backward(198)
painter.right(90)
painter.forward(100)
painter.left(90)
painter.forward(198)

#draws top of rocket
painter.backward(198)
painter.left(350)
painter.forward(70)

window = trtl.Screen()
window.mainloop()