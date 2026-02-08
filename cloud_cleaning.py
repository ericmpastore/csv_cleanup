import pandas as pd

def get_frame(input_file):
    """
    Docstring for get_frame

    Imports data from input_file and exports DataFrame

    EPastore, 02/08/2026
    
    :param input_file: identifies the input CSV file containing data
    """
    in_frame = pd.read_csv(input_file)
    
    return in_frame

def main():
    """
    Docstring for main

    Executes all functions

    EPastore, 02/07/2026
    """
    print(get_frame('cloud_data.csv').head(100))

if __name__ == "__main__":
    main()