# A small utility program that tracks how much data you have uploaded and downloaded from the net during the course 
# of your current online session. 
# See if you can find out what periods of the day you use more and less and generate a report or graph that shows it.
import time
import psutil

def main():
    old_value = 0    

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        time.sleep(1)

def convert_to_gbit(value):
    return value # /1024./1024./1024.*8

def send_stat(value):
    print ("%0.3f" % convert_to_gbit(value))

main()