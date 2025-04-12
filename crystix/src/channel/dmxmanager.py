MasterUniverse = []

def initiateMasterUniverse():
    for i in range(1, 512):
        MasterUniverse.append(0)
    import crystix.src.console.color as TextColor
    print(TextColor.green + "> Master Universe initiated")