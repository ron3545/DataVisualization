import matplotlib.pyplot as plt

def create_robotics_pie_chart():
    # Data for the pie chart
    components = ['Sensors', 'Actuators', 'Microcontrollers', 'Power Supply', 'Mechanical Parts']
    percentages = [25, 20, 20, 15, 20]

    # Plotting the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(percentages, labels=components, autopct='%1.1f%%', startangle=140, colors=['blue', 'orange', 'green', 'red', 'purple'])
    plt.title('Robotics Project Components')
    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

    # Show the pie chart
    plt.show()

# Call the function to create and display the pie chart
create_robotics_pie_chart()
