import os
from fpdf import FPDF

def create_shirtificate(name):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Set font and size for the title
    pdf.set_font("Arial", size=24)
    pdf.cell(200, 10, "CS50 Shirtificate", ln=True, align='C')

    # Add image of shirt
    pdf.image("shirtificate.png", x=50, y=40, w=110)

    # Set font and size for the name
    pdf.set_font("Arial", size=18)
    pdf.set_text_color(255, 255, 255)  # White color
    pdf.set_xy(50, 180)  # Adjust coordinates as needed
    pdf.cell(0, 10, name, ln=True, align='C')

    pdf.output("shirtificate.pdf")

def main():
    name = input("Enter your name: ")
    create_shirtificate(name)

if __name__ == "__main__":
    main()
