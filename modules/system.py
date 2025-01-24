import subprocess
import psutil
import os


def get_cpu_usage(interval=1):
    cpu_usage = psutil.cpu_percent(interval)
    return round(cpu_usage, 2)


def get_ram_usage():
    ram_usage = psutil.virtual_memory()
    # ram_total = ram.total / (1024 * 1024)  # Convert to MB
    # ram_used = ram.used / (1024 * 1024)    # Convert to MB
    ram_percentage = ram_usage.percent
    # "total_mb": round(ram_total, 2),
    # "used_mb": round(ram_used, 2),
    # "percentage": f"{ram_percentage}%"
    return round(ram_percentage, 2)


def get_temperature(verbose=False):
    temp = 0
    try:
        if os.path.exists('/sys/class/thermal/thermal_zone0/temp'):
            if verbose:
                print('Using /sys/class/thermal/thermal_zone0/temp')
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                temp = int(f.read()) / 1000.0
        else:
            if verbose:
                print('Using sensors command')
            result = subprocess.run(
                ['sensors'], stdout=subprocess.PIPE, text=True)

            if verbose:
                print(result.stdout)

            for line in result.stdout.split('\n'):
                if verbose:
                    print(line)
                if 'temp1' in line:
                    temp = float(line.split()[1].replace('°C', ''))

                    break
    except Exception as e:
        print("Error getting temperature:", e)
        temp = 0
    return temp
