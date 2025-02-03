from matplotlib import pyplot as plt

#plt.style.available #shows all available styles
plt.style.use("Solarize_Light2")

ages_x = [25,26,27,28,29,30,31,32,33,34,35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


plt.plot(ages_x, dev_y,color="black" ,linestyle='--', marker='.', linewidth=3, label = 'All Devs')
plt.plot(ages_x, py_dev_y ,color="blue",marker='o',linewidth=5,label = 'Python Devs')
plt.plot(ages_x, js_dev_y ,color="orange",marker='o',label = 'JS Devs')

plt.grid(True)

plt.legend()

plt.tight_layout() # makes a difference on smaller screens


plt.title("Median Salary (USD) by age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.savefig("plot.png")
plt.show()

