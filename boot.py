# Open Source Lighting Controller

# import necessary modules
import sys, tkinter, datetime, ctypes
import crystix.src.console.console as Console

# Start logic
print("clearing terminal for crystix... (hello there :p)"); print("\n" * 100)
ctypes.windll.kernel32.SetConsoleTitleW("Crystix control OnPC terminal")
Console.AsciiArt.PrintMoon(Console.AsciiArt)
print("> importing...", end="\r")
Break : bool = False

# import modules
import crystix.src.console.color as TextColor
import crystix.src.storage.showfile as ShowFileManager
import crystix.src.channel.dmxmanager as mdmx
import crystix.src.storage.states as st
import crystix.src.fixture.fixturemanager as fxm

# ask for Showfile
print("> importing... 100%")
print("> importing fixtures...    ", end="\r")

FixtureList = fxm.load_fixtures()
fxm.get_loaded_fixtures(FixtureList)

print("> importing fixtures... 100%")
print("> Starting Boot Process, select Showfile:")

# showfile logic
ShowFileName = ShowFileManager.ShowFile.ask(ShowFileManager.ShowFile)
ShowFileManager.ShowFile.read(ShowFileManager.ShowFile,ShowFileName)
if ShowFileManager.ShowFile.no_showfile_mode == False:
    try: ShowFileManager.ShowFile.process(ShowFileManager.ShowFile) 
    except: Break = True; print("> Error: Showfile not valid" + TextColor.reset)

# gui logic
print("> Starting WindowManager...", end='\r')
print("> Starting WindowManager... 100%")

# dmx logic
print("> Starting DMX Manager...", end='\r')
mdmx.initiateMasterUniverse()
print("> Starting DMX Manager... 100%")


import tkinter
import crystix.src.gui.button as btn

# For storing patch data
patched_fixtures = []

# Initialize Main Window
print("> Loading Gui (Windows)", end="\r")
MainWindow = tkinter.Tk()
MainWindow.title("CrystiX " + Console.Build.build)
MainWindow.geometry("1200x900")
MainWindow.resizable(0, 0)
print("> Loading Gui (Buttons)", end="\r")

# Open number pad window
# def open_numb_select_window():
#     NumberKeyWindow = tkinter.Tk()
#     NumberKeyWindow.title("Enter Number...")
#     NumberKeyWindow.geometry("500x600")
#     NumberKeyWindow.resizable(0, 0)

#     for i in range(1, 10):
#         btn_widget = tkinter.Button(NumberKeyWindow, text=str(i), width=10, height=5)
#         row = (i - 1) // 3
#         col = (i - 1) % 3
#         btn_widget.grid(row=row, column=col, padx=5, pady=5)

#     st.is_number_window_open = True
#     NumberKeyWindow.mainloop()

#btn.open_numb_callback = open_numb_select_window

# Add command prompt frame
cmd_frame = tkinter.Frame(MainWindow)
cmd_frame.pack(fill='x', padx=10, pady=10)

cmd_entry = tkinter.Entry(cmd_frame, width=100)
cmd_entry.pack(side='left', padx=5)

cmd_output = tkinter.Text(MainWindow, height=10, width=120)
cmd_output.pack(pady=5)

def run_command(event=None):
    command = cmd_entry.get().strip()
    cmd_entry.delete(0, 'end')
    
    if command.startswith("patch list"):
        cmd_output.insert('end', "Patched Fixtures:\n")
        for f in patched_fixtures:
            cmd_output.insert('end', f" - {f['fixture']} @ {f['channel']} on universe {f['universe']}\n")
        cmd_output.insert('end', "\n")
    elif command.startswith("patch "):
        parts = command.split()
        if len(parts) < 3:
            cmd_output.insert('end', "Invalid patch syntax. Use: patch <fixture> <channel> [universe]\n\n")
            return
        
        fixture = parts[1]
        try:
            channel = int(parts[2])
        except ValueError:
            cmd_output.insert('end', "Invalid channel. Must be a number.\n\n")
            return

        universe = int(parts[3]) if len(parts) > 3 else 1

        patched_fixtures.append({
            "fixture": fixture,
            "channel": channel,
            "universe": universe
        })

        cmd_output.insert('end', f"Patched {fixture} to channel {channel} on universe {universe}\n\n")
    else:
        cmd_output.insert('end', "Unknown command.\n\n")

    cmd_output.see('end')  # Auto-scroll to bottom

cmd_entry.bind("<Return>", run_command)

# ip of mc.originrealms.net/crystix: 192.168.178.136
# Layout buttons
buttons = [btn.EXIT, btn.COPY, btn.PSTE, btn.EXEC, btn.NEXT, btn.PREV, btn.ENTR, btn.NUMB]
buttons_management = [btn.SETUP, btn.FIXTURES, btn.OUTPUTS]

for idx, button in enumerate(buttons):
    row = idx // 3
    col = idx % 3
    button.grid(row=row, column=col, padx=0, pady=0)

for idx, button in enumerate(buttons_management):
    button.pack(padx=0, pady=0)

print("> Loading Gui 100%      ", end="\r")

MainWindow.mainloop()

