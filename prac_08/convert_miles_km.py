"""
CP1404 Practical 8

Convert miles to kilometers

"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_FACTOR = 1.60934


class ConvertMilesToKilometres(App):
    """App to convert miles to kilometres."""
    miles = StringProperty()

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        self.output_label = None

    def build(self):
        """Build the app"""
        self.title = 'Convert miles to kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Convert miles from input to kilometres."""
        miles = self.convert_input_to_float()
        kilometers = miles * MILES_FACTOR
        self.root.ids.output_label.text = str(kilometers)

    def handle_increment(self, change):
        """Increment the miles value depending on button pressed."""
        miles = self.convert_input_to_float() + change
        self.root.ids.text_input.text = str(miles)
        self.handle_conversion()

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.miles = self.root.ids.text_input.text

    def convert_input_to_float(self):
        """Convert input to float."""
        try:
            value = float(self.root.ids.text_input.text)
            return value
        except ValueError:
            return 0.0


ConvertMilesToKilometres().run()
