import customtkinter as ctk
import lscooldowncalc as cooldownCalc

def onSubmit(event=None):
    global default_cooldown
    try:
        grow = float(grow_entry.get())
        cooldown = float(cooldown_entry.get())
        if 0 < default_cooldown:
            default_cooldown = (default_cooldown + cooldownCalc.getCooldown(grow, default_cooldown)) / 2
        else:
            default_cooldown = cooldownCalc.getDefaultCooldown(grow, cooldown)
        result_label.configure(text=f"기준 쿨타임 : {default_cooldown}")
    except ValueError:
        result_label.configure(text="잘못된 입력입니다.")

def onClear():
    global default_cooldown
    default_cooldown = 0.0
    grow_entry.delete(0, 'end')
    cooldown_entry.delete(0, 'end')
    result_label.configure(text="기준 쿨타임 : X")

app = ctk.CTk()
app.geometry("400x200")
default_cooldown = 0.0

intro_label = ctk.CTkLabel(app, text="육성수치와 쿨타임을 입력하면 기준 쿨타임을 계산합니다.")
intro_label.pack(padx=20, pady=10)

entry_frame = ctk.CTkFrame(app)
entry_frame.pack(padx=10, pady=10)

grow_entry = ctk.CTkEntry(entry_frame, placeholder_text="육성수치")
grow_entry.pack(side="left", padx=10)
grow_entry.bind("<Return>", onSubmit)  # 엔터키 입력 시 onSubmit 실행

cooldown_entry = ctk.CTkEntry(entry_frame, placeholder_text="쿨타임")
cooldown_entry.pack(side="left", padx=10)
cooldown_entry.bind("<Return>", onSubmit)  # 엔터키 입력 시 onSubmit 실행

submit_button = ctk.CTkButton(app, text="Submit", command=onSubmit, width=150)
submit_button.pack(padx=20, pady=10)

result_label = ctk.CTkLabel(app, text="기준 쿨타임 : -")
result_label.pack()

clear_button = ctk.CTkButton(app, text="Clear", command=onClear, width=70)
clear_button.pack(side="right")

app.mainloop()