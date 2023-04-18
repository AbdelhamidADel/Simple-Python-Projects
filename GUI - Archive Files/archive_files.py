import sys
import os
import zipfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget

class ArchiveApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Archive App')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.file_label = QLabel('No files selected')
        layout.addWidget(self.file_label)

        browse_button = QPushButton('Browse Files')
        browse_button.clicked.connect(self.browse_files)
        layout.addWidget(browse_button)

        archive_button = QPushButton('Create Archive')
        archive_button.clicked.connect(self.create_archive)
        layout.addWidget(archive_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.file_list = []

    def browse_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        files, _ = QFileDialog.getOpenFileNames(self, 'Select Files', '',
                                                'Images (*.png *.xpm *.jpg);;All Files (*)', options=options)
        if files:
            self.file_list = files
            self.file_label.setText(f'Selected {len(files)} files')
        else:
            self.file_label.setText('No files selected')

    def create_archive(self):
        if not self.file_list:
            self.file_label.setText('No files selected')
            return

        options = QFileDialog.Options()
        archive_name, _ = QFileDialog.getSaveFileName(self, 'Save Archive As', '',
                                                      'ZIP Archive (*.zip);;All Files (*)', options=options)
        if archive_name:
            if not archive_name.endswith('.zip'):
                archive_name += '.zip'

            with zipfile.ZipFile(archive_name, 'w') as archive:
                for file in self.file_list:
                    archive.write(file, os.path.basename(file))

            self.file_label.setText(f'Archive created: {archive_name}')
            self.file_list = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = ArchiveApp()
    main_win.show()
    sys.exit(app.exec_())