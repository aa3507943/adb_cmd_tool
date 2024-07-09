import tkinter as tk
from tkinter import scrolledtext
from subprocess import Popen, PIPE, STDOUT
import threading

class CmdTool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("cmd工具")
        self.geometry("600x400")
        
        self.process = None
        
        self.create_widgets()
        
    def create_widgets(self):
        self.device_label = tk.Label(self, text="機種:")
        self.device_label.pack()
        
        self.device_entry = tk.Entry(self)
        self.device_entry.pack()
        
        self.ip_label = tk.Label(self, text="wifi ip:")
        self.ip_label.pack()
        
        self.ip_entry = tk.Entry(self)
        self.ip_entry.pack()
        
        self.operation_label = tk.Label(self, text="操作:")
        self.operation_label.pack()
        
        self.operation_entry = tk.Entry(self)
        self.operation_entry.pack()
        
        self.param_label = tk.Label(self, text="參數:")
        self.param_label.pack()
        
        self.param_entry = tk.Entry(self)
        self.param_entry.pack()
        
        self.connect_button = tk.Button(self, text="連線", command=self.run_command)
        self.connect_button.pack()
        
        self.log_text = scrolledtext.ScrolledText(self, state='disabled')
        self.log_text.pack(expand=True, fill='both')
        
        self.execute_button = tk.Button(self, text="執行", command=self.run_command)
        self.execute_button.pack()
        
        self.stop_button = tk.Button(self, text="中斷", command=self.stop_command)
        self.stop_button.pack()
        
    def run_command(self):
        command = "adb logcat"  # 您可以将其更改为任何持续输出的命令
        self.process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)
        self.thread = threading.Thread(target=self.read_output)
        self.thread.start()
        
    def read_output(self):
        for line in iter(self.process.stdout.readline, ''):
            self.log_text.configure(state='normal')
            self.log_text.insert(tk.END, line)
            self.log_text.configure(state='disabled')
            self.log_text.see(tk.END)
        self.process.stdout.close()
        
    def stop_command(self):
        if self.process:
            self.process.terminate()
            self.thread.join()
            self.log_text.configure(state='normal')
            self.log_text.insert(tk.END, "Process terminated\n")
            self.log_text.configure(state='disabled')
            self.log_text.see(tk.END)

if __name__ == "__main__":
    app = CmdTool()
    app.mainloop()
