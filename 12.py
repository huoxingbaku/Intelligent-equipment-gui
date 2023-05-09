from PIL import Image

# Load the icon
icon = Image.open("icon1.png")

# Change the icon's color
icon = icon.convert("RGBA")  # Convert to RGBA mode to support alpha channel
data = icon.getdata()  # Get pixel data
new_data = []  # Create a new list to store the modified pixel data

# Modify the pixel data to change the icon's color
for item in data:
    # Change the color of each pixel from blue to green
    if item[0] == 0 and item[1] == 0 and item[2] == 255:
        new_data.append((0, 255, 0, item[3]))  # Set the new color and alpha value
    else:
        new_data.append(item)  # Keep the original pixel data

# Update the icon with the modified pixel data
icon.putdata(new_data)

# Save the updated icon
icon.save("updated_icon.png")
