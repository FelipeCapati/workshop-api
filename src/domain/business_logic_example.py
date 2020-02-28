

class BusinessLogicExample:
    @staticmethod
    def process(number: int, bool: bool) -> str:
        if number >= 10:
            response = "The number is greater than or equal 10 and bool is %s" % str(bool)
        else:
            response = "The number is less than 10 and bool is %s" % str(bool)

        return response
