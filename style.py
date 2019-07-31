# Window Style


style_sheet = """
QMainWindow
{
    background-color: #f7f7f7;
    background: #f7f7f7;
    border: none;
}

QMenu 
{
    color: #31363B;
    background-color: #fefefe;
    border: none;
}

QMenu::item
{
    color: #31363B;
    background-color: #fefefe;
}

QMenu::item:selected 
{ 
    background-color: #C9ECFF;
    color: #31363B;
}

QMenuBar 
{
    background-color: #FFFFFF;
    border: none;
}

QMenuBar::item 
{
    color: #31363B;
    spacing: 5px;
    padding: 3px 5px;
    background: transparent;
    border-radius: 1px;
}

QMenuBar::item:selected 
{
    background: #C9ECFF;
}

QMenuBar::item:pressed 
{
    background: #C9ECFF ;
}

QWidget#preview_area
{
     border: 1px solid grey;
}

QTextEdit#line_display
{
    background-color: #DCDCDC;
    border: 1px solid grey;
    font-size:10pt;
}

QPlainTextEdit#text_edit
{   
    border: none;
    font-size:10pt;
    background-color: #ffffff;
    color: #000000;
    selection-background-color: #0087EE;
    selection-color: #ffffff;
    padding-left: 3px;
}

QPlainTextEdit#text_edit QScrollBar:vertical 
{
     border: none;
     background: #f7f7f7;
     background-color: #f7f7f7;
     width: 17px;
     margin: 0;
}
QPlainTextEdit#text_edit QScrollBar::handle:vertical
{
     background: #DCDCDC;
     min-height: 20px;
}
QPlainTextEdit#text_edit QScrollBar::add-line:vertical 
{
     border: none;
     background: #32CC99;
     height: 0px;
     width: 0px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}

QPlainTextEdit#text_edit QScrollBar::sub-line:vertical 
{
     border:  none;
     background: #32CC99;
     height: 0px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}
QPlainTextEdit#text_edit QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical 
{
     border: none;
     width: 0px;
     height: 0px;
     background: #DCDCDC;
     background-color: #DCDCDC;
}

QPlainTextEdit#text_edit QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical 
{
     background: none;
}
 
 QPlainTextEdit#text_edit QScrollBar:horizontal 
{
     border: none;
     background: #f7f7f7;
     background-color: #f7f7f7;
     width: 17px;
     margin: 0;
}
QPlainTextEdit#text_edit QScrollBar::handle:horizontal 
{
     background: #DCDCDC;
     min-height: 20px;
}

QPlainTextEdit#text_edit QScrollBar::add-line:horizontal 
{
     border: none;
     background: #32CC99;
     height: 0px;
     width: 0px;
     subcontrol-position: right;
     subcontrol-origin: margin;
}

QPlainTextEdit#text_edit QScrollBar::sub-line:horizontal 
{
     border:  none;
     background: #32CC99;
     height: 0px;
     subcontrol-position: left;
     subcontrol-origin: margin;
}

QPlainTextEdit#text_edit QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal 
{

     border: none;
     width: 0px;
     height: 0px;
     background: #DCDCDC;
     background-color: #DCDCDC;
}

QPlainTextEdit#text_edit QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal 
{
     background: none;
}

QWidget#number_bar_extension
{
    background: #dcdcdc;
}
"""


about_window_stylesheet = """
QDialog
{
    background-color: #ffffff;
}
"""


find_window_stylesheet = """
QDialog
{
    background-color: #fcfcfc;
}
"""
