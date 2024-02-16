# README for BodePlotter

## Overview

This Python script utilizes the pandas and matplotlib libraries to read frequency response data from a CSV file and plot the magnitude (in dB) and phase (in degrees) as functions of frequency. The script generates two subplots: one for the frequency vs magnitude and another for the frequency vs phase. The frequency axis is plotted on a logarithmic scale for better visualization of a wide range of frequencies.

## Requirements

- Python 3.x
- pandas
- matplotlib

Make sure you have Python installed on your system. You can then install pandas and matplotlib using pip if you haven't done so already:

```bash
pip install pandas matplotlib
```

## Input Data Format

Your input data should be in a CSV file named `data.csv` located in the same directory as the script. The CSV file should have at least three columns:
- `frequency`: The frequency in radians per second (rad/s).
- `magnitude_db`: The magnitude of the response in decibels (dB).
- `phase_degrees`: The phase of the response in degrees.

Example of `data.csv` content:

```
frequency,magnitude_db,phase_degrees
0.1, -20, -45
1, -15, -30
10, -10, -15
```

## Usage Instructions

1. Ensure you have `data.csv` in the same directory as the script. The CSV file should be formatted as described in the Input Data Format section.
2. Run the script with Python:

```bash
python main.py
```

3. After running the script, two plots will be displayed in a single window:
   - The top plot shows the frequency vs magnitude.
   - The bottom plot shows the frequency vs phase.

Both plots have a logarithmic scale for the frequency axis, and they include grid lines for easier reading of the data. You can analyze the frequency response of your system with these visualizations.

## Customization

You can customize the plots by modifying the script. For example, you can change the line color, style, marker, or the grid's appearance by adjusting the parameters in the `semilogx()` and `grid()` function calls. You can also modify the labels, titles, or the size of the figure to better suit your needs.