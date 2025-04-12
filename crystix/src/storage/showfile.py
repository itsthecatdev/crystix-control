class ShowFile:
    storage = "crystix/showfile/"
    DataAll = []
    DataFixtures = []
    DataOutputs = []
    DataMisc = []
    no_showfile_mode = False
    def read(self,filename):

        # import TextColor for console formatting
        import crystix.src.console.color as TextColor
        if filename.endswith("."):
            print(TextColor.green + "> Booting without Showfile! [THERE WILL BE CRASHES]")
            self.no_showfile_mode = True
            return
        
        # log
        print("> Reading " + self.storage+filename)

        # try open the requested showfile
        try: 
            with open(self.storage+filename, "r") as f:
                content = f.read()
        except: 
            print(TextColor.red + "> Error: File not found, File corrupted or empty")
            return FileNotFoundError("File not found, File corrupted or empty")
        self.DataAll = content
        if filename.endswith(".cshw"):
            print(TextColor.green + "> Showfile successfully read")
        elif filename.endswith(".show"):
            print(TextColor.green + "> Showfile successfully read [experimental mode]")

    def process(self):
        import crystix.src.console.color as TextColor

        # log 
        print("> Processing Showfile...")

        # process the showfile
        d = self.DataAll
        d.split(";section;") 
        self.DataFixtures = d[0]
        self.DataOutputs = d[1]
        self.DataMisc = d[2]
        print(TextColor.green + "> Showfile successfully processed")
    
    # ask user for showfile
    def ask(self):
        import crystix.src.console.color as TextColor
        e = input(TextColor.pink + "Show File to load: "+ TextColor.yellow); return e
    
    # save showfile
    def save(self):
        import crystix.src.console.color as TextColor
        print(TextColor.green + "> Showfile successfully saved") # print since theres no logic yet