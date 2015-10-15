import urwid

def on_input(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
#     txt.set_text(repr(key))
    
def ls():
    return ["file1", "file2", "file3"]
    
    
textList = []
for fileName in ls():
    textList.append(urwid.Text(fileName))
    
file_list = urwid.ListBox(textList)

body = urwid.Columns([urwid.LineBox(file_list)])
mainPanel = urwid.Frame(body, header=urwid.Text("header"), footer=urwid.Text("footer"))
loop = urwid.MainLoop(mainPanel, unhandled_input=on_input)
loop.run()
