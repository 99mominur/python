from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager


class TestApp(App):
    def build(self):
        username = ObjectProperty(None)
        new_username = ObjectProperty(None)
        layout = BoxLayout(orientation='vertical')

        # Access the progress bar by its id from the .kv file
        self.progress_bar = self.root.ids.progress_bar

        # Schedule the progress update
        Clock.schedule_interval(self.update_progress, .01)

        return self.root

    def update_progress(self, dt):
        # Update the progress value by a certain amount
        self.progress_bar.value += 1

        # Check if the progress bar is full (reached 100)
        if self.progress_bar.value >= 100:
            self.progress_bar.value = 0

            # Redirect to the 'second' screen
            self.root.current = 'second'
    def on_text_input_change(self):
        username = self.username.text
        print("Text Input Changed:", username)

class SecondWindow(ScreenManager): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
               
    def on_text_input_change(self):
        username = self.username.text
        print("Text Input Changed:", username)
        
        
        
if __name__ == '__main__':
    TestApp().run()
