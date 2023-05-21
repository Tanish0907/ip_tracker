import subprocess
import re

def get_wifi_signal_strength(interface='wlo1'):
    cmd_output = subprocess.check_output(['iwconfig', interface])
    cmd_output = cmd_output.decode('utf-8')
    
    signal_strength = None
    
    for line in cmd_output.split('\n'):
        if 'Signal level' in line:
            signal_strength = re.findall('(-\d+) dBm', line)[0]
            break
    
    return abs(int(signal_strength))

# example usage
# signal_strength = get_wifi_signal_strength()
# print(f"Signal strength: {signal_strength} dBm")
