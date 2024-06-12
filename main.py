from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

Window.clearcolor = (255/255, 186/255, 3/255, 1)

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.apricot = 0
        self.apricot_need = 100
        self.file = open('files/apr.txt', 'r')
        self.file1 = open('files/aprn.txt', 'r')
        for line in self.file:
            self.apricot = int(line.strip())
        self.file.close()
        for line in self.file1:
            self.apricot_need = int(line.strip())
        self.file1.close()
        self.quality_clicks = Label(text=f'{self.apricot}/{self.apricot_need}\nApricots', 
                                    font_size ="40sp",
                                    color =(0, 0, 0, 1),
                                    font_name = "files/Comic.ttf"
                                    )
        self.click_button = Button(
                                   size_hint = (.64, .42),
                                   pos_hint = {"x":0.18, "center_y":0.25},
                                   background_normal= 'files/apricot.png',
                                   background_down = 'files/apricot-dark.png'
                                   )
        self.click_button.bind(on_press = self.click)
    def click(self, event):
        self.apricot += 1
        self.quality_clicks.text = f'{self.apricot}/{self.apricot_need}\nApricots'
        sound = SoundLoader.load('files/click-sound.wav')
        sound.play()
        self.file = open('files/apr.txt', 'w')
        self.file.write(str(self.apricot))
        self.file.seek(0)
        if self.apricot == self.apricot_need:
            self.quality_clicks.text = f"{self.apricot_need} apricots!"
            self.apricot_need += 200
            self.file1 = open('files/aprn.txt', 'w')
            self.file1.write(str(self.apricot_need))
            self.file1.close()
            sound = SoundLoader.load('files/happy.wav')
            sound.play()

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.quality_clicks)
        box.add_widget(self.click_button)

        return box

if __name__ == "__main__":
    MyApp().run()
