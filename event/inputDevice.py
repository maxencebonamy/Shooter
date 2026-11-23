class InputDevice:

    def __init__(self):
        self.pressed = []

    def has(self, pressed):
        return pressed in self.pressed

    def set(self, pressed):
        self.pressed.append(pressed)

    def remove(self, pressed):
        self.pressed.remove(pressed)