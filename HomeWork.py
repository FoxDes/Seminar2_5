# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: -1
# out
# The data is incorrect

# from random import choices

# def abc_list(count, source):
#     result = []
#     if count < 0:
#         print("Вы ввели не положительное число!")
#     for i in range(count):
#         temp = choices(source, k=3)
#         result.append("".join(temp))
#     return result

# def out_abc(words: str) -> str:
#     return words.replace(" абв", "")
    
# count, source = int(input("Введите число: ")), input("Введите слово: ")
# words = abc_list(count, source)
# print(words)
# print(words)
# _______________________________________________________________________________________________________

# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

with open('text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст для кодировки: '))
with open('text_words.txt', 'r', encoding='UTF-8') as file:
    my_text = file.readline()
    text_compression = my_text.split()
print(my_text)

def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding
text_code_words = rle_encode(my_text)

with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_code_words}')
print(text_code_words)


# 3. * Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# Эмодзи

# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"