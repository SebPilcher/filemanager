import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QModelIndex

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



        self.tree.setColumnWidth(0, 300)


        layout = QVBoxLayout()
        layout.addWidget(self.tree)


        self.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)


    demo = FileSystemView(".")
    demo.show()

    sys.exit(app.exec_())