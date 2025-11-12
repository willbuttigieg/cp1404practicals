"""
CP1404 Practical 8
Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

names = {'will', 'eryn', 'seth', 'sarah', 'jason'}


class DynamicLabels(App):
    """Dynamic Labels App"""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = names

    def build(self):
        """Build main app"""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create dynamic labels"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)

DynamicLabels().run()