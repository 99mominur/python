import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("epic.kv")

class LoginForm(Widget):
    name = ObjectProperty(None)

    def press(self):
        name = self.name.text

        # print(f"hello {username}, Welcome to Epic app!")
        if name != "":
            # self.add_widget(
                # Label(text=f"Hello {username}, Welcome to Epic app!"))
            print(f"Hello {name}, Welcome to Epic app!")
        self.name.text = ""


class AwesomeApp(App):
    def build(self):
        return LoginForm()


if __name__ == "__main__":
    AwesomeApp().run()
