"""
This is a simple recursive code that will search for a pixel of some colour, find out the colour of the pixels next to it
and check if they have a similar colour. then to know the are of something in an image, we just have to count those pixels
with the same colour.
"""


from PIL import Image
from IPython.display import display
import sys

sys.setrecursionlimit(10**4)

"""
photo names for easy access: "photo96 (1984)_resized.png"(120p) "photo_96_resized.png" (120p) "photo_124_resized.png" (110p) "photo124 (1984)_resized.png"(120p) "photo_752_resized.png" (201p)
							 "photo752 (1984)_resized.png" (232p) "photo_138_resized.png" (162p) "photo138 (1984)_resized.png" (197p) "photo_759_resized.png" (150p) "photo_111_resized.png" (87p)
							 "photo111 (1984)_resized.png" (140p)

colour rgb codes for easy acess in order: (50, 77, 69), (52, 81, 97), (43, 70, 89), (42, 70, 74) , (44, 73, 91), (56, 86, 84), (53, 75, 89), (0, 23, 49), (34, 71, 89), (197, 183, 157), (151, 156, 142)
"""
#set up the colour we'll be searching and the image we want to know the area of

colour = (42, 70, 74)
im = Image.open("photo124 (1984)_resized.png")

#basic image processing

basewidth = 120
wpercent = (basewidth / float(im.size[0]))
hsize = int((float(im.size[1]) * float(wpercent)))

img = im.resize((basewidth, hsize), Image.ANTIALIAS)

rgb_im = img.convert('RGB')
pi = rgb_im.load()


counter = 0
blue_pixels = []
seen = []


#need to adjust according to the image, and what best suits it
´
red_error = 6
green_error = 6
blue_error = 6


#find the first first pixel that correponds to our selected color

for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = rgb_im.getpixel((x, y))
		if r == colour[0] and g == colour[1] and b == colour[2]:
			pixel = (rgb_im.getpixel((x,y)), x, y)
			break

#the recursive function to analyze pixels near one another

def check_near(pixel, l):
	try:
		if l ==2400:
			return

		pixel1 = (pixel[1]+1,pixel[2])
		pixel2 = (pixel[1]-1,pixel[2])
		pixel3 = (pixel[1],pixel[2] + 1)
		pixel4 = (pixel[1],pixel[2] - 1)

		r, g, b = rgb_im.getpixel(pixel1)
		if (r >= pixel[0][0] - red_error and r <= pixel[0][0] + red_error) and (g >= pixel[0][1] - green_error and g <= pixel[0][1] + green_error) and (b >= pixel[0][2] - blue_error and b <= pixel[0][2] + blue_error):
			pixel1 = ((r,g,b), pixel1[0], pixel1[1])
			if not(pi[pixel1[1],pixel1[2]] == (0,0,0)):
				blue_pixels.append(pixel1)
				pi[pixel1[1],pixel1[2]] = (0,0,0)
				if not(pixel1 in seen):
					seen.append(pixel1)
					check_near(pixel1, l+1)

		r, g, b = rgb_im.getpixel(pixel2)

		if (r >= pixel[0][0] - red_error and r <= pixel[0][0] + red_error) and (g >= pixel[0][1] - green_error and g <= pixel[0][1] + green_error ) and (b >= pixel[0][2] - blue_error and b <= pixel[0][2] + blue_error):
			pixel2 = ((r,g,b), pixel2[0], pixel2[1])
			if not(pi[pixel2[1],pixel2[2]] == (0,0,0)):
				blue_pixels.append(pixel2)
				pi[pixel2[1],pixel2[2]] = (0,0,0)
				if not(pixel2 in seen):
					seen.append(pixel2)
					check_near(pixel2, l+1)

		r, g, b = rgb_im.getpixel(pixel3)

		if (r >= pixel[0][0] - red_error and r <= pixel[0][0] + red_error) and (g >= pixel[0][1] - green_error  and g <= pixel[0][1] + green_error) and (b >= pixel[0][2] - blue_error and b <= pixel[0][2] + blue_error):
			pixel3 = ((r,g,b), pixel3[0], pixel3[1])
			if not(pi[pixel3[1],pixel3[2]] == (0,0,0)):
				blue_pixels.append(pixel3)
				pi[pixel3[1],pixel3[2]] = (0,0,0)
				if not(pixel3 in seen):
					seen.append(pixel3)
					check_near(pixel3, l+1)

		r, g, b = rgb_im.getpixel(pixel4)

		if (r >= pixel[0][0] - red_error and r <= pixel[0][0] + red_error) and (g >= pixel[0][1] - green_error and g <= pixel[0][1] + green_error) and (b >= pixel[0][2] - blue_error and b <= pixel[0][2] + blue_error):
			pixel4 = ((r,g,b), pixel4[0], pixel4[1])
			if not(pi[pixel4[1],pixel4[2]] == (0,0,0)):
				blue_pixels.append(pixel4)
				pi[pixel4[1],pixel4[2]] = (0,0,0)
				if not(pixel4 in seen):
					seen.append(pixel4)
					check_near(pixel4, l+1)

		return
	except:
		pass
check_near(pixel,0)

# print the total pixels (area in pixels)
print(len(blue_pixels))

#show the image with the are in black to adjust parameters if needed for a better colouring
rgb_im.show()