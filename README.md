# Karkhana.io-Assignment

Möbius Strip Modeling in Python
This project is a simple yet powerful Python script that models a Möbius strip using parametric equations. It generates a 3D surface mesh, approximates the surface area using numerical integration, and calculates the edge length along the boundary. The script also includes a 3D plot for visualizing the strip.

Features
Models a Mobius strip using parametric equations

Calculates surface area using numerical integration

Computes the edge length along both boundaries

Visualizes the strip in 3D using matplotlib

Parametric Equations Used
The Möbius strip is defined using the following equations:

x(u,v) = (R + v * cos(u/2)) * cos(u)  
y(u,v) = (R + v * cos(u/2)) * sin(u)  
z(u,v) = v * sin(u/2)
Where:

u is in [0, 2π]

v is in [-w/2, w/2]

R is the radius from the center to the strip

w is the width of the strip

How to Use
Make sure you have Python installed.

Install the required libraries:
pip install numpy matplotlib scipy

Run the script:
python mobius_strip_model.py

You’ll see a 3D visualization of the strip, along with printed values for the surface area and edge length.

Why I Built This
This was created as part of an internship assignment focused on 3D parametric modeling and numerical geometry in Python. It helped me get hands-on with real-world applications of math, code structuring, and data visualization.

Output Example

![image](https://github.com/user-attachments/assets/02e6b563-52e4-4d1b-97c0-ba370b14636f)

