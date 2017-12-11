#=============================================================================
#
# Utility class to read in a file and return a list of lines
#
#-----------------------------------------------------------------------------

#=============================================================================
def read_file(name):
#
#-----------------------------------------------------------------------------
    lines = []
    with open(name) as fp:
        lines = fp.readlines()
    return [line.strip() for line in lines]


#=============================================================================
def raw_read_file(name):
#
#-----------------------------------------------------------------------------
    lines = []
    text = ""
    with open(name) as fp:
        text = fp.read()
    return text