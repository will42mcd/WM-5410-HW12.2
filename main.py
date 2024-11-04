from PIL import Image, ImageOps
import math

def convolve(img, sz, step):
    # if pixels are an odd size we need a whole num
    start = math.floor(sz/2)
    con_pixels = []
    for x in range(start, img.size[0]-1, step):
        for y in range(start, img.size[1]-1, step):
            # top row
            tl = img.getpixel((y-1, x-1))
            tc = img.getpixel((y-1, x))
            tr = img.getpixel((y-1, x+1))

            # center row
            lc = img.getpixel((y, x-1))
            cc = img.getpixel((y, x))
            rc = img.getpixel((y, x+1))

            # bottom row
            bl = img.getpixel((y+1, x-1))
            bc = img.getpixel((y+1, x))
            br = img.getpixel((y+1, x+1))

            sum = tl*3 + tc*10 + tr*3 + lc*0 + cc*0 + rc*0 + bl*-3 + bc*-10 + br*-3
            div = 1
            r_ave = math.floor(sum/div)
            if r_ave < 0:
                r_ave = 0 

            sum = tl*-3 + tc*-10 + tr*-3 + lc*0 + cc*0 + rc*0 + bl*3 + bc*10 + br*3
            div = 1
            l_ave = math.floor(sum/div)
            if l_ave < 0:
                l_ave = 0

            sum = tl*3 + tc*0 + tr*-3 + lc*10 + cc*0 + rc*-10 + bl*3 + bc*0 + br*-3
            div = 1
            b_ave = math.floor(sum/div)
            if b_ave < 0:
                b_ave = 0

            sum = tl*-3 + tc*0 + tr*3 + lc*-10 + cc*0 + rc*10 + bl*-3 + bc*0 + br*3
            div = 1
            t_ave = math.floor(sum/div)
            if t_ave < 0:
                t_ave = 0

            ave = math.floor(r_ave + l_ave + b_ave + t_ave)
            con_pixels.append(ave)
    # Our new image is smaller than original and needs to be whole num
    dims = (math.floor(img.size[0]/step)-1, math.floor(img.size[1]/step)-1)
    output = Image.new('L', dims)
    print(len(con_pixels))
    output.putdata(con_pixels)
    output.show()
# end convolve():

def main():
    og_image = Image.open("demo.png")
    # Convert to greyscale
    gray_image = ImageOps.grayscale(og_image)
    # open original for comparison
    gray_image.show()
    # kernal size of 3x3
    convolve(gray_image,3, 2)
# end of main()

if __name__ == "__main__":
    main() 