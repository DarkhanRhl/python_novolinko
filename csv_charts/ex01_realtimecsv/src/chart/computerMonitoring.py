
import psutil

class ComputerMonitoring:

    def getInformations(self):
        infos = [psutil.cpu_percent(), psutil.virtual_memory()[2]]
        return infos

    def handler(self):
        return self.getInformations()