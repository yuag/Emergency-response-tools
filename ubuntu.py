import subprocess
import yara
import os

from html import escape


class YaraScanner:
    def __init__(self):
        pass

    def execute_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return output.decode(), error.decode()

    def load_yara_rules(self, rule_folder=None, target_directory=None):
        if rule_folder is None:
            rule_folder = input("输入YARA规则文件夹路径: ")
            if not rule_folder:
                return

        if target_directory is None:
            target_directory = input("输入扫描目录路径: ")
            if not target_directory:
                return

        try:
            rule_files = [f for f in os.listdir(rule_folder) if os.path.isfile(os.path.join(rule_folder, f))]

            compiled_rules = []
            for rule_file in rule_files:
                rule_file_path = os.path.join(rule_folder, rule_file)
                try:
                    compiled_rule = yara.compile(filepath=rule_file_path)
                    compiled_rules.append((compiled_rule, rule_file))  
                except yara.Error as e:
                    print(f"编译YARA规则失败 '{rule_file}': {e}")

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
                            print(f"读取文件失败 '{file_path}': {e}")

            print("\n".join(matched_results))

        except Exception as e:
            print(f"加载或匹配YARA规则失败: {e}")


    def execute_all_commands(self, output_file_path="Ubuntu.html"):
        
        results = []

        commands = [
            
      


            ("获取对外网络连接情况", "sudo lsof -i"),
            ("显示进程", "ps -ef"),
            ("任务启动项","systemctl list-unit-files --type=service"),
            ("检查异常端口","netstat -antlp|more"),
            ("检查定时任务", "crontab -l"),
            ("监控与目标IP通信的进程","ps -ef"),
            ("CPU降序排序","top -n 1 -b"),
            ("查询历史命令","history"),
            ("7天内被修改过的文件","sudo find /usr/bin/ /usr/sbin/ /bin/ /usr/local/bin/ -type f -mtime +7 | xargs ls -la"),
            ("登录记录","last"),
            
            
            ("多少IP在爆破主机的root帐号","sudo grep Failed password for root /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | more"),
           
           
            
            ("哪些IP在爆破","sudo grep 'Failed password' /var/log/auth.log | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' | uniq -c"),
         
            ("爆破用户名字典是什么", """sudo grep 'Failed password' /var/log/auth.log | perl -e 'while($_=<>){ /for(.*?) from/; print "$1\\n";}' | uniq -c | sort -nr"""),

            ("登录成功的日期、用户名、IP：","sudo grep 'Accepted ' /var/log/auth.log | awk '{print $1,$2,$3,$9,$11}'"),
            
            
            
            ("查询sudo权限账户","sudo grep -v \"^#\\|^$\" /etc/sudoers | grep \"ALL=(ALL)\""),

            ("查找72小时内新增的文件","find / -ctime -2"),


       
        ]
        


        
        with open(output_file_path, 'w') as html_file:
            html_file.write("<html><body>\n")


            for command_name, command in commands:
                output, _ = self.execute_command(command)
                results.append((command_name, output))
          
                html_file.write(f"<h3>{command_name}</h3>\n")
                result_html = escape(output)
                html_file.write(f"<pre>{result_html}</pre>\n")
 
            html_file.write("</body></html>")
            print(f"输入结果: {output_file_path}")    
                









    def main(self):
        while True:
            print("选择一个命令:")            
            print("1.  获取对外网络连接情况")
            print("2.  显示进程")
            print("3.  任务启动项 ")
            print("4.  检查异常端口")
            print("5.  检查定时任务 ")
            print("6.  监控与目标IP通信的进程")
            print("7.  CPU降序排序")
            print("8.  查询历史命令")
            print("9.  7天内被修改过的文件")
            print("10. 登录记录")
            print("11. 多少IP在爆破主机的root帐号")
            print("12. 哪些IP在爆破")
            print("13. 爆破用户名字典是什么")
            print("14. 登录成功的日期、用户名、IP：")
            print("15. 查询sudo权限账户")
            print("16. 使用YARA规则检测文件")
            print("17. 一键执行所有命令并导出")
            print("18. 查找72小时内新增的文件")            
            print("0.  退出")
     
            

            choice = input("输入命令编号 (0-17): ")

            if choice == '0':
                break
            elif choice == '1':
                output, _ = self.execute_command("sudo lsof -i")
                print(output)

            elif choice == '2':
                output, _ = self.execute_command("ps -ef ")
                print(output)

            elif choice == '3':
                output, _ = self.execute_command("systemctl list-unit-files --type=service")
                print(output)

            elif choice == '4':
                output, _ = self.execute_command("netstat -antlp|more")
                print(output)

            elif choice == '5':
                output, _ = self.execute_command("crontab -l")
                print(output)

            elif choice == '6':
                output, _ = self.execute_command("ps -ef ")
                print(output)                

            elif choice == '7':
                output, _ = self.execute_command("top -n 1 -b")
                print(output)


            elif choice == '8':
                output, _ = self.execute_command("history")
                print(output)


            elif choice == '9':
                output, _ = self.execute_command("find /usr/bin/ /usr/sbin/ /bin/ /usr/local/bin/ -type f -mtime +7 | xargs ls -la")
                print(output)


            elif choice == '10':
                output, _ = self.execute_command("last")
                print(output)

            elif choice == '11':
                output, _ = self.execute_command("sudo grep Failed password for root /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | more")
                print(output)

            elif choice == '12':
                output, _ = self.execute_command("sudo grep 'Failed password' /var/log/auth.log | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' | uniq -c")
                print(output)

            elif choice == '13':
                output, _ = self.execute_command("""sudo grep 'Failed password' /var/log/auth.log | perl -e 'while($_=<>){ /for(.*?) from/; print "$1\\n";}' | uniq -c | sort -nr""")
                print(output)

            elif choice == '14':
                output, _ = self.execute_command("sudo grep 'Accepted ' /var/log/auth.log | awk '{print $1,$2,$3,$9,$11}'")
                print(output)



            elif choice == '15':
                output, _ = self.execute_command("sudo grep -v \"^#\\|^$\" /etc/sudoers | grep \"ALL=(ALL)\"")
                print(output)


            elif choice == '18':
                output, _ = self.execute_command("find / -ctime -2")
                print(output)



            elif choice == '16':
                self.load_yara_rules()


            elif choice == '17':
                self.execute_all_commands()
            else:
                print("无效的命令编号，请重新输入.")




if __name__ == "__main__":
    yara_scanner = YaraScanner()
    yara_scanner.main()

