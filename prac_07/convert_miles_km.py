from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILE_TO_KM = 1.609344

class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting Miles to Kilometres """
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        value = self.get_valid_miles()
        result = value * MILE_TO_KM
        result = float(result)
        self.root.ids.output_label.text = "{:.3f}".format(result)

    def handle_increment(self, value, increment):
        if value == '':
            value = 0
        result = int(value) + increment
        self.root.ids.input_number.text = str(result)
        self.handle_calculate(value)

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

ConvertMilesApp().run()