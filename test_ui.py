import tkinter as tk
from tkinter import ttk, messagebox
from adb_func import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.adb_func = ADBFunction()

        self.title("cmd工具")
        self.geometry("600x350")

        # 定義介面元素
        self.device_label = tk.Label(self, text="機種:")
        self.device_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.device_combo = ttk.Combobox(self, values=self.adb_func.get_device_name())
        self.device_combo.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.wifi_ip_label = tk.Label(self, text="wifi ip:")
        self.wifi_ip_label.grid(row=0, column=2, padx=5, pady=5, sticky='e')

        self.wifi_ip_var = tk.StringVar()
        self.wifi_ip_entry = tk.Entry(self, textvariable=self.wifi_ip_var, state='readonly')
        self.wifi_ip_entry.grid(row=0, column=3, padx=5, pady=5, sticky='w')

        self.connect_button = tk.Button(self, text="連線", command=self.connect)
        self.connect_button.grid(row=0, column=4, padx=5, pady=5)

        self.action_label = tk.Label(self, text="操作:")
        self.action_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        self.action_combo = ttk.Combobox(self, state='disabled', width=40, values= self.adb_func.get_func_name())
        self.action_combo.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='w')

        self.execute_button = tk.Button(self, text="執行", command=self.execute, state='disabled')
        self.execute_button.grid(row=1, column=3, padx=5, pady=5)

        self.disconnect_button = tk.Button(self, text="斷線", command=self.disconnect, state='disabled')
        self.disconnect_button.grid(row=1, column=4, padx=5, pady=5)

        self.text_frame = tk.Frame(self)
        self.text_frame.grid(row = 2, column= 0, columnspan= 5, padx= 5, pady= 5, sticky= "nsew")
        self.console_text = tk.Text(self.text_frame, bg="black", fg="white", wrap= "word")
        self.console_text.pack(side= tk.LEFT, fill = tk.BOTH, expand= True)
        self.scrollbar = ttk.Scrollbar(self.text_frame, orient= tk.VERTICAL, command=self.console_text.yview)
        self.scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
        self.console_text.config(yscrollcommand= self.scrollbar.set)

        # 設定規則
        self.device_combo.bind("<<ComboboxSelected>>", self.on_device_selected)
        self.action_combo.bind("<<ComboboxSelected>>", self.on_action_selected)
        self.connected = False

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def connect(self):
        # 模擬連線動作
        self.console_text.insert(tk.END, "連線中...\n")
        self.connected = True
        # self.wifi_ip_var.set("192.168.1.1")  # 假設生成IP
        text = self.adb_func.adb_connect(self.wifi_value)
        # self.console_text.insert(tk.END, "Connected!\n")
        self.console_text.insert(tk.END, f"{text}")
        self.console_text.insert(tk.END, "已連接至目標裝置\n")
        self.console_text.yview_moveto(1.0)
        self.action_combo.config(state='normal')
        self.execute_button.config(state='normal')
        self.disconnect_button.config(state='normal')

    def disconnect(self):
        # 模擬斷線動作
        # self.console_text.insert(tk.END, "Disconnecting...\n")
        self.connected = False
        # self.wifi_ip_var.set("")  # 清除IP
        self.console_text.insert(tk.END, "斷開連接中...\n")
        text = self.adb_func.adb_kill_server()
        # print(text)
        self.console_text.insert(tk.END, "已斷線\n\n")
        self.console_text.yview_moveto(1.0)    
        self.action_combo.config(state='disabled')
        self.execute_button.config(state='disabled')
        self.disconnect_button.config(state='disabled')

    def execute(self):
        if not self.connected:
            messagebox.showerror("錯誤", "請先連線")
            return
        
        selected_action = self.action_combo.get()
        if selected_action:
            self.console_text.insert(tk.END, f"Executing {selected_action}...\n")
            text = self.adb_func.run_adb_func(selected_action)
            self.console_text.insert(tk.END, f"{text}")
        else:
            messagebox.showerror("錯誤", "請選擇一個操作")
        
        self.console_text.yview_moveto(1.0)

    def on_device_selected(self, event):
        # if not self.connected:
        #     messagebox.showerror("錯誤", "請先連線")
        self.wifi_value = self.adb_func.get_wifi(self.device_combo.get())
        self.wifi_ip_var.set(self.wifi_value)

    def on_action_selected(self, event):
        if not self.connected:
            messagebox.showerror("錯誤", "請先連線")
    


