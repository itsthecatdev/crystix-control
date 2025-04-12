class Build:
    build = "com.github.shxcat.crystix:main:0.1-SNAPSHOT"
    version = "0.1-SNAPSHOT"
    branch = "main"

class commands:
    CMD_exit = ['exit', 'close', 'kill all', 'kill *']

class ConsoleManager:                                                                           # this is not the cmd window!!!
    def send(self,text):
        body = text.lower()
        for cmd in commands.CMD_exit:
            if cmd in body:
                import crystix.src.console.color as TextColor
                print(TextColor.green + "> Closing Crystix...")
                exit()

# ascii
class AsciiArt:
    Raw_Moon = ["⠀⠀⠀⠀⠀⠀⢀⡤⠂",                                                                # https://emojicombos.com/moon-ascii-art
            "⠀⠀⠀⠀⢀⣴⡿⠁",
            "⠀⠀⢀⣴⣿⡿⠁",
            "⠀⢀⣾⣿⣿⡇",
            "⠀⣼⣿⣿⣿⠀",
            "⢰⣿⣿⣿⣿⡀",
            "⢸⣿⣿⣿⣿⡇",
            "⢸⣿⣿⣿⣿⣿⡀",
            "⢸⣿⣿⣿⣿⣿⣷⡀",
            "⠀⢿⣿⣿⣿⣿⣿⣿⣆",
            "⠀⠘⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀",
            "⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣀⣀⣀⣀⣠⣤⣴⣶⣾⣿⠋",
            "⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁",
            "⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠿⠿⠟⠛⠋⠁",
            "crystiX controll OnPC by shxcat"]
    def PrintMoon(self):
        print("\n" * 5)
        for i in self.Raw_Moon:
            print("             "+i)
        print("\n" * 5)