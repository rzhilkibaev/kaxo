import urwid

def main():
    FileManager().run()

class FileManager():
    def __init__(self):
        self.ui = UI()

    def run(self):
        self.ui.run()

class UI():
    def __init__(self):
        self.loop = urwid.MainLoop(MainFrame(), unhandled_input=self.on_input)

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
        urwid.Frame.__init__(self, TabFrame())

class TabFrame(urwid.Frame):
    def __init__(self):
        urwid.Frame.__init__(self, NavigatorFrame())

class NavigatorFrame(urwid.Frame):
    def __init__(self):
        urwid.Frame.__init__(self, urwid.Columns([urwid.LineBox(TabularNavigatorWidget())]))

class TabularNavigatorWidget(urwid.ListBox):
    def __init__(self):
        urwid.ListBox.__init__(self, [urwid.Text("file1"), urwid.Text("file2")])

if __name__ == "__main__":
    main()
