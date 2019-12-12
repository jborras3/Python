from DHCP import DHCP
from PC import PC

class so(object):

    def __init__(self, name, version, architecture, onlyCommands, caseSensitive, spaceRequeriment):
        self.name = name
        self.version = version
        self.architecture = architecture
        self.onlyCommands = onlyCommands
        self.caseSensitive = caseSensitive
        self.spaceRequeriment = spaceRequeriment

    def getName(self):
        return self.name

    def getVersion(self):
        return self.version

    def getArchitecture(self):
        return self.architecture

    def getOnlyCommands(self):
        return self.onlyCommands

    def getCaseSensitive(self):
        return self.caseSensitive

    def getSpaceRequeriment(self):
        return self.spaceRequeriment

    def setName(self, name):
        self.name=name

    def setVersion(self, version):
        self.version=version

    def setArchitecture(self, architecture):
        self.architecture=architecture

    def setOnlyCommands(self, onlyCommands):
        self.onlyCommands=onlyCommands

    def setCaseSensitive(self, caseSensitive):
        self.caseSensitive=caseSensitive

    def setSpaceRequeriment(self, spaceRequeriment):
        self.spaceRequeriment=spaceRequeriment