# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(total_seconds):
    hour = total_seconds / 3600
    if int(hour) != 1:
        h = "hours"
    else:
        h = "hour"    
    minute = total_seconds % 3600 / 60
    if int(minute) != 1:
        m = "minutes"
    else:
        m = "minute"
    second = float(total_seconds - int(minute) * 60 - int(hour) * 3600)
    if second - int(second) == 0:
        second = int(second)
    if second != 1:
        s = "seconds"
    else:
        s = "second"
    return str(int(hour)) + " " + h + ", " + str(int(minute)) + " " + m + ", " + str(second) + " " + s

def download_time(file_size, file_size_unit, bandwidth, bandwidth_unit):
    if file_size_unit == "kb":
        file_size_unit = 2 ** 10
    if file_size_unit == "kB":
        file_size_unit = 2 ** 10 * 8
    if file_size_unit == "Mb":
        file_size_unit = 2 ** 20
    if file_size_unit == "MB":
        file_size_unit = 2 ** 20 * 8
    if file_size_unit == "Gb":
        file_size_unit = 2 ** 30
    if file_size_unit == "GB":
        file_size_unit = 2 ** 30 * 8
    if file_size_unit == "Tb":
        file_size_unit = 2 ** 40
    if file_size_unit == "TB":
        file_size_unit = 2 ** 40 * 8
    if bandwidth_unit == "kb":
        bandwidth_unit = 2 ** 10
    if bandwidth_unit == "kB":
        bandwidth_unit = 2 ** 10 * 8
    if bandwidth_unit == "Mb":
        bandwidth_unit = 2 ** 20
    if bandwidth_unit == "MB":
        bandwidth_unit = 2 ** 20 * 8
    if bandwidth_unit == "Gb":
        bandwidth_unit = 2 ** 30
    if bandwidth_unit == "GB":
        bandwidth_unit = 2 ** 30 * 8
    if bandwidth_unit == "Tb":
        bandwidth_unit = 2 ** 40
    if bandwidth_unit == "TB":
        bandwidth_unit = 2 ** 40 * 8
    return convert_seconds((file_size * file_size_unit * 1.0) / (bandwidth * bandwidth_unit))

print(download_time(1024,'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print(download_time(1024,'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13,'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13,'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10,'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10,'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

#additional
print(download_time(11,'GB', 5, 'MB'))
#>>> 0 hours, 37 minutes, 32.8 seconds
