import tkinter

GeneralButtonConfig = {
    "width": 12,
    "height": 2,
}

open_numb_callback = None

button_frame = tkinter.Frame()
button_frame.pack(side="bottom", anchor="e", padx=10, pady=10)
button_frame_m = tkinter.Frame()
button_frame_m.pack(side="bottom", anchor="e", padx=10, pady=10)

EXIT = tkinter.Button(button_frame, text="EXIT", command=lambda: exit(), **GeneralButtonConfig)          # exit
COPY = tkinter.Button(button_frame,text="COPY", **GeneralButtonConfig)                                   # copy
PSTE = tkinter.Button(button_frame,text="PSTE", **GeneralButtonConfig)                                   # paste
EXEC = tkinter.Button(button_frame,text="EXEC", **GeneralButtonConfig)                                   # execute
NEXT = tkinter.Button(button_frame,text="NEXT", **GeneralButtonConfig)                                   # next
PREV = tkinter.Button(button_frame,text="PREV", **GeneralButtonConfig)                                   # previous
ENTR = tkinter.Button(button_frame,text="ENTR", **GeneralButtonConfig)                                                                          # enter
HGHL = tkinter.Button(button_frame,text="HGHL", **GeneralButtonConfig)                                                                          # highlight
NUMB = tkinter.Button(button_frame,text="NUMB", command=lambda: open_numb_callback(), **GeneralButtonConfig)                                    # number  key

SETUP = tkinter.Button(button_frame_m,text="SETUP", **GeneralButtonConfig)                                                                      # setup
FIXTURES = tkinter.Button(button_frame_m,text="FIXTURES", **GeneralButtonConfig)                                                                # fixtures
OUTPUTS = tkinter.Button(button_frame_m,text="OUTPUTS", **GeneralButtonConfig)                                                                  # outputs
