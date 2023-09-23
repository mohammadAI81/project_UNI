from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import * 
from PyQt5.QtGui import QFont, QIcon

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Login of Site")
    window.setWindowIcon(QIcon("download.png"))
    window.setStyleSheet("background-color: white ; color : block ; font-family : Times New Roman")
    window.resize(1200, 700)

    title_of_window = QLabel(window)
    title_of_window.setText("Login")
    title_of_window.setFont(QFont( "Times New Roman" , 20))
    title_of_window.move(10, 10)

    username = QLabel(window)
    username.setText("username: ".title())
    username.setFont(QFont("Times New Roman" , 14))
    username.move(400, 150)
    
    password = QLabel(window)
    password.setText("password: ".title())
    password.setFont(QFont("Times New Roman" , 14))
    password.move(400, 200)

    text1 = QLineEdit(window)
    text1.setFont(QFont("" , 10))
    text1.setStyleSheet("border : 2px solid block ; border-radius: 3px ; font-weight : bold")
    text1.setGeometry(500, 150, 270, 35)

    text2 = QLineEdit(window)
    text2.setFont(QFont("" , 10))
    text2.setEchoMode(QLineEdit.Password)
    text2.setStyleSheet("border : 2px solid block ; border-radius: 3px ; font-weight : bold")
    text2.setGeometry(500, 200, 270, 35)

    def exit_the_window():
        window.close()

    butten_exit = QPushButton(window)
    butten_exit.setGeometry(10, 640, 80, 50)
    butten_exit.setText("خروج")
    butten_exit.setFont(QFont("" , 10 ,100 ))
    butten_exit.setStyleSheet("background-color : red ; border : 2px solid red ; border-radius: 5px ")
    butten_exit.clicked.connect(exit_the_window)

    message_login = QMessageBox()
    message_login_error = QMessageBox()
    def go_to_excel():
        with open("data_base.csv" , "r") as f :
            data_base = f.readlines()

        for data in data_base :
            data = data[:-1]
            data = data.split(",")
            username = data[1]
            password = data[2]
            if text1.text() == username and text2.text() == password:
                message_login.setWindowTitle("Login")
                message_login.setText("you are login".title())
                message_login.setStandardButtons(QMessageBox.Ok)
                message_login.show()
                window.close()
                return
            else:
                message_login_error.setWindowTitle("Error")
                message_login_error.setText("password or username is not existing".title())
                message_login_error.setStandardButtons(QMessageBox.Ok)
        
        message_login_error.show()
                


    butten_sign_in = QPushButton(window)
    butten_sign_in.setText("ورود")
    butten_sign_in.setFont(QFont("" , 10 ,100))
    butten_sign_in.setGeometry(500, 640, 80, 50)
    butten_sign_in.setStyleSheet("background-color : blue ; border :2px solid blue ; border-radius : 5px")
    butten_sign_in.clicked.connect(go_to_excel)

    def go_to_new_window():
        window.close()
        window_register.setWindowIcon(QIcon("download.png"))
        window_register.setWindowTitle("Register")
        window_register.setStyleSheet("background-color : white ; color : block ; font-family : Times New Roman")
        window_register.resize(1200, 700)

        text_for_title = QLabel(window_register)
        text_for_title.setText("Register")
        text_for_title.setFont(QFont("", 20))
        text_for_title.move(10, 10)

        text_for_name = QLabel(window_register)
        text_for_name.setText(" نام و نام خانوادگی ")
        text_for_name.setFont(QFont("Times New Roman" , 14))
        text_for_name.move(900, 100)

        text_for_username = QLabel(window_register)
        text_for_username.setText("نام کاربری ")
        text_for_username.setFont(QFont("Times New Roman" , 14))
        text_for_username.move(900, 150)

        text_for_password = QLabel(window_register)
        text_for_password.setText("پسورد ")
        text_for_password.setFont(QFont("Times New Roman" , 14))
        text_for_password.move(900, 200)

        text_for_repassword = QLabel(window_register)
        text_for_repassword.setText("تکرار پسورد")
        text_for_repassword.setFont(QFont("Times New Roman" , 14))
        text_for_repassword.move(900, 250)

        line_for_name = QLineEdit(window_register)
        line_for_name.setFont(QFont("Times New Roman" , 10))
        line_for_name.setStyleSheet("border : 1px solid gray ; border-radius : 3px ; font-weight : bold")
        line_for_name.setGeometry(615, 100 , 270, 35)

        line_for_username = QLineEdit(window_register)
        line_for_username.setFont(QFont("Times New Roman" , 10))
        line_for_username.setStyleSheet("border : 1px solid gray ; border-radius : 3px ; font-weight : bold")
        line_for_username.setGeometry(615, 150 , 270, 35)

        line_for_password = QLineEdit(window_register)
        line_for_password.setEchoMode(QLineEdit.Password)
        line_for_password.setFont(QFont("Times New Roman" , 10))
        line_for_password.setStyleSheet("border : 1px solid gray ; border-radius : 3px ; font-weight : bold")
        line_for_password.setGeometry(615, 200 , 270, 35)

        line_for_repassword = QLineEdit(window_register)
        line_for_repassword.setEchoMode(QLineEdit.Password)
        line_for_repassword.setFont(QFont("Times New Roman" , 10))
        line_for_repassword.setStyleSheet("border : 1px solid gray ; border-radius : 3px ; font-weight : bold")
        line_for_repassword.setGeometry(615, 250 , 270, 35)

        massag_error = QMessageBox()
        massag_done = QMessageBox()
        def save_data():
            name = line_for_name.text()
            username = line_for_username.text()
            password = line_for_password.text()
            repassword = line_for_repassword.text()
            if password != repassword:
                
                massag_error.setIcon(QMessageBox.Critical)
                massag_error.setWindowTitle("Error")
                massag_error.setText("پسورد و تکرار پسورد مساوری نیستند")
                massag_error.setStandardButtons(QMessageBox.Ok)
                massag_error.show()
                
            elif name == "" or password == "" or username == "" or repassword == "" :
                message_empty = QMessageBox()
                message_empty.setWindowTitle("Empyt")
                message_empty.setIcon(QMessageBox.information)
                message_empty.setText("لطفا جای های خالی را پر کنید")
                message_empty.setStandardButtons(QMessageBox.Ok)
                message_empty.show()

            else:
                # massag_done.setWindowTitle("Done")
                # massag_done.setText("آیا از پسورد و نام کابری خود مطئن هستید")
                # massag_done.setStandardButtons(QMessageBox.Save | QMessageBox.No)
                # massag_done.show()
                # if massag_done == QMessageBox.Save:
                with open("data_base.csv" , mode="a") as f:
                    f.write(f"{name},{username},{password}\n")

                window_register.close()
                window.show()

            

        butten_true = QPushButton(window_register)
        butten_true.setText("ثبت")
        butten_true.setFont(QFont("" , 10 ,100))
        butten_true.setStyleSheet("background-color : green ; border: 2px solid green ; border-radius : 5px")
        butten_true.setGeometry(615, 640, 80, 50)
        butten_true.clicked.connect(save_data)

        def exit_the_register():
            window_register.close()
            window.show()

        butten_false = QPushButton(window_register)
        butten_false.setText("لغو")
        butten_false.setFont(QFont("" ,10 , 100))
        butten_false.setStyleSheet("background-color : red ; border : 2px solid red ; border-radius: 5px")
        butten_false.setGeometry(705, 640, 80, 50)
        butten_false.clicked.connect(exit_the_register)


        window_register.show()

    butten_sign_up = QPushButton(window)
    butten_sign_up.setText("ثبت نام")
    butten_sign_up.setFont(QFont("" , 10 , 100))
    butten_sign_up.setGeometry(590, 640, 80, 50)
    butten_sign_up.setStyleSheet("background-color : green ; border : 2px solid green ; border-radius : 5px")
    butten_sign_up.clicked.connect(go_to_new_window)
    # New Window For Register 
    # line 61 - 137 
    window_register = QWidget()

    window.show()
    app.exec()
