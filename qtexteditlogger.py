from PySide6 import QtCore, QtWidgets
import logging

class QTextEditLogger(logging.Handler, QtWidgets.QPlainTextEdit):
    '''Custom widget to display application log.
    Taken from here: https://stackoverflow.com/a/75149586'''
    class Emitter(QtCore.QObject):
        log = QtCore.Signal(str)

    def __init__(self, parent):
        super().__init__()
        QtWidgets.QPlainTextEdit.__init__(self, parent)
        self.setReadOnly(True)
        self.emitter = QTextEditLogger.Emitter()
        self.emitter.log.connect(self.addText)

    def addText(self, text: str):
        self.appendPlainText(text)
        # TODO: add setting or checkbox for autoscroll
        self.ensureCursorVisible()  # scroll to end of log

    def emit(self, record):
        msg = self.format(record)
        self.emitter.log.emit(msg)