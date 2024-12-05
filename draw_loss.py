import matplotlib.pyplot as plt

precision = [0.32,0.82,1.00,0.98,0.54,0.71,0.81,0.93,0.81,0.64]

recall = [1,2,3,4,5,6,7,8,9,10]

plt.plot(recall, precision, linewidth=3, color='r')  # 将列表传递给plot,并设置线宽，设置颜色，默认为蓝色
plt.title("loss_box", fontsize=20, color='b')  # 设置标题，并给定字号,设置颜色
plt.xlabel("", fontsize=14, color='g')  # 设置轴标题，并给定字号,设置颜色
plt.ylabel("", fontsize=14, color='g')

a = 10
plt.xticks(recall)
plt.yticks([1/a, 2/a, 3/a, 4/a, 5/a, 6/a, 7/a, 8/a, 9/a, 10/a])  # 设置x和y轴的刻度

plt.tick_params(axis='both', labelsize=14)  # 设置刻度标记的大小
plt.show()  # 显示