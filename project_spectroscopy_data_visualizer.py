import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

wavelengths = np.arange(200, 300, 10)
absorbance = np.array([0.15, 0.25, 0.40, 0.65, 0.85, 0.90, 0.80, 0.60, 0.40, 0.20])

df = pd.DataFrame({"Wavelength": wavelengths, "Absorbance": absorbance})
df["Calculated"] = df["Absorbance"].rolling(window=3, center=True).mean()

plt.plot(df["Wavelength"], df["Absorbance"], label="Original", marker='o', color = "black" , markerfacecolor = "red" , linestyle = "dashed" , linewidth = 0.5)
plt.plot(df["Wavelength"], df["Calculated"], label="Calculated", linestyle="dashdot", color="red")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.legend()
plt.title("UV-Vis Absorbance Spectrum")
plt.grid(True)
plt.show()