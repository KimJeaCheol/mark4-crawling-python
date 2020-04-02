try:
    a = 10
    b = 0

    print(a)
    print(b)
    print(a / 0)
except IndexError:
    print(' IndexError 예외처리')
except ZeroDivisionError:
    print(' ZeroDivisionError 예외처리')
else:
    print("정상적으로 실행됬을 때")
finally:
    print("최종적으로 무조건 실행되는 구문")
