import random
# importing PIL.Image library and os library
from PIL import Image
import os

ran_numr = random.randint(-100, 100)
ran_numg = random.randint(-100, 100)
ran_numb = random.randint(-100, 100)
rate = []

print(
    "In the following questions, you can pick more than one choice,but only 1 each time."
)
ans = (input(
    "1. How do you feel of last picture? (,,・ω・,,)\n Too warm:1 (´ﾟдﾟ`)\n\n Too cold:2 (°ཀ°)\n\n Too Bright:3 ╰(〒皿〒)╯\n\n Too dark:4 (◞‸◟)\n\n Too gray:5 (╥﹏╥)\n\n Not bad: fine ╮(′～‵〞)╭\n"
))
rate.append(ans)
if ans == "1":
    print("(´ﾟдﾟ`)")
elif ans == "2":
    print("°ཀ°")
elif ans == "3":
    print("╰(〒皿〒)╯")
elif ans == "4":
    print("(◞‸◟)")
elif ans == "5":
    print("(╥﹏╥)")
else:
    print("╮(′～‵〞)╭")
if ans == "fine":
    rate = []
while "fine" not in rate or "no" not in rate:
    #if "fine" in rate:
    #break
    ans = input(("And you next concern is___?" + "(If no, just say no)\n"))
    if ans == "no":
        break
    rate.append(ans)
    if ans == "1":
        print("(´ﾟдﾟ`)")
    elif ans == "2":
        print("°ཀ°")
    elif ans == "3":
        print("╰(〒皿〒)╯")
    elif ans == "4":
        print("(◞‸◟)")
    elif ans == "5":
        print("(╥﹏╥)")
    else:
        print("╮(′～‵〞)╭")
    if "1" in rate and "2" in rate:
        print(
            "Stop being naughty, can't pick 2 options against  each other. (❍ᴥ❍ʋ)"
        )
        break
    elif "3" in rate and "4" in rate:
        print(
            "Stop being naughty, can't pick 2 options against  each other. (❍ᴥ❍ʋ)"
        )
        break
    elif "fine" in rate:
        print("You've already chosen 'not bad'. Try to customize. (´◉‿◉｀)")
        break
    for i in range(len(rate)):
        count = 0
        p = rate[i]
        for i in range(len(rate)):
            if rate[i] == p:
                count += 1
    if count > 1:
        print("I knew that you have 2 same options,stop it(╬☉ д⊙)")
        break
if not rate == []:
    n = int(input("Unsatisfied rate________?(1 to 10)\n"))
mode = input("Wanna customize? ( ﾟ∀ﾟ)o彡ﾟ\n")
if mode == "no":
    print("Fine. Let's try it next time. (〒︿〒)")
else:
    a = int(input("expected change value in red: from -256 to 256\n"))
    e = int(input("expected change value in green: from -256 to 256\n"))
    c = int(input("expected change value in blue: from -256 to 256\n"))
# Deletes old created images if they exist
if os.path.exists("newImage.jpg"):
    os.remove("newImage.jpg")

# Prints two blank lines to start our program output
print("\n\n")

# Opens image - Local File in repl.it
img = Image.open('glow1.jpg')

# Rescale image size down, if needed
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
    scale = mwidth
else:
    scale = mheight
if scale != 0:
    img = img.resize((width // scale, height // scale))


########################
#        Filter        #
########################
def newFilter():
    # Starts at the first pixel in the image
    location = 0
    # Continues until it has looped through all pixels
    while location < len(new_pixels):
        # Gets the current color of the pixel at location
        p = new_pixels[location]

        # Splits color into red, green and blue components
        r = p[0]
        g = p[1]
        b = p[2]
        # Perform pixel manipulation and stores results
        # to a new red, green and blue components
        if mode == "yes":
            newr = r + a
            newg = g + e
            newb = b + c
        if "1" in rate:
            newr = r // n
            newg = g + 4 * n
            newb = b + 10 * n
        if "2" in rate:
            newr = r + 10 * n
            newg = g - 4 * n
            newb = b // n
        if "3" in rate:
            newr = r - 10 * n
            newg = g - 10 * n
            newb = b - 10 * n
        if "4" in rate:
            newr = r + 10 * n
            newg = g + 10 * n
            newb = b + 10 * n
        if "5" in rate:
            newr = r + ran_numr
            newg = g + ran_numg
            newb = b + ran_numb
        #elif ans==""
        # Assign new red, green and blue components to pixel
        # at that specific location
        new_pixels[location] = (newr, newg, newb)
        # Changes the location to the next pixel in array
        location = location + 1
    # Creates a new image, the same size as the original
    # using RGB value format
    newImage = Image.new("RGB", img.size)
    # Assigns the pixel values to newImage
    newImage.putdata(new_pixels)
    # Saves the new image file
    newImage.save("newImage.jpg")


# Creates an ImageCore Object from original image
pixels = img.getdata()
# Creates empty array to hold new pixel values
new_pixels = []
# For every pixel from our original image, it saves
# a copy of that pixel to our new_pixels array
for p in pixels:
    new_pixels.append(p)
print("Whirr,whirr,whirr,whirr——————")
newFilter()
print("           ____________")
print("          /           /")
print("          ‖           ‖")
print("          ‖           ‖")
print("          ‖           ‖")
print("          ‖           ‖")
print("          /===========/ ▄▃▂▂▂")
print("       ▇████████████▇▆▅▇▆▅▄▄▂")
print("      █   ▂▂▂▂▂Ⓦ ▂▂▂▂▂▂   ▌+ ▍")
print("      █▂▂▂█┗----------┛█▂▂▌▂▂▍")
print("        / // ▆▇█▇▆▅▄▃ // /")
print("      /__//    ▼     //__/")
print("      /_// ▅▃▅  ▅▂▅ //_/")
print("       /============/")
print("Da,Da! It is printed now! Recive your picure!")
# Calls the newFilter function to create the image
