import liwc from C:\Users\orko\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages'

parse, category_names = liwc.load_token_parser("../LIWC2007_Portugues_win.dic")

class TokenManipulator:
    def __init__(self):
        self.posemo = 0
        self.negemo = 0
        self.anx = 0
        self.swear = 0


    def getPosemo(self):
        return self.posemo

    def setPosemo(self, newPosemo):
        self.posemo = newPosemo

    def getNegemo(self):
        return self.negemo

    def setNegemo(self, newNegemo):
        self.negemo = newNegemo

    def getAnx(self):
        return self.anx

    def setAnx(self, newAnx):
        self.anx = newAnx

    def getSwear(self):
        return self.swear

    def setSwear(self, newSwear):
        self.swear = newSwear

    def calculateLIWC(self, text):
        tokens = text

        for p in tokens:
            resp = list(parse(p))

            if resp != []:  # Verifica se a palavra existe no liwc
                if "swear" in resp:
                    self.setSwear(self.getSwear() + 1)
                if "anx" in resp:
                    self.setAnx(self.getAnx() + 1)
                if "posemo" in resp:
                    self.setPosemo(self.getPosemo() + 1)
                if "negemo" in resp:
                    self.setNegemo(self.getNegemo() + 1)
