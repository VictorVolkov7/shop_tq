def generate_sequence(n: int) -> list[int]:
    """
    Напишите программу, которая выводит n первых элементов последовательности 122333444455555…
    (число повторяется столько раз, чему оно равно).
    :param n: количество элементов в последовательности
    :return: список с первыми n элементами последовательности
    """
    sequence: list = []
    start_num: int = 1

    while len(sequence) < n:
        sequence.extend([start_num] * start_num)
        start_num += 1

    return sequence[:n]


num = int(input("Введите число n: "))
result = generate_sequence(num)
print("Первые", num, "элементов последовательности:", result)
