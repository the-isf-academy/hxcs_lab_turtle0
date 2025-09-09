# /////////// INSTRUCTIONS /////////////////
# 🔁 Let's use a loop to draw! 

# 💻️⃣  Run the file and see what happens! 

# 💻️⃣  How could you incorporate a loop into the shape() function?

# 💻️⃣  Lines 26-29 
#       How could you incorporate a loop into where the shape() function is used?

# 💻️⃣  Change the code in the shape function to create own shape! 
# ////////////////////////////////////////////

from turtle import * 

# This is a function. It's an easy way to name a block of code.
def shape(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)

# This is where the shape() function is used 
shape(100)
shape(200)
shape(300)
shape(400)
