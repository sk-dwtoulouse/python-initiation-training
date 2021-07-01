"""
Pandas getting started script.

Pandas introduction demo script for Python beginners.
Makes a few calls taken from the official docs to see what can be done
with Pandas.

See Also:
https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html

"""
import pandas as pd

if __name__ == "__main__":
    # Read dataframe from CSV file
    frame: pd.DataFrame = pd.read_excel("files/demo-file-1000.xls")
    # Get basic information on data
    print(frame.dtypes)

    # Access, within column zero, to all rows
    for row in frame["First Name"]:
        print(row)

    # Make the equivalent to a SELECT WHERE query
    # Get a frame where the age column is >= 40
    print(frame[frame["Age"] >= 40])
