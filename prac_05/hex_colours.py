COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Aqua": "#00ffff", "Baker-Miller Pink": "#ff91af",
                  "Bitter Lemon": "#cae00d", "Black Coffee": "#3b2f2f", "Bleu de France": "#318ce7",
                  "Bright Lilac": "#d891ef", "Brilliant Rose": "#ff5a3", "Bulgarian Rose": "480607",
                  "Cadmium Green": "#006b3c"}

colour_name = input("Enter the colour name: ").title()
while colour_name != "":
    print(f"The code for {colour_name} is {COLOUR_TO_CODE.get(colour_name)}")
    colour_name = input("Enter the colour name: ").title()

print("Thank you and see you again next time.")