# A small utility program that tracks how much data you have uploaded and downloaded from the net during the course 
# of your current online session. 
# See if you can find out what periods of the day you use more and less and generate a report or graph that shows it.
from datetime import datetime
from psutil import net_io_counters
import csv
import time

def convert_to_gbit(value):
    return value # /1024./1024./1024.*8

def send_stat(value):
    t = datetime.now()
    hour, minute, second = t.hour, t.minute, t.second
    # print ("%0.3f" % convert_to_gbit(value))
    csv_writer.writerow([value,hour,minute,second])


old_value = 0    
byte_ctr_obj =  open('byte_counts.csv','w',newline='')
csv_writer = csv.writer(byte_ctr_obj,delimiter=',')
csv_writer.writerow(['bytes','hour','minute','second'])
ticker = []

for n in range(720): # 1 hour at 5 second intervals
    ticker.append('.')
    print(n)
    new_value = net_io_counters().bytes_sent + net_io_counters().bytes_recv

    if old_value:
        send_stat(new_value - old_value)

    old_value = new_value

    time.sleep(5)

byte_ctr_obj.close()