from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty


Builder.load_file("main.kv")

class AwesomeApp(App):
    def build(self):
        username
        layout = BoxLayout(orientation='vertical')

        self.progress_bar = self.root.ids.progress_bar

        Clock.schedule_interval(self.update_progress, .01)

        return self.root

    def update_progress(self, dt):

        self.progress_bar.value += 1

        if self.progress_bar.value >= 100:
            self.progress_bar.value = 0

            self.root.current = 'second'


if __name__ == '__main__':
    AwesomeApp().run()
