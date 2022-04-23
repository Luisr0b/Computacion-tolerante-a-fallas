import psutil

if __name__ == '__main__':
    perc_cpu = psutil.cpu_percent(interval=1, percpu=True)
    mem_virt = int(psutil.virtual_memory().used / (1024 ** 2))
    avail_mem = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    print(f'''Estado actual del PC:
    La CPU esta al {perc_cpu}%
    Se esta usando {mem_virt} Mb de memoria
    Queda {avail_mem}% de memoria libre''')