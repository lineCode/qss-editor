import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSlot
from style import style_sheet
from style import about_window_stylesheet
from style import find_window_stylesheet
import webbrowser


cs = False
wwo = False
find_text = ''


class FindWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(785, 440, 350, 130)
        self.setFixedSize(350, 130)
        self.setWindowTitle('Find and Replace')
        self.setWindowIcon(QtGui.QIcon('icon_pencil.png'))
        self.setStyleSheet(find_window_stylesheet)

        self.label_find = QtWidgets.QLabel('Find:', self)
        self.label_find.setGeometry(10, 15, 50, 22)

        self.label_replace = QtWidgets.QLabel('Replace with:', self)
        self.label_replace.setGeometry(10, 42, 100, 22)

        self.line_edit_find = QtWidgets.QLineEdit(self)
        self.line_edit_find.setGeometry(90, 15, 150, 20)

        self.line_edit_replace = QtWidgets.QLineEdit(self)
        self.line_edit_replace.setGeometry(90, 42, 150, 20)

        self.button_find = QtWidgets.QPushButton("Find", self)
        self.button_find.setGeometry(260, 14, 80, 22)

        self.button_replace = QtWidgets.QPushButton("Replace", self)
        self.button_replace.setGeometry(260, 41, 80, 22)

        self.button_replace_all = QtWidgets.QPushButton("Replace All", self)
        self.button_replace_all.setGeometry(260, 68, 80, 22)

        self.button_close = QtWidgets.QPushButton("Close", self)
        self.button_close.setGeometry(260, 95, 80, 22)
        self.button_close.clicked.connect(self.close_find_win)

        self.case_sensitive = QtWidgets.QCheckBox('Case sensitive', self)
        self.case_sensitive.setGeometry(90, 72, 100, 20)
        self.case_sensitive.stateChanged.connect(self.cs)

        self.whole_words = QtWidgets.QCheckBox('Whole words only', self)
        self.whole_words.setGeometry(90, 95, 150, 20)
        self.whole_words.stateChanged.connect(self.wwo)

    def cs(self, state):
        global cs

        if state == QtCore.Qt.Checked:
            cs = True
        else:
            cs = False

    def wwo(self, state):
        global wwo

        if state == QtCore.Qt.Checked:
            wwo = True
        else:
            wwo = False

    def close_find_win(self):
        self.hide()


class AboutWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(825, 410, 270, 225)
        self.setWindowIcon(QtGui.QIcon('icon_pencil.png'))
        self.setWindowTitle('About QSS Editor++')
        self.setMinimumSize(270, 225)
        self.setFixedSize(270, 225)
        self.setModal(True)
        self.setStyleSheet(about_window_stylesheet)

        font1 = QtGui.QFont()
        font1.setPointSize(10)

        label_header = QtWidgets.QLabel('<html><b>QSS Editor++ 1.0.2</b</html>', self)
        label_header.setGeometry(30, 10, 200, 30)
        label_header.setFont(font1)
        label_header.show()

        label_description = QtWidgets.QLabel('QSS Editor++  is a tool to edit and preview \nQt stylesheets. '
                                             'It contains 30 of the most \ncommon '
                                             'Qt widgets in various states.', self)
        label_description.setGeometry(30, 45, 300, 40)
        label_description.show()

        label_instruction = QtWidgets.QLabel('You can either open an existing stylesheet to\n'
                                             'edit and preview or write one from scratch. \n'
                                             "To apply changes to the preview widgets \n"
                                             "simply press 'Ctrl+ Enter' or click 'Apply', \n"
                                             "located in the 'View' section of the menu bar.", self)
        label_instruction.setGeometry(30, 95, 300, 70)
        label_instruction.show()

        label_copyright = QtWidgets.QLabel('(C) 2019 Niklas Henning', self)
        label_copyright.setGeometry(30, 173, 150, 20)
        label_copyright.show()


class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywords_settings = ['\\bbackground\\b', '\\bbackground-color\\b', '\\bselection-background-color\\b',
                             '\\bmargin\\b', '\\bpadding\\b', '\\bpadding-left\\b', '\\bpadding-right\\b',
                             '\\bpadding-top\\b', '\\bpadding-bottom\\b', '\\bborder\\b', '\\bborder-style\\b',
                             '\\bborder-color\\b', '\\bborder-radius\\b', '\\bborder-width\\b', '\\bfont-size\\b',
                             '\\bopacity\\b', '\\bimage\\b', '\\bmin-height\\b', '\\bheight\\b',
                             '\\bsubcontrol-position\\b', '\\bsubcontrol-origin\\b', '\\bwidth\\b', '\\bheight\\b',
                             '\\btext-align\\b', '\\bspacing\\b', '\\bmargin-left\\b', '\\bmargin-right\\b',
                             '\\bmargin-top\\b', '\\bmargin-bottom\\b', '\\bborder-bottom-style\\b', '\\btop\\b',
                             '\\bborder-top-left-radius\\b', '\\bborder-top-right-radius\\b', '\\bcolor\\b',
                             '\\bgridline-color\\b', '\\bbottom\\b', '\\bleft\\b', '\\bright\\b',
                             '\\balternate-background-color\\b', '\\bselection-color\\b',
                             '\\bshow-decoration-selected\\b', '\\bposition\\b', '\\bmin-width\\b',
                             '\\bmessagebox-text-interaction-flags\\b', '\\blineedit-password-character\\b',
                             '\\bfont\\b', '\\bbutton-layout\\b', '\\boutline\\b', '\\bbtitlebar-normal-icon\\b',
                             '\\btitlebar-close-icon\\b', '\\bqproperty-drawBase\\b', '\\btitlebar-normal-icon\\b',
                             '\\bdisplay\\b', '\\bpaint-alternating-row-colors-for-empty-area\\b', '\\bicon-size\\b',
                             '\\bstop\\b', '\\bmessagebox-warning-icon\\b', '\\bmessagebox-question-icon\\b',
                             '\\bmessagebox-information-icon\\b', '\\bmessagebox-critical-icon\\b']

        keywords_settings_format = QtGui.QTextCharFormat()
        keywords_settings_format.setForeground(Qt.blue)

        self.highlightingRules = [(QtCore.QRegExp(pattern), keywords_settings_format)
                for pattern in keywords_settings]

        Q_format = QtGui.QTextCharFormat()
        Q_format.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QtCore.QRegExp("\\bQ[A-Za-z]+\\b"), Q_format))

        exceptions_format = QtGui.QTextCharFormat()
        exceptions_format.setForeground(Qt.black)
        self.highlightingRules.append((QtCore.QRegExp('\\bQLinearGradient\\b'), exceptions_format))

        single_line_comment_format = QtGui.QTextCharFormat()
        single_line_comment_format.setForeground(Qt.gray)
        self.highlightingRules.append((QtCore.QRegExp("//[^\n]*"), single_line_comment_format))

        colon_format = QtGui.QTextCharFormat()
        colon_format.setForeground(Qt.darkBlue)
        self.highlightingRules.append((QtCore.QRegExp('\\:[A-Za-z-!]+\\b'), colon_format))

        double_colon_format = QtGui.QTextCharFormat()
        double_colon_format.setForeground(Qt.darkBlue)
        self.highlightingRules.append((QtCore.QRegExp('\\::[A-Za-z-]+\\b'), double_colon_format))

        colon_space_format = QtGui.QTextCharFormat()
        colon_space_format.setForeground(Qt.black)
        self.highlightingRules.append((QtCore.QRegExp('\\: [A-Za-z-! ]+\\b'), colon_space_format))

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.gray)

        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)


class NumberBar(QtWidgets.QWidget):
    def __init__(self, editor):
        QtWidgets.QWidget.__init__(self, editor)

        self.editor = editor
        self.editor.blockCountChanged.connect(self.updateWidth)
        self.editor.updateRequest.connect(self.updateContents)
        self.font = QtGui.QFont()
        self.numberBarColor = QtGui.QColor("#DCDCDC")

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.fillRect(event.rect(), self.numberBarColor)

        block = self.editor.firstVisibleBlock()

        # Iterate over all visible text blocks in the document.
        while block.isValid():
            blockNumber = block.blockNumber()
            block_top = self.editor.blockBoundingGeometry(block).translated(self.editor.contentOffset()).top()

            # Check if the position of the block is out side of the visible area.
            if not block.isVisible() or block_top >= event.rect().bottom():
                break

            # We want the line number for the selected line to be bold.
            if blockNumber == self.editor.textCursor().blockNumber():
                self.font.setBold(False)
                painter.setPen(QtGui.QColor("#000000"))
            else:
                self.font.setBold(False)
                painter.setPen(QtGui.QColor("#000000"))
            painter.setFont(self.font)

            # Draw the line number right justified at the position of the line.
            paint_rect = QtCore.QRect(0, block_top, self.width(), self.editor.fontMetrics().height())
            painter.drawText(paint_rect, Qt.AlignRight, str(blockNumber + 1))

            block = block.next()

        painter.end()

        QtWidgets.QWidget.paintEvent(self, event)

    def getWidth(self):
        width = 40
        return width

    def updateWidth(self):
        width = self.getWidth()
        if self.width() != width:
            self.setFixedWidth(width)
            self.editor.setViewportMargins(width, 0, 0, 0)

    def updateContents(self, rect, scroll):
        if scroll:
            self.scroll(0, scroll)
        else:
            self.update(0, rect.y(), self.width(), rect.height())

        if rect.contains(self.editor.viewport().rect()):
            fontSize = self.editor.currentCharFormat().font().pointSize()
            self.font.setPointSize(10)
            self.font.setStyle(QtGui.QFont.StyleNormal)
            self.updateWidth()


class TextEditor(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        QtWidgets.QPlainTextEdit.__init__(self, parent)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.highlightCurrentLine()

    @pyqtSlot()
    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QtWidgets.QTextEdit.ExtraSelection()
            lineColor = QtGui.QColor(Qt.lightGray).lighter(115)
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSS Editor++')
        self.setGeometry(0, 0, 1920, 1080)
        self.setMinimumSize(1920, 1080)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon('icon_pencil.png'))
        self.setCursor(Qt.ArrowCursor)
        self.current_file = ''

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        view_menu = menubar.addMenu('View')
        help_menu = menubar.addMenu('Help')

        open_action = QtWidgets.QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file2)
        self.text_open = ''
        self.file_name = ''

        save_action = QtWidgets.QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)

        save_as_action = QtWidgets.QAction('Save as...', self)
        save_as_action.setShortcut('Shift+Ctrl+S')
        save_as_action.triggered.connect(self.save_as_file)

        undo_action = QtWidgets.QAction('Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.undo)

        redo_action = QtWidgets.QAction('Redo', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.redo)

        separator = QtWidgets.QAction('separator', self)
        separator.setSeparator(True)

        copy_action = QtWidgets.QAction('Copy', self)
        copy_action.triggered.connect(self.copy_text)
        copy_action.setShortcut('Ctrl+C')

        paste_action = QtWidgets.QAction('Paste', self)
        paste_action.triggered.connect(self.paste_text)
        paste_action.setShortcut('Ctrl+V')

        cut_action = QtWidgets.QAction('Cut', self)
        cut_action.triggered.connect(self.cut_text)

        clear_action = QtWidgets.QAction('Clear', self)
        clear_action.triggered.connect(self.clear_text_edit)

        minimize_action = QtWidgets.QAction('Minimize', self)
        minimize_action.triggered.connect(self.minimize_win)

        maximize_action = QtWidgets.QAction('Maximize', self)
        maximize_action.triggered.connect(self.maximize_win)

        separator2 = QtWidgets.QAction('separator', self)
        separator2.setSeparator(True)

        preview_action = QtWidgets.QAction('Apply', self)
        preview_action.setShortcut('Ctrl+Return')
        preview_action.triggered.connect(self.preview)

        find_action = QtWidgets.QAction('Find', self)
        find_action.setShortcut('Ctrl+F')
        find_action.triggered.connect(self.find_)

        about_qt_action = QtWidgets.QAction('About Qt', self)
        about_qt_action.triggered.connect(self.about_qt)

        about_qss_action = QtWidgets.QAction('About QSS Editor++', self)
        about_qss_action.triggered.connect(self.about_qss_editor)

        changelog_action = QtWidgets.QAction('View changelog', self)
        changelog_action.triggered.connect(self.open_changelog)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addAction(separator)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(cut_action)
        view_menu.addAction(minimize_action)
        view_menu.addAction(maximize_action)
        view_menu.addAction(separator2)
        view_menu.addAction(find_action)
        view_menu.addAction(preview_action)
        help_menu.addAction(about_qt_action)
        help_menu.addAction(about_qss_action)
        help_menu.addAction(changelog_action)

        self.line_display = QtWidgets.QTextEdit(self)
        self.line_display.setObjectName('line_display')
        self.line_display.setGeometry(10, 35, 1049, 970)
        self.line_display.setReadOnly(True)
        self.line_display.show()

        self.text_edit = TextEditor(self)
        self.text_edit.setObjectName('text_edit')
        self.text_edit.setGeometry(11, 36, 1047, 968)
        self.text_edit.setTabStopDistance(16)
        self.text_edit.show()
        self.text_edit.setFocus()

        self.syntax_highlighter = Highlighter(self.text_edit.document())

        self.preview_area = QtWidgets.QWidget(self)
        self.preview_area.setObjectName('preview_area')
        self.preview_area.setGeometry(1080, 35, 825, 970)
        self.preview_area.show()

        self.number_bar = NumberBar(self.text_edit)
        self.number_bar.setObjectName('number_bar')
        self.number_bar.setGeometry(0, 0, 50, 968)
        self.number_bar.show()

        self.number_bar_extension = QtWidgets.QWidget(self)
        self.number_bar_extension.setObjectName('number_bar_extension')
        self.number_bar_extension.setGeometry(51, 36, 4, 968)
        self.number_bar_extension.show()

        # Button Widgets

        self.button_group = QtWidgets.QGroupBox('Buttons', self)
        self.button_group.setGeometry(1106, 50, 780, 95)
        self.button_group.show()

        self.pushbutton1 = QtWidgets.QPushButton('PushButton', self)
        self.pushbutton1.setGeometry(1125, 72, 120, 25)
        self.pushbutton1.show()

        self.pushbutton2 = QtWidgets.QPushButton('Disabled PushButton', self)
        self.pushbutton2.setGeometry(1125, 105, 120, 25)
        self.pushbutton2.setDisabled(True)
        self.pushbutton2.show()

        self.toolbutton1 = QtWidgets.QToolButton(self)
        self.toolbutton1.setText('ToolButton')
        self.toolbutton1.setGeometry(1270, 72, 120, 25)
        self.toolbutton1.show()

        self.toolbutton2 = QtWidgets.QToolButton(self)
        self.toolbutton2.setText('Disabled ToolButton')
        self.toolbutton2.setGeometry(1270, 105, 120, 25)
        self.toolbutton2.setDisabled(True)
        self.toolbutton2.show()

        self.checkbox1 = QtWidgets.QCheckBox('CheckBox', self)
        self.checkbox1.setGeometry(1410, 73, 120, 20)
        self.checkbox1.setChecked(True)
        self.checkbox1.show()

        self.checkbox2 = QtWidgets.QCheckBox('Tristate CheckBox', self)
        self.checkbox2.setGeometry(1410, 92, 120, 20)
        self.checkbox2.setCheckState(Qt.PartiallyChecked)
        self.checkbox2.setTristate(True)
        self.checkbox2.show()

        self.checkbox3 = QtWidgets.QCheckBox('Disabled CheckBox', self)
        self.checkbox3.setGeometry(1410, 111, 120, 20)
        self.checkbox3.setChecked(True)
        self.checkbox3.setDisabled(True)
        self.checkbox3.show()

        self.radiobutton1 = QtWidgets.QRadioButton('Radiobutton', self)
        self.radiobutton1.setGeometry(1540, 73, 120, 20)
        self.radiobutton1.show()

        self.radiobutton2 = QtWidgets.QRadioButton('Radiobutton', self)
        self.radiobutton2.setGeometry(1540, 92, 120, 20)
        self.radiobutton2.show()

        self.radiobutton3 = QtWidgets.QRadioButton('Disabled Radiobutton', self)
        self.radiobutton3.setGeometry(1540, 111, 120, 20)
        self.radiobutton3.setDisabled(True)
        self.radiobutton3.setChecked(True)
        self.radiobutton3.show()

        self.command_link_button2 = QtWidgets.QCommandLinkButton(' Disabled CommandLinkButton', self)
        self.command_link_button2.setGeometry(1670, 101, 210, 40)
        self.command_link_button2.setDisabled(True)
        self.command_link_button2.show()

        self.command_link_button1 = QtWidgets.QCommandLinkButton(' Enabled CommandLinkButton', self)
        self.command_link_button1.setGeometry(1670, 61, 210, 40)
        self.command_link_button1.show()

        # Input Widgets

        self.input_group = QtWidgets.QGroupBox('Input Widgets', self)
        self.input_group.setGeometry(1106, 155, 780, 258)
        self.input_group.show()

        self.combobox1 = QtWidgets.QComboBox(self)
        self.combobox1.setGeometry(1125, 180, 100, 22)
        self.combobox1.addItem('Item 1')
        self.combobox1.addItem('Item 2')
        self.combobox1.addItem('Item 3')
        self.combobox1.show()

        self.combobox2 = QtWidgets.QComboBox(self)
        self.combobox2.setGeometry(1125, 212, 100, 22)
        self.combobox2.setDisabled(True)
        self.combobox2.addItem('Disabled row')
        self.combobox2.addItem('Item 1')
        self.combobox2.addItem('Item 2')
        self.combobox2.addItem('Item 3')
        self.combobox2.show()

        self.combobox3 = QtWidgets.QComboBox(self)
        self.combobox3.setGeometry(1125, 244, 100, 22)
        self.combobox3.setEditable(True)
        self.combobox3.addItem('Item 1')
        self.combobox3.addItem('Item 2')
        self.combobox3.addItem('Item 3')
        self.combobox3.show()

        self.combobox4 = QtWidgets.QComboBox(self)
        self.combobox4.setGeometry(1125, 276, 100, 22)
        self.combobox4.setEditable(True)
        self.combobox4.setDisabled(True)
        self.combobox4.addItem('Disabled row')
        self.combobox4.addItem('Item 1')
        self.combobox4.addItem('Item 2')
        self.combobox4.addItem('Item 3')
        self.combobox4.show()

        self.datetime_edit1 = QtWidgets.QDateTimeEdit(self)
        self.datetime_edit1.setGeometry(1245, 180, 150, 22)
        self.datetime_edit1.show()

        self.datetime_edit2 = QtWidgets.QDateTimeEdit(self)
        self.datetime_edit2.setGeometry(1245, 212, 150, 22)
        self.datetime_edit2.setDisabled(True)
        self.datetime_edit2.show()

        self.font_box1 = QtWidgets.QFontComboBox(self)
        self.font_box1.setGeometry(1245, 244, 150, 22)
        self.font_box1.show()

        self.font_box2 = QtWidgets.QFontComboBox(self)
        self.font_box2.setGeometry(1245, 276, 150, 22)
        self.font_box2.setDisabled(True)
        self.font_box2.show()

        self.shortcut1 = QtWidgets.QKeySequenceEdit(self)
        self.shortcut1.setGeometry(1415, 180, 145, 22)
        self.shortcut1.show()

        self.shortcut2 = QtWidgets.QKeySequenceEdit(self)
        self.shortcut2.setGeometry(1415, 212, 145, 22)
        self.shortcut2.setDisabled(True)
        self.shortcut2.show()

        self.line_edit1 = QtWidgets.QLineEdit('Line Edit', self)
        self.line_edit1.setGeometry(1415, 244, 145, 22)
        self.line_edit1.show()

        self.line_edit2 = QtWidgets.QLineEdit('Disabled Line Edit', self)
        self.line_edit2.setGeometry(1415, 276, 145, 22)
        self.line_edit2.setDisabled(True)
        self.line_edit2.show()

        self.time_edit1 = QtWidgets.QTimeEdit(self)
        self.time_edit1.setGeometry(1580, 180, 110, 22)
        self.time_edit1.show()

        self.time_edit2 = QtWidgets.QTimeEdit(self)
        self.time_edit2.setGeometry(1580, 212, 110, 22)
        self.time_edit2.setDisabled(True)
        self.time_edit2.show()

        self.date_edit1 = QtWidgets.QDateEdit(self)
        self.date_edit1.setGeometry(1580, 244, 110, 22)
        self.date_edit1.show()

        self.date_edit2 = QtWidgets.QDateEdit(self)
        self.date_edit2.setGeometry(1580, 276, 110, 22)
        self.date_edit2.setDisabled(True)
        self.date_edit2.show()

        self.spinbox1 = QtWidgets.QSpinBox(self)
        self.spinbox1.setGeometry(1710, 180, 95, 22)
        self.spinbox1.show()

        self.spinbox2 = QtWidgets.QSpinBox(self)
        self.spinbox2.setGeometry(1710, 212, 95, 22)
        self.spinbox2.setDisabled(True)
        self.spinbox2.show()

        self.double_spinbox1 = QtWidgets.QDoubleSpinBox(self)
        self.double_spinbox1.setGeometry(1710, 244, 95, 22)
        self.double_spinbox1.show()

        self.double_spinbox2 = QtWidgets.QDoubleSpinBox(self)
        self.double_spinbox2.setGeometry(1710, 276, 95, 22)
        self.double_spinbox2.setDisabled(True)
        self.double_spinbox2.show()

        self.slider1 = QtWidgets.QSlider(self)
        self.slider1.setGeometry(1825, 180, 20, 220)
        self.slider1.setValue(23)
        self.slider1.show()

        self.slider2 = QtWidgets.QSlider(self)
        self.slider2.setGeometry(1856, 180, 20, 220)
        self.slider2.setDisabled(True)
        self.slider2.setValue(72)
        self.slider2.show()

        self.text_edit1 = QtWidgets.QTextEdit('<html><b>Text</b</html> Edit', self)
        self.text_edit1.setGeometry(1125, 310, 140, 90)
        self.text_edit1.show()

        self.text_edit2 = QtWidgets.QTextEdit('Disabled <html><b>Text</b</html> Edit', self)
        self.text_edit2.setGeometry(1280, 310, 140, 90)
        self.text_edit2.setDisabled(True)
        self.text_edit2.show()

        self.plain_text_edit1 = QtWidgets.QPlainTextEdit('Plain Text Edit', self)
        self.plain_text_edit1.setGeometry(1435, 310, 135, 90)
        self.plain_text_edit1.show()

        self.plain_text_edit2 = QtWidgets.QPlainTextEdit('Disabled Plain Text Edit', self)
        self.plain_text_edit2.setGeometry(1585, 310, 135, 90)
        self.plain_text_edit2.setDisabled(True)
        self.plain_text_edit2.show()

        self.dial1 = QtWidgets.QDial(self)
        self.dial1.setGeometry(1730, 315, 80, 80)
        self.dial1.show()

        # Other

        self.preview_scrollbar = QtWidgets.QScrollBar(QtCore.Qt.Horizontal, self)
        self.preview_scrollbar.setGeometry(1081, 984, 823, 20)
        self.preview_scrollbar.show()

        self.other_group = QtWidgets.QGroupBox('Other Widgets', self)
        self.other_group.setGeometry(1106, 425, 780, 230)
        self.other_group.show()

        self.table_widget = QtWidgets.QTableWidget(self)
        self.table_widget.setGeometry(1125, 450, 230, 190)
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(3)
        self.table_widget.setItem(0, 0, QtWidgets.QTableWidgetItem('1,1'))
        self.table_widget.setItem(0, 1, QtWidgets.QTableWidgetItem('1,2'))
        self.table_widget.setItem(1, 0, QtWidgets.QTableWidgetItem('2,2'))
        self.table_widget.setItem(1, 1, QtWidgets.QTableWidgetItem('2,2'))
        self.table_widget.setItem(2, 0, QtWidgets.QTableWidgetItem('3,1'))
        self.table_widget.setItem(2, 1, QtWidgets.QTableWidgetItem('3,2'))
        self.table_widget.setItem(3, 0, QtWidgets.QTableWidgetItem('4,1'))
        self.table_widget.setItem(3, 1, QtWidgets.QTableWidgetItem('4,2'))
        self.table_widget.setItem(4, 0, QtWidgets.QTableWidgetItem('5,1'))
        self.table_widget.setItem(4, 1, QtWidgets.QTableWidgetItem('5,2'))
        self.table_widget.setItem(0, 2, QtWidgets.QTableWidgetItem('1,3'))
        self.table_widget.setItem(1, 2, QtWidgets.QTableWidgetItem('2,3'))
        self.table_widget.setItem(2, 2, QtWidgets.QTableWidgetItem('3,3'))
        self.table_widget.setItem(3, 2, QtWidgets.QTableWidgetItem('4,3'))
        self.table_widget.setItem(4, 2, QtWidgets.QTableWidgetItem('5,3'))
        self.table_widget.show()

        self.table_widget2 = QtWidgets.QTableWidget(self)
        self.table_widget2.setGeometry(1375, 450, 230, 190)
        self.table_widget2.setRowCount(5)
        self.table_widget2.setColumnCount(3)
        self.table_widget2.setItem(0, 0, QtWidgets.QTableWidgetItem('1,1 (Disabled)'))
        self.table_widget2.setItem(0, 1, QtWidgets.QTableWidgetItem('1,2 (Disabled)'))
        self.table_widget2.setItem(1, 0, QtWidgets.QTableWidgetItem('2,2 (Disabled)'))
        self.table_widget2.setItem(1, 1, QtWidgets.QTableWidgetItem('2,2 (Disabled)'))
        self.table_widget2.setItem(2, 0, QtWidgets.QTableWidgetItem('3,1 (Disabled)'))
        self.table_widget2.setItem(2, 1, QtWidgets.QTableWidgetItem('3,2 (Disabled)'))
        self.table_widget2.setItem(3, 0, QtWidgets.QTableWidgetItem('4,1 (Disabled)'))
        self.table_widget2.setItem(3, 1, QtWidgets.QTableWidgetItem('4,2 (Disabled)'))
        self.table_widget2.setItem(4, 0, QtWidgets.QTableWidgetItem('5,1 (Disabled)'))
        self.table_widget2.setItem(4, 1, QtWidgets.QTableWidgetItem('5,2 (Disabled)'))
        self.table_widget2.setItem(0, 2, QtWidgets.QTableWidgetItem('1,3 (Disabled)'))
        self.table_widget2.setItem(1, 2, QtWidgets.QTableWidgetItem('2,3 (Disabled)'))
        self.table_widget2.setItem(2, 2, QtWidgets.QTableWidgetItem('3,3 (Disabled)'))
        self.table_widget2.setItem(3, 2, QtWidgets.QTableWidgetItem('4,3 (Disabled)'))
        self.table_widget2.setItem(4, 2, QtWidgets.QTableWidgetItem('5,3 (Disabled)'))
        self.table_widget2.setDisabled(True)
        self.table_widget2.show()

        self.vert_line = QtWidgets.QFrame(self)
        self.vert_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.vert_line.setGeometry(1595, 450, 50, 190)
        self.vert_line.show()

        self.hor_line = QtWidgets.QFrame(self)
        self.hor_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.hor_line.setGeometry(1630, 530, 235, 30)
        self.hor_line.show()

        header = QtWidgets.QTreeWidgetItem(['Id', 'Value'])
        self.treeview_1 = QtWidgets.QTreeWidget(self)
        self.treeview_1.setGeometry(1630, 450, 235, 85)
        self.treeview_1.setHeaderItem(header)
        self.tree_item1 = QtWidgets.QTreeWidgetItem(self.treeview_1, ['1', '187'])
        self.tree_subitem_1 = QtWidgets.QTreeWidgetItem(self.tree_item1, ['1', '187'])
        self.tree_item2 = QtWidgets.QTreeWidgetItem(self.treeview_1, ['2', '1337'])
        self.tree_subitem_2 = QtWidgets.QTreeWidgetItem(self.tree_item2, ['2', '1337'])
        self.treeview_1.show()

        header2 = QtWidgets.QTreeWidgetItem(['Disabled', 'Treewidget'])
        self.treeview_2 = QtWidgets.QTreeWidget(self)
        self.treeview_2.setGeometry(1630, 555, 235, 85)
        self.treeview_2.setHeaderItem(header2)
        self.tree_item3 = QtWidgets.QTreeWidgetItem(self.treeview_2, ['1', '187'])
        self.tree_subitem_3 = QtWidgets.QTreeWidgetItem(self.tree_item3, ['1', '187'])
        self.tree_item4 = QtWidgets.QTreeWidgetItem(self.treeview_2, ['2', '1337'])
        self.tree_subitem_4 = QtWidgets.QTreeWidgetItem(self.tree_item4, ['2', '1337'])
        self.treeview_2.setDisabled(True)
        self.treeview_2.show()

        self.tabs = QtWidgets.QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.setGeometry(1106, 670, 780, 295)
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")
        self.tabs.show()

        self.label1 = QtWidgets.QLabel('Enabled Progressbar:', self.tab1)
        self.label1.setOpenExternalLinks(False)
        self.label1.setGeometry(541, 19, 110, 20)
        self.label1.show()

        self.label2 = QtWidgets.QLabel('Disabled Progressbar:', self.tab1)
        self.label2.setOpenExternalLinks(False)
        self.label2.setGeometry(541, 75, 120, 20)
        self.label2.show()

        self.label3 = QtWidgets.QLabel('Enabled LCDNumber:', self.tab1)
        self.label3.setOpenExternalLinks(False)
        self.label3.setGeometry(541, 130, 100, 20)
        self.label3.show()

        self.label4 = QtWidgets.QLabel('Disabled LCDNumber:', self.tab1)
        self.label4.setOpenExternalLinks(False)
        self.label4.setGeometry(541, 191, 110, 20)
        self.label4.show()

        self.label5 = QtWidgets.QLabel('Enabled Calendar Widget:', self.tab2)
        self.label5.setOpenExternalLinks(False)
        self.label5.setGeometry(140, 3, 150, 20)
        self.label5.show()

        self.label6 = QtWidgets.QLabel('Disabled Calendar Widget:', self.tab2)
        self.label6.setOpenExternalLinks(False)
        self.label6.setGeometry(505, 3, 150, 20)
        self.label6.show()

        self.progress_bar1 = QtWidgets.QProgressBar(self.tab1)
        self.progress_bar1.setGeometry(540, 40, 230, 32)
        self.progress_bar1.setValue(69)
        self.progress_bar1.show()

        self.progress_bar2 = QtWidgets.QProgressBar(self.tab1)
        self.progress_bar2.setGeometry(540, 95, 230, 32)
        self.progress_bar2.setValue(69)
        self.progress_bar2.setDisabled(True)
        self.progress_bar2.show()

        self.ldc_number1 = QtWidgets.QLCDNumber(self.tab1)
        self.ldc_number1.setGeometry(540, 149, 210, 40)
        self.ldc_number1.display(1337)
        self.ldc_number1.show()

        self.ldc_number2 = QtWidgets.QLCDNumber(self.tab1)
        self.ldc_number2.setGeometry(540, 210, 210, 40)
        self.ldc_number2.setDisabled(True)
        self.ldc_number2.display(1337)
        self.ldc_number2.show()

        self.list1 = QtWidgets.QListWidget(self.tab1)
        self.list1.setGeometry(20, 20, 110, 230)
        self.list1.addItem('Item 1')
        self.list1.addItem('Item 2')
        self.list1.addItem('Item 3')
        self.list1.addItem('Item 4')
        self.list1.addItem('Item 5')
        self.list1.addItem('Item 6')
        self.list1.addItem('Item 7')
        self.list1.addItem('Item 8')
        self.list1.addItem('Item 9')
        self.list1.addItem('Item 10')
        self.list1.addItem('Item 11')
        self.list1.addItem('Item 12')
        self.list1.addItem('Item 13')
        self.list1.addItem('Item 14')
        self.list1.addItem('Item 15')
        self.list1.show()

        self.list2 = QtWidgets.QListWidget(self.tab1)
        self.list2.setGeometry(150, 20, 110, 230)
        self.list2.addItem('(Disabled)')
        self.list2.addItem('Item 1')
        self.list2.addItem('Item 2')
        self.list2.addItem('Item 3')
        self.list2.addItem('Item 4')
        self.list2.addItem('Item 5')
        self.list2.addItem('Item 6')
        self.list2.addItem('Item 7')
        self.list2.addItem('Item 8')
        self.list2.addItem('Item 9')
        self.list2.addItem('Item 10')
        self.list2.addItem('Item 11')
        self.list2.addItem('Item 12')
        self.list2.addItem('Item 13')
        self.list2.addItem('Item 14')
        self.list2.addItem('Item 15')
        self.list2.setDisabled(True)
        self.list2.show()

        self.textbrowser1 = QtWidgets.QTextBrowser(self.tab1)
        self.textbrowser1.setGeometry(280, 20, 110, 230)
        self.textbrowser1.setOpenLinks(False)
        self.textbrowser1.setText('<html><b>Text</b</html> <html><u>browser</u</html> '
                                  '<html><i>with</i</html> <a href="http://www.google.com">link</a>')
        self.textbrowser1.show()

        self.textbrowser2 = QtWidgets.QTextBrowser(self.tab1)
        self.textbrowser2.setGeometry(410, 20, 110, 230)
        self.textbrowser2.setOpenLinks(False)
        self.textbrowser2.setText('Disabled <html><b>Text</b</html> <html><u>browser</u</html> '
                                  '<html><i>with</i</html> <a href="http://www.google.com">link</a>')
        self.textbrowser2.setDisabled(True)
        self.textbrowser2.show()

        self.calendar1 = QtWidgets.QCalendarWidget(self.tab2)
        self.calendar1.setGeometry(20, 23, 360, 228)

        self.calendar2 = QtWidgets.QCalendarWidget(self.tab2)
        self.calendar2.setGeometry(395, 23, 360, 228)
        self.calendar2.setDisabled(True)

    def apply_style_preview(self, stylesheet):
        self.preview_area.setStyleSheet(stylesheet)
        self.button_group.setStyleSheet(stylesheet)
        self.pushbutton1.setStyleSheet(stylesheet)
        self.pushbutton2.setStyleSheet(stylesheet)
        self.toolbutton1.setStyleSheet(stylesheet)
        self.toolbutton2.setStyleSheet(stylesheet)
        self.checkbox1.setStyleSheet(stylesheet)
        self.checkbox2.setStyleSheet(stylesheet)
        self.checkbox3.setStyleSheet(stylesheet)
        self.radiobutton1.setStyleSheet(stylesheet)
        self.radiobutton2.setStyleSheet(stylesheet)
        self.radiobutton3.setStyleSheet(stylesheet)
        self.command_link_button1.setStyleSheet(stylesheet)
        self.command_link_button2.setStyleSheet(stylesheet)
        self.input_group.setStyleSheet(stylesheet)
        self.combobox1.setStyleSheet(stylesheet)
        self.combobox2.setStyleSheet(stylesheet)
        self.combobox3.setStyleSheet(stylesheet)
        self.combobox4.setStyleSheet(stylesheet)
        self.datetime_edit1.setStyleSheet(stylesheet)
        self.datetime_edit2.setStyleSheet(stylesheet)
        self.font_box1.setStyleSheet(stylesheet)
        self.font_box2.setStyleSheet(stylesheet)
        self.shortcut1.setStyleSheet(stylesheet)
        self.shortcut2.setStyleSheet(stylesheet)
        self.line_edit1.setStyleSheet(stylesheet)
        self.line_edit2.setStyleSheet(stylesheet)
        self.time_edit1.setStyleSheet(stylesheet)
        self.time_edit2.setStyleSheet(stylesheet)
        self.date_edit1.setStyleSheet(stylesheet)
        self.date_edit2.setStyleSheet(stylesheet)
        self.spinbox1.setStyleSheet(stylesheet)
        self.spinbox2.setStyleSheet(stylesheet)
        self.double_spinbox1.setStyleSheet(stylesheet)
        self.double_spinbox2.setStyleSheet(stylesheet)
        self.slider1.setStyleSheet(stylesheet)
        self.slider2.setStyleSheet(stylesheet)
        self.text_edit1.setStyleSheet(stylesheet)
        self.text_edit2.setStyleSheet(stylesheet)
        self.plain_text_edit1.setStyleSheet(stylesheet)
        self.plain_text_edit2.setStyleSheet(stylesheet)
        self.dial1.setStyleSheet(stylesheet)
        self.preview_scrollbar.setStyleSheet(stylesheet)
        self.other_group.setStyleSheet(stylesheet)
        self.table_widget.setStyleSheet(stylesheet)
        self.table_widget2.setStyleSheet(stylesheet)
        self.vert_line.setStyleSheet(stylesheet)
        self.hor_line.setStyleSheet(stylesheet)
        self.treeview_1.setStyleSheet(stylesheet)
        self.treeview_2.setStyleSheet(stylesheet)
        self.progress_bar1.setStyleSheet(stylesheet)
        self.progress_bar2.setStyleSheet(stylesheet)
        self.ldc_number1.setStyleSheet(stylesheet)
        self.ldc_number2.setStyleSheet(stylesheet)
        self.list1.setStyleSheet(stylesheet)
        self.list2.setStyleSheet(stylesheet)
        self.textbrowser1.setStyleSheet(stylesheet)
        self.textbrowser2.setStyleSheet(stylesheet)
        self.label1.setStyleSheet(stylesheet)
        self.label2.setStyleSheet(stylesheet)
        self.tabs.setStyleSheet(stylesheet)
        self.calendar1.setStyleSheet(stylesheet)
        self.calendar2.setStyleSheet(stylesheet)
        self.label3.setStyleSheet(stylesheet)
        self.label4.setStyleSheet(stylesheet)
        self.label5.setStyleSheet(stylesheet)
        self.label6.setStyleSheet(stylesheet)

    def open_changelog(self):
        webbrowser.open('https://github.com/niklas-henning/qss-editor/blob/master/changelog.txt')

    def isModified(self):
        return self.text_edit.document().isModified()

    def undo(self):
        self.text_edit.undo()

    def redo(self):
        self.text_edit.redo()

    def closeEvent(self, e):
        if self.maybeSave():
            e.accept()
        else:
            e.ignore()

    def maybeSave(self):
        editor_text = self.text_edit.toPlainText()

        if self.current_file != '':
            with open(self.current_file, "r") as file:
                current_file_text = file.read()

                if current_file_text == editor_text:
                    return True

        if self.current_file == '':
            if editor_text == '':
                return True

        c_dialog = QtWidgets.QMessageBox.question(self, 'Warning',
                                                  'The file has been modified.\nDo you want to save changes before closing?',
                                                  QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)

        if c_dialog == QtWidgets.QMessageBox.Save:
            if self.current_file == '':
                self.save_as_file()
                if not self.file_name_save:
                    return False
            else:
                self.save_file()
                return True

        if c_dialog == QtWidgets.QMessageBox.Discard:
            return True

        if c_dialog == QtWidgets.QMessageBox.Cancel:
            return False

        return True

    def open_file2(self):
        editor_text = self.text_edit.toPlainText()

        if self.current_file != '':
            with open(self.current_file, "r") as c_file:
                current_file_text = c_file.read()

        if self.current_file == '' and editor_text == '':
            self.open_file()

        elif self.current_file == '' and editor_text != '':
            dialog = QtWidgets.QMessageBox.question(self, 'Warning',
                                            'The file has been modified.\nDo you want to save changes first?',
                                            QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)

            if dialog == QtWidgets.QMessageBox.Save:
                self.save_file()
                self.open_file()

            elif dialog == QtWidgets.QMessageBox.Discard:
                self.open_file()

            elif dialog == QtWidgets.QMessageBox.Cancel:
                return False

        elif self.current_file != '' and editor_text == current_file_text:
            self.open_file()

        elif self.current_file != '' and editor_text != current_file_text:
            dialog2 = QtWidgets.QMessageBox.question(self, 'Warning',
                                                    'The file has been modified.\nDo you want to save changes first?',
                                                    QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)

            if dialog2 == QtWidgets.QMessageBox.Save:
                self.save_file()
                self.open_file()

            elif dialog2 == QtWidgets.QMessageBox.Discard:
                self.open_file()

            elif dialog2 == QtWidgets.QMessageBox.Cancel:
                return False

    def open_file(self):
        self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, '', '', 'QSS File (*.qss)')
        if not self.file_name.startswith('C:/'):
            return False

        self.current_file = self.file_name
        with open(self.file_name, "r") as file:
            self.text_open = file.read()
            self.text_edit.clear()
            self.text_edit.appendPlainText(self.text_open)
            style = self.text_edit.toPlainText()
            self.apply_style_preview(style)

    def save_file(self):
        if self.current_file != '':
            with open(self.current_file, "w") as f:
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_name_save, _ = QtWidgets.QFileDialog.getSaveFileName(self, '', '', 'QSS File (*.qss)')
        if not self.file_name_save:
            return False

        self.current_file = self.file_name_save
        with open(self.file_name_save, "w") as f:
            text = self.text_edit.toPlainText()
            f.write(text)
            f.close()

    def about_qt(self):
        messagebox = QtWidgets.QMessageBox.aboutQt(self)

    def about_qss_editor(self):
        self.about_win = AboutWindow()
        self.about_win.show()

    def find_(self):
        global find_text

        find_win = FindWindow(self)
        find_win.show()

        def handle_find():
            find_text = find_win.line_edit_find.text()
            replace_text = find_win.line_edit_replace.text()

            cursor = self.text_edit.textCursor()

            flags = QtGui.QTextDocument.FindFlags()

            if cs == False and wwo == False:
                flags = QtGui.QTextDocument.FindFlags()

            elif cs == True and wwo == False:
                flags = QtGui.QTextDocument.FindFlags() | QtGui.QTextDocument.FindCaseSensitively

            elif cs == False and wwo == True:
                flags = QtGui.QTextDocument.FindFlags() | QtGui.QTextDocument.FindWholeWords

            elif cs == True and wwo == True:
                flags = QtGui.QTextDocument.FindFlags() | QtGui.QTextDocument.FindCaseSensitively | QtGui.QTextDocument.FindWholeWords

            r = self.text_edit.find(find_text, flags)

            if r:
                pass
            else:
                flags2 = QtGui.QTextDocument.FindBackward

                if cs == False and wwo == False:
                    flags2 = QtGui.QTextDocument.FindBackward

                elif cs == True and wwo == False:
                    flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindCaseSensitively

                elif cs == False and wwo == True:
                    flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindWholeWords

                elif cs == True and wwo == True:
                    flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindCaseSensitively | QtGui.QTextDocument.FindWholeWords

                if self.text_edit.find(find_text, flags2) > 0:
                    self.text_edit.moveCursor(QtGui.QTextCursor.Start)
                    r2 = self.text_edit.find(find_text, flags)

        def handle_replace():
            find_text = find_win.line_edit_find.text()
            replace_text = find_win.line_edit_replace.text()

            cursor = self.text_edit.textCursor()
            cursor.beginEditBlock()

            flags = QtGui.QTextDocument.FindFlags()

            if cs == False and wwo == False:
                flags = QtGui.QTextDocument.FindFlags()

            elif cs == True and wwo == False:
                flags = QtGui.QTextDocument.FindFlags() | QtGui.QTextDocument.FindCaseSensitively

            elif cs == False and wwo == True:
                flags = QtGui.QTextDocument.FindFlags() | QtGui.QTextDocument.FindWholeWords

            elif cs == True and wwo == True:
                flags = QtGui.QTextDocument.FindFlags() | QtGui.QTextDocument.FindCaseSensitively | QtGui.QTextDocument.FindWholeWords

            if cursor.hasSelection():
                cursor.insertText(replace_text)
                r = self.text_edit.find(find_text, flags)

                if r:
                    pass

                else:
                    flags2 = QtGui.QTextDocument.FindBackward

                    if cs == False and wwo == False:
                        flags2 = QtGui.QTextDocument.FindBackward

                    elif cs == True and wwo == False:
                        flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindCaseSensitively

                    elif cs == False and wwo == True:
                        flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindWholeWords

                    elif cs == True and wwo == True:
                        flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindCaseSensitively | QtGui.QTextDocument.FindWholeWords

                    if self.text_edit.find(find_text, flags2) > 0:
                        self.text_edit.moveCursor(QtGui.QTextCursor.Start)
                        self.text_edit.find(find_text, flags)

            else:
                r2 = self.text_edit.find(find_text, flags)
                if r2:
                    temp_cursor = self.text_edit.textCursor()
                    if temp_cursor.hasSelection():
                        temp_cursor.insertText(replace_text)
                        self.text_edit.find(find_text, flags)
                else:
                    flags2 = QtGui.QTextDocument.FindBackward

                    if cs == False and wwo == False:
                        flags2 = QtGui.QTextDocument.FindBackward

                    elif cs == True and wwo == False:
                        flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindCaseSensitively

                    elif cs == False and wwo == True:
                        flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindWholeWords

                    elif cs == True and wwo == True:
                        flags2 = QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindCaseSensitively | QtGui.QTextDocument.FindWholeWords

                    if self.text_edit.find(find_text, flags2) > 0:
                        self.text_edit.moveCursor(QtGui.QTextCursor.Start)
                        r3 = self.text_edit.find(find_text, flags)
                        temp_cursor2 = self.text_edit.textCursor()
                        temp_cursor2.insertText(replace_text)
                        self.text_edit.find(find_text, flags)

            cursor.endEditBlock()

        def handle_replace_all():
            find_text = find_win.line_edit_find.text()
            replace_text = find_win.line_edit_replace.text()

            current_text = self.text_edit.toPlainText()
            replaced_text = current_text.replace(find_text, replace_text)

            cursor = self.text_edit.textCursor()
            cursor.beginEditBlock()

            cursor.select(QtGui.QTextCursor.Document)
            cursor.removeSelectedText()
            cursor.insertText(replaced_text)

            cursor.endEditBlock()

        find_win.button_find.clicked.connect(handle_find)
        find_win.button_replace.clicked.connect(handle_replace)
        find_win.button_replace_all.clicked.connect(handle_replace_all)

    def preview(self):
        text = self.text_edit.toPlainText()
        self.apply_style_preview(text)

    def clear_text_edit(self):
        self.text_edit.clear()
        text = self.text_edit.toPlainText()
        self.apply_style_preview(text)

    def copy_text(self):
        self.text_edit.copy()

    def paste_text(self):
        self.text_edit.paste()

    def cut_text(self):
        self.text_edit.cut()

    def minimize_win(self):
        self.showMinimized()

    def maximize_win(self):
        self.showMaximized()


app = QtWidgets.QApplication(sys.argv)
main_win = MainWindow()
app.setStyleSheet(style_sheet)
main_win.show()
sys.exit(app.exec_())
