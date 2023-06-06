def islower(c) -> bool:
    for n in range(97, 123):
        if ord(c) == n:
            return True
    return False
