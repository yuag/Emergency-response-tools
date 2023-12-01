from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import subprocess
import yara
import os


class CommandThread(QtCore.QThread):
    # 通过该信号传递查询结果
    result_signal = QtCore.pyqtSignal(str)

    def __init__(self, command):
        super(CommandThread, self).__init__()
        self.command = command

    def run(self):
        try:
            result = subprocess.check_output(self.command, shell=True, text=True)
            self.result_signal.emit(result)
        except subprocess.CalledProcessError as e:
            self.result_signal.emit(f"Command failed with error: {e}")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 160, 771, 441))
        self.textBrowser.setObjectName("textBrowser")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 97, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(150, 80, 151, 21))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(150, 20, 141, 21))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(340, 20, 97, 21))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 50, 97, 21))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 50, 97, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(340, 80, 131, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(340, 50, 97, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(30, 80, 97, 21))
        self.radioButton_9.setObjectName("radioButton_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 20, 81, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 70, 81, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 120, 101, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(30, 110, 81, 16))
        self.radioButton_10.setObjectName("radioButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 为按钮添加点击事件

        self.pushButton.clicked.connect(self.execute_command)
        self.pushButton_2.clicked.connect(self.clear_output)
        self.pushButton_3.clicked.connect(self.load_yara_rules)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Emergency response tools", "Emergency response tools"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "系进程列表"))
        self.radioButton_7.setText(_translate("MainWindow", "近三天内修改的文件"))
        self.radioButton_6.setText(_translate("MainWindow", "显示进程和服务信息"))
        self.radioButton_5.setText(_translate("MainWindow", "计划任务"))
        self.radioButton_4.setText(_translate("MainWindow", "系统日志"))
        self.radioButton_3.setText(_translate("MainWindow", "网络连接"))
        self.radioButton_8.setText(_translate("MainWindow", "显示进程和所有者"))
        self.radioButton_2.setText(_translate("MainWindow", "系统服务"))
        self.radioButton_9.setText(_translate("MainWindow", "共享资源"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_2.setText(_translate("MainWindow", "清除"))
        self.pushButton_3.setText(_translate("MainWindow", "加载yara规则库"))
        self.radioButton_10.setText(_translate("MainWindow", "Yara"))




    def execute_command(self):
        # 获取选中的单选按钮
        selected_button = self.get_selected_radio_button()

        # 根据选择的按钮执行相应的命令
        if selected_button:
            # 使用多线程执行命令，防止阻塞主界面
            command_thread = CommandThread(selected_button)
            command_thread.result_signal.connect(self.handle_command_result)
            command_thread.start()





    def execute_command(self):
        # 获取选中的单选按钮
        selected_button = self.get_selected_radio_button()

        # 根据选择的按钮执行相应的命令
        if selected_button == "系进程列表":
            self.run_command("tasklist")
        elif selected_button == "系统服务":
            self.run_command("sc query")
        elif selected_button == "系统日志":
            self.run_command('forfiles /P C:\\ /S /M * /D -3 /C "cmd /c echo @file @fdate @ftime"')
        elif selected_button == "网络连接":
            self.run_command("netstat -ano")
        elif selected_button == "计划任务":
            self.run_command("schtasks /query /fo list")
        elif selected_button == "共享资源":
            self.run_command("net share")
        elif selected_button == "显示进程和服务信息":
            self.run_command("tasklist")
        elif selected_button == "显示进程和所有者":
            self.run_command("tasklist /V")
        # 添加其他命令的处理逻辑
        elif selected_button == "近三天内修改的文件":
            self.run_command('forfiles /P C:\\ /S /M * /D -3 /C "cmd /c echo @file @fdate @ftime"')


    def handle_command_result(self, result):
        # 处理查询结果
        self.textBrowser.setPlainText(result)





    def get_selected_radio_button(self):
        # 获取选中的单选按钮文本
        for button in self.centralwidget.findChildren(QtWidgets.QRadioButton):
            if button.isChecked():
                return button.text()

    def run_command(self, command):
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            self.textBrowser.setPlainText(result)
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(None, "Error", f"Command failed with error: {e}")

    def clear_output(self):
        # 清除文本浏览器内容
        self.textBrowser.clear()
  


    def load_yara_rules(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

  
        rule_folder = QFileDialog.getExistingDirectory(None, "加载yar脚本", options=options)

        if rule_folder:
            try:
               
                rule_files = [f for f in os.listdir(rule_folder) if os.path.isfile(os.path.join(rule_folder, f))]

           
                compiled_rules = []
                for rule_file in rule_files:
                    rule_file_path = os.path.join(rule_folder, rule_file)
                    try:
                        compiled_rule = yara.compile(filepath=rule_file_path)
                        compiled_rules.append((compiled_rule, rule_file))  # Store both rule and filename
                    except yara.Error as e:
                        QMessageBox.critical(None, "Error", f"编译YARA规则失败 '{rule_file}': {e}")

            
                target_directory = QFileDialog.getExistingDirectory(None, "加载扫描目录", options=options)

                if target_directory:
               
                    matched_results = []
                    for compiled_rule, rule_file in compiled_rules:
                        for root, dirs, files in os.walk(target_directory):
                            for file in files:
                                file_path = os.path.join(root, file)
                                try:
                                    with open(file_path, "rb") as file_data:
                                        matches = compiled_rule.match(data=file_data.read())
                                        if matches:
                                            matched_results.append(f"Rule ({rule_file}): Matches in {file_path}: {matches}")
                                except Exception as e:
                                    QMessageBox.critical(None, "Error", f"读取文件失败 '{file_path}': {e}")

                    # Display matching results in the text browser
                    self.textBrowser.setPlainText("\n".join(matched_results))

            except Exception as e:
                QMessageBox.critical(None, "Error", f"加载或匹配YARA规则失败: {e}")

# 主程序入口
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
