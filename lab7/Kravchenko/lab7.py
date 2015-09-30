import matplotlib.pyplot as plt
from math import log, sin

funcs = dict()
funcs['pow'] = lambda x: x ** 1.5
funcs['linear'] = lambda x: x
funcs['nlogn'] = lambda x: x * log(x)
funcs['sin'] = lambda x: sin(x) * 100


def example_plot(fig, ax):
    xrng = xrange(1, 100, 10)
    for name, func in funcs.iteritems():
        ax.plot(xrng, map(func, xrng), label=name)

    ax.set_xlabel('size', fontsize=8)
    ax.set_ylabel('ms', fontsize=8)
    ax.set_title('random [0, 10000]', fontsize=8)


def show_grid():
    fig = plt.figure()
    for i in xrange(2):
        for j in xrange(3):
            ax = plt.subplot2grid((2, 3), (i, j))
            example_plot(fig, ax)
    plt.legend(loc='upper left', title="funcs")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    show_grid()
