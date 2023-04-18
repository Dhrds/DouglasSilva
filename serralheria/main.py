from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

class GerenciarTelas(ScreenManager):
    pass
class Home(Screen):
    pass

class Serralheria(MDApp):   
    def build(self):

        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = '700'
        return GerenciarTelas()


#Serralheria().run()


