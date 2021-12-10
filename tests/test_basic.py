import sotrends


def test_basic():
    data = sotrends.fetch_data(["c++"])
    plt = sotrends.plot_per_day(data)
    plt.show()
