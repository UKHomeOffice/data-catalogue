import logging

log = logging.getLogger(__name__)

def getIAOName(value):
    if value.startswith("type"):
        lines = value.split("\n")
        if lines[1].startswith("name"): 
            return lines[1][6:];
    else:
        return value

def getIAOEmail(value):
    if value.startswith("type"):
        lines = value.split("\n")
        if len(lines) > 2:
            if lines[2].startswith("email"): 
                return lines[2][7:];
    return ""

#method to create a short version of the description automatically
def createSummary(description):
    if len(description) < 170:
        return description
    else:
        try:
            if description[150:].index(".") > -1:
                return description[0:description[150:].index(".")+151]
        except ValueError:
            return description[0:180]
    return ""
