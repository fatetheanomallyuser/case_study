import pandas as pd
import os
import gc
from datetime import datetime




#Retrive the CSV file from the local drive
file_path = r"C:\Users\Pandas\Case Study\cc_data.csv"

#Error Handling if file is not found
if not os.path.exists(file_path):
    raise FileNotFoundError(f" The file at {file_path}does not exist. check path")

df = pd.read_csv(file_path)

# Find the single date where the calls is the highest
max_calls = df['Incoming Calls'].max()  
date_of_highest_calls  = df.loc[df['Incoming Calls'] == max_calls, ['Index','Date', 'Column1','Incoming Calls']]

#Convert the date strings into a format Pandas can retrive
df['Date'] = pd.to_datetime(df['Date'])


# Sort the data by the Incoming calls column
sorted_df = df.sort_values('Incoming Calls', ascending=False)


# Find 30 dates where the calls are the highest
top_30_highest_calls = sorted_df.head(30)

#find 30 dates where the calls are teh lowest
top_30_lowest_calls = sorted_df.tail(30)

# find the median value to recall and calculate for 25% - 35% within the median range.
median_value = df['Incoming Calls'].median()

# Calculation to find the the Median range of calls 25% - 35%
median_range_df = df[
    (df['Incoming Calls'] >= 2.5 * median_value) &
    (df['Incoming Calls'] <= 3.5 * median_value)
]


# Sort after the calculation for median values
top_30_median_calls = median_range_df.sort_values('Incoming Calls').head(30)

print("Top 30 Dates with Highest Calls:")
print(top_30_highest_calls[['Date', 'Incoming Calls']])

print("\nTop 30 Dates with Lowest Calls:")
print(top_30_lowest_calls[['Date', 'Incoming Calls']])

print("\nTop 30 Dates in the Median Range of Calls:")
print(top_30_median_calls[['Date', 'Incoming Calls']])




###### This section of the script will pull the log files from the server to compare with the "CC_data" ########


""" """ 
# Disable garbage collector to run smoother on CPU
gc.disable()

# Convert posix into readable date and time
def posix_to_date(posix_string):
    return datetime.utcfromtimestamp(int(posix_string))

# Retrieve log file by naming path where log files are located
log_file = r"C:\Users\Pandas\Case Study\logs.csv"

# Correct path for the timestamp file
timestamp_file = r"C:\Users\Pandas\Case Study\last_run_timestamp.txt"

# Function to save the file if file is new with the error handling "except" argument
def is_log_file_new(log_file, timestamp_file):
    file_savetime = os.path.getmtime(log_file)
    
    # Ensure the directory exists before creating the timestamp file
    timestamp_dir = os.path.dirname(timestamp_file)
    if not os.path.exists(timestamp_dir):
        os.makedirs(timestamp_dir)
    
    try:
        with open(timestamp_file, 'r') as f:
            last_timestamp = float(f.read().strip())
    except (FileNotFoundError, ValueError):
        # Assumes the file is new if no timestamp has been entered
        last_timestamp = 0

    # Update the referenced timestamp
    with open(timestamp_file, 'w') as f:
        f.write(str(file_savetime))

    # Return True if the file is new (or has been modified)
    return file_savetime > last_timestamp

# Retrieve the logfile if it is new
if is_log_file_new(log_file, timestamp_file):
    # Set 'get_logs' variable to the retrieved logs for easier recall
    get_logs = pd.read_csv(log_file, header=0, index_col=0)

    # Store data into HDFStore for file compression and easier recall in the future
    def store_data(store):
        with pd.HDFStore('log_data.h5', complib='blosc') as store:
            store['all_logs'] = get_logs

    store_data(get_logs)


# Enable garbage collection after data is retrieved
gc.enable() 