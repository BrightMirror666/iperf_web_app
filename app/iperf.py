import subprocess
import json 
import os 


def triggerIperf():
    process = subprocess.Popen(["iperf3","-c","127.0.0.1","-p","5201","-J"],stdout=subprocess.PIPE)
    output = process.stdout.read()
    output_str = output.decode('utf-8')
    output_json = json.loads(output_str)
    result_mbps = output_json["end"]["streams"][0]['sender']['bits_per_second']
    
    return result_mbps

