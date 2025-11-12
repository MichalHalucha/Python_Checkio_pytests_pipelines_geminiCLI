def determine_sign(num: int) -> str:
    if num > 0:
        return "positive"
    elif num == 0:
        return "zero"
    else:
        return "negative"
