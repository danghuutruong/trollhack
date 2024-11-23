import tkinter as tk
import time
import random
import webbrowser
import socket
import platform
import psutil  
import keyboard  

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
        'OS': platform.system(),  
        'Machine': platform.machine(),  
        'IP Address': socket.gethostbyname(socket.gethostname()),  
        'Hostname': socket.gethostname(),  
        'CPU Usage': psutil.cpu_percent(),  
        'Memory Usage': psutil.virtual_memory().percent,  
        'Disk Usage': psutil.disk_usage('/').percent,  
    }
    return system_info

root = tk.Tk()
root.title("Hack Tool")
root.configure(bg="black")
root.attributes("-fullscreen", True)  

console = tk.Text(root, bg="black", fg="green", insertbackground="green", font=("Consolas", 12), wrap="none", borderwidth=0)
console.pack(fill="both", expand=True)

def run_fake_console():
    ascii_art = """
                                          
ooooo   ooooo       .o.         .oooooo.   oooo    oooo    ooooooooooooo ooooooooo.     .oooooo.   ooooo        ooooo        
`888'   `888'      .888.       d8P'  `Y8b  `888   .8P'     8'   888   `8 `888   `Y88.  d8P'  `Y8b  `888'        `888'        
 888     888      .8"888.     888           888  d8'            888       888   .d88' 888      888  888          888         
 888ooooo888     .8' `888.    888           88888[              888       888ooo88P'  888      888  888          888         
 888     888    .88ooo8888.   888           888`88b.            888       888`88b.    888      888  888          888         
 888     888   .8'     `888.  `88b    ooo   888  `88b.          888       888  `88b.  `88b    d88'  888       o  888       o 
o888o   o888o o88o     o8888o  `Y8bood8P'  o888o  o888o        o888o     o888o  o888o  `Y8bood8P'  o888ooooood8 o888ooooood8 










    """
    system_info = get_system_info()

    lines = [
        ascii_art,  
        "Connecting to the system...",
        "---------------------------------",
        f"System: {system_info['OS']} {system_info['Machine']}",
        f"Hostname: {system_info['Hostname']}",
        f"IP Address: {system_info['IP Address']}",
        "",
        "Initializing protocols...",
        "---------------------------------",
        f"CPU Usage: {system_info['CPU Usage']}%",
        f"Memory Usage: {system_info['Memory Usage']}%",
        f"Disk Usage: {system_info['Disk Usage']}%",
        "",
        "Ping to remote server...",
        f"Pinging {random.choice(['192.168.1.1', '10.0.0.1', '8.8.8.8'])} with 32 bytes of data:",
        "Reply from {0}: bytes=32 time<1ms",
        "Reply from {0}: bytes=32 time<1ms",
        "Reply from {0}: bytes=32 time<1ms",
        "",
        "Ping statistics for {0}:",
        "    Packets: Sent = 3, Received = 3, Lost = 0 (0% loss),",
        "Approximate round trip times in milli-seconds:",
        "    Minimum = 0ms, Maximum = 0ms, Average = 0ms",
        "",
        "!!! WARNING: Unauthorized access detected !!!",
        "Attempting to bypass firewall...",
        "Bypassing successfully...",
        "---------------------------------",
        "Opening backdoor...",
        "---------------------------------",
        "Connection established. Remote session active.",
        "Redirecting to target...",
        "",
    ]

    for line in lines:
        type_text(console, line + "\n", delay=10)
        time.sleep(0.2)

    time.sleep(2)
    rickroll_and_close()

root.after(100, run_fake_console)

def close_on_escape(event):
    root.destroy()

def block_all_keys(event):
    return "break"  

keyboard.block_key('win')  
root.bind("<KeyPress>", block_all_keys)  
root.bind("<KeyRelease>", block_all_keys)  

root.mainloop()
