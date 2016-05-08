import numpy as np
import matplotlib.pyplot as plt


# http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor
# http://stackoverflow.com/questions/25071968/heatmap-with-text-in-each-cell-with-matplotlibs-pyplot



def heatmap(data, title, xlabel, ylabel):
    plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    c = plt.pcolor(data, edgecolors='k', linewidths=4, cmap='RdBu', vmin=0.0, vmax=1.0)
    plt.colorbar(c)

def main():
    title = "ROC's AUC"
    xlabel = "Timeshift"
    ylabel = "Scales"
    data = np.random.rand(8, 12)
    heatmap(data, title, xlabel, ylabel)
    plt.show()


if __name__ == '__main__':
    main()