from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self):
        super().__init__()
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('label_demo.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
