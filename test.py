from kivymd.app import MDApp
from kivy.lang import Builder


class Main(MDApp):
    def changeText(self):
        l = self.root.ids.txt
        l.text = "The world's [i]nicest[/i] animal"

    def build(self):
        return Builder.load_file("ui.kv")


Main().run()