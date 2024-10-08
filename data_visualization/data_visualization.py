# import libaries matplotlib and pandas
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pandas as pd

# Example-data: Numbers from 0 to 9 and their squares and cubes
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**2 for i in x] # squares
z = [i**3 for i in x] # cubes

# Create line chart
plt.plot(x, y, label='square numbers')
plt.plot(x, z, label='cubic numbers')

# Add titles and axis labels
plt.title('Square and cubic numbers from 0 to 9')
plt.xlabel('number')
plt.ylabel('cubes and squares')

# Show legend
plt.legend()

# Print png
plt.savefig('data.visualization.png')

# Show diagramm
plt.show()

# Create a simple Panda DataFrame
data = {
    "numbers": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "squares": [i**2 for i in x],
    "cubes": [i**3 for i in x]

}

# load data into a DataFrame object:
df = pd.DataFrame(data)

# save diagramm
df.to_csv('number.csv', sep='\t', encoding='utf-8')
