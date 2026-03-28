import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess
import threading

scanning = False

# Run scan command
def run_scan(command):
    global scanning
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            if not scanning:
                break
            output.insert(tk.END, line)
            output.see(tk.END)
    except Exception as e:
        output.insert(tk.END, str(e))

# Start scan
def start_scan(scan_type):
    global scanning
    scanning = True

    target = target_entry.get()
    start_port = start_port_entry.get()
    end_port = end_port_entry.get()

    if not target:
        output.insert(tk.END, "Enter a valid target\n")
        return

    if scan_type == "basic":
        cmd = f"nmap -p {start_port}-{end_port} {target}"
    elif scan_type == "syn":
        cmd = f"nmap -sS {target}"
    elif scan_type == "service":
        cmd = f"nmap -sV {target}"
    elif scan_type == "os":
        cmd = f"nmap -O {target}"
    elif scan_type == "aggressive":
        cmd = f"nmap -A {target}"
    else:
        cmd = f"nmap {target}"

    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Running: {cmd}\n\n")

    threading.Thread(target=run_scan, args=(cmd,), daemon=True).start()

# Stop scan
def stop_scan():
    global scanning
    scanning = False
    output.insert(tk.END, "\n[SCAN STOPPED]\n")

# Clear output
def clear_output():
    output.delete(1.0, tk.END)

# Save results
def save_output():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(output.get(1.0, tk.END))

# Theme toggle
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg = "black" if dark_mode else "white"
    fg = "lime" if dark_mode else "black"
    root.configure(bg=bg)
    output.configure(bg=bg, fg=fg)

# GUI setup
root = tk.Tk()
root.title("SmartScan Pro – Advanced Port Scanner")
root.geometry("750x520")

dark_mode = True

tk.Label(root, text="Target (IP / Host)").pack()
target_entry = tk.Entry(root, width=40)
target_entry.pack()

tk.Label(root, text="Start Port").pack()
start_port_entry = tk.Entry(root)
start_port_entry.insert(0, "1")
start_port_entry.pack()

tk.Label(root, text="End Port").pack()
end_port_entry = tk.Entry(root)
end_port_entry.insert(0, "1024")
end_port_entry.pack()

# Scan buttons
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Basic Scan", command=lambda: start_scan("basic")).grid(row=0, column=0)
tk.Button(frame, text="SYN Scan", command=lambda: start_scan("syn")).grid(row=0, column=1)
tk.Button(frame, text="Service Scan", command=lambda: start_scan("service")).grid(row=0, column=2)
tk.Button(frame, text="OS Detection", command=lambda: start_scan("os")).grid(row=0, column=3)
tk.Button(frame, text="Aggressive Scan", command=lambda: start_scan("aggressive")).grid(row=0, column=4)

tk.Button(root, text="Start Scan", command=lambda: start_scan("basic")).pack()
tk.Button(root, text="Stop Scan", command=stop_scan).pack()
tk.Button(root, text="Clear Output", command=clear_output).pack()
tk.Button(root, text="Save Results", command=save_output).pack()
tk.Button(root, text="Dark / Light Mode", command=toggle_theme).pack()

output = scrolledtext.ScrolledText(root, width=90, height=20)
output.pack()

root.mainloop()
