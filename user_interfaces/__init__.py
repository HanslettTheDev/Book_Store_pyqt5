import os

from PySide2.QtCore import QUrl

from config import PARENT_TEMP_LOCATION, PDFJS_VIEWER_PATH, TEMP_LOCATION


TempPath = os.path.join(os.environ['WINDIR'].split(':\\')[0] + ":\\", PARENT_TEMP_LOCATION, TEMP_LOCATION)
PDFJS = QUrl.fromLocalFile(os.path.join(TempPath, PDFJS_VIEWER_PATH)).toString()

def verify(key):
    global score 
    score = 0

    check_digit = key[2] 
    check_digit_2 = key[8]
    count_1 = 0 
    count_2 = 0

    chunks = key.split("-")
    for chunk in chunks:
        if len(chunk) != 5:
            return False
        
        for char in chunk:
            if char == check_digit:
                count_1 += 1
            if char == check_digit_2:
                count_2 += 1
            score += ord(char) 
            
    if score > 2200 and score < 2300 and count_1 == 4 and count_2 == 2:
        return True
    else:
        return False