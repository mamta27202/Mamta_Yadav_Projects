import tkinter as tk
from tkinter import messagebox

elements = {"H": {"name": "Hydrogen", "atomic_number": 1, "atomic_mass": "1.008", "group": "Reactive nonmetal"},
"He": {"name": "Helium", "atomic_number": 2, "atomic_mass": "4.0026", "group": "Noble gas"},
"Li": {"name": "Lithium", "atomic_number": 3, "atomic_mass": "6.94", "group": "Alkali metal"},
"Be": {"name": "Beryllium", "atomic_number": 4, "atomic_mass": "9.0122", "group": "Alkaline earth metal"},
"B": {"name": "Boron", "atomic_number": 5, "atomic_mass": "10.81", "group": "Metalloid"},
"C": {"name": "Carbon", "atomic_number": 6, "atomic_mass": "12.011", "group": "Reactive nonmetal"},
"N": {"name": "Nitrogen", "atomic_number": 7, "atomic_mass": "14.007", "group": "Reactive nonmetal"},
"O": {"name": "Oxygen", "atomic_number": 8, "atomic_mass": "15.999", "group": "Reactive nonmetal"},
"F": {"name": "Fluorine", "atomic_number": 9, "atomic_mass": "18.998", "group": "Reactive nonmetal"},
"Ne": {"name": "Neon", "atomic_number": 10, "atomic_mass": "20.180", "group": "Noble gas"},
"Na": {"name": "Sodium", "atomic_number": 11, "atomic_mass": "22.990", "group": "Alkali metal"},
"Mg": {"name": "Magnesium", "atomic_number": 12, "atomic_mass": "24.305", "group": "Alkaline earth metal"},
"Al": {"name": "Aluminium", "atomic_number": 13, "atomic_mass": "26.982", "group": "Post-transition metal"},
"Si": {"name": "Silicon", "atomic_number": 14, "atomic_mass": "28.085", "group": "Metalloid"},
"P": {"name": "Phosphorus", "atomic_number": 15, "atomic_mass": "30.974", "group": "Reactive nonmetal"},
"S": {"name": "Sulfur", "atomic_number": 16, "atomic_mass": "32.06", "group": "Reactive nonmetal"},
"Cl": {"name": "Chlorine", "atomic_number": 17, "atomic_mass": "35.45", "group": "Reactive nonmetal"},
"Ar": {"name": "Argon", "atomic_number": 18, "atomic_mass": "39.948", "group": "Noble gas"},
"K": {"name": "Potassium", "atomic_number": 19, "atomic_mass": "39.098", "group": "Alkali metal"},
"Ca": {"name": "Calcium", "atomic_number": 20, "atomic_mass": "40.078", "group": "Alkaline earth metal"},
"Sc": {"name": "Scandium", "atomic_number": 21, "atomic_mass": "44.956", "group": "Transition metal"},
"Ti": {"name": "Titanium", "atomic_number": 22, "atomic_mass": "47.867", "group": "Transition metal"},
"V": {"name": "Vanadium", "atomic_number": 23, "atomic_mass": "50.942", "group": "Transition metal"},
"Cr": {"name": "Chromium", "atomic_number": 24, "atomic_mass": "51.996", "group": "Transition metal"},
"Mn": {"name": "Manganese", "atomic_number": 25, "atomic_mass": "54.938", "group": "Transition metal"},
"Fe": {"name": "Iron", "atomic_number": 26, "atomic_mass": "55.845", "group": "Transition metal"},
"Co": {"name": "Cobalt", "atomic_number": 27, "atomic_mass": "58.933", "group": "Transition metal"},
"Ni": {"name": "Nickel", "atomic_number": 28, "atomic_mass": "58.693", "group": "Transition metal"},
"Cu": {"name": "Copper", "atomic_number": 29, "atomic_mass": "63.546", "group": "Transition metal"},
"Zn": {"name": "Zinc", "atomic_number": 30, "atomic_mass": "65.38", "group": "Transition metal"},
"Ga": {"name": "Gallium", "atomic_number": 31, "atomic_mass": "69.723", "group": "Post-transition metal"},
"Ge": {"name": "Germanium", "atomic_number": 32, "atomic_mass": "72.63", "group": "Metalloid"},
"As": {"name": "Arsenic", "atomic_number": 33, "atomic_mass": "74.922", "group": "Metalloid"},
"Se": {"name": "Selenium", "atomic_number": 34, "atomic_mass": "78.971", "group": "Reactive nonmetal"},
"Br": {"name": "Bromine", "atomic_number": 35, "atomic_mass": "79.904", "group": "Reactive nonmetal"},
"Kr": {"name": "Krypton", "atomic_number": 36, "atomic_mass": "83.798", "group": "Noble gas"},
"Rb": {"name": "Rubidium", "atomic_number": 37, "atomic_mass": "85.468", "group": "Alkali metal"},
"Sr": {"name": "Strontium", "atomic_number": 38, "atomic_mass": "87.62", "group": "Alkaline earth metal"},
"Y": {"name": "Yttrium", "atomic_number": 39, "atomic_mass": "88.906", "group": "Transition metal"},
"Zr": {"name": "Zirconium", "atomic_number": 40, "atomic_mass": "91.224", "group": "Transition metal"},
"Nb": {"name": "Niobium", "atomic_number": 41, "atomic_mass": "92.906", "group": "Transition metal"},
"Mo": {"name": "Molybdenum", "atomic_number": 42, "atomic_mass": "95.95", "group": "Transition metal"},
"Tc": {"name": "Technetium", "atomic_number": 43, "atomic_mass": "98", "group": "Transition metal"},
"Ru": {"name": "Ruthenium", "atomic_number": 44, "atomic_mass": "101.07", "group": "Transition metal"},
"Rh": {"name": "Rhodium", "atomic_number": 45, "atomic_mass": "102.91", "group": "Transition metal"},
"Pd": {"name": "Palladium", "atomic_number": 46, "atomic_mass": "106.42", "group": "Transition metal"},
"Ag": {"name": "Silver", "atomic_number": 47, "atomic_mass": "107.87", "group": "Transition metal"},
"Cd": {"name": "Cadmium", "atomic_number": 48, "atomic_mass": "112.41", "group": "Transition metal"},
"In": {"name": "Indium", "atomic_number": 49, "atomic_mass": "114.82", "group": "Post-transition metal"},
"Sn": {"name": "Tin", "atomic_number": 50, "atomic_mass": "118.71", "group": "Post-transition metal"},
"Sb": {"name": "Antimony", "atomic_number": 51, "atomic_mass": "121.76", "group": "Metalloid"},
"Te": {"name": "Tellurium", "atomic_number": 52, "atomic_mass": "127.60", "group": "Metalloid"},
"I": {"name": "Iodine", "atomic_number": 53, "atomic_mass": "126.90", "group": "Reactive nonmetal"},
"Xe": {"name": "Xenon", "atomic_number": 54, "atomic_mass": "131.29", "group": "Noble gas"},
"Cs": {"name": "Cesium", "atomic_number": 55, "atomic_mass": "132.91", "group": "Alkali metal"},
"Ba": {"name": "Barium", "atomic_number": 56, "atomic_mass": "137.33", "group": "Alkaline earth metal"},
"La": {"name": "Lanthanum", "atomic_number": 57, "atomic_mass": "138.91", "group": "Lanthanide"},
"Ce": {"name": "Cerium", "atomic_number": 58, "atomic_mass": "140.12", "group": "Lanthanide"},
"Pr": {"name": "Praseodymium", "atomic_number": 59, "atomic_mass": "140.91", "group": "Lanthanide"},
"Nd": {"name": "Neodymium", "atomic_number": 60, "atomic_mass": "144.24", "group": "Lanthanide"},
"Pm": {"name": "Promethium", "atomic_number": 61, "atomic_mass": "145", "group": "Lanthanide"},
"Sm": {"name": "Samarium", "atomic_number": 62, "atomic_mass": "150.36", "group": "Lanthanide"},
"Eu": {"name": "Europium", "atomic_number": 63, "atomic_mass": "151.96", "group": "Lanthanide"},
"Gd": {"name": "Gadolinium", "atomic_number": 64, "atomic_mass": "157.25", "group": "Lanthanide"},
"Tb": {"name": "Terbium", "atomic_number": 65, "atomic_mass": "158.93", "group": "Lanthanide"},
"Dy": {"name": "Dysprosium", "atomic_number": 66, "atomic_mass": "162.50", "group": "Lanthanide"},
"Ho": {"name": "Holmium", "atomic_number": 67, "atomic_mass": "164.93", "group": "Lanthanide"},
"Er": {"name": "Erbium", "atomic_number": 68, "atomic_mass": "167.26", "group": "Lanthanide"},
"Tm": {"name": "Thulium", "atomic_number": 69, "atomic_mass": "168.93", "group": "Lanthanide"},
"Yb": {"name": "Ytterbium", "atomic_number": 70, "atomic_mass": "173.05", "group": "Lanthanide"},
"Lu": {"name": "Lutetium", "atomic_number": 71, "atomic_mass": "174.97", "group": "Lanthanide"},
"Hf": {"name": "Hafnium", "atomic_number": 72, "atomic_mass": "178.49", "group": "Transition metal"},
"Ta": {"name": "Tantalum", "atomic_number": 73, "atomic_mass": "180.95", "group": "Transition metal"},
"W": {"name": "Tungsten", "atomic_number": 74, "atomic_mass": "183.84", "group": "Transition metal"},
"Re": {"name": "Rhenium", "atomic_number": 75, "atomic_mass": "186.21", "group": "Transition metal"},
"Os": {"name": "Osmium", "atomic_number": 76, "atomic_mass": "190.23", "group": "Transition metal"},
"Ir": {"name": "Iridium", "atomic_number": 77, "atomic_mass": "192.22", "group": "Transition metal"},
"Pt": {"name": "Platinum", "atomic_number": 78, "atomic_mass": "195.08", "group": "Transition metal"},
"Au": {"name": "Gold", "atomic_number": 79, "atomic_mass": "196.97", "group": "Transition metal"},
"Hg": {"name": "Mercury", "atomic_number": 80, "atomic_mass": "200.59", "group": "Transition metal"},
"Tl": {"name": "Thallium", "atomic_number": 81, "atomic_mass": "204.38", "group": "Post-transition metal"},
"Pb": {"name": "Lead", "atomic_number": 82, "atomic_mass": "207.2", "group": "Post-transition metal"},
"Bi": {"name": "Bismuth", "atomic_number": 83, "atomic_mass": "208.98", "group": "Post-transition metal"},
"Po": {"name": "Polonium", "atomic_number": 84, "atomic_mass": "209", "group": "Post-transition metal"},
"At": {"name": "Astatine", "atomic_number": 85, "atomic_mass": "210", "group": "Metalloid"},
"Rn": {"name": "Radon", "atomic_number": 86, "atomic_mass": "222", "group": "Noble gas"},
"Fr": {"name": "Francium", "atomic_number": 87, "atomic_mass": "223", "group": "Alkali metal"},
"Ra": {"name": "Radium", "atomic_number": 88, "atomic_mass": "226", "group": "Alkaline earth metal"},
"Ac": {"name": "Actinium", "atomic_number": 89, "atomic_mass": "227", "group": "Actinide"},
"Th": {"name": "Thorium", "atomic_number": 90, "atomic_mass": "232.04", "group": "Actinide"},
"Pa": {"name": "Protactinium", "atomic_number": 91, "atomic_mass": "231.04", "group": "Actinide"},
"U": {"name": "Uranium", "atomic_number": 92, "atomic_mass": "238.03", "group": "Actinide"},
"Np": {"name": "Neptunium", "atomic_number": 93, "atomic_mass": "237", "group": "Actinide"},
"Pu": {"name": "Plutonium", "atomic_number": 94, "atomic_mass": "244", "group": "Actinide"},
"Am": {"name": "Americium", "atomic_number": 95, "atomic_mass": "243", "group": "Actinide"},
"Cm": {"name": "Curium", "atomic_number": 96, "atomic_mass": "247", "group": "Actinide"},
"Bk": {"name": "Berkelium", "atomic_number": 97, "atomic_mass": "247", "group": "Actinide"},
"Cf": {"name": "Californium", "atomic_number": 98, "atomic_mass": "251", "group": "Actinide"},
"Es": {"name": "Einsteinium", "atomic_number": 99, "atomic_mass": "252", "group": "Actinide"},
"Fm": {"name": "Fermium", "atomic_number": 100, "atomic_mass": "257", "group": "Actinide"},
"Md": {"name": "Mendelevium", "atomic_number": 101, "atomic_mass": "258", "group": "Actinide"},
"No": {"name": "Nobelium", "atomic_number": 102, "atomic_mass": "259", "group": "Actinide"},
"Lr": {"name": "Lawrencium", "atomic_number": 103, "atomic_mass": "266", "group": "Actinide"},
"Rf": {"name": "Rutherfordium", "atomic_number": 104, "atomic_mass": "267", "group": "Transition metal"},
"Db": {"name": "Dubnium", "atomic_number": 105, "atomic_mass": "270", "group": "Transition metal"},
"Sg": {"name": "Seaborgium", "atomic_number": 106, "atomic_mass": "271", "group": "Transition metal"},
"Bh": {"name": "Bohrium", "atomic_number": 107, "atomic_mass": "270", "group": "Transition metal"},
"Hs": {"name": "Hassium", "atomic_number": 108, "atomic_mass": "277", "group": "Transition metal"},
"Mt": {"name": "Meitnerium", "atomic_number": 109, "atomic_mass": "278", "group": "Unknown"},
"Ds": {"name": "Darmstadtium", "atomic_number": 110, "atomic_mass": "281", "group": "Unknown"},
"Rg": {"name": "Roentgenium", "atomic_number": 111, "atomic_mass": "282", "group": "Unknown"},
"Cn": {"name": "Copernicium", "atomic_number": 112, "atomic_mass": "285", "group": "Transition metal"},
"Nh": {"name": "Nihonium", "atomic_number": 113, "atomic_mass": "286", "group": "Unknown"},
"Fl": {"name": "Flerovium", "atomic_number": 114, "atomic_mass": "289", "group": "Post-transition metal"},
"Mc": {"name": "Moscovium", "atomic_number": 115, "atomic_mass": "290", "group": "Unknown"},
"Lv": {"name": "Livermorium", "atomic_number": 116, "atomic_mass": "293", "group": "Unknown"},
"Ts": {"name": "Tennessine", "atomic_number": 117, "atomic_mass": "294", "group": "Unknown"},
"Og": {"name": "Oganesson", "atomic_number": 118, "atomic_mass": "294", "group": "Unknown"}}

colors = {"Alkali metal": "Light pink",
"Alkaline earth metal": "orange",
"Lanthanide": "Yellow",
"Actinide": "Green",
"Transition metal": "Light blue",
"Post-transition metal": "hot pink",
"Metalloid": "Violet",
"Reactive nonmetal": "Red",
"Noble gas": "Magenta",
"Unknown": "Gray"}

# Layout (R, C, S)
layout = [# Period 1 
(0, 0, "H"), (0, 17, "He"),
# Period 2
(1, 0, "Li"), (1, 1, "Be"), (1, 12, "B"), (1, 13, "C"), (1, 14, "N"), (1, 15, "O"), (1, 16, "F"), (1, 17, "Ne"),
# Period 3
(2, 0, "Na"), (2, 1, "Mg"), (2, 12, "Al"), (2, 13, "Si"), (2, 14, "P"), (2, 15, "S"), (2, 16, "Cl"), (2, 17, "Ar"),
# Period 4
(3, 0, "K"), (3, 1, "Ca"), (3, 2, "Sc"), (3, 3, "Ti"), (3, 4, "V"), (3, 5, "Cr"), (3, 6, "Mn"), (3, 7, "Fe"), 
(3, 8, "Co"), (3, 9, "Ni"), (3, 10, "Cu"), (3, 11, "Zn"), (3, 12, "Ga"), (3, 13, "Ge"), (3, 14, "As"), 
(3, 15, "Se"), (3, 16, "Br"), (3, 17, "Kr"),
# Period 5
(4, 0, "Rb"), (4, 1, "Sr"), (4, 2, "Y"), (4, 3, "Zr"), (4, 4, "Nb"), (4, 5, "Mo"), (4, 6, "Tc"), (4, 7, "Ru"), 
(4, 8, "Rh"), (4, 9, "Pd"), (4, 10, "Ag"), (4, 11, "Cd"), (4, 12, "In"), (4, 13, "Sn"), (4, 14, "Sb"), 
(4, 15, "Te"), (4, 16, "I"), (4, 17, "Xe"),
# Period 6
(5, 0, "Cs"), (5, 1, "Ba"), (5, 2, "La"), (5, 3, "Hf"), (5, 4, "Ta"), (5, 5, "W"), (5, 6, "Re"), (5, 7, "Os"), 
(5, 8, "Ir"), (5, 9, "Pt"), (5, 10, "Au"), (5, 11, "Hg"), (5, 12, "Tl"), (5, 13, "Pb"), (5, 14, "Bi"), 
(5, 15, "Po"), (5, 16, "At"), (5, 17, "Rn"),
# Period 7
(6, 0, "Fr"), (6, 1, "Ra"), (6, 2, "Ac"), (6, 3, "Rf"), (6, 4, "Db"), (6, 5, "Sg"), (6, 6, "Bh"), (6, 7, "Hs"), 
(6, 8, "Mt"), (6, 9, "Ds"), (6, 10, "Rg"), (6, 11, "Cn"), (6, 12, "Nh"), (6, 13, "Fl"), (6, 14, "Mc"), 
(6, 15, "Lv"), (6, 16, "Ts"), (6, 17, "Og"),
# Lanthanides (separated)
(8, 3, "Ce"), (8, 4, "Pr"), (8, 5, "Nd"), (8, 6, "Pm"), (8, 7, "Sm"), (8, 8, "Eu"), (8, 9, "Gd"), 
(8, 10, "Tb"), (8, 11, "Dy"), (8, 12, "Ho"), (8, 13, "Er"), (8, 14, "Tm"), (8, 15, "Yb"), (8, 16, "Lu"),
# Actinides (separated)
(9, 3, "Th"), (9, 4, "Pa"), (9, 5, "U"), (9, 6, "Np"), (9, 7, "Pu"), (9, 8, "Am"), (9, 9, "Cm"), 
(9, 10, "Bk"), (9, 11, "Cf"), (9, 12, "Es"), (9, 13, "Fm"), (9, 14, "Md"), (9, 15, "No"), (9, 16, "Lr"),]

def element_color(symbol):
    data = elements.get(symbol)
    if data:
        group = data.get("group", "Unknown")
        return colors.get(group, "gray")
    return "gray"

def show_element_info(symbol):
    try:
        data = elements[symbol]
        info = f"Element: {data['name']}\nSymbol: {symbol}\nAtomic Number: {data['atomic_number']}\nAtomic Mass: {data['atomic_mass']}\nGroup: {data['group']}"
        messagebox.showinfo("Element Information", info)
    except KeyError:
        messagebox.showerror("Not Found", f"No data found for {symbol}")

def create_legend(parent):
    legend_frame = tk.Frame(parent, bg="white")
    legend_frame.pack(pady=10)

    tk.Label(legend_frame, text="Element Groups", font=("Times New Roman", 12, "bold"), bg="white").pack()
    legend_grid = tk.Frame(legend_frame, bg="light gray")
    legend_grid.pack()

    for i, (group, color) in enumerate(colors.items()):
        item = tk.Frame(legend_grid, bg="light gray")
        item.grid(row=i // 3, column=i % 3, padx=10, pady=5, sticky="w")
        color_box = tk.Label(item, text="  ", bg=color, width=3, relief="solid", borderwidth=1)
        color_box.pack(side="left")
        label = tk.Label(item, text=group, font=("Times New Roman", 10, "bold"), bg="light gray")
        label.pack(side="left", padx=5)

def main():
    r = tk.Tk()
    r.title("Digital Periodic Table Of Elements")
    r.geometry("1000x800")
    r.configure(bg="white")

    main_frame = tk.Frame(r, bg="white")
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)

    tk.Label(main_frame, text="Digital Periodic Table Of Elements", font=("Times New Roman", 20, "bold"), bg="white").pack(pady=(0, 20))

    # Main grid frame for numbers and elements
    label_frame = tk.Frame(main_frame, bg="white")
    label_frame.pack()

    # Group 
    for col in range(18):
        tk.Label(label_frame, text=str(col+1), width=4, bg="white", fg="black", font=("Times New Roman", 10)).grid(row=0, column=col+1)

    # Period 
    for row in range(1, 8):
        tk.Label(label_frame, text=str(row), width=4, bg="white", fg="black", font=("Times New Roman", 10)).grid(row=row, column=0)

    # Main periodic table 
    for row, col, symbol in layout:
        color = element_color(symbol)
        btn = tk.Button(label_frame, text=symbol, width=4, height=2, bg=color,
                        font=("Times New Roman", 10, "bold"),
                        command=lambda s=symbol: show_element_info(s),
                        relief="raised", borderwidth=2)
        btn.grid(row=row+1, column=col+1, padx=1, pady=1)

    # Separator line
    separator = tk.Frame(label_frame, height=2, bg="black")
    separator.grid(row=8, column=1, columnspan=18, sticky="ew", pady=10)

    # Ln
    tk.Label(label_frame, text="Lanthanides\n[La-Lu]", font=("Times New Roman", 10, "bold"), bg="white").grid(row=9, column=1, columnspan=3, sticky="w")

    # Ac
    tk.Label(label_frame, text="Actinides\n[Ac-Lr]", font=("Times New Roman", 10, "bold"), bg="white").grid(row=10, column=1, columnspan=3, sticky="w")

    create_legend(main_frame)
    r.mainloop()

main()

