
import tkinter as tk
from tkinter import ttk






root = tk.Tk()
root.geometry('900x500')
width= root.winfo_screenwidth()
height=root.winfo_screenheight()
root.title("Metrics converter")


metrics=tk.IntVar()
metrics=0

def perform_conversion(metrics):
    unit = metrics
    conversion = conversion_var.get()
    value = float(entry.get())

    if unit == "Length":
        if conversion == "Centimeter to Meter":
            result =float(value / 100)
        elif conversion == "Meter to Centimeter":
            result = value * 100
        elif conversion == "Centimeter to Inch":
            result = value / 2.54
        elif conversion == "Inch to Centimeter":
            result = value * 2.54
        elif conversion == "Centimeter to Kilometer":
            result = value / 100000
        elif conversion == "Kilometer to Centimeter":
            result = value * 100000
        elif conversion == "Centimeter to Feet":
            result = value / 30.48
        elif conversion == "Feet to Centimeter":
            result = value * 30.48
        elif conversion == "Kilometer to Mile":
            result = value / 1.609
        elif conversion == "Mile to Kilometer":
            result = value * 1.609
        elif conversion == "Centimeter to Feet":
            result = value / 30.48
        elif conversion == "Feet to Inches":
            result = value * 12
        elif conversion == "Square Feet to Square Meters":
            result = value / 10.764
        elif conversion == "Square Feet to Hectares":
            result = value / 107639.104
        elif conversion == "Square Feet to Acres":
            result = value / 43560
        # Add more length conversions here

    elif unit == "Mass":
        if conversion == "Gram to Kilogram":
            result = value / 1000
        elif conversion == "Kilogram to Gram":
            result = value * 1000
        elif conversion == "Kilogram to Tonne":
            result = value / 1000
        elif conversion == "Tonne to Kilogram":
            result = value * 1000
        elif conversion == "Milligram to Kilogram":
            result = value / 1e+6
        elif conversion == "Kilogram to Milligram":
            result = value * 1e+6
        elif conversion == "Milligram to Gram":
            result = value / 1000
        elif conversion == "Gram to Milligram":
            result = value * 1000
        elif conversion == "Kilogram to Pound (lb)":
            result = value * 2.20462
        elif conversion == "Pound (lb) to Kilogram":
            result = value / 2.20462
        elif conversion == "Micrograms to Gram":
            result = value / 1e+6
        elif conversion == "Micrograms to Kilogram":
            result = value / 1e+9
        # Add more mass conversions here

    elif unit == "Temperature":
        if conversion == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
        elif conversion == "Celsius to Kelvin":
            result = value + 273.15
        elif conversion == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
        elif conversion == "Fahrenheit to Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif conversion == "Kelvin to Celsius":
            result = value - 273.15
        elif conversion == "Kelvin to Fahrenheit":
            result = (value * 9/5) - 459.67
        # Add more temperature conversions here

    # Add similar conversion logic for other unit types
    elif unit == "Speed":
        if conversion == "Mile per hour to kilometer per hour":
            result = value * 1.60934
        elif conversion == "Kilometer per hour to Mile per hour":
            result = value / 1.60934
        elif conversion == "Mile per hour to Meter per Second":
            result = value / 2.237
        elif conversion == "Meter per Second to Mile per hour":
            result = value * 2.237
        elif conversion == "Kilometer per hour to Meter per Second":
            result = value / 3.6
        elif conversion == "Meter per Second to Kilometer per hour":
            result = value * 3.6
        
    elif unit == "Energy":
        if conversion == "Joule to Kilojoule":
            result = value / 1000
        elif conversion == "Kilojoule to Joule":
            result = value * 1000
        elif conversion == "Joule to Kilocalorie":
            result = value / 4184
        elif conversion == "Kilocalorie to Joule":
            result = value * 4184
        elif conversion == "Kilojoule to Kilocalorie":
            result = value / 4.184
        elif conversion == "Kilocalorie to Kilojoule":
            result = value * 4.184
            
    elif unit == "Pressure":
        if conversion == "Bar to Pascal":
            result = value * 100000
        elif conversion == "Bar to Standard atmosphere":
            result = value / 1.013
        elif conversion == "Pascal to Bar":
            result = value / 100000
        elif conversion == "Pascal to Standard atmosphere":
            result = value / 101325
        elif conversion == "Standard atmosphere to Pascal":
            result = value * 101325
        elif conversion == "Standard atmosphere to Bar":
            result = value * 1.01325

    return result
    if result is not None:
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Invalid conversion")






#####################################################







#####################################################



# Function to update the second Combobox based on the selected category
def update_conversion_options(event):
    selected = unit_var.get()
    if selected == "Length":
        conversion_options = [
            "Centimeter to Meter",
            "Meter to Centimeter",
            "Centimeter to INCH",
            "INCH to Centimeter",
            "Centimeter to KiloMetre",
            "KiloMetre to Centimeter",
            "Centimeter to FOOT",
            "FOOT to Centimeter",
            "Kilometre to Mile",
            "Mile to Kilometre",
            "Centimeter to Feets",
            "Feet to Inches",
            "Sqft to sqmtrs",
            "Sqft to Hectare/Acres"
        ]
    elif selected == "Mass":
        conversion_options = [
            "Gram to Kilogram",
            "Kilogram to Gram",
            "Kilogram to Tonne",
            "Tonne to Kilogram",
            "Milligram to Kilogram",
            "Kilogram to Milligram",
            "Milligram to Gram",
            "Gram to Milligram",
            "kilogram to pound (lb)",
            "pound (lb) to Kilogram",
            "Micrograms to gram",
            "Micrograms to Kilogram"
        ]
    elif selected == "Temperature":
        conversion_options = [
            "Celsius to Fahrenheit",
            "Celsius to Kelvin",
            "Fahrenheit to Celsius",
            "Fahrenheit to Kelvin",
            "Kelvin to Celsius",
            "Kelvin to Fahrenheit"
        ]
    elif selected == "Time":
        conversion_options = [
            "Second to Minute",
            "Minute to Second",
            "Second to Hour",
            "Minute to Hour",
            "Hour to Minute",
            "Day to Hour",
            "Hour to Day"
        ]
    elif selected == "Speed":
        conversion_options = [
            "Mile per hour to kilometer per hour",
            "Kilometer per hour to Mile per hour",
            "Mile per hour to Meter per Second",
            "Meter per Second to Mile per hour",
            "Kilometer per hour to Meter per Second",
            "Meter per Second to Kilometer per hour"
        ]
    elif selected == "Energy":
        conversion_options = [
            "Joule to Kilojoule",
            "Kilojoule to Joule",
            "Joule to Kilocalorie",
            "Kilocalorie to Joule",
            "Kilojoule to Kilocalorie",
            "Kilocalorie to Kilojoule"
        ]
    elif selected == "Pressure":
        conversion_options = [
            "Bar to Pascal",
            "Bar to Standard atmosphere",
            "Pascal to Bar",
            "Pascal to Standard atmosphere",
            "Standard atmosphere to Pascal",
            "Standard atmosphere to Bar"
        ]
        

    else:
        conversion_options = []

    conversion_menu['values'] = conversion_options
    conversion_var.set("")




#define options frame
options_frame = tk.Frame(root, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=250, height=height)


#define buttons for options frame
lenbtn=tk.Button(options_frame, text="Length", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: perform_conversion(metrics="Length"))
lenbtn.pack(padx=10, pady=10)
# lenbtn.place(x=10,y=50)

massbtn=tk.Button(options_frame, text="Mass", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: perform_conversion(metrics="Mass"))
massbtn.pack(padx=10, pady=10)
# massbtn.place(x=10,y=50)

tempbtn=tk.Button(options_frame, text="Temperature", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: perform_conversion(metrics="Temperature"))
tempbtn.pack(padx=10, pady=10)
# tempbtn.place(x=10,y=50)

timebtn=tk.Button(options_frame, text="Time", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: perform_conversion(metrics="Time"))
timebtn.pack(padx=10, pady=10)
# timebtn.place(x=10,y=50)

speedbtn=tk.Button(options_frame, text="Speed", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: perform_conversion(metrics="Speed"))
speedbtn.pack(padx=10, pady=10)
# speedbtn.place(x=10,y=50)

energybtn=tk.Button(options_frame, text="Energy", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: perform_conversion(metrics="Energy"))
energybtn.pack(padx=10, pady=10)
# energybtn.place(x=10,y=50)

preassurebtn=tk.Button(options_frame, text="Preassure", width=90, font=('light',10), fg='black', bg='#b5b5b5' , bd=0,  command=lambda: perform_conversion(metrics="Pressure"))
preassurebtn.pack(padx=10, pady=10)
# preassurebtn.place(x=10,y=50)









#define main frame
main_frame = tk.Frame(root, bg='#b5b5b5')

width= root.winfo_screenwidth()
height=root.winfo_screenheight()

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=height, width=width-250, padx=10, pady=10)






#create and set unit conversion variables
unit_var = tk.StringVar()
conversion_var = tk.StringVar()

# Create a label and entry for entering the value to convert
entry_label = tk.Label(main_frame, text="Enter a number to convert:")
entry_label.pack()

entry = tk.Entry(main_frame)
entry.pack()

# Create drop-down menus for unit and conversion
# unit_label = tk.Label(main_frame, text="Select Unit:")
# unit_label.pack()

# unit_menu = ttk.Combobox(main_frame, textvariable=unit_var)
# unit_menu['values'] = ("Length", "Mass", "Temperature", "Time", "Speed", "Energy", "Pressure")
# unit_menu.pack()


# Bind the update function to the category Combobox's <<ComboboxSelected>> event
# unit_menu.bind("<<ComboboxSelected>>", update_conversion_options)

# Create a label for conversion selection
conversion_label = tk.Label(main_frame, text="Select Conversion:")
conversion_label.pack()

# Create a second Combobox for selecting the conversion options
conversion_menu = ttk.Combobox(main_frame, textvariable=conversion_var)
conversion_menu.pack()




unit_label = tk.Label(root, text="Select Unit:")
unit_label.pack()

unit_menu = ttk.Combobox(root, textvariable=unit_var)
unit_menu['values'] = ("Length", "Mass", "Temperature", "Time", "Speed", "Energy", "Pressure")
unit_menu.pack()




root.mainloop()