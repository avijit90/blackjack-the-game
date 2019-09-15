from tkinter import PhotoImage


class Card:

    def __init__(self, face_value, face_img_path, back_img_path):
        self.face_value = face_value
        self.face_img_path = face_img_path
        self.face_img = None  # PhotoImage(file=face_img)
        self.back_img_path = back_img_path
        self.back_img = None  # PhotoImage(file=back_img)
        self.visible = False

    def __str__(self):
        return f'face_value : {self.face_value},\n face_img : {self.face_img_path},\n ' \
               f'back_img : {self.back_img_path},\n visible : {self.visible}'

    def get_card_image(self):
        return self.face_img if self.visible else self.back_img

    def show_card(self):
        self.visible = True

    def create_card_images(self):
        self.face_img = PhotoImage(file=self.face_img_path)
        self.back_img = PhotoImage(file=self.back_img_path)
