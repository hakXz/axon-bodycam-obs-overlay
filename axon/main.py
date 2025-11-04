import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

CONFIG_PATH = "config.js"

def save_config(model):
    js_time_setting = "const customStartTime = new Date();"

    model_label = model
    serial_prefix = "X"
    if "FLEET" in model:
        serial_prefix = "F"

    js_content = f"""
{js_time_setting}
const model = "{model_label}";
const serial = "{serial_prefix}" + Math.floor(10000000 + Math.random() * 89999999);

document.getElementById("line2").innerText = `${{model}} ${{serial}}`;

function updateTime() {{
  const now = new Date();
  const elapsed = now - customStartTime;
  const current = new Date(customStartTime.getTime() + elapsed);

  const tzOffset = current.getTimezoneOffset() / -60;
  const sign = tzOffset >= 0 ? "+" : "-";
  const formatted = current.getFullYear() + "-" +
    String(current.getMonth()+1).padStart(2, '0') + "-" +
    String(current.getDate()).padStart(2, '0') + " " +
    String(current.getHours()).padStart(2, '0') + ":" +
    String(current.getMinutes()).padStart(2, '0') + ":" +
    String(current.getSeconds()).padStart(2, '0') + " " +
    sign + String(Math.abs(tzOffset)).padStart(2, '0') + "00";

  document.getElementById("line1").innerText = formatted;
}}

setInterval(updateTime, 1000);
updateTime();
"""

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)

    messagebox.showinfo("Başarılı", "Ayarlar kaydedildi! OBS'yi yenileyebilirsin.")

def create_gui():
    root = tk.Tk()
    root.title("Axon Overlay Kontrol Paneli")
    root.geometry("400x250")
    root.resizable(False, False)

    ttk.Label(root, text="AXON Bodycam Overlay Kontrolü", font=("Segoe UI", 12, "bold")).pack(pady=10)

    ttk.Label(root, text="Model Seç:").pack()
    model_var = tk.StringVar(value="AXON BODY 3")
    model_combo = ttk.Combobox(root, textvariable=model_var, values=["AXON BODY 2", "AXON BODY 3", "AXON BODY 4", "AXON FLEET 2", "AXON FLEET 3"], state="readonly", width=20)
    model_combo.pack(pady=10)

    ttk.Label(root, text="Zaman: Şu anki zamandan başlatılacak", font=("Segoe UI", 9)).pack(pady=5)

    ttk.Button(root, text="Kaydet ve Başlat", command=lambda: save_config(model_var.get())).pack(pady=20)

    ttk.Label(root, text="OBS'de overlay'i yenileyerek değişiklikleri görebilirsin.", font=("Segoe UI", 8)).pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
