import customtkinter as ctk
import lscooldowncalc as cooldownCalc

def onSubmit(event=None):
    global default_cooldown, accum
    try:
        grow = float(grow_entry.get())
        cooldown = float(cooldown_entry.get())
        if 0 < default_cooldown:
            default_cooldown = (default_cooldown + cooldownCalc.getCooldown(grow, cooldown)) / 2
        else:
            default_cooldown = cooldownCalc.getDefaultCooldown(grow, cooldown)
        accum += 1
        result_label.configure(text=f"기준 쿨타임 : {default_cooldown} (누적 연산 {accum}회차)")
    except ValueError:
        result_label.configure(text="잘못된 입력입니다.")

def onClear():
    global default_cooldown, accum
    default_cooldown = 0.0
    accum = 0
    grow_entry.delete(0, 'end')
    cooldown_entry.delete(0, 'end')
    result_label.configure(text="기준 쿨타임 : X")

app = ctk.CTk()
app.geometry("600x200")
default_cooldown = 0.0
accum= 0

main_frame = ctk.CTkFrame(app)
main_frame.pack(side="left", fill="both", expand=True)

intro_label = ctk.CTkLabel(main_frame, text="육성수치와 쿨타임을 입력하면 기준 쿨타임을 계산합니다.")
intro_label.pack(padx=20, pady=10)

entry_frame = ctk.CTkFrame(main_frame)
entry_frame.pack(padx=10, pady=10)

grow_entry = ctk.CTkEntry(entry_frame, placeholder_text="육성수치")
grow_entry.pack(side="left", padx=10)
grow_entry.bind("<Return>", onSubmit)

cooldown_entry = ctk.CTkEntry(entry_frame, placeholder_text="쿨타임")
cooldown_entry.pack(side="left", padx=10)
cooldown_entry.bind("<Return>", onSubmit)

submit_button = ctk.CTkButton(entry_frame, text="계산", command=onSubmit, width=150)
submit_button.pack(padx=20, pady=10)

result_label = ctk.CTkLabel(main_frame, text="기준 쿨타임 : -")
result_label.pack()

clear_button = ctk.CTkButton(main_frame, text="초기화", command=onClear, width=70)
clear_button.pack()

app.mainloop()