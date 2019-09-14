from tkinter import *

top = Tk()

C = Canvas(top, bg="green", height=600, width=1100)

closed_card = PhotoImage(file="../resources/90X150/card_back.png")
face_card = PhotoImage(file="../resources/90X150/2_of_clubs.png")

# Stack
C.create_image(100 + 100, 250, anchor=NE, image=closed_card)
C.create_image(100 + 103, 250, anchor=NE, image=closed_card)
C.create_image(100 + 106, 250, anchor=NE, image=closed_card)
C.create_image(100 + 109, 250, anchor=NE, image=closed_card)
C.create_image(100 + 112, 250, anchor=NE, image=closed_card)
C.create_image(100 + 115, 250, anchor=NE, image=closed_card)

# Dealer
C.create_image(400 + 220, 50, anchor=NE, image=face_card)

# Player
C.create_image(400 + 220, 400, anchor=NE, image=face_card)
C.create_image(305 + 220, 400, anchor=NE, image=face_card)

C.pack()

top.mainloop()
