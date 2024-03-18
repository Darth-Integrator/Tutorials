import matplotlib.pyplot as plt

# 7,18,2,4,5,5,1,8,8,25,3,6,4,17,1,19,6,2

# Setting up title & plot sizes
plt.figure(figsize = (10, 5))
plt.suptitle("Ettore Majorana's Mystery")

# 1st sub plot
plt.subplot(121)
xValues = [7, 2, 5, 1]
yValues = [18, 4, 5, 8]
plt.axis([0, 15, 0, 20])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.plot([xValues], [yValues], 'ro')

# 2nd sub plot
plt.subplot(122)
uValues = [8, 3, 4, 1, 6]
vValues = [25, 6, 17, 19, 2]
plt.axis([0, 10, 0, 25])
plt.xlabel('U Values')
plt.ylabel('V Values')
plt.plot([uValues], [vValues], 'b^')

plt.show()