# case_study
This is a case study based on a real-life situation

Case Study: Network Infrastructure and Log Analysis for Latency Improvement
Freelancer Consultant Project

Objective: This case study involves the analysis of network infrastructure and logs for a small to medium-sized company. The goal is to identify symptoms of network issues, latency, and potential security vulnerabilities. The company does not have a dedicated Security Operations Center (SOC) and has a small operations department responsible for data collection. My task is to analyze network traffic through a SaaS platform, identify bottlenecks, and propose improvements for hardening the network.

Scripts Overview:

Script 1: Network Traffic and Log Analysis

This script is designed to:

Retrieve and analyze a CSV file (cc_data.csv) containing incoming call data through the company's SaaS platform.
Identify the day with the highest number of incoming calls.
Sort and retrieve the top 30 dates with the highest and lowest calls.
Calculate the median number of calls and find dates where the number of incoming calls falls within a specific range (25% - 35% of the median value).
Retrieve log files (logs.csv) from the server and compare them with the call data to identify potential issues, such as abnormal spikes or discrepancies.
The script also includes error handling for missing files, and functionality to store log data in a compressed format for future analysis.
Key Functions:

posix_to_date: Converts POSIX timestamp to a readable date.
is_log_file_new: Checks whether the log file is new or has been modified since the last check, ensuring only new data is processed.
store_data: Stores the processed log data in an HDF5 file for efficient storage and retrieval.
Script 2: Log File Analysis

This script focuses on analyzing the log data in logs.csv:

It reads the log file and converts the timestamp to a readable date.
It sorts the log entries by time and extracts key information such as process ID (Pid), event ID, content, and log records.
The script then outputs the top 10 most recent log entries based on the timestamp for further investigation.
How to Use:

Data Files:

cc_data.csv: Contains the incoming call data for analysis.
logs.csv: Contains log data from the server to analyze network-related events.
Script Execution:

Make sure the required CSV files are located in the specified directories.
Run Script 1 to analyze the call data and log files. This will output the top 30 highest/lowest call days and the dates within the median range.
Run Script 2 to analyze the most recent log entries and display key process information.
Possible Improvements:

Network traffic bottlenecks and spikes in incoming calls could indicate performance issues that need addressing, such as optimizing server capacity or adjusting network configurations.
Log analysis might reveal unusual patterns or errors that could point to network-related problems or security vulnerabilities.
By identifying these issues, I will propose recommendations to improve network performance, fix latency issues, and harden the overall infrastructure against potential risks.
