import numpy as np

def color_converter(color):
    """Converts rgb color format.

    Basically it only multiplies the array specifying a color times 256.
    Which corresponds to the format required in .bash_profile - in apple script.

    >>> Example: color_converter(color=[1, 1, 1])
    """
    return list(np.array(color) * 256)