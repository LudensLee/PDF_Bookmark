from PyPDF2 import PdfFileReader ,PdfFileWriter
import os
import json
import argparse
import sys

class ReAct:
    def __init__(self):
        self.FileName = ""
        self.Contens = ""



    def add(self,strFileName,strOutputName,strContentsPath):
        with open(strContentsPath, "r") as f:
            self.Contens = json.load(f)
        self.FileName = strFileName
        self.output = PdfFileWriter()
        self.input = PdfFileReader(open(self.FileName, 'rb'), strict=False)
        print "the PDF Pages Num is {}".format(self.input.getNumPages())
        for i in range(0,self.input.getNumPages()):
            self.output.addPage(self.input.getPage(i))
            vaule = self.Contens.get("Content")[str(i+1)]
            self.output.addBookmark("{}.{}".format(i+1,vaule), i)
            self.output.write(open(strOutputName, 'wb'))

if __name__ == '__main__':
    pass