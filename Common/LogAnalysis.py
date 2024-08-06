import re
from collections import defaultdict
import matplotlib.pyplot as plt

filename = r"D:\APP\VS2022\project\Gtest\Gtest\test1.log"
data = defaultdict(int)

# 用正则表达式提取每行中的 "CallbacksPerSecond" 后面的数值
pattern = r'CallbacksPerSecond: (\d+)(\d+)'

with open(filename, 'r') as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            value = int(match.group(2))
            data[value] += 1
            print(match)

# 提取数据用于绘制条形图
x = list(data.keys())
values = list(data.values())

# 绘制竖直条形图
plt.figure(figsize=(10, 6))
bars = plt.bar(x, values)
plt.xlabel('Callbacks Per Second')
plt.ylabel('Frequency')
plt.title('Frequency of Callbacks Per Second in Log File')

# 设置底部坐标轴刻度为连续显示的方式
plt.xticks(range(min(x), max(x) + 1))

# 在每个条形上方显示具体的数值
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(value), ha='center', va='bottom')

plt.tight_layout()

# 统计并打印数据条数
total_records = sum(values)
print(f"Total records in log file: {total_records}")

# 显示图形
plt.show()
