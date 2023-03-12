# Team Submission File
# Jan Beyati:101186335, Gabriella Candussi:101187607, Muhammad Ameen:101196524
# Group: T016

# Imports

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, get_height, get_width

from simple_Cimpl_filters import grayscale

# Functions : Filters

def extreme_constrast(image: Image) -> Image: 
    """
    This functions takes an image and alters its 'r,g,b' values according to 
    its current value. Any value falling below and equal to 127 will be set to 
    0 and anything over will be set to 255.
    
    >>> image = load_image(choose_file())
    >>> show(extreme_constrast(image))
    """
    new_image = copy(image)
    
    for x,y, (r,g,b) in image:
        
        # FINDING THE RED PIXEL VALUES
        if 0 <= r <= 127:
            red = 0
        else:
            red = 255
        
        # FINDING THE GREEN PIXEL VALUES    
        if 0 <= g <= 127:
            green = 0
        else:
            green = 255  
        
        # FINDING THE BLUE PIXEL VALUES    
        if 0 <= b <= 127:
            blue = 0
        else:
            blue = 255
            
        ex_con = create_color(red,green,blue)
        set_color(new_image,x,y,ex_con)
        
    return new_image

def posterize(image: Image) -> Image: 
    """
    This functions takes an image and alters its 'r,g,b' values according to 
    its current value, by using the '_adjust_component' it can determine which 
    quadrant a value falls under and then assigns it to a new value.
    
    >>> image = load_image(choose_file())
    >>> show(posterize(image))
    """    
    new_image = copy(image)
    
    for x,y, (r,g,b) in image:
        
        # FINDING THE RED PIXEL VALUES 
        red = _adjust_component(r)
        
        # FINDING THE GREEN PIXEL VALUES      
        green = _adjust_component(g)
        
        # FINDING THE BLUE PIXEL VALUES      
        blue = _adjust_component(b)
    
        post = create_color(red,green,blue)
        set_color(new_image,x,y,post)
        
    return new_image

def sepia_tinting(image: Image) -> Image: 
    """
    This functions takes an image and alters its 'r,g,b' values according to 
    its current value. This function works in unison with 'grayscale' because
    the image is first put through 'grayscale' and then the individual pixels 
    are changed according to whatver value it is. If the current value of 'r' 
    in 'grayscale' is greater than or equal to 0 and less than 63, then the new
    'b' and 'g' values are multiplied by 0.9 and 1.1 respectively. This is then
    done twice more to check other potential values.
    
    >>> image = load_image(choose_file())
    >>> show(sepia_tinting(image))
    """ 
    new_image = copy(image)
    grayscale_image = grayscale(new_image)
    for x,y, (r,g,b) in grayscale_image:
        
        if 0 <= r < 63:
            blue = (b*0.9)
            red = (r*1.1)
            green = g       
        elif 63 <= r <= 191:
            blue = (b*0.85)
            red = (r*1.15)
            green = g
        else:
            blue = (b*0.93)
            red = (r*1.08)
            green = g
            
        sep_tin = create_color(red,green,blue)
        set_color(grayscale_image,x,y,sep_tin)
        
    return grayscale_image

def three_tone (image: Image, first: str, second: str, third:str) -> Image: 
    """
    This functions takes an image and three strings that can be chosen from the 
    pre-set colors. This function looks at each individual pixel and determines
    the brightness. If the brightness at the pixel is greater than or equal to 0
    and less than or equal to 84 then the 'r' value of the pixel is set to the 
    'r' value of the FIRST given string. This is then done again to check if the
    brightness at the pixel is greater than or equal to 85 and less than or equal 
    to 170, if this is true then the 'r' value of the pixel is set to the 'r' 
    value of the SECOND string. Then the same check is done for anything over 
    255 where if that's true then the 'r' value of the pixel is set the the 'r'
    value of the THIRD string. This process is then repeated for the 'g' and 'b' 
    values.
    
    >>> image = load_image(choose_file())
    >>> show(three_tone(image))
    """     
    new_image = copy(image)
    
    for x,y, (r,g,b) in image:
        
        brightness = (r+g+b)/3
        
        # FINDING THE RED PIXEL VALUES
        if 0 <= brightness <= 84:
            red = first[0]
        elif 85<= brightness <= 170:
            red = second[0]
        else:
            red = third[0]
         
        # FINDING THE GREEN PIXEL VALUES    
        if 0 <= brightness <= 84:
            green = first[1]
        elif 85<= brightness <= 170:
            green = second[1]
        else:
            green = third[1]
        
        # FINDING THE BLUE PIXEL VALUES    
        if 0 <= brightness <= 84:
            blue = first[2]
        elif 85<= brightness <= 170:
            blue = second[2]
        else:
            blue = third[2]
            
        tone = create_color(red,green,blue)
        set_color(new_image,x,y,tone)
        
    return new_image

def detect_edges (image: Image, threshold:int) -> Image: 
    """
    This function takes an image and a threshold value and alters the 'r,g,b' values 
    of each pixel. The brightness of a pixel is first taken using the 'brightness'
    function and then the brightness of the pixel directly underneath is also taken.
    The absolute difference is found between the two brightness' and then that value
    is checked to be greater or less than the threshold value. If the value is greater
    than the threshold then the pixel is set to black, if it is less than the threshold
    then the pixel is set to white. Any pixel that is within the last row of the image
    is set to white.
    
    >>> image = load_image(choose_file())
    >>> show(detect_edges(image))
    """
    new_image = copy(image)
    
    for x,y, (r,g,b) in image:
        
        if  y != get_height(image)-1:
            
            pixel_under = get_color(image, x, y+1)
            if abs(_brightness(r,g,b) - _brightness(pixel_under[0], pixel_under[1], pixel_under[2]))  > threshold:  
                red = 0
                green = 0
                blue = 0
            else:
                red = 255
                green = 255
                blue = 255
                        
                det_im = create_color(red,green,blue)
                set_color(new_image,x,y,det_im)
        else:
            red = 255
            green = 255
            blue = 255   
            
    return new_image

def flip_vertical(image: Image) -> Image:
    """
    A function that takes in an image and
    returns a copy of the image flipped vertically.
    
    >>> flip_vertical(image)
    """
    new_image = copy(image)
    width = get_width(image)
    height = get_height(image)
    for x in range(width):
        for y in range(height//2):
            color_up = get_color(image, x, y)
            color_down = get_color(image, x, height - y - 1)
            set_color(new_image, x, height - y - 1, color_up)
            set_color(new_image, x, y, color_down)
            
    return new_image

# Functiond : Helper

def _adjust_component (x):
    """
    This functions takes a number and checks which quadrant between 0 and 255
    it will fall under.
    
    >>> _adjust_component (45)
    31
    >>> _adjust_component (78)
    95
    >>> _adjust_component (140)
    159
    >>> _adjust_component (230)
    223
    """  
    if 0 <= x <= 63:
        color = 31
    elif 64 <= x <= 127:
        color = 95
    elif 128 <= x <= 191:
        color = 159
    elif 192 <= x <= 255:
        color = 223
        
    return color

def _brightness (red:int, green:int, blue:int): 
    """
    Takes three integer values and returns the average.
    
    >>>_brightness(3,4,5)
    4
    """
    br = (red + green + blue) / 3
    
    return br

"""
# Main Script

image = load_image(choose_file())

# Pre-Set Colors for 'three_tone' function

lemon = (255,255,0)
cyan = (0,255,255)
green = (0,255,0)
white = (255, 255, 255)
magenta = (255, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
blood = (255, 0, 0)
gray = (128, 128, 128)

show(extreme_constrast(image))
show(posterize(image))
show(sepia_tinting(image))
show(three_tone(image, magenta, green, white))
show(detect_edges(image,8))
"""
image = load_image(choose_file())

show(flip_vertical(image))
