import pandas as pd
import matplotlib.pyplot as plt

# run in terminal: pip install numpy==1.19.3


if __name__ == '__main__':

    data = {
        'apples': [3, 2, 0, 1],
        'oranges': [0, 3, 7, 2]
    }

    purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

    print(purchases)

    print("\n-----------")
    print(purchases.loc['June'])

    print("\n-----------")
    print(purchases.info())

    print("\n-----------")
    print(purchases.shape)

    print("\n-----------")
    print(purchases.columns)

    print("\n-----------")
    print(purchases.isnull())

    # Removing null values
    purchases.dropna()

    print("\n-----------")
    print(purchases.describe())
    #count, mean, std, min, max

    plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})  # set font and plot size to be larger
    purchases.plot(kind='scatter', x='apples', y='oranges', title='Revenue (millions) vs Rating')
    # purchases['apples'].plot(kind='hist', title='Rating')

    df = pd.read_csv('C:/Users/apatsimas/Desktop/projects/sam/imports/asd.csv')
    print("\n-----------")
    print(df)

    df.to_json('new_purchases.json')

    df_json = pd.read_json('new_purchases.json')
    print("\n-----------")
    print(df_json)
