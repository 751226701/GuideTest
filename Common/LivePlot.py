import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class LivePlot:
    def __init__(self, data_generator, xlim=100, ylim=(0, 70), interval=1000):
        self.data_generator = data_generator
        self.data_x = []
        self.data_y = []

        self.xlim = xlim

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.ax.set_xlim(0, xlim)
        self.ax.set_ylim(ylim)  # 初始 y 轴范围
        self.ax.set_xlabel('Time (minutes)')
        self.ax.set_ylabel('Random Value')
        self.ax.set_title('Live Data Plot')

        self.ani = animation.FuncAnimation(
            self.fig, self.update, init_func=self.init, frames=None,
            interval=interval, repeat=False, save_count=99999
        )

    def init(self):
        self.line.set_data([], [])
        return self.line,

    def update(self, frame):
        self.data_x.append(frame)
        self.data_y.append(self.data_generator())

        # 更新数据
        self.line.set_data(self.data_x, self.data_y)

        # 动态调整x轴范围
        if len(self.data_x) > self.xlim:
            self.ax.set_xlim(self.data_x[-self.xlim], self.data_x[-1])
        else:
            self.ax.set_xlim(0, self.xlim)

        # 动态调整y轴范围
        if self.data_y:
            min_y = min(self.data_y)
            max_y = max(self.data_y)
            margin = 10  # 可以调整的边距以避免数据点紧贴边界
            self.ax.set_ylim(min_y - margin, max_y + margin)

        return self.line,

    def show(self):
        plt.show()


def random_data():
    return np.random.randint(20, 61)

if __name__ == '__main__':
    plot = LivePlot(data_generator=random_data, interval=1000)
    plot.show()
