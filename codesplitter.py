from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import StringProperty 
from kivy.uix.togglebutton import ToggleButton
import os, sys
from kivy.resources import resource_add_path


CHAR_NUMBER_LIMIT = 4000
options = [2000, 4000, 6000, 8000]

class MyApp(App):
    char_limit = StringProperty(str(CHAR_NUMBER_LIMIT)) 
    
    def build(self):
        filename = 'codesplitter.kv'
        # if not(os.path.isfile(filename)):
        #     filename = os.path.join(os.getcwd(), '_internal',filename)
        return Builder.load_file(filename)

    def paste_from_clipboard(self):
        self.root.ids.text_input.text = Clipboard.paste()
        self.root.ids.split_toggle_placeholder.clear_widgets()
        for option in options:
            tb = ToggleButton(text=str(option)+'\nchars', group="char_limit")
            tb.bind(on_press=self.update_char_limit_and_split)
            if option==CHAR_NUMBER_LIMIT:
                tb.state = 'down' # Active
            self.root.ids.split_toggle_placeholder.add_widget(tb)
        self.root.ids.split_boxlayout.opacity = 1 if self.root.ids.text_input.text else 0
    def update_char_limit_and_split(self, instance):
        global CHAR_NUMBER_LIMIT
        CHAR_NUMBER_LIMIT = int(instance.text.split('\n')[0])
        self.split_text()
    def reset(self):
        self.root.ids.text_input.text = ''
        self.root.ids.scroll_layout.clear_widgets()
        self.root.ids.split_boxlayout.opacity = 0

    def split_text(self):
        self.root.ids.scroll_layout.clear_widgets()
        text = self.root.ids.text_input.text
        lines = text.split('\n')
        self.string_list = []
        current_segment = ""
        for line in lines:
            if len(current_segment) + len(line) > CHAR_NUMBER_LIMIT-100:
                self.string_list.append(current_segment)
                current_segment = line
            else:
                current_segment += '\n' + line
        self.string_list.append(current_segment)
        for i, _ in enumerate(self.string_list):
            segment_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            button = Button(text=str(i), size_hint_y=None, height=40)
            button.bind(on_press=self.copy_to_clipboard)
            segment_text = TextInput(text=self.string_list[i], multiline=True, readonly=False, size_hint_y=None, height=40)
            segment_text.cursor = (0, 0)
            segment_layout.add_widget(button)
            segment_layout.add_widget(segment_text)
            self.root.ids.scroll_layout.add_widget(segment_layout)

    def copy_to_clipboard(self, instance):
        index = int(instance.text)
        Clipboard.copy(self.string_list[index])
        print(f'Copied code segment {index} to clipboard')
        instance.background_color = [0.7, 0.7, 0.7, 1]

if __name__ == '__main__':
    # For pyinstaller
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MyApp().run()
