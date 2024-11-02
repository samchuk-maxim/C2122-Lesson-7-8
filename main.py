# class Human:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
#
# human_list=[Human("Andriy",22),
#             Human("Bohdan",52),
#             Human("Artem",19)]
#
# print(human_list)
#
# human_iter=iter(human_list)
#
# for elem in human_iter:
#     print(elem.Name, elem.Age)

# class Counter:
#     def __init__(self,max_value):
#         self.value = 0
#         self.max_value=max_value
#
#     def __iter__(self):
#         self.value=0
#         return self
#
#     def __next__(self):
#         self.value += 1
#         if self.value > self.max_value:
#             raise StopIteration
#         return self.value
#
# timer = Counter(10)
#
# print(next(timer))
# print(next(timer))
# print(next(timer))
# print(next(timer))
# print(next(timer))
# print(next(timer))
# print(next(timer))
# print(next(timer))
# print(next(timer))
#
#
# def raise_to_the_degrees(number, max_degree):
#     i=0
#     for _ in range(max_degree):
#         yield number**i
#         i+=1
#
# res = raise_to_the_degrees(10000,3)
#
# for _ in res:
#     print(_)

import logging
from fileinput import filename

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="%(asctime)s: %(levelname)s  - %(message)s")

logging.info("info")

try:
    print(10/0)
except Exception:
    logging.exception("Exeption")


try:
    print(16/0)
except Exception:
    logging.exception("Exeption")


