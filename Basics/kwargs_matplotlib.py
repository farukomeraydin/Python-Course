import math
import matplotlib.pyplot as plt

xpoints = []
ypoints = []

x = -6.
while x <= 6:
    xpoints.append(x)
    ypoints.append(math.sin(x))
    x += 0.01
    
plt.title('Sinüs Grafiği', fontsize=18, color='blue', pad=20, fontstyle='italic')        
plt.plot(xpoints, ypoints, color='red', linewidth=6, linestyle='--', alpha=0.5)
plt.text(2, -0.50, 'Test', fontsize=16, color='green', fontweight='bold')
plt.show()
