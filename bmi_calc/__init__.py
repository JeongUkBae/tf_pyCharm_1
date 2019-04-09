from bmi_calc.bmi import Bmi


def main():
    bmi = Bmi(input("이름")
              , int(input("몸무게"))
              , int(input("키")))
    print(" 이름 :: {} 몸무게 :: {} 키 :: {} BMI :: {} "
          .format(bmi.name
                  , bmi.w
                  , bmi.h
                  , bmi.get_bmi()))


if __name__ == '__main__':
    main()
