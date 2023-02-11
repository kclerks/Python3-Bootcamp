import psutil
import time
import csv

def calculate_network_bytes():
    net_io_counters = psutil.net_io_counters()
    return (net_io_counters.bytes_sent + net_io_counters.bytes_recv)

def bandwidth_usage(start_bytes, start_time):
    current_time = time.time()
    elapsed_time = current_time - start_time
    current_bytes = calculate_network_bytes()
    return (current_bytes - start_bytes) / elapsed_time

# Set the initial values for bytes received and start time
start_bytes = calculate_network_bytes()
start_time = time.time()

# Open a CSV file for writing
with open('bandwidth_usage.csv', 'w', newline='') as csvfile:
    fieldnames = ['Time', 'Bandwidth Usage (MB/s)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Continuously calculate and print bandwidth usage
    while True:
        # Calculate bandwidth usage
        usage = bandwidth_usage(start_bytes, start_time)

        # Write the current time and bandwidth usage to the CSV file
        writer.writerow({'Time': time.ctime(), 'Bandwidth Usage (MB/s)': usage / (1024 * 1024)})

        # Sleep for 1 second
        time.sleep(1)
