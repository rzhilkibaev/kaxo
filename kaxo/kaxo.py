import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))
    
def create_panel_container():
    pass
    
txt = urwid.Text("Hello")
fill = urwid.Filler(txt, urwid.MIDDLE)
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()
