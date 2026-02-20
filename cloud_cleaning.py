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

    # Handle blank vm_ids with an incrementing id value, EPastore 02152026
    mask = output_frame['vm_id'].isna()
    null_count = mask.sum()
    output_frame.loc[mask,'vm_id'] = [f'zzzz-zzzz-{i:04d}' for i in range(1,null_count+1)]

    # Handle numerical nulls using fillna(mean), EPastore 02172026
    output_frame['cpu_usage'] = output_frame['cpu_usage'].fillna(output_frame['cpu_usage'].mean())
    output_frame['memory_usage'] = output_frame['memory_usage'].fillna(output_frame['memory_usage'].mean())
    output_frame['network_traffic'] = output_frame['network_traffic'].fillna(output_frame['network_traffic'].mean())
    output_frame['power_consumption'] = output_frame['power_consumption'].fillna(output_frame['power_consumption'].mean())
    output_frame['num_executed_instructions'] = output_frame['num_executed_instructions'].fillna(output_frame['num_executed_instructions'].mean())
    output_frame['execution_time'] = output_frame['execution_time'].fillna(output_frame['execution_time'].mean())
    output_frame['energy_efficiency'] = output_frame['energy_efficiency'].fillna(output_frame['energy_efficiency'].mean())

    # Handle timestamp nulls using the backwards fill method, EPastore 02162026
    output_frame['timestamp'] = output_frame['timestamp'].bfill()

    # Handle task field nulls with 'Unknown', EPastore 02172026
    output_frame['task_type'] = output_frame['task_type'].fillna('unknown')
    output_frame['task_priority'] = output_frame['task_priority'].fillna('unknown')
    output_frame['task_status'] = output_frame['task_status'].fillna('unknown')

    return output_frame

def main():
    """
    Docstring for main

    Executes all functions

    EPastore, 02/07/2026
    """
    clean_frame = clean_nulls(get_frame('C:\\Users\\epas0\\OneDrive\\vmCloud_data.csv'))
    sample_frame = clean_nulls(get_frame('cloud_data.csv'))
    print(clean_frame.describe())
    print(sample_frame.describe())

if __name__ == "__main__":
    main()