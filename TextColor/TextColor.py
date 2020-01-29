class TextColor:
    def __init__(self):
        self.damage = '\033[1;31;31m' #red
        self.life = '\033[1;0;32m' #green
        self.level = self.critical = '\033[1;0;33m' #yellow
        self.dodge = '\033[1;0;33m' #orange

        self.normal = '\033[1;37;37m' #reset to normal terminal colors
        self.bold = '\033[1;1;1m' #just bolded text