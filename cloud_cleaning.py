import pandas as pd

def handle_nulls(input_file):
    in_frame = pd.read_csv(input_file)
    
    return in_frame

def main():
    print(handle_nulls('cloud_data.csv').head(100))

if __name__ == "__main__":
    main()