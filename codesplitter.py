from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import StringProperty 

CHAR_NUMBER_LIMIT = 8000

class MyApp(App):
    char_limit = StringProperty(str(CHAR_NUMBER_LIMIT)) 
    
    def build(self):
        return Builder.load_file('codesplitter.kv')

    def paste_from_clipboard(self):
        self.root.ids.text_input.text = Clipboard.paste()
        self.root.ids.split_button.opacity = 1 if self.root.ids.text_input.text else 0

    def reset(self):
        self.root.ids.text_input.text = ''
        self.root.ids.scroll_layout.clear_widgets()
        self.root.ids.split_button.opacity = 0

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
    MyApp().run()
