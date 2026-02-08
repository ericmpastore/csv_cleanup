# csv_cleanup
The script cloud_cleanup.py is a tool to focus on null handling and normalization in CSV files with large null counts across multiple fields.

## Objective
The dataset used in this project is cloud_data.csv and looks at system performance metrics of several Virtual Machines (VMs) in a cloud computing environment.

The original goal of this project was to calculate energy efficiency and examine ways to reduce energy consumption.

The current goal of this project is to produce a clean data set for further analysis. 

## Process
Since the goal of this project is clean the dataset, primarily by handling nulls, the first priority is to do a quick exploration of the data. The next step is determine what values should be in the data in order to determine how to fill null values.

The full process for this project is here:
1. Obtain the original dataset from Kaggle (https://www.kaggle.com/datasets/abdurraziq01/cloud-computing-performance-metrics/data).
2. Export a smaller subset of the data, since its original size was over 200MB.
3. Import the smaller subset into a DataFrame.
4. Start Exploratory Data Analysis (EDA) by taking distinct counts of vm_id.

## Data Dictionary
(Coming Soon)




