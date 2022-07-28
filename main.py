from genericpath import isdir
import os
from send2trash import send2trash
from pickle import TRUE
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QHBoxLayout
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QKeySequence

class FileSystemView(QWidget):
    def __init__(self, path_str):
        super().__init__()

        appWidth = 800
        appHeight = 400

        self.setWindowTitle('File Manager')
        self.setGeometry(300,300,appWidth,appHeight)

        path = Path(path_str)

        self.model = QFileSystemModel()
        self.model.setRootPath("")

        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.expand(self.model.index(path.as_posix()))
        self.tree.expandAll()

        self.tree.selectionModel().currentChanged.connect(self.currentChanged)
        self.tree.doubleClicked.connect(self.doubleClicked)

        self.tree.setColumnWidth(0, 300)

        self.preview = PreviewPanel()



        layout = QHBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.preview)


        self.setLayout(layout)

    def currentChanged(self, index):
        if not self.model.isDir(index):
            self.preview.displayPreview(self.model.filePath(index))
            
        

    def doubleClicked(self, signal):
        index = self.tree.currentIndex()

        if not self.model.isDir(index):
            os.startfile(self.model.filePath(index))

    def keyPressEvent(self, event):
        index = self.tree.currentIndex()


        if event == QKeySequence.StandardKey.InsertParagraphSeparator:
            if self.model.isDir(index):
                self.tree.expand(index)
            else:
                os.startfile(self.model.filePath(index))
        if event == QKeySequence.StandardKey.Delete:
            file_path = self.model.filePath(index)
            file_path = file_path.replace("/","\\")
            send2trash(file_path)

        


class PreviewPanel(QWidget):
    def __init__(self):
        super().__init__()


    def displayPreview(self, path):
        # display preview of path
        pass





if __name__ == '__main__':
    app = QApplication(sys.argv)


    demo = FileSystemView(".")
    demo.show()

    sys.exit(app.exec_())