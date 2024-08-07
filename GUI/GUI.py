import tkinter as tk
from tkinter import ttk
import requests
import json

class ApiTestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('APITEST')
        self.geometry('500x450')
        self.configure(padx=10, pady=10)
        self.resizable(False, False)

        # 创建输入框架
        input_frame = ttk.LabelFrame(self, text="Request")
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # 创建URL输入框
        self.url_label = ttk.Label(input_frame, text='URL:')
        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.url_input = ttk.Entry(input_frame, width=50)
        self.url_input.grid(row=0, column=1, padx=10, pady=10)

        # 创建请求体输入框
        self.body_label = ttk.Label(input_frame, text='DATA:')
        self.body_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.body_input = ttk.Entry(input_frame, width=50)
        self.body_input.grid(row=1, column=1, padx=10, pady=10)

        # 创建请求方法下拉选择框
        self.method_label = ttk.Label(input_frame, text='Method:')
        self.method_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.method_combo = ttk.Combobox(input_frame, width=20)
        self.method_combo['values'] = ('POST', 'GET')
        self.method_combo.current(0)
        self.method_combo.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # 创建发送按钮
        self.send_button = ttk.Button(input_frame, text='Send', command=self.send_request)
        self.send_button.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        # 创建显示响应的文本区域框架
        response_frame = ttk.LabelFrame(self, text="Response")
        response_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # 创建显示响应的文本区域
        self.response_text = tk.Text(response_frame, wrap='word', width=50, height=10)
        self.response_text.pack(padx=10, pady=10)
        self.response_text.configure(state='disabled')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def send_request(self):
        url = self.url_input.get()
        body = self.body_input.get()
        method = self.method_combo.get()

        try:
            if method == 'POST':
                body_data = json.loads(body)
                response = requests.post(url, json=body_data)
            elif method == 'GET':
                response = requests.get(url)

            self.response_text.configure(state='normal')
            self.response_text.delete('1.0', tk.END)
            self.response_text.insert(tk.END, response.text)
            self.response_text.configure(state='disabled')

        except json.JSONDecodeError:
            self.response_text.configure(state='normal')
            self.response_text.delete('1.0', tk.END)
            self.response_text.insert(tk.END, 'Invalid JSON format for request body.')
            self.response_text.configure(state='disabled')

        except requests.RequestException as e:
            self.response_text.configure(state='normal')
            self.response_text.delete('1.0', tk.END)
            self.response_text.insert(tk.END, str(e))
            self.response_text.configure(state='disabled')

if __name__ == '__main__':
    app = ApiTestApp()
    app.mainloop()


