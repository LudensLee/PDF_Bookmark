from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog
from AddContens import Ui_Form
from Execute import ReAct
import os

class MyWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


        self.Select.clicked.connect(self.SelectPdfPath)
        self.Contens.clicked.connect(self.SelectContensPath)
        self.Start.clicked.connect(self.Add)
        self.PdfPath = ""
        self.PdfFileType = ""
        self.ConPath = ""
        self.ConFileType = ""
        self.FilePath.setDisabled(True)
        self.ContensPath.setDisabled(True)
        self.execute = ReAct()
        self.setWindowTitle("PDF Add Bookmark v1.0")
    def SelectPdfPath(self):

        self.PdfPath, self.PdfFileType = QFileDialog.getOpenFileNames(self,
                                                  "select",
                                                  "./",
                                                  "Pdf Files (*.pdf)")
        print(self.PdfPath, self.PdfFileType)
        if self.PdfPath !=[]:
            self.FilePath.setText((self.PdfPath)[0])
            self.PutPath.setText((self.PdfPath)[0])
            dirname, filename = os.path.split(os.path.abspath((self.PdfPath)[0]))
            print "the path :{}".format(dirname)
            os.chdir(dirname)

    def SelectContensPath(self):

        self.ConPath, self.ConFileType = QFileDialog.getOpenFileNames(self,
                                                  "select",
                                                  "./",
                                                  "Json Files (*.json)")
        print(self.ConPath, self.ConFileType)
        if self.ConPath !=[]:
            self.ContensPath.setText((self.ConPath)[0])
            dirname, filename = os.path.split(os.path.abspath((self.ConPath)[0]))
            print "the path :{}".format(dirname)
            os.chdir(dirname)



    def Add(self):
        OutputPath = self.PutPath.text()
        ContensPath = self.ContensPath.text()
        print OutputPath
        if ContensPath !="":
            if (self.PdfPath)[0] == OutputPath:
                QtWidgets.QMessageBox.warning(self, "", "The Output file name is same as the input file name",
                                                         QtWidgets.QMessageBox.Cancel)
            else:
                self.execute.add((self.PdfPath)[0], OutputPath,(self.ConPath)[0])
        else:
            QtWidgets.QMessageBox.warning(self, "", "Please select the Contnes Config",
                                          QtWidgets.QMessageBox.Cancel)







from PySide2.QtWidgets import QApplication
import  sys


class cApp(QApplication):
    def __init__(self):
        super(cApp, self).__init__(sys.argv)
        self.objMainWindow = MyWindow()
        self.objMainWindow.show()
    def Start(self):
        sys.exit(self.exec_())





if __name__ == '__main__':
    objApp = cApp()
    objApp.Start()






