from cv2 import VideoCapture,imwrite

class image:
    def __init__(self):
        self.camera = VideoCapture(0)

    def capture(self):
        for i in range(20):
            self.retval,self.im = self.camera.read()
        self.retval,self.im = self.camera.read()
        imwrite("E:/Project/known_people/temp.jpg",self.im)
        del(self.camera)

if __name__=="__main__":
    ob = image()
    ob.capture()