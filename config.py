
HARFILED = "modeldata/haarcascade_frontalface_default.xml"

ImagePath = "modeldata/image/"


def getSemImagePath(sem):
    return ImagePath + sem + "/"


def getSemImagePathtf(sem):
    return "modeldata/tf_train/" + sem + "/"

def getTrainedModelPath(sem):
    return "modeldata/trainningImageLabel/" + sem + "/Trainner.yml"