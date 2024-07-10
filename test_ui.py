# import tkinter as tk
# from tkinter import ttk, messagebox
# from adb_func import *
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.adb_func = ADBFunction()
        
#         self.title("cmd工具")
#         self.geometry("600x350")

#         # 定義介面元素
#         self.device_label = tk.Label(self, text="機種:")
#         self.device_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

#         self.device_combo = ttk.Combobox(self, values=self.adb_func.get_device_name())
#         self.device_combo.grid(row=0, column=1, padx=5, pady=5, sticky='w')

#         self.wifi_ip_label = tk.Label(self, text="wifi ip:")
#         self.wifi_ip_label.grid(row=0, column=2, padx=5, pady=5, sticky='e')

#         self.wifi_ip_var = tk.StringVar()
#         self.wifi_ip_entry = tk.Entry(self, textvariable=self.wifi_ip_var, state='readonly')
#         self.wifi_ip_entry.grid(row=0, column=3, padx=5, pady=5, sticky='w')

#         self.connect_button = tk.Button(self, text="連線", command=self.connect)
#         self.connect_button.grid(row=0, column=4, padx=5, pady=5)

#         self.disconnect_button = tk.Button(self, text="斷線", command=self.disconnect, state='disabled')
#         self.disconnect_button.grid(row=0, column=5, padx=5, pady=5)

#         self.action_label = tk.Label(self, text="操作:")
#         self.action_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

#         self.action_combo = ttk.Combobox(self, state='disabled', width=25, values= self.adb_func.get_func_name())
#         self.action_combo.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='w')

#         self.param_label = tk.Label(self, text="參數:", state= 'disabled')
#         self.param_label.grid(row=1, column=2, padx=5, pady=5, sticky='e')

#         self.param_entry = tk.Entry(self, state='disabled', width= 20)
#         self.param_entry.grid(row=1, column= 3, padx=5, pady=5, sticky='w')

#         self.execute_button = tk.Button(self, text="執行", command=self.execute, state='disabled')
#         self.execute_button.grid(row=1, column=4, padx=5, pady=5)

#         self.terminal_button = tk.Button(self, text="中斷", state="disabled", command=self.terminal)
#         self.terminal_button.grid(row=1, column=5, padx=5, pady=5)

#         self.text_frame = tk.Frame(self)
#         self.text_frame.grid(row = 2, column= 0, columnspan= 10, padx= 5, pady= 5, sticky= "nsew")
#         self.console_text = tk.Text(self.text_frame, bg="black", fg="white", wrap= "word")
#         self.console_text.pack(side= tk.LEFT, fill = tk.BOTH, expand= True)
#         self.scrollbar = ttk.Scrollbar(self.text_frame, orient= tk.VERTICAL, command=self.console_text.yview)
#         self.scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
#         self.console_text.config(yscrollcommand= self.scrollbar.set)

#         # 設定規則
#         self.device_combo.bind("<<ComboboxSelected>>", self.on_device_selected)
#         self.action_combo.bind("<<ComboboxSelected>>", self.on_action_selected)
#         self.connected = False

#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure(2, weight=1)
#         self.grid_columnconfigure(3, weight=1)
#         self.grid_columnconfigure(4, weight=1)
#         self.grid_rowconfigure(2, weight=1)

#     def connect(self):
#         # 模擬連線動作
#         self.console_text.insert(tk.END, "連線中...\n")
#         self.connected = True
#         # self.wifi_ip_var.set("192.168.1.1")  # 假設生成IP
#         text = self.adb_func.adb_connect(self.wifi_value)
#         # self.console_text.insert(tk.END, "Connected!\n")
#         self.console_text.insert(tk.END, f"{text}")
#         self.console_text.insert(tk.END, "已連接至目標裝置\n")
#         self.console_text.yview_moveto(1.0)
#         self.action_combo.config(state='normal')
#         self.execute_button.config(state='normal')
#         self.disconnect_button.config(state='normal')

#     def disconnect(self):
#         # 模擬斷線動作
#         # self.console_text.insert(tk.END, "Disconnecting...\n")
#         self.connected = False
#         # self.wifi_ip_var.set("")  # 清除IP
#         self.console_text.insert(tk.END, "斷開連接中...\n")
#         text = self.adb_func.adb_kill_server()
#         # print(text)
#         self.console_text.insert(tk.END, "已斷線\n\n")
#         self.console_text.yview_moveto(1.0)    
#         self.action_combo.config(state='disabled')
#         self.execute_button.config(state='disabled')
#         self.disconnect_button.config(state='disabled')
#         self.terminal_button.config(state="disabled")

#     def execute(self):
#         if not self.connected:
#             messagebox.showerror("錯誤", "請先連線")
#             return
        
#         selected_action = self.action_combo.get()
#         self.terminal_button.config(state="normal")
#         if selected_action:
#             self.console_text.insert(tk.END, f"執行 {selected_action}...\n")
#             text = self.adb_func.run_adb_func(selected_action, self.param_entry.get())
#             self.console_text.insert(tk.END, f"{text}")
#         else:
#             messagebox.showerror("錯誤", "請選擇一個操作")
        
#         self.console_text.yview_moveto(1.0)

#     def terminal(self):
#         self.execute_button.config(state="normal")
#         self.terminal_button.config(state="disabled")
#         selected_action = self.action_combo.get()
#         text = self.adb_func.interrupt_function()
#         self.console_text.insert(tk.END, f"{text}")
#         self.console_text.insert(tk.END, f"強制中斷 {selected_action} 正在執行的動作 \n")

#     def on_device_selected(self, event):
#         # if not self.connected:
#         #     messagebox.showerror("錯誤", "請先連線")
#         self.wifi_value = self.adb_func.get_wifi(self.device_combo.get())
#         self.wifi_ip_var.set(self.wifi_value)

#     def on_action_selected(self, event):
#         if self.action_combo.get() == "取得裝置Log":
#             self.param_label.config(state="normal")
#             self.param_entry.config(state="normal")
#         else:
#             self.param_label.config(state="disabled")
#             self.param_entry.config(state="disabled")
#         if not self.connected:
#             messagebox.showerror("錯誤", "請先連線")
    


# import tkinter as tk
# from tkinter import ttk, messagebox
# from adb_func import *
# import threading

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.adb_func = ADBFunction()
#         self.current_thread = None
#         self.title("cmd工具")
#         self.geometry("600x350")

#         # 定義介面元素
#         self.device_label = tk.Label(self, text="機種:")
#         self.device_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

#         self.device_combo = ttk.Combobox(self, values=self.adb_func.get_device_name())
#         self.device_combo.grid(row=0, column=1, padx=5, pady=5, sticky='w')

#         self.wifi_ip_label = tk.Label(self, text="wifi ip:")
#         self.wifi_ip_label.grid(row=0, column=2, padx=5, pady=5, sticky='e')

#         self.wifi_ip_var = tk.StringVar()
#         self.wifi_ip_entry = tk.Entry(self, textvariable=self.wifi_ip_var, state='readonly')
#         self.wifi_ip_entry.grid(row=0, column=3, padx=5, pady=5, sticky='w')

#         self.connect_button = tk.Button(self, text="連線", command=self.connect)
#         self.connect_button.grid(row=0, column=4, padx=5, pady=5)

#         self.disconnect_button = tk.Button(self, text="斷線", command=self.disconnect, state='disabled')
#         self.disconnect_button.grid(row=0, column=5, padx=5, pady=5)

#         self.action_label = tk.Label(self, text="操作:")
#         self.action_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

#         self.action_combo = ttk.Combobox(self, state='disabled', width=25, values= self.adb_func.get_func_name())
#         self.action_combo.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='w')

#         self.param_label = tk.Label(self, text="參數:", state= 'disabled')
#         self.param_label.grid(row=1, column=2, padx=5, pady=5, sticky='e')

#         self.param_entry = tk.Entry(self, state='disabled', width= 20)
#         self.param_entry.grid(row=1, column= 3, padx=5, pady=5, sticky='w')

#         self.execute_button = tk.Button(self, text="執行", command=self.execute, state='disabled')
#         self.execute_button.grid(row=1, column=4, padx=5, pady=5)

#         self.terminal_button = tk.Button(self, text="中斷", state="disabled", command=self.terminal)
#         self.terminal_button.grid(row=1, column=5, padx=5, pady=5)

#         self.text_frame = tk.Frame(self)
#         self.text_frame.grid(row = 2, column= 0, columnspan= 10, padx= 5, pady= 5, sticky= "nsew")
#         self.console_text = tk.Text(self.text_frame, bg="black", fg="white", wrap= "word")
#         self.console_text.pack(side= tk.LEFT, fill = tk.BOTH, expand= True)
#         self.scrollbar = ttk.Scrollbar(self.text_frame, orient= tk.VERTICAL, command=self.console_text.yview)
#         self.scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
#         self.console_text.config(yscrollcommand= self.scrollbar.set)

#         # 設定規則
#         self.device_combo.bind("<<ComboboxSelected>>", self.on_device_selected)
#         self.action_combo.bind("<<ComboboxSelected>>", self.on_action_selected)
#         self.connected = False

#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure(2, weight=1)
#         self.grid_columnconfigure(3, weight=1)
#         self.grid_columnconfigure(4, weight=1)
#         self.grid_rowconfigure(2, weight=1)

#     def connect(self):
#         # 模擬連線動作
#         self.console_text.insert(tk.END, "連線中...\n")
#         self.connected = True
#         # self.wifi_ip_var.set("192.168.1.1")  # 假設生成IP
#         text = self.adb_func.adb_connect(self.wifi_value)
#         # self.console_text.insert(tk.END, "Connected!\n")
#         self.console_text.insert(tk.END, f"{text}")
#         self.console_text.insert(tk.END, "已連接至目標裝置\n")
#         self.console_text.yview_moveto(1.0)
#         self.action_combo.config(state='normal')
#         self.execute_button.config(state='normal')
#         self.disconnect_button.config(state='normal')

#     def disconnect(self):
#         # 模擬斷線動作
#         # self.console_text.insert(tk.END, "Disconnecting...\n")
#         self.connected = False
#         # self.wifi_ip_var.set("")  # 清除IP
#         self.console_text.insert(tk.END, "斷開連接中...\n")
#         text = self.adb_func.adb_kill_server()
#         # print(text)
#         self.console_text.insert(tk.END, "已斷線\n\n")
#         self.console_text.yview_moveto(1.0)    
#         self.action_combo.config(state='disabled')
#         self.execute_button.config(state='disabled')
#         self.disconnect_button.config(state='disabled')
#         self.terminal_button.config(state="disabled")

#     def execute(self):
#         if not self.connected:
#             messagebox.showerror("錯誤", "請先連線")
#             return
#         selected_action = self.action_combo.get()
#         self.terminal_button.config(state="normal")
#         if selected_action:
#             self.console_text.insert(tk.END, f"執行 {selected_action}...\n")
#             def run_command():
#                 text = self.adb_func.run_adb_func(selected_action, self.param_entry.get())
#                 self.console_text.insert(tk.END, f"{text}")
#                 self.console_text.yview_moveto(1.0)
#             self.current_thread = threading.Thread(target=run_command)
#             self.current_thread.start()
#             # text = self.adb_func.run_adb_func(selected_action, self.param_entry.get())
#             # self.console_text.insert(tk.END, f"{text}")
#         else:
#             messagebox.showerror("錯誤", "請選擇一個操作")
        
#         self.console_text.yview_moveto(1.0)

#     def terminal(self):
#         self.terminal_button.config(state="disabled")
#         self.disconnect_button.config(state="disabled")
#         self.execute_button.config(state="disabled")
#         selected_action = self.action_combo.get()
#         # self.second_thread = threading.Thread(target=self.adb_func.interrupt)
#         # self.second_thread.start()
#         self.adb_func.interrupt()
#         self.console_text.insert(tk.END, f"強制中斷 {selected_action} 正在執行的動作 \n")
#         self.action_combo.set(value= "")
#         self.action_combo.config(state='disabled')
#         self.param_entry.delete(0, 'end')
#         self.param_entry.config(state='disabled')
#         self.param_label.config(state='disabled')

#     def on_device_selected(self, event):
#         # if not self.connected:
#         #     messagebox.showerror("錯誤", "請先連線")
#         self.wifi_value = self.adb_func.get_wifi(self.device_combo.get())
#         self.wifi_ip_var.set(self.wifi_value)

#     def on_action_selected(self, event):
#         if self.action_combo.get() == "取得裝置Log":
#             self.param_label.config(state="normal")
#             self.param_entry.config(state="normal")
#         else:
#             self.param_label.config(state="disabled")
#             self.param_entry.config(state="disabled")
#         if not self.connected:
#             messagebox.showerror("錯誤", "請先連線")
    

import tkinter as tk
from tkinter import ttk, messagebox
from adb_func import *
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.adb_func = ADBFunction()
        self.current_thread = None
        self.title("cmd工具")
        self.stop_event = threading.Event()
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{int(self.screen_width)//2}x{int(self.screen_height//1.45)}+{(self.screen_width)//4}+{(self.screen_height)//6}")
        #定義字體
        self.default_font = ("Microsoft JhengHei", int(12*(self.screen_height/1080)))
        self.bold_font = ("Microsoft JhengHei", int(12*(self.screen_height/1080)), "bold")
        # 定義介面元素
        self.checkbox_var = tk.BooleanVar()
        self.check_box = ttk.Checkbutton(self, variable=self.checkbox_var, text="視窗置頂", command=self.topmost_window)
        self.check_box.grid(row=0, column=5, padx=5, pady=5, sticky='ne')

        self.device_label = tk.Label(self, text="機種:", font=self.bold_font)
        self.device_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        self.device_combo = ttk.Combobox(self, values=self.adb_func.get_device_name(), font=self.default_font)
        self.device_combo.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.wifi_ip_label = tk.Label(self, text="wifi ip:", font=self.bold_font)
        self.wifi_ip_label.grid(row=1, column=2, padx=5, pady=5, sticky='e')

        self.wifi_ip_var = tk.StringVar()
        self.wifi_ip_entry = tk.Entry(self, textvariable=self.wifi_ip_var, state='readonly', font=self.default_font)
        self.wifi_ip_entry.grid(row=1, column=3, padx=5, pady=5, sticky='w')

        self.connect_button = tk.Button(self, text="連線", command=self.connect, font= self.bold_font)
        self.connect_button.grid(row=1, column=4, padx=5, pady=5)

        self.disconnect_button = tk.Button(self, text="斷線", command=self.disconnect, state='disabled', font= self.bold_font)
        self.disconnect_button.grid(row=1, column=5, padx=5, pady=5)

        self.action_label = tk.Label(self, text="操作:", font=self.bold_font)
        self.action_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

        self.action_combo = ttk.Combobox(self, state='disabled', width=int(25*self.screen_width/1920), values=self.adb_func.get_func_name(), font= self.default_font)
        self.action_combo.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky='w')

        self.param_label = tk.Label(self, text="參數:", state='disabled', font=self.bold_font)
        self.param_label.grid(row=2, column=2, padx=5, pady=5, sticky='e')

        self.param_entry = tk.Entry(self, state='disabled', width=int(25*self.screen_width/1920), font= self.default_font)
        self.param_entry.grid(row=2, column=3, padx=5, pady=5, sticky='w')

        self.execute_button = tk.Button(self, text="執行", command=self.execute, state='disabled', font= self.bold_font)
        self.execute_button.grid(row=2, column=4, padx=5, pady=5)

        self.terminal_button = tk.Button(self, text="中斷", state="disabled", command=self.terminal, font= self.bold_font)
        self.terminal_button.grid(row=2, column=5, padx=5, pady=5)

        self.text_frame = tk.Frame(self)
        self.text_frame.grid(row=3, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")
        self.console_text = tk.Text(self.text_frame, bg="black", fg="white", wrap="word", font= ("Microsoft JhengHei", int(15*self.screen_height/1080)))
        self.console_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = ttk.Scrollbar(self.text_frame, orient=tk.VERTICAL, command=self.console_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.console_text.config(yscrollcommand=self.scrollbar.set)

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
        self.console_text.insert(tk.END, "連線中...\n")
        self.connected = True
        text = self.adb_func.adb_connect(self.wifi_value)
        self.console_text.insert(tk.END, f"{text}")
        self.console_text.insert(tk.END, "已連接至目標裝置\n")
        self.console_text.yview_moveto(1.0)
        self.action_combo.config(state='normal')
        self.execute_button.config(state='normal')
        self.disconnect_button.config(state='normal')

    def disconnect(self):
        self.connected = False
        self.console_text.insert(tk.END, "斷開連接中...\n")
        text = self.adb_func.adb_kill_server()
        self.console_text.insert(tk.END, "已斷線\n\n")
        self.console_text.yview_moveto(1.0)
        self.action_combo.config(state='disabled')
        self.execute_button.config(state='disabled')
        self.disconnect_button.config(state='disabled')
        self.terminal_button.config(state="disabled")

    def execute(self):
        if not self.connected:
            messagebox.showerror("錯誤", "請先連線")
            return
        selected_action = self.action_combo.get()
        self.terminal_button.config(state="normal")
        if selected_action:
            self.console_text.insert(tk.END, f"執行 {selected_action}...\n")
            self.stop_event.clear()
            self.current_thread = threading.Thread(target=self.run_command, args=(selected_action,))
            self.current_thread.start()
        else:
            messagebox.showerror("錯誤", "請選擇一個操作")
        self.console_text.yview_moveto(1.0)

    def run_command(self, action):
        def callback(output):
            self.console_text.after(0, self.update_console, output)
        self.adb_func.run_adb_func(action, self.param_entry.get(), callback)

    def update_console(self, output):
        try:
            self.console_text.insert(tk.END, output)
            self.console_text.yview_moveto(1.0)
        except tk.TclError as e:
            print(f"TclError: {e}")

    def terminal(self):
        self.terminal_button.config(state="disabled")
        self.disconnect_button.config(state="disabled")
        self.execute_button.config(state="disabled")
        self.adb_func.interrupt()
        selected_action = self.action_combo.get()
        self.console_text.insert(tk.END, f"強制中斷 {selected_action} 正在執行的動作 \n")
        self.action_combo.set(value="")
        self.action_combo.config(state='disabled')
        self.param_entry.delete(0, 'end')
        self.param_entry.config(state='disabled')
        self.param_label.config(state='disabled')

    def on_device_selected(self, event):
        self.wifi_value = self.adb_func.get_wifi(self.device_combo.get())
        self.wifi_ip_var.set(self.wifi_value)

    def on_action_selected(self, event):
        if self.action_combo.get() == "取得裝置Log":
            self.param_label.config(state="normal")
            self.param_entry.config(state="normal")
        else:
            self.param_label.config(state="disabled")
            self.param_entry.config(state="disabled")
        if not self.connected:
            messagebox.showerror("錯誤", "請先連線")
    
    def topmost_window(self):
        if self.checkbox_var.get():
            self.wm_attributes("-topmost", 1)
        else:
            self.wm_attributes("-topmost", 0)