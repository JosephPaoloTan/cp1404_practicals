from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATE = 1.60934


class MilesConversionApp(App):
    """Kivy App to convert miles to kilometres."""

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_miles()
        result = value * CONVERSION_RATE
        self.root.ids.output_label.text = str(result)

    def get_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        value = self.get_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()


MilesConversionApp().run()
