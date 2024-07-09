# import json, subprocess, os

# class ADBFunction:
#     def __init__(self):
#         # with open("log.txt", "w", encoding= "utf-8") as f:
#         #     sys.stdout = f
#         with open(os.path.abspath("./content/device_info.json"), mode= "r", encoding= "utf-8") as file:
#             self.data:dict = json.load(file)
#         with open(os.path.abspath("./content/operation.json"), mode="r", encoding="utf-8") as file:
#             self.func:dict = json.load(file)
#         self.operated_path = os.path.abspath("scrcpy")
#         # os.system(f"cd /d {self.operated_path}")
#         os.chdir(self.operated_path)
#         # print(os.getcwd())
#     def run_adb_func(self, title, param=""):
#         # console:str = os.popen(f"{self.func[title]}").read()
#         # os.system(f"{self.func[title]}")
#         try:
#             if "adb shell " in self.func[title]:
#                 # adb = self.func[title].replace("adb shell ", "")
#                 # console = subprocess.run(["adb", "shell", f"{adb}"], shell= True, capture_output= True, text= True, check= True)
#                 # console = subprocess.run(f"{self.func[title]}", shell= True, capture_output= True, text= True, check= True)
#                 self.process = subprocess.Popen(f"{self.func[title]}", shell= True, stdout= subprocess.PIPE, stderr= subprocess.STDOUT)
#                 output = self.process.stdout.read().decode('utf-8')
#                 print(output)
#             # elif "adb" in self.func[title] and "shell" not in self.func[title]:
#             #     commandList = self.func[title].split(" ")
#             #     console = subprocess.run(["adb", f"{commandList}"], capture_output= True, text= True, check= True)
#             elif "adb logcat" in self.func[title]:
#                 self.process = subprocess.Popen(['adb', 'logcat'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding= 'utf-8', errors='replace')
#                 output = []
#                 try:
#                     while True:
#                         line = self.process.stdout.readline()
#                         if not line:
#                             break
#                         output.append(line)
#                         if param in line:
#                             print(line.strip())  # 只打印包含 "progress" 的行
#                 except UnicodeDecodeError as e:
#                     print(f"解碼錯誤: {e}")
#                 except KeyboardInterrupt:
#                     self.process.terminate()
#                 finally:
#                     self.process.stdout.close()
#                     self.process.stderr.close()
#                     subprocess.run(['adb', 'kill-server'])
#                 return output
#                 # 打印所有捕獲的輸出
#             else:
#                 commandList = self.func[title].split(" ")
#                 console = subprocess.run(commandList, capture_output= True, text= True, check= True)
#                 output = console.stdout
#                 print(output)
#             return output
#         except subprocess.CalledProcessError as e:
#             output = e.stderr
#             print(output)
#             return output
#         # time.sleep(1)
#         # print(console.stdout.strip())
#         # return console.stdout.strip()
#         # print("這是console", console)
#         # return console
#     def interrupt(self):
#         self.process.kill()
#     def get_device_name(self):
#         return list(self.data.keys())
#     def get_func_name(self):
#         # print(list(self.func.keys()))
#         return list(self.func.keys())
#     def get_wifi(self, device):
#         return self.data[device]
#     def adb_connect(self, wifi):
#         # os.system(f"adb connect {wifi}")
#         # console = os.popen(f"adb connect {wifi}").read()
#         # os.system(f"adb connect {wifi}")
#         # console = subprocess.run(["adb", f"adb connect {wifi}"], capture_output= True, text= True, check= True)
#         console = subprocess.run(["adb", "connect" ,f"{wifi}"], capture_output= True, text= True, check= True)
#         if console.returncode == 0:
#             output = console.stdout
#         else:
#             output = console.stderr
#         print(output)
#         return output
#         # print(f"\n\n****{console}****\n\n")
        
#         # print(console.stdout.strip())
#         # return console.stdout.strip()
#         # print("我來印東西", t)    
#     def adb_kill_server(self):
#         # os.system("adb kill-server")
#         # console = os.popen(f"adb kill-server").read()
#         # os.system(f"adb kill-server")
#         console = subprocess.run(["adb", "kill-server"], capture_output= True, text= True, check= True)
#         if console.returncode == 0:
#             output = console.stdout
#         else:
#             output = console.stderr
#         print(output)
#         return output
#         # print("我來印東西", t)
#         # print(f"\n\n****{console}****\n\n")
#         # print(console.stdout.strip())
#         # return console.stdout.strip()
#         # result = str(console)
#         # print(result)
#         # return result

# # adb = ADBFunction()
# # adb.adb_kill_server()
# # adb.adb_connect("172.21.10.146")
# # # adb.run_adb_func("取得裝置列表")
# # adb.run_adb_func("取得wifi mac address")


import json, subprocess, os

class ADBFunction:
    def __init__(self):
        with open(os.path.abspath("./content/device_info.json"), mode= "r", encoding= "utf-8") as file:
            self.data = json.load(file)
        with open(os.path.abspath("./content/operation.json"), mode="r", encoding="utf-8") as file:
            self.func = json.load(file)
        self.operated_path = os.path.abspath("scrcpy")
        os.chdir(self.operated_path)
        self.process = None

    def run_adb_func(self, title, param="", callback=None):
        output = ""
        try:
            if "adb logcat" in self.func[title]:
                self.process = subprocess.Popen(['adb', 'logcat'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', errors='replace')
                while self.process and self.process.poll() is None:
                    line = self.process.stdout.readline()
                    if not line:
                        break
                    if callback:
                        if param in line:
                            callback(line)
            elif "adb shell " in self.func[title]:
                # adb = self.func[title].replace("adb shell ", "")
                # console = subprocess.run(["adb", "shell", f"{adb}"], shell= True, capture_output= True, text= True, check= True)
                # console = subprocess.run(f"{self.func[title]}", shell= True, capture_output= True, text= True, check= True)
                self.process = subprocess.Popen(f"{self.func[title]}", shell= True, stdout= subprocess.PIPE, stderr= subprocess.STDOUT)
                output = self.process.stdout.read().decode('utf-8')
                if callback:
                    callback(output)
            else:
                commandList = self.func[title].split(" ")
                console = subprocess.run(commandList, capture_output=True, text=True, check=True)
                output = console.stdout
                if callback:
                    callback(output)
            return output
        except subprocess.CalledProcessError as e:
            output = e.stderr
            if callback:
                callback(output)
            return output

    def interrupt(self):
        if self.process:
            self.process.kill()
            self.process = None

    def get_device_name(self):
        return list(self.data.keys())

    def get_func_name(self):
        return list(self.func.keys())

    def get_wifi(self, device):
        return self.data[device]

    def adb_connect(self, wifi):
        console = subprocess.run(["adb", "connect", f"{wifi}"], capture_output=True, text=True, check=True)
        output = console.stdout if console.returncode == 0 else console.stderr
        print(output)
        return output

    def adb_kill_server(self):
        console = subprocess.run(["adb", "kill-server"], capture_output=True, text=True, check=True)
        output = console.stdout if console.returncode == 0 else console.stderr
        print(output)
        return output
