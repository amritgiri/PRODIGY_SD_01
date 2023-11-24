import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Temperature Conversion")
root.geometry("900x510")
root.resizable(False, False)

PRIMARY_COLOR = "#1DA756"
SECONDARY_COLOR = "#212121"
PRIM_SHADE1="#136C38"
SEC_SHADE1 = "#303030"

def getFont(size = 9, bold = False):
    return ("Helvetica", size, "bold" if bold else "normal")

def validate(P):
    empty = P ==""
    digit = empty or P[-1].isdigit()
    minus = P=="-" and len(P) == 1
    decimal = P.count(".") == 1
    out = empty or digit or minus or decimal

    return out

calFunc = {
    "cf" : lambda x: x*9/5 +32, #cel to fren
    "ck" : lambda x: x + 273.15, #cel to kel
    "fc" : lambda x: (x-32)*5/9, #fren to cel
    "kc" : lambda x: x-273.15 # kel to cel
}

calFunc["fk"] = lambda x: calFunc["ck"](calFunc["fc"](x))
calFunc["kf"] = lambda x: calFunc["cf"](calFunc["kc"](x))

def convert(fromInpt, fromUnitVar, toUnitVar, resultVar):
    fromU = fromUnitVar.get().lower()
    toU = toUnitVar.get()[0].lower()

    try:
        val = float(fromInpt.get())
    except ValueError:
        resultVar.set("Invalid Input")
        return
    
    if fromU == toU:
        res = val
    else:
        res = calFunc[fromU + toU](val)

    if not toU == "k":
        resultVar.set(f"{res:.2f}° {toU.upper()}")
    else:
        resultVar.set(f"{res:.2f} {toU.upper()}")

reg = root.register(validate)

borderFrame = tk.Frame(root,bg=SECONDARY_COLOR, width=450, height= 500)
borderFrame.place(x=0, y=0)

leftFrame = tk.Frame(borderFrame, bg=PRIMARY_COLOR, width=440, height=500)
leftFrame.place(x=5, y=5)

enterLabel = tk.Label(leftFrame, text= "Enter Temperature", bg=PRIMARY_COLOR, fg= SECONDARY_COLOR, font= getFont(16,True))
enterLabel.place(x=30, y=50)

degLabel = tk.Label(leftFrame, text="Degree", bg= PRIMARY_COLOR, fg=SECONDARY_COLOR, font=getFont(9))
degLabel.place(x=30, y=120)

inptEntry = tk.Entry(leftFrame, bg=PRIM_SHADE1, fg="#ffffff", insertbackground= "#ffffff", borderwidth=5, relief="flat",validatecommand=(reg,"%P"), validate="key")
inptEntry.place(x=30,y=160, width=265, height=42)

unitVar = tk.StringVar(root)
unitVar.set("C")

convertVar = tk.StringVar(root)
convertVar.set("Farenheit")

s= ttk.Style()
s.configure("unit.TMenubutton", background = SECONDARY_COLOR, relief = "flat")

s.configure("convertTo.TMenubutton", relief = "flat", background = PRIM_SHADE1, foreground = "#ffffff", width=320)

unitMenu = tk.OptionMenu(leftFrame, unitVar, "C", "F", "K")
unitMenu.place(x=300, y=160, width=50, height=42)

convertLabel= tk.Label(leftFrame, text="Convert To", bg= PRIMARY_COLOR, fg= SECONDARY_COLOR, font=getFont(9))
convertLabel.place(x=30, y=280)

convertMenu = ttk.OptionMenu(leftFrame, convertVar, "Farenheit", "Celcius", "Farenheit", "Kelvin")
convertMenu.place(x=30, y=320, width=320, height= 42)

convertButton = tk.Button(leftFrame, text="convert", bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, font= getFont(12), relief="flat", activebackground= SEC_SHADE1, bd=0)
convertButton.place(x=150, y=420, width=140,height=40)

rightFrame= tk.Frame(root, bg=SECONDARY_COLOR, width=450,height=510)
rightFrame.place(x=450, y=0)

resultVar = tk.StringVar(root)
resultVar.set("")

resultLabel = tk.Label(rightFrame, textvariable= resultVar, bg=SECONDARY_COLOR, fg= PRIMARY_COLOR, font= getFont(64,True))
# rely=(LEFT_FRAME_HEIGHT*0.5)/RIGHT_FRAME_HEIGHT
resultLabel.place(relx= 0.5, rely= 0.4901, anchor=tk.CENTER)

convertButton.configure(command= lambda:convert(inptEntry, unitVar, convertVar, resultVar))

root.mainloop()