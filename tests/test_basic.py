import sotrends


def test_basic():
    data = sotrends.fetch_data(["c++"])
    plt = sotrends.plot(data)
    plt.show()
