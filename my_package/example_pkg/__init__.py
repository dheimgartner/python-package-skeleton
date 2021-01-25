# If I do not include this then my_fun has to be imported explicitly:
# import example_pkg will now allow you to write example_pkg.my_fun...
# Generally you might not want to force users to import modules when loading the package.
# But in this case, I want!
from example_pkg import my_fun