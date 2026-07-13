from menu import Menu

class Num:
    def __init__(self):
        self.menu = Menu()

    def start(self):
        self.menu.run()

obj = Num()
obj.start()