# A series of utility functions that do not depend on neopixel
# or Raspberry Pi specific libraries


# INPUTS: rgb color in ([0,255], [0,255], [0,255])
# OUTPUTS: hsv color in ([0,360], [0,1], [0,1])
# EFFECT: Returns given rgb color in hsv
def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn

    if mx == mn: 
        h = 0
    else:
        if mx == r: h = (60 * ((g-b)/df) + 360) % 360
        if mx == g: h = (60 * ((b-r)/df) + 120) % 360
        if mx == b: h = (60 * ((r-g)/df) + 240) % 360

    if mx == 0:
        s = 0
    else:
        s = (df/mx)
    v = mx
    return h, s, v


# INPUTS: hsv color in ([0,360], [0,1], [0,1])
# OUTPUTS: rgb color in ([0,255], [0,255], [0,255]), rgb are ints
# EFFECT: Returns given hsv color in rgb
def hsv_to_rgb(h, s, v):
    if h > 360 or s > 1 or v > 1:
        print("hsv_to_rgb expects input ([0,360], [0,1], [0,1])")
        return (0, 0, 0)
    h = h / 360.
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; 
    p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); 
    v*=255; i%=6
    v = int(v)
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)
    print("hsv_to_rgb failed if chain")
    return (0, 0, 0)


# INPUTS: integer pos in [0,255]
# OUTPUTS: rgb color in ([0,255], [0,255], [0,255]), rgb are ints
# EFFECT: Maps a single variable to an rgb color smoothly
def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)


# INPUTS: 
#   - Value to be translates
#   - Lower and upper bound of the input range
#   - Lower and upper bound of the output range
# OUTPUTS: The translated float
# EFFECT: Translates a value in one range linearly onto another
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
