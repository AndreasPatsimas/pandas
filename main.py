import pandas as pd

# run in terminal: pip install numpy==1.19.3


if __name__ == '__main__':

    data = {
        'apples': [3, 2, 0, 1],
        'oranges': [0, 3, 7, 2]
    }

    purchases = pd.DataFrame(data)

    print(purchases)


