from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
from scapy.all import*
from scapy.sendrecv import *
import sys
import project
import design

pck = []
pck2 = []
filtr = ''
inface = ''
counter = 0

class snThread(QThread):
    def __init__(self, ftr):
        QThread.__init__(self)
        self.ftr = ftr

    def __del__(self):
        self.wait()

    def snFn(self, ftr):
        global pck
        global inface
        if inface == 'All Network Interfaces':
            p = sniff(count=1)
        else:
            p = sniff(count=1, iface=inface)
        pck.append(p[0])
        return project.get_info(p[0])

    def run(self):
        global filtr
        while 1:
            x = self.snFn(filtr)
            self.emit(SIGNAL('add_pct(int)'), 1)

class Sniffer(QtGui.QDialog, design.Ui_Dialog):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btn_start.clicked.connect(self.starter)
        self.tbl.cellClicked.connect(self.handleCellClicked)
        self.btn_save.setEnabled(False)
        self.btn_save.clicked.connect(self.saver)
        self.btn_apply.clicked.connect(self.applyer)
        ifaces = project.get_interfaces()
        self.combo.addItem('All Network Interfaces')
        for i in range(len(ifaces)):
            self.combo.addItem(ifaces[i])
        self.combo.activated[str].connect(self.selector)
        
    def selector(self, text):
        global inface
        inface = text
        
    def starter(self):
        global filtr
        self.sn_thread = snThread(filtr)
        self.connect(self.sn_thread, SIGNAL("add_pct(int)"), self.printer)
        self.sn_thread.start()
        self.btn_stop.setEnabled(True)
        self.btn_start.setEnabled(False)
        self.in_fltr.setEnabled(False)
        self.btn_save.setEnabled(True)
        self.btn_apply.setEnabled(False)
        self.btn_stop.clicked.connect(self.stopper)

    def printer(self, pct_text):
        global pck
        global pck2
        global filtr
        global counter
        todisp = project.get_info(pck[counter]) 
        if (filtr == '' or filtr == str(todisp[3])):
            rowPosition = self.tbl.rowCount()
            pck2.append(pck[counter])
            self.tbl.insertRow(rowPosition)
            self.tbl.setItem(rowPosition,0, QtGui.QTableWidgetItem(str(todisp[0])))
            self.tbl.setItem(rowPosition,1, QtGui.QTableWidgetItem(str(todisp[1])))
            self.tbl.setItem(rowPosition,2, QtGui.QTableWidgetItem(str(todisp[2])))
            self.tbl.setItem(rowPosition,3, QtGui.QTableWidgetItem(str(todisp[3])))
            self.tbl.setItem(rowPosition,4, QtGui.QTableWidgetItem(str(todisp[4])))
        counter += 1

        
    def stopper(self):
        self.btn_stop.setEnabled(False)
        self.btn_apply.setEnabled(True)
        self.btn_start.setEnabled(True)
        self.in_fltr.setEnabled(True)
        self.sn_thread.terminate()

    def applyer(self):
        global filtr
        filtr = self.in_fltr.text()
        if len(pck) == 0:
            return
        else:
            global pck2
            pck2 = []
            self.tbl.setRowCount(0)
            for i in range (0,len(pck)):
                global counter
                counter = i
                self.printer(0)
            
    def handleCellClicked (self, row, col):
        global pck
        pcktxt = project.display_packetdata(pck[row])
        self.txt.setText(pcktxt)
        pckhex = project.get_hexa(pck[row])
        self.hexa.setText(pckhex)

    def saver(self):
        global pck
        global pck2
        if len(pck2) == 0:
            project.save(pck)
        else:
            project.save(pck2)

def main():
    app = QtGui.QApplication(sys.argv)
    form = Sniffer()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()