from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting Miles to Kilometres """
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        result = value * 1.609344
        result = float(result)
        self.root.ids.output_label.text = "{:.3f}".format(result)

    def handle_increment(self, value, increment):
        result = value + increment
        print(result)
        self.root.ids.input_number.text = str(result)

ConvertMilesApp().run()