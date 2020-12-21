from PIL import Image
  def Set_LSB(val, bit):
  if bit == '0':
    val = val & 254
  else:
    val = val | 1
  return val
  def Hide_text(transporter, text, outfile):
  text += chr(0)
  c_image = Image.open(transporter)
  c_image = c_image.convert('RGBA')
  
  out = Image.new(c_image.mode, c_image.size)
  pixel_list = list(c_image.getdata())
  new_array = []
  
  for i in range(len(text)):
    char_int = ord(text[i])
    cb = str(bin(char_int))[2:].zfill(8)
    pix1 = pixel_list[i*2]
    pix2 = pixel_list[(i*2)+1]
    newpix1 = []
    newpix2 = []
    
    
    for j in range(0,4):
        newpix1.append(Set_LSB(pix1[j], cb[j]))
        newpix2.append(Set_LSB(pix2[j], cb[j+4]))
        new_array.append(tuple(newpix1))
        new_array.append(tuple(newpix2))
        
new_array.extend(pixel_list[len(text)*2:])

out.putdata(new_array)
out.save(outfile)
print ("Image saved to" + " " + outfile)
Hide_text('c:\\Python\\bluecar.png', 'Give me six hours to chop down a tree and I will spend the first four sharpening the ax.', 'texthidden.png')
