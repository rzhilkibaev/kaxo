import urwid
import random

def main():
    FileManager().run()

class FileManager():
    def __init__(self):
        self.ui = UI()

    def run(self):
        self.ui.run()

class UI():
    def __init__(self):
        palette = [("tab_inactive", "black", "white"),
                   ("tab_active", "white", "black")]
        self.loop = urwid.MainLoop(MainFrame(), palette=palette, unhandled_input=self.on_input)

    def run(self):
        self.loop.run()

    def on_input(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

class MainFrame(urwid.Frame):
    def __init__(self):
        urwid.Frame.__init__(self, WorkspaceFrame())

class WorkspaceFrame(urwid.Frame):
    def __init__(self):
        urwid.Frame.__init__(self, TabbedFrame(NavigatorFrame("first")))

class TabbedFrame(urwid.Frame):
    def __init__(self, navigator_frame):
        urwid.Frame.__init__(self, navigator_frame, header=TabSet())
        self.__navigators = []
        self.__current_navigator_index = -1
        self.__add_navigator(navigator_frame)
        
    def keypress(self, size, key):
        if key == "t":
            navigator_name = str(random.randint(0, 100))
            self.__add_navigator(NavigatorFrame(navigator_name))
        elif key == "]":
            self.__next_navigator()
        elif key == "[":
            self.__prev_navigator()
        return urwid.Frame.keypress(self, size, key)
    
    def __add_navigator(self, navigator_frame):
        self.__navigators.append(navigator_frame)
        self.__current_navigator_index = len(self.__navigators) - 1
        
        self.header.add_tab(navigator_frame.caption)
         
        self.body = navigator_frame

    def __next_navigator(self):
        if self.__current_navigator_index < len(self.__navigators) - 1:
            self.__current_navigator_index += 1
            self.header.activate_tab(self.__current_navigator_index)
            self.body = self.__navigators[self.__current_navigator_index]

    def __prev_navigator(self):
        if self.__current_navigator_index > 0:
            self.__current_navigator_index -= 1
            self.header.activate_tab(self.__current_navigator_index)
            self.body = self.__navigators[self.__current_navigator_index]
            
class NavigatorFrame(urwid.Frame):
    def __init__(self, caption):
        self.__caption = caption
        urwid.Frame.__init__(self, urwid.Columns([urwid.LineBox(TabularNavigatorWidget(caption))]))
        
    @property
    def caption(self):
        return self.__caption

class TabularNavigatorWidget(urwid.ListBox):
    def __init__(self, text):
        urwid.ListBox.__init__(self, [urwid.Text(text)])
        
class TabSet(urwid.Columns):
    def __init__(self):
        urwid.Columns.__init__(self, [("pack", urwid.AttrMap(urwid.Text("|"), "tab_inactive"))])
        
    def add_tab(self, caption):
        self.contents.append((urwid.AttrMap(urwid.Text(caption), "tab_inactive"), self.options("pack")))
        self.contents.append((urwid.AttrMap(urwid.Text("|"), "tab_inactive"), self.options("pack")))
    
    def remove_tab(self, index):
        pass
    
    def activate_tab(self, index):
        for (attr_map, _) in self.contents:
            attr_map.set_attr_map({None: "tab_inactive"})
        (attr_map, _) = self.contents[index * 2 + 1]
        attr_map.set_attr_map({None: "tab_active"})
        
if __name__ == "__main__":
    main()
