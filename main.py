import tkinter as tk
import time
import random
import webbrowser
import socket
import platform
import psutil
import keyboard
import uuid

def type_text(widget, text, delay=10):
    for char in text:
        widget.insert(tk.END, char)
        widget.see(tk.END)
        widget.update()
        time.sleep(delay / 1000)

def rickroll_and_close():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    root.destroy()

def get_system_info():
    system_info = {
        'OS': platform.system() + " " + platform.release(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'CPU Count': psutil.cpu_count(logical=True),
        'IP Address': socket.gethostbyname(socket.gethostname()),
        'Hostname': socket.gethostname(),
        'MAC Address': ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1]),
        'CPU Usage': psutil.cpu_percent(),
        'Memory Usage': psutil.virtual_memory().percent,
        'Disk Usage': psutil.disk_usage('/').percent,
        'Uptime': time.strftime("%H:%M:%S", time.gmtime(time.time() - psutil.boot_time())),
        'Active Connections': len(psutil.net_connections())
    }
    return system_info

root = tk.Tk()
root.title("System Infiltration Tool")
root.configure(bg="black")
root.attributes("-fullscreen", True)

console = tk.Text(root, bg="black", fg="green", insertbackground="green", font=("Consolas", 12), wrap="none", borderwidth=0)
console.pack(fill="both", expand=True)

def run_fake_console():
    ascii_art = """
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝  troll
https://github.com/danghuutruong

    """
    
    system_info = get_system_info()

    lines = [
        ascii_art,  
        "Connecting to the target system...",
        "---------------------------------",
        f"Operating System: {system_info['OS']}",
        f"Machine Type: {system_info['Machine']}",
        f"Processor: {system_info['Processor']}",
        f"CPU Count: {system_info['CPU Count']}",
        f"Hostname: {system_info['Hostname']}",
        f"IP Address: {system_info['IP Address']}",
        f"MAC Address: {system_info['MAC Address']}",
        "",
        "Gathering sensitive data...",
        "---------------------------------",
        f"CPU Usage: {system_info['CPU Usage']}%",
        f"Memory Usage: {system_info['Memory Usage']}%",
        f"Disk Usage: {system_info['Disk Usage']}%",
        f"System Uptime: {system_info['Uptime']}",
        f"Active Network Connections: {system_info['Active Connections']}",
        "",
        "!!! CRITICAL WARNING: Unauthorized access detected !!!",
        "Attempting to bypass security measures...",
        "Bypassing firewall... SUCCESS",
        "Installing backdoor... COMPLETE",
        "---------------------------------",
        "Initiating system lockdown...",
        "Locking all critical files...",
        "System control: 100%",
        "Redirecting to remote server...",
        "",
        "!!! WARNING: Your system is now under control !!!",
        "Preparing to erase all data...",
        "Data erase initiated in 5 seconds...",
        "",
    ]

    for line in lines:
        type_text(console, line + "\n", delay=10)
        time.sleep(0.2)

    time.sleep(5)  
    rickroll_and_close()

root.after(100, run_fake_console)

def close_on_escape(event=None):
    root.destroy()

def block_all_keys(event):
    return "break"  

keyboard.block_key('win')  
root.bind("<KeyPress>", block_all_keys)  
root.bind("<KeyRelease>", block_all_keys)  

root.bind("<Control-c>", close_on_escape)

root.mainloop()
