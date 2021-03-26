class FourDigitYearConverter:
    regex = '\d{4}'
    def to_python(self,value): #숫자 정수로 변환
        return int(value)
    def to_url(self, value):
        return "%04d" % value # 정수로 넘어온 값을 문자열로 변환 -> Url 반환 시 호출 문자열 변환