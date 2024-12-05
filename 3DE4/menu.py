eqFolder = os.path.dirname(__file__).replace('\\','/')+f'/Nuke{nuke.NUKE_VERSION_MAJOR}.{nuke.NUKE_VERSION_MINOR}'
if os.path.isdir(eqFolder):
    lst = [file for file in os.listdir(eqFolder) if file.endswith('.dll')]
    if lst:
        eqMenu = nuke.menu('Nodes').addMenu('3DE4',icon='3DE4.png')
        for file in lst:
            name = os.path.splitext(file)[0]
            eqMenu.addCommand(name,f"nuke.createNode('{name}')")