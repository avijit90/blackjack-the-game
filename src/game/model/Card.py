class Card:

    def __init__(self, face_value, face_img, back_img):
        self.face_value = face_value
        self.face_img = face_img
        self.back_img = back_img
        self.visible = False

    def __str__(self):
        return f'face_value : {self.face_value},\n face_img : {self.face_img},\n ' \
               f'back_img : {self.back_img},\n visible : {self.visible}'
