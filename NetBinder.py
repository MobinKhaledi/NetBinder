import os
import shutil
import subprocess
import tkinter as tk
import sys
from tkinter import filedialog, messagebox, StringVar
import psutil
import socket
from tkinter import ttk
import subprocess


def get_ip_addresses():
    return {
        interface: addr.address
        for interface, addrs in psutil.net_if_addrs().items()
        for addr in addrs if addr.family == socket.AF_INET
    }

def get_icon_path():
    # If the application is running from a bundled executable
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'Icon.ico')
    # If running in a normal environment
    return os.path.join(os.path.dirname(__file__), 'Icon.ico')

def get_forcebindip_path():
    # Check if the application is running in a PyInstaller bundle
    if hasattr(sys, '_MEIPASS'):
        # Return the path to the executable in the temporary folder created by PyInstaller
        return os.path.join(sys._MEIPASS, 'ForceBindIP', 'ForceBindIP.exe')
    # Return the path for development
    return os.path.join('ForceBindIP', 'ForceBindIP.exe')



def format_path(path):
    return f"...{path[-53:]}" if len(path) > 53 else path

def install_forcebindip():
    forcebindip_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ForceBindIP")
    target_dir = "C:\\Program Files (x86)\\ForceBindIP" if os.environ.get('PROGRAMFILES(X86)') else "C:\\Program Files\\ForceBindIP"

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    try:
        for item in os.listdir(forcebindip_src):
            s = os.path.join(forcebindip_src, item)
            d = os.path.join(target_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)
        messagebox.showinfo("Success", "ForceBindIP installed successfully.")
    except PermissionError:
        messagebox.showerror("Error", "Please run the app as administrator to install ForceBindIP.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

original_forcebindip_path = ""

def update_forcebindip_path():
    global original_forcebindip_path
    paths = [
        "C:\\Program Files (x86)\\ForceBindIP\\ForceBindIP.exe",
        "C:\\Program Files\\ForceBindIP\\ForceBindIP.exe"
    ]
    for path in paths:
        if os.path.isfile(path):
            original_forcebindip_path = path
            forcebindip_var.set(format_path(path))
            return
    # Check if the forcebindip executable exists in its expected location
    if os.path.isfile(get_forcebindip_path()):  # Updated line
        original_forcebindip_path = get_forcebindip_path()
        forcebindip_var.set(format_path(original_forcebindip_path))
        return
    original_forcebindip_path = ""
    forcebindip_var.set("")

original_app_path = ""

def select_app():
    global original_app_path
    file_path = filedialog.askopenfilename()
    if file_path:
        original_app_path = os.path.normpath(file_path)
        app_path.set(format_path(original_app_path))

def run_force_bind_ip():
    selected_network = network_var.get()
    if not original_app_path or not selected_network:
        messagebox.showerror("Error", "Please select both an app and a network.")
        return

    ip_address = ip_addresses.get(selected_network)
    if not ip_address:
        messagebox.showerror("Error", "Could not retrieve IP address for the selected network.")
        return

    command = [get_forcebindip_path(), ip_address, original_app_path]  # Updated line
    try:
        subprocess.Popen(command, shell=False)
        messagebox.showinfo("Success", f"Application successfully bound to {selected_network} with IP {ip_address}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_ip_address(event):
    selected_network = network_var.get()
    ip_address_var.set(ip_addresses.get(selected_network, "No IP found"))

root = tk.Tk()
root.title("App Network Binder")
root.resizable(False, False)
root.geometry("600x360")
root.iconbitmap(get_icon_path())
forcebindip_path_var = tk.StringVar()

style = ttk.Style()
style.theme_use('clam')
bg_color = root.cget("background")
style.configure("TLabel", font=("Roboto", 12), background=bg_color)
style.configure("TButton", font=("Roboto", 12))
style.configure("TCombobox", font=("Roboto", 12), background=bg_color)
style.configure("TFrame", background=bg_color)

ip_addresses = get_ip_addresses()
if not ip_addresses:
    messagebox.showerror("Error", "No active network interfaces found.")
    root.destroy()

# Network selection frame
network_frame = ttk.Frame(root, style="TFrame")
network_frame.pack(anchor="w", padx=(25, 5), pady=(25, 5))

network_var = StringVar(value="")
network_label = ttk.Label(network_frame, text="Select a Network:", background=bg_color)
network_label.pack(side="left", padx=(0, 10))

network_dropdown = ttk.Combobox(network_frame, textvariable=network_var, values=list(ip_addresses.keys()), state="readonly", font=("Roboto", 12))
network_dropdown.pack(side="left")
network_var.set("Choose your connection")
network_dropdown.bind("<<ComboboxSelected>>", update_ip_address)

# IP address display frame
ip_frame = ttk.Frame(root, style="TFrame")
ip_frame.pack(anchor="w", padx=(25, 5), pady=(10, 5))

ip_label = ttk.Label(ip_frame, text="IP Address:", background=bg_color)
ip_label.pack(side="left")

ip_address_var = StringVar(value="")
ip_address_display = ttk.Label(ip_frame, textvariable=ip_address_var, background=bg_color)
ip_address_display.pack(side="left")

# ForceBindIP path frame
forcebindip_frame = ttk.Frame(root, style="TFrame")
forcebindip_frame.pack(anchor="w", padx=(25, 5), pady=(10, 5))

forcebindip_label = ttk.Label(forcebindip_frame, text="ForceBindIP Path:", background=bg_color)
forcebindip_label.pack(side="left")

forcebindip_var = StringVar(value="")
forcebindip_path_label = ttk.Label(forcebindip_frame, textvariable=forcebindip_var, background=bg_color)
forcebindip_path_label.pack(side="left")

update_forcebindip_path()

# Button frame
button_frame = ttk.Frame(root, style="TFrame")
button_frame.pack(anchor="w", padx=(25, 5), pady=(5, 10))

def select_forcebindip_path():
    path = filedialog.askopenfilename(title="Select ForceBindIP Executable", filetypes=[("Executable Files", "*.exe")])
    if path:
        if os.path.isfile(path) and path.endswith('.exe'):
            forcebindip_path_var.set(path)
        else:
            messagebox.showerror("Invalid Selection", "Please select a valid .exe file.")
    else:
        return  # Do nothing if the user cancels

forcebindip_button = ttk.Button(button_frame, text="Select ForceBindIP Path", command=select_forcebindip_path)
install_button = ttk.Button(button_frame, text="Install ForceBindIP", command=install_forcebindip)

forcebindip_button.pack(side="left", padx=(0, 5))
install_button.pack(side="left", padx=(5, 0))

# Application path frame
app_frame = ttk.Frame(root, style="TFrame")
app_frame.pack(anchor="w", padx=(25, 5), pady=(10, 5))

app_label = ttk.Label(app_frame, text="Application Path:", background=bg_color)
app_label.pack(side="left")

app_path = StringVar(value="")
app_path_label = ttk.Label(app_frame, textvariable=app_path, background=bg_color)
app_path_label.pack(side="left")

app_button = ttk.Button(root, text="Select App", command=select_app)
app_button.pack(anchor="w", pady=(5, 10), padx=(25, 5))

separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", padx=(100, 100), pady=10)

launch_button = ttk.Button(root, text="NetBind App", command=run_force_bind_ip, width=20)
launch_button.pack(anchor="center", pady=(10, 0))

root.mainloop()
