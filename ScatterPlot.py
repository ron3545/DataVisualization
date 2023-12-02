import matplotlib.pyplot as plt
import numpy as np

def create_robotics_scatter_plot():
    # Generating random data for demonstration
    np.random.seed(42)
    num_robots = 50
    robot_weights = np.random.uniform(5, 30, num_robots)
    robot_battery_life = np.random.uniform(10, 100, num_robots)

    # Creating the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(robot_weights, robot_battery_life, c='blue', marker='o', edgecolors='black', alpha=0.7)
    
    # Adding labels and title
    plt.title('Robotics Scatter Plot')
    plt.xlabel('Robot Weight (kg)')
    plt.ylabel('Battery Life (hours)')

    # Show the scatter plot
    plt.grid(True)
    plt.show()

# Call the function to create and display the scatter plot
create_robotics_scatter_plot()
