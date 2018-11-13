#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import Worker
import re
import time

if __name__ == "__main__":
    fh = open("weburl.txt")
    channels = [ line.strip('\n') for line in fh.readlines()]
    channels = list(set(channels))

    fh.close()
    start_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

    Worker.Worker.store_channel_links(channels, 8)
    # Worker.Worker.store_recommended_links(channels)
    Worker.Worker.start_test(16)
    end_time =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
   # Worker.Worker.send_result_mail(start_time, end_time)

    #Worker.Worker.send_mail()

    #Worker.Worker.test_and_record(start_time,end_time)
   # Worker.Worker.read_data()
