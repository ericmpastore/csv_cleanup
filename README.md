# csv_cleanup
The script cloud_cleanup.py is a tool to focus on null handling and normalization in CSV files with large null counts across multiple fields.

## Objective
The dataset used in this project is cloud_data.csv and looks at system performance metrics of several Virtual Machines (VMs) in a cloud computing environment.

The original goal of this project was to calculate energy efficiency and examine ways to reduce energy consumption.

The current goal of this project is to produce a clean data set for further analysis. 

## Process
Since the goal of this project is clean the dataset, primarily by handling nulls, the first priority was to do a quick exploration of the data. The next step was to determine what values should be in the data in order to determine how to fill null values.

The full process for this project is here:
1. Obtain the original dataset from Kaggle (https://www.kaggle.com/datasets/abdurraziq01/cloud-computing-performance-metrics/data).
2. Export a smaller subset of the data, since its original size was over 200MB.
3. Import the smaller subset into a DataFrame.
4. Start Exploratory Data Analysis (EDA) by taking distinct counts of vm_id. Result: All values are unique.
5. Continue profiling remaining data fields. Result: roughly 10% of all records per field were nulls.
6. Decide on the best method to handle nulls in each field.
7. Fill all null vm_ids using an incrementing id in the format 'zzzz-zzzz-####' where #### is a random number. This preserves the field as a unique identifier.
8. Fill all timestamps using a backwards fill from the previous timestamp, in order to preserve a similar timestamp distribution.
9. Fill all nulls in the cpu_usage, memory_usage, network_traffic, power_consumption, num_executed_instructions,execution_time, and energy_efficiency field with their mean values in order to preserve a similar distribution.
10. Fill all nulls in the task_type, task_priority, and task_status fields with 'unknown' to identify missing values and enable analysis of those specific records later.
11. Test script on full dataset and view descriptive statistics.

## Result
With the full dataset able to run and the descriptive statistics similar to the statistics on the sample data, the dataset was clean and ready for analysis.

In a real project, we would have already loaded the dataset to a data warehouse to be ready for reporting and visualization. We may perform that step in a future project.




