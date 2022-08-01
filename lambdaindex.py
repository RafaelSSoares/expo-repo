# a = lambda x, y: x * y

# print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 3],
    ['P3', 16],
    ['P4', 14],
    ['P5', 22],
]

# def func(item):
#     return item[1]

# lista.sort(key=lambda item: item [1], reverse=True)

print(sorted(lista, key=lambda i: i[1]))