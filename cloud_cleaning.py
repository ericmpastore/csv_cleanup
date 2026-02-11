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

def clean_nulls(input_frame):
    """
    Docstring for clean_nulls

    Imports a DataFrame and performs null handling operations on all fields

    EPastore, 02/09/2026
    
    :param input_frame: takes in a DataFrame
    """
    output_frame = input_frame

    # Handle numerical nulls using fillna(0)
    output_frame['vm_id'] = output_frame['vm_id'].dropna()
    output_frame['cpu_usage'] = output_frame['cpu_usage'].fillna(0)
    output_frame['memory_usage'] = output_frame['memory_usage'].fillna(0)

    # Handle timestamp nulls

    # Handle task field nulls

    return output_frame

def main():
    """
    Docstring for main

    Executes all functions

    EPastore, 02/07/2026
    """
    print(clean_nulls(get_frame('cloud_data.csv').head(100)))
    print(get_frame('cloud_data.csv').describe())

if __name__ == "__main__":
    main()