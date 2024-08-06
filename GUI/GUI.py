import tkinter as tk
from tkinter import ttk
import requests
import json

class ApiTestApp():
    def __init__(self, root):
        self.root = root
        self.root.title('APITEST')
        self.root.geometry('300x400')

        # 创建URL输入框
        self.url_label = ttk.Label(root, text='URL:')
        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.url_input = ttk.Entry(root, width=50)
        self.url_input.grid(row=0, column=1, padx=10, pady=10)

        # 创建请求体输入框
        self.url_label = ttk.Label(root, text='DATA:')
        self.url_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.body_input = ttk.Entry(root, width=50)
        self.body_input.grid(row=1, column=1, padx=10, pady=10)

        # 创建请求方法下拉选择框
        self.method_combo = ttk.Combobox(root, width=20)
        self.method_combo['values'] = ('POST', 'GET')
        self.method_combo.current(0)
        self.method_combo.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # 创建发送按钮
        self.send_button = ttk.Button(root, text='Send', command=self.send_request)
        self.send_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        # 创建显示响应的文本区域
        self.response_text = tk.Text(root, wrap='word', width=50, height=10)
        self.response_text.grid(row=4, column=0, columnspan=2, pady=10)
        self.response_text.configure(state='disabled')

    def send_request(self):
        url = self.url_input.get()
        body = self.body_input.get()
        method = self.method_combo.get()

        if method == 'POST':
            try:
                body_data = json.loads(body)
                response = requests.post(url, json=body_data)
            except json.JSONDecodeError:
                self.response_text.configure(state='normal')
                self.response_text.delete('1.0', tk.END)
                self.response_text.insert(tk.END, 'Invalid JSON format for request body.')
                self.response_text.configure(state='disabled')
                return
        elif method == 'GET':
            response = requests.get(url)

        self.response_text.configure(state='normal')
        self.response_text.delete('1.0', tk.END)
        self.response_text.insert(tk.END, response.text)
        self.response_text.configure(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    app = ApiTestApp(root)
    root.mainloop()

