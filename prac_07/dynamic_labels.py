from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["James", "John", "Peter", "Malachi", "Achilles"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text = str(name))
            temp_label.name = name
            self.root.ids.main.add_widget(temp_label)

    def display_labels(self, instance):
        name = instance.name
        instance.text = str(name)
        self.status_text = f"{name}"


DynamicLabelsApp().run()
