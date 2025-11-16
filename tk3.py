from tkinter import*
from PIL import Image, ImageTk  

#cretae a widow with atitle bar and et its geometry as well
root = Tk()
root.title("Image in Tkinter")
root.geometry("400x408")

#NOw use Image.open to open and identify the given image file
upload = Image.open("python.png")

#COnvert this image to a Tkinter-compatible photo image
img = ImageTk.PhotoImage(upload)

#ADd image to TKinter LAbel
label = Label(root, image=img, height=350, width=300)
label.place(x=50, y=0)
label2 = Label(root, text="Python Logo", font=("Arial", 20))
label2.place(x=40, y=360)

#rUN THE APPLICATION
root.mainloop()
