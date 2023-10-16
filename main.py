import tkinter as tk
from tkinter import ttk

#calls conversion function and displays the result
def convert_and_display():
    # result_label.config(text="cnd1")
    result = perform_conversion()
    # result_label.config(text="cnd1after")
    if result is not None:
        # result_label.config(text="cnd2")
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Invalid conversion")
        # result_label.config(text="cnd3")

def perform_conversion():
    # unit = unit_var.get()
    conversion = conversion_var.get()
    value = float(entry.get())
    # result=unit
    result=9686165305

    if conversion == "cm to m":
        result =float(value / 100)
    elif conversion == "m to cm":
        result = value * 100
    elif conversion == "cm to in":
        result = value / 2.54
    elif conversion == "in to cm":
        result = value * 2.54
    elif conversion == "cm to km":
        result = value / 100000
    elif conversion == "km to cm":
        result = value * 100000
    elif conversion == "cm to ft":
        result = value / 30.48
    elif conversion == "ft to cm":
        result = value * 30.48
    elif conversion == "km to mi":
        result = value / 1.609
    elif conversion == "mi to km":
        result = value * 1.609
    # elif conversion == "cm to ft":
    #     result = value / 30.48
    # elif conversion == "ft to ines":
    #     result = value * 12
    # elif conversion == "Square ft to Square ms":
    #     result = value / 10.764
    # elif conversion == "Square ft to Hectares":
    #     result = value / 107639.104
    # elif conversion == "Square ft to Acres":
    #     result = value / 43560
    elif conversion == "cm to ft":
        result = value * 0.0328084
    elif conversion == "Sqft to sqmtrs":
        result = value * 0.092903
    elif conversion == "sq ft to acre":
        result = value / 43560
    elif conversion == "sq ft to ha":
        result = value / 107639.1
    elif conversion == "ft to in":
        result = value / 107639.1
    # Add more length conversions here

    elif conversion == "g to kg":
        result = value / 1000
    elif conversion == "kg to g":
        result = value * 1000
    elif conversion == "kg to t":
        result = value / 1000
    elif conversion == "t to kg":
        result = value * 1000
    elif conversion == "mg to kg":
        result = value / 1e+6
    elif conversion == "kg to mg":
        result = value * 1e+6
    elif conversion == "mg to g":
        result = value / 1000
    elif conversion == "g to mg":
        result = value * 1000
    elif conversion == "kg to lb":
        result = value * 2.20462
    elif conversion == "lb to kg":
        result = value / 2.20462
    elif conversion == "mg to g":
        result = value / 1e+6
    elif conversion == "mg to kg":
        result = value / 1e+9
    # Add more mass conversions here

    elif conversion == "C to F":
        result = (value * 9/5) + 32
    elif conversion == "C to K":
        result = value + 273.15
    elif conversion == "F to C":
        result = (value - 32) * 5/9
    elif conversion == "F to K":
        result = (value - 32) * 5/9 + 273.15
    elif conversion == "K to C":
        result = value - 273.15
    elif conversion == "K to F":
        result = (value * 9/5) - 459.67
    # Add more temperature conversions here

# Add similar conversion logic for other unit types

    elif conversion == "miph to kmph":
        result = value * 1.60934
    elif conversion == "kmph to miph":
        result = value / 1.60934
    elif conversion == "miph to m/s":
        result = value / 2.237
    elif conversion == "m/s to miph":
        result = value * 2.237
    elif conversion == "kmph to m/s":
        result = value / 3.6
    elif conversion == "m/s to kmph":
        result = value * 3.6
    

    elif conversion == "J to kJ":
        result = value / 1000
    elif conversion == "kJ to J":
        result = value * 1000
    elif conversion == "J to kcal":
        result = value / 4184
    elif conversion == "kcal to J":
        result = value * 4184
    elif conversion == "kJ to kcal":
        result = value / 4.184
    elif conversion == "kcal to kJ":
        result = value * 4.184
        

    elif conversion == "bar to Pa":
        result = value * 100000
    elif conversion == "bar to atm":
        result = value / 1.013
    elif conversion == "Pa to bar":
        result = value / 100000
    elif conversion == "Pa to atm":
        result = value / 101325
    elif conversion == "atm to Pa":
        result = value * 101325
    elif conversion == "atm to bar":
        result = value * 1.01325
    # result_label.config(text="c2mrb")
    return result
    # result_label.config(text="c2mra")
    if result is not None:
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Invalid conversion")

# Function to update the s Combobox based on the selected category
def update_conversion_options(unit):
    selected = unit
    if selected == "Length":
        conversion_options = [
            "m to cm",
            "cm to m",
            "in to cm",
            "cm to km",
            "km to cm",
            "cm to in",
            # "cm to ft",
            "ft to cm",
            "km to mi",
            "mi to km",
            "cm to ft",
            "ft to ines",
            "Sqft to sqmtrs",
            "Sqft to acre",
            "Sqft to ha"
        ]
    elif selected == "Mass":
        conversion_options = [
            "g to kg",
            "kg to g",
            "kg to t",
            "t to kg",
            "mg to kg",
            "kg to mg",
            "mg to g",
            "g to mg",
            "kg to lb",
            "lb to kg",
            "µg to g",
            "µg to kg"
        ]
    elif selected == "Temperature":
        conversion_options = [
            "C to F",
            "C to K",
            "F to C",
            "F to K",
            "K to C",
            "K to F"
        ]
    elif selected == "Time":
        conversion_options = [
            "s to min",
            "min to s",
            "s to hr",
            "min to hr",
            "hr to min",
            "d to hr",
            "hr to d"
        ]
    elif selected == "Speed":
        conversion_options = [
            "miph to kmph",
            "kmph to miph",
            "miph to m/s",
            "m/s to miph",
            "kmph to m/s",
            "m/s to kmph"
        ]
    elif selected == "Energy":
        conversion_options = [
            "J to kJ",
            "kJ to J",
            "J to kcal",
            "kcal to J",
            "kJ to kcal",
            "kcal to kJ"
        ]
    elif selected == "Pressure":
        conversion_options = [
            "bar to Pa",
            "bar to atm",
            "Pa to bar",
            "Pa to atm",
            "atm to Pa",
            "atm to bar"
        ]
        

    else:
        conversion_options = []

    conversion_menu['values'] = conversion_options
    conversion_var.set("")



#create root
root = tk.Tk()
root.geometry('900x500')
width= root.winfo_screenwidth()
height=root.winfo_screenheight()
root.title("Metrics converter")


#define options frame
options_frame = tk.Frame(root, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=250, height=height)

def set_unit(metrics):
    # unit_var.set(metrics)
    unit_var=metrics
    update_conversion_options(unit_var)
    # unit_var.set(metrics)
    # result_label.config(text=f"{unit_var}")

# def su(a,b):
    # result_label.config(text=f"{a} and {b}")

#define buttons for options frame
lenbtn=tk.Button(options_frame, text="Length", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: set_unit(metrics="Length"))
lenbtn.pack(padx=10, pady=10)

massbtn=tk.Button(options_frame, text="Mass", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: set_unit(metrics="Mass"))
massbtn.pack(padx=10, pady=10)

tempbtn=tk.Button(options_frame, text="Temperature", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: set_unit(metrics="Temperature"))
tempbtn.pack(padx=10, pady=10)

timebtn=tk.Button(options_frame, text="Time", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: set_unit(metrics="Time"))
timebtn.pack(padx=10, pady=10)

speedbtn=tk.Button(options_frame, text="Speed", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: set_unit(metrics="Speed"))
speedbtn.pack(padx=10, pady=10)

energybtn=tk.Button(options_frame, text="Energy", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: set_unit(metrics="Energy"))
energybtn.pack(padx=10, pady=10)

preassurebtn=tk.Button(options_frame, text="Preassure", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: set_unit(metrics="Pressure"))
preassurebtn.pack(padx=10, pady=10)

#define main frame
main_frame = tk.Frame(root, bg='#b5b5b5')
width= root.winfo_screenwidth()
height=root.winfo_screenheight()
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=height, width=width-250, padx=10, pady=10)

#variables defined
result=tk.DoubleVar()
metrics=tk.StringVar()
metrics="Length"
unit_var=tk.StringVar()
conversion_var=tk.StringVar()
entry=tk.Entry(main_frame)

#Input field
entry_label = tk.Label(main_frame, text="Enter a number to convert:")
entry_label.pack()
#assigning the value of input field to the variable
entry = tk.Entry(main_frame)
entry.pack()

# Create a label for conversion selection
conversion_label = tk.Label(main_frame, text="Select Conversion:")
conversion_label.pack()
# Create a s Combobox for selecting the conversion options
conversion_menu = ttk.Combobox(main_frame, textvariable=conversion_var)
conversion_menu.pack()

#result label
result_label = tk.Label(main_frame, text="", bg='#b5b5b5')
result_label.pack()

# Create a "Convert" button
convert_button = tk.Button(main_frame, text="Convert", command=convert_and_display)
convert_button.pack()

root.mainloop()