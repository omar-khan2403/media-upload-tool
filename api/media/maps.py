import pandas as pd

def check_csv(csv_file):

    df = pd.read_csv(csv_file)

    # check df columns to see if there is longitude and latitude
    required = ['longitude', 'latitude']
    columns = [col.lower() for col in list(df.columns)]

    if all(x in columns for x in required) is True:
        return True

    else: 
        return False


def read_csv(csv_file):

    metadata = None

    return metadata