import requests
import pandas
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# NewEngland = c("CONNECTICUT", "MAINE", "MASSACHUSETTS", "NEW_HAMPSHIRE", "RHODE_ISLAND", "VERMONT"),
#   MiddleAtlantic = c("DELAWARE", "MARYLAND", "NEW_JERSEY", "NEW_YORK", "PENNSYLVANIA"), 
#   South = c("ALABAMA", "ARKANSAS", "FLORIDA", "GEORGIA", "KENTUCKY", "LOUISIANA", "MISSISSIPPI", "MISSOURI", "NORTH_CAROLINA", "SOUTH_CAROLINA", "TENNESSEE", "VIRGINIA", "WEST_VIRGINIA"),
#   Midwest = c("ILLINOIS", "INDIANA", "IOWA", "KANSAS", "MICHIGAN", "MINNESOTA", "NEBRASKA", "NORTH_DAKOTA", "OHIO", "SOUTH_DAKOTA", "WISCONSIN"), 
#   Southwest = c("ARIZONA", "NEW_MEXICO", "OKLAHOMA", "TEXAS"), 
#   West = c("ALASKA", "CALIFORNIA", "HAWAII", "IDAHO", "MONTANA", "NEVADA", "OREGON", "UTAH", "WASHINGTON", "WYOMING", "COLORADO"),
#   Other = c("DISTRICT_OF_COLUMBIA", "DODEA", "NATIONAL")

def main():
    url = 'https://datausa.io/api/data?drilldowns=State&measures=Population'
    r = requests.get(url)
    print(r.json())
    df = pandas.DataFrame(r.json()['data'])
    print(df.head())
    # get dimensions of df
    print(df.shape)
    sns.lineplot(x=df.Year, y=df.Population, hue=df.State)
    plt.show()


if __name__ == '__main__':
    main()