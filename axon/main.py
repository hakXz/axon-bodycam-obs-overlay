import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

CONFIG_PATH = "config.js"

def save_config(model, time_mode, date_input, time_input):
    try:
        if time_mode == "now":
            js_time_setting = f'const customStartTime = new Date();'

        elif time_mode == "date_only":
            selected_date = datetime.strptime(date_input, "%Y-%m-%d").date()
            now = datetime.now()
            combined = datetime.combine(selected_date, now.time())
            js_time_setting = f'const customStartTime = new Date({combined.year}, {combined.month - 1}, {combined.day}, {combined.hour}, {combined.minute}, {combined.second});'

        elif time_mode == "date_time":
            selected_datetime = datetime.strptime(f"{date_input} {time_input}", "%Y-%m-%d %H:%M:%S")
            js_time_setting = f'const customStartTime = new Date({selected_datetime.year}, {selected_datetime.month - 1}, {selected_datetime.day}, {selected_datetime.hour}, {selected_datetime.minute}, {selected_datetime.second});'

        else:
            messagebox.showerror("Hata", "Zaman modu seçilmedi.")
            return

    except ValueError:
        messagebox.showerror("Hata", "Tarih veya saat formatı yanlış!\nTarih: 2025-11-05\nSaat: 14:30:00")
        return

    serial_prefix = "F" if "FLEET" in model else "X"

    js_content = f"""{js_time_setting}
const model = "{model}";
const serial = "{serial_prefix}" + Math.floor(10000000 + Math.random() * 89999999);

function updateTime() {{
  const current = customStartTime; 
  customStartTime.setSeconds(customStartTime.getSeconds() + 1); 

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
  document.getElementById("line2").innerText = `${{model}} ${{serial}}`;
}}

setInterval(updateTime, 1000);
updateTime();
"""

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)

    messagebox.showinfo("Başarılı", "Ayarlar kaydedildi! OBS veya HTML'yi yenile (Ctrl+F5).")

def create_gui():
    root = tk.Tk()
    root.title("Axon Overlay Kontrol Paneli")
    root.geometry("420x340")
    root.resizable(False, False)

    ttk.Label(root, text="AXON Bodycam Overlay Kontrolü", font=("Segoe UI", 12, "bold")).pack(pady=10)

    ttk.Label(root, text="Model Seç:").pack()
    model_var = tk.StringVar(value="AXON BODY 3")
    ttk.Combobox(root, textvariable=model_var,
                 values=["AXON BODY 2", "AXON BODY 3", "AXON BODY 4", "AXON FLEET 2", "AXON FLEET 3"],
                 state="readonly", width=20).pack(pady=5)

    ttk.Label(root, text="Zaman Ayarı:").pack(pady=(10, 0))
    time_mode = tk.StringVar(value="now")
    ttk.Radiobutton(root, text="Şu anki tarih ve saat", variable=time_mode, value="now").pack(anchor="w", padx=40)
    ttk.Radiobutton(root, text="Seçtiğim tarih (şu anki saatle)", variable=time_mode, value="date_only").pack(anchor="w", padx=40)
    ttk.Radiobutton(root, text="Seçtiğim tarih ve saat", variable=time_mode, value="date_time").pack(anchor="w", padx=40)

    ttk.Label(root, text="Tarih (YYYY-MM-DD):").pack(pady=(10, 0))
    date_entry = ttk.Entry(root, width=20)
    date_entry.pack()

    ttk.Label(root, text="Saat (HH:MM:SS):").pack(pady=(5, 0))
    time_entry = ttk.Entry(root, width=20)
    time_entry.pack()

    ttk.Button(root, text="Kaydet ve Başlat",
               command=lambda: save_config(model_var.get(), time_mode.get(), date_entry.get(), time_entry.get())).pack(pady=20)

    ttk.Label(root, text="OBS veya HTML'yi yenileyerek değişiklikleri görebilirsin.", font=("Segoe UI", 8)).pack()
    root.mainloop()

if __name__ == "__main__":
    create_gui()
