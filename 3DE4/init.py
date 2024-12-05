eqFolder = os.path.dirname(__file__).replace('\\','/')+f'/Nuke{nuke.NUKE_VERSION_MAJOR}.{nuke.NUKE_VERSION_MINOR}'
if os.path.isdir(eqFolder):
	nuke.pluginAddPath(eqFolder)