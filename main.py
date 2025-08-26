import customtkinter as ctk
import math

# ---------------- APP SETUP ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("420x600")
app.title("Calculator")

# ---------------- ENTRY & RESULT ----------------
entry = ctk.CTkEntry(app, height=50, width=400, font=("Arial", 20))
entry.pack(pady=10)

result = ctk.CTkLabel(app, height=50, width=400, text="", font=("Arial", 20))
result.pack(pady=5)

frame = ctk.CTkFrame(app, width=400, height=500)
frame.pack(pady=10)

# ---------------- FUNCTIONS ----------------

def showbig():
    value = int(result.cget("text"))
    entry.delete(0, "end")       
    entry.insert(0, str(value))
    result.configure(text = "")


def evaluate():
    try:
        expr =entry.get()
        ans = eval(expr)
        result.configure(text=ans)
    except TypeError:
        result.configure(text="Processing....")
    except ZeroDivisionError:
        result.configure(text="Undefined")

        
def all_clear():
    entry.delete(0, "end")
    result.configure(text="")

def number(num):
    entry.insert("end", str(num))
    evaluate()

def factorial():
    try:
        num = int(entry.get())
        result.configure(text=math.factorial(num))
    except:
        result.configure(text="Error")

def percent():
    try :
        num = entry.get().split(",")
        base , total = float(num[0]), float(num[1])
        outcome = base/total
        ans=outcome*100
        result.configure(text=ans)
    except :
        num = float(entry.get())
        ans= num/100
        result.configure(text = ans)





def remainder():
    try:
        nums = entry.get().split(",")   # Example: 10,3
        base, div = float(nums[0]), float(nums[1])
        result.configure(text=base % div)
    except:
        result.configure(text="Enter a Number : Example: 10,3 ")

def sqrt():
    try:
        num = float(entry.get())
        result.configure(text=math.sqrt(num))
    except:
        result.configure(text="Enter a number ")

def power():
    try:
        nums = entry.get().split(",")   # Example: 2,3
        base, exp = float(nums[0]), float(nums[1])
        result.configure(text=math.pow(base, exp))
    except:
        result.configure(text="Enetr  (use like 2,3)")

def pi_value():
    result.configure(text=math.pi)


# ---------------- BUTTONS ----------------
# Row 0 - Scientific
ctk.CTkButton(frame, text="AC", hover_color="light blue", command=all_clear, width=80).grid(row=0, column=0, padx=5, pady=5)
ctk.CTkButton(frame, text="%",hover_color="light blue", command=percent, width=80).grid(row=0, column=1, padx=5, pady=5)
ctk.CTkButton(frame, text="√", hover_color="light blue",command=sqrt, width=80).grid(row=0, column=2, padx=5, pady=5)
ctk.CTkButton(frame, text="!", hover_color="light blue",command=factorial, width=80).grid(row=0, column=3, padx=5, pady=5)

# Row 1 - More scientific
ctk.CTkButton(frame, text="^", hover_color="light blue",command=power, width=80).grid(row=1, column=0, padx=5, pady=5)
ctk.CTkButton(frame, text="π", hover_color="light blue",command=pi_value, width=80).grid(row=1, column=1, padx=5, pady=5)
ctk.CTkButton(frame, text="Rem", hover_color="light blue",command=remainder, width=80).grid(row=1, column=2, padx=5, pady=5)
ctk.CTkButton(frame, text="/", hover_color="light blue",command=lambda: number("/"), width=80).grid(row=1, column=3, padx=5, pady=5)

# Row 2
ctk.CTkButton(frame, text="7", hover_color="light blue",command=lambda: number(7), width=80).grid(row=2, column=0, padx=5, pady=5)
ctk.CTkButton(frame, text="8",hover_color="light blue", command=lambda: number(8), width=80).grid(row=2, column=1, padx=5, pady=5)
ctk.CTkButton(frame, text="9",hover_color="light blue", command=lambda: number(9), width=80).grid(row=2, column=2, padx=5, pady=5)
ctk.CTkButton(frame, text=",",hover_color="light blue", command=lambda: number(","), width=80).grid(row=2, column=3, padx=5, pady=5)

# Row 3
ctk.CTkButton(frame, text="4",hover_color="light blue", command=lambda: number(4), width=80).grid(row=3, column=0, padx=5, pady=5)
ctk.CTkButton(frame, text="5",hover_color="light blue", command=lambda: number(5), width=80).grid(row=3, column=1, padx=5, pady=5)
ctk.CTkButton(frame, text="6",hover_color="light blue", command=lambda: number(6), width=80).grid(row=3, column=2, padx=5, pady=5)
ctk.CTkButton(frame, text="-",hover_color="light blue", command=lambda: number("-"), width=80).grid(row=3, column=3, padx=5, pady=5)

# Row 4
ctk.CTkButton(frame, text="1",hover_color="light blue", command=lambda: number(1), width=80).grid(row=4, column=0, padx=5, pady=5)
ctk.CTkButton(frame, text="2",hover_color="light blue", command=lambda: number(2), width=80).grid(row=4, column=1, padx=5, pady=5)
ctk.CTkButton(frame, text="3",hover_color="light blue", command=lambda: number(3), width=80).grid(row=4, column=2, padx=5, pady=5)
ctk.CTkButton(frame, text="+",hover_color="light blue", command=lambda: number("+"), width=80).grid(row=4, column=3, padx=5, pady=5)

# Row 5
ctk.CTkButton(frame, text="0",hover_color="light blue", command=lambda: number(0), width=80).grid(row=5, column=0, padx=5, pady=5)
ctk.CTkButton(frame, text=".",hover_color="light blue", command=lambda: number("."), width=80).grid(row=5, column=1, padx=5, pady=5)
ctk.CTkButton(frame, text="Calculator",hover_color="light blue",command= result.configure(text ="Abhay Gupta") ,width=80).grid(row=5, column=2, padx=5, pady=5)

ctk.CTkButton(frame, text="x",hover_color="light blue", command=lambda: number("*"), width=80).grid(row=5, column=3, padx=5, pady=5)

# Row 6 - Equal
ctk.CTkButton(frame, text="=", width=340, fg_color="green", hover_color="darkgreen", command= showbig).grid(row=6, column=0, columnspan=4, padx=5, pady=10)

# ---------------- RUN APP ----------------
app.mainloop()