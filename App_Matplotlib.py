import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def plot_country_cases(country_filter):
    df=pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv")
    country=make_valid_name(country_filter)
    if country in df.countriesAndTerritories.values:
        d1 = df[(df['countriesAndTerritories'] == country)]

        fig, ax = plt.subplots(1, 1)
        fig.set_size_inches(18.5, 10.5, forward=True)

        ax.plot(d1.dateRep, d1.cases)

        ax.set_xticks(d1.dateRep[::5])
        plt.xticks(rotation=75,size=13)
        ax.invert_xaxis()

        plt.title(country_filter,size=20)
        ax.set_xlabel('Date',size=15)
        ax.set_ylabel('Number of Cases',size=15)
        # plt.savefig("italy_cases.jpg", dpi=200)
        plt.show(block=False)
    else:
        print("not a valid country")


def make_valid_name(name:str):
    return name.capitalize()


# plot_country_cases("Italy")