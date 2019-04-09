class Bmi:

    def __init__(self, name, w, h):
        self.w = w
        self.h = h
        self.name = name

    def get_bmi(self):
        bmi = self.w/((self.h*self.h)/10000)
        if bmi >= 40.0:
            result = "고도비만"
        elif bmi >= 35.0:
            result = "중등도비만"
        elif bmi >= 30.0:
            result = "경도비만"
        elif bmi >= 25.0:
            result = "과체중"
        elif bmi >= 18.0:
            result = "정상체중"
        elif bmi < 18.0:
            result = "저체중"

        return result