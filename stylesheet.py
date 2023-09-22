class STYLES:
    splash = ('''
        #title_label {
            font-size: 50px;
            color: #ffffff;
        }
        #desc_label {
            font-size: 20px;
            color: #c2ced1;
        }
        #loading_label {
            font-size: 30px;
            color: #e8e8eb;
        }
        QFrame {
            background-color: #625899;
            color: #c8c8c8;
        }
        QProgressBar {
            background-color: #000000;
            color: white;
            border-style: none;
            border-radius: 5px;
            text-align: center;
            font-size: 25px;
        }
        QProgressBar::chunk {
            border-radius: 5px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #44DD44);
        }
'''
    )

    frame_pages = (
        "QListView {\n"
        "background-color: rgb(246, 246, 246);\n"
        "font-size: 20px;\n"
        "color: black;\n"
        "font-weight: bold;\n"
        "border: 1px solid black;\n"
        "border-radius: 10px;\n"
        "padding: 5px;\n"
        "}\n"
        "#dropdown_menu_3 {\n"
        "background-color: rgb(246, 246, 246);\n"
        "font-size: 20px;\n"
        "color: black;\n"
        "font-weight: bold;\n"
        "border: 1px solid black;\n"
        "border-radius: 10px;\n"
        "padding: 5px;\n"
        "}\n"
        "#dropdown_box {\n"
        "background-color: #143363;\n"
        "padding: 5px;\n"
        "}\n"
        "#button_6, #button_7, #button_8{\n"
        "margin-bottom: 5px;\n"
        "}\n"
    )
    frame = (
    "QPushButton {\n"
    "color: white;\n"
    "font-weight: bold;\n"
    "background-color: #AA14F0;\n"
    "border-radius: 5px;\n"
    "border: 1px solid black;\n"
    "font-size: 15px;\n"
    "padding: 5px;\n"
    "margin-left: 5px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "background-color: #F8485E;\n"
    "}\n"
    )
    default_styles = (
        "#label_3 {\n"
        "font-size: 15px;\n"
        "font-weight: bold;\n"
        "color:black;\n"
        "}\n"
        "#label_4 {\n"
        "font-size: 20px;\n"
        "font-weight: bold;\n"
        "color:blue;\n"
        "background-color: transparent;\n"
        "}\n"
        "line {\n"
        "color: black;\n"
        "}\n"
        "#label_2 {\n"
        "font-size: 20px;\n"
        "font-weight: bold;\n"
        "color: white;\n"
        "}\n"
        "frame {\n"
        "border: 1px solid gray;\n"
        "}\n"
    )

    window_bar = ('''
    #window_bar {
    }
    ''')