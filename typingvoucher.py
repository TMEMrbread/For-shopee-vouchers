#This program is used for applying Shopee voucher at a set time.
#Please remember to add your email first.
#and remember to CHECK YOUR PHONE CONNECTION WITH YOUR COMPUTER
#and untick the other voucher
import time
import datetime
import subprocess
def click(shell):
#click apply
    shell.stdin.write("input tap 915 352\n")
    shell.stdin.flush()
    time.sleep(0.6)
#testing coordinates "1000", "2000"
#real order coordinates "900", "2200
    for i in range(20):
        shell.stdin.write("input tap 900 2200\n")
        shell.stdin.flush()
        time.sleep(0.1)
shell = subprocess.Popen(
    ["adb", "shell"],
    stdin=subprocess.PIPE,
    text=True,
    bufsize=1,
)
while(1):
    print("type the target time")
    month = int(input("target month:"))
    day = int(input("target date:"))
    hour = int(input("target hour:"))
    minute = int(input("target minute:"))
    targettime = datetime.datetime(2026, month, day, hour, minute) 
    if(targettime > datetime.datetime.now()): break
while(1): 
    if(datetime.datetime.now() >= targettime - datetime.timedelta(milliseconds=100)):
       click(shell)
       break
    if(targettime - datetime.datetime.now()).total_seconds() > 3: time.sleep(1)
