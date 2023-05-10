import psutil
# TODO : Mohammad Ahmadi - Tehran_North Branch
cpu_percent = psutil.cpu_percent()
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq().current

mem_total = psutil.virtual_memory().total
mem_used = psutil.virtual_memory().used
mem_free = psutil.virtual_memory().available

disk_usage = psutil.disk_usage('/')

log = {
    'cpu_percent': cpu_percent,
    'cpu_count': cpu_count,
    'cpu_freq': cpu_freq,
    'mem_total': mem_total,
    'mem_used': mem_used,
    'mem_free': mem_free,
    'disk_usage': {
        'total': disk_usage.total,
        'used': disk_usage.used,
        'free': disk_usage.free
    }
}


print(log)

