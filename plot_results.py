import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator


def plot_results(results, title=None, slant_x_ticks=False):
    if not results:
        return

    ordered = sorted(results, key=lambda result: result["size"])
    sizes = [result["size"] for result in ordered]
    times = [result["time"] for result in ordered]
    indices = [result["index"] for result in ordered]
    iterations = [result["iterations"] for result in ordered]
    func_name = ordered[0]["func"]
    chart_title = title or func_name

    fig, ax = plt.subplots()
    y_positions = list(range(len(sizes)))
    bars = ax.barh(y_positions, times)
    ax.bar_label(
        bars,
        labels=[
            f"index={index}\niterations={count}\ntime={time:.3f} ms"
            for index, count, time in zip(indices, iterations, times)
        ],
        padding=3,
        fontsize=9,
    )
    ax.set_xlabel("time (ms)")
    ax.set_ylabel("size")
    ax.set_yticks(y_positions, labels=[f"{size:,}" for size in sizes])
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    if slant_x_ticks:
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    ax.invert_yaxis()
    fig.suptitle(chart_title)
    plt.show()
