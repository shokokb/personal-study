# coding : UTF-8

from enum import Enum

class Http:
    @staticmethod
    def error(no) -> str:
        try:
            err_no = HttpError(no)
        except ValueError:
            err_no = None

        match (err_no):
            case HttpError.UNKNOWN_ERROR:
                return "Unknown Error"
            case HttpError.BAD_REQUEST:
                return "Bad Request"
            case HttpError.NOT_FOUND:
                return "Not Found"
            case _:
                return f"I don't know this error {no}"

class HttpError(Enum):
    UNKNOWN_ERROR = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404    

class Color:
    @staticmethod
    def get_color_name(color):
        match (color):
            case [0, 0, 0]:
                return "Black"
            case [255, 0, 0]:
                return "Red"
            case [255, _, _]:
                return "Something Red-ish"                
            case _:
                return "Unknown Color"

def main():
    queue = [400, 200, 300]
    for err_no in queue:
        print(Http.error(err_no))

    color = [255, 1, 0]
    print(Color.get_color_name(color))


if __name__  == "__main__":
    main()
