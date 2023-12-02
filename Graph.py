import matplotlib.pyplot as plt
import numpy as np

def create_up_and_down_graph():
    num_points = 100
    x_values = np.linspace(0, 4 * np.pi, num_points)
    y_values = np.sin(x_values)  # Use a sine function for an up-and-down pattern

    plt.plot(x_values, y_values, linestyle='-', color='b')
    plt.title('Up-and-Down Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    create_up_and_down_graph()
