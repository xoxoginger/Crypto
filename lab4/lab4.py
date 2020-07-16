import random
import string
import urllib.request


cnt_rnd_txt = 10
len_rnd_txt = 500000


def count_common_letters(text1, text2):
    cnt = 0
    for char1, char2 in zip(text1, text2):
        if (char1 == char2) and (char1 != ' ') and (char1 != '\0') and (char1 != '\n'):
            # print(char1)
            cnt += 1
    return cnt


def match_perc(text1, text2):
    return count_common_letters(text1, text2) / len(text1)


def gen_random_letters(n):
    text = ''
    while len(text) < n:
        len_word = random.randint(3, 10)
        word = ''.join(random.choice(string.ascii_letters) for _ in range(len_word))
        text += ' ' + word
    rem = len(text) - n
    if rem != 0:
        text = text[:-rem]
    return text


def gen_random_words(n):
    url = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
    response = urllib.request.urlopen(url)
    words = response.read().decode()
    words = words.splitlines()
    text = ''
    while len(text) < n:
        text += ' ' + random.choice(words)
    rem = len(text) - n
    if rem != 0:
        text = text[:-rem]
    return text


def full_of_sense():
    print("1. Два осмысленных текста на естественном языке.")
    handle1 = open('1.txt', 'r')
    text1 = handle1.read()
    # text1 = [line.rstrip() for line in text1]
    handle2 = open('2.txt', 'r')
    text2 = handle2.read()
    # text2 = [line.rstrip() for line in text2]
    min_len = min(len(text1), len(text2))
    text1 = text1[:min_len]
    text2 = text2[:min_len]
    print("Длина текста: {0}".format(min_len))
    print("Количество совпадений: {0}".format(count_common_letters(text1, text2)))
    print("Процент совпадений: {0}".format(match_perc(text1, text2)))


def sense_and_randoml():
    print("2. Осмысленный текст и текст из случайных букв.")
    handle1 = open('1.txt', 'r')
    text1 = handle1.read()
    s = 0
    for _ in range(cnt_rnd_txt):
        text2 = gen_random_letters(len(text1))
        s += match_perc(text1, text2)
    s /= cnt_rnd_txt
    print("Длина текста: {0}".format(len(text1)))
    print("Количество совпадений: {0}".format(count_common_letters(text1, text2)))
    print("Процент совпадений: {0}".format(s))


def sense_and_randomw():
    print("3. Осмысленный текст и текст из случайных слов.")
    handle1 = open('1.txt', 'r')
    text1 = handle1.read()
    s = 0
    for _ in range(cnt_rnd_txt):
        text2 = gen_random_words(len(text1))
        s += match_perc(text1, text2)
    s /= cnt_rnd_txt
    print("Длина текста: {0}".format(len(text1)))
    print("Количество совпадений: {0}".format(count_common_letters(text1, text2)))
    print("Процент совпадений: {0}".format(s))


def randoml():
    print("4. Два текста из случайных букв.")
    s = 0
    for _ in range(cnt_rnd_txt):
        text1 = gen_random_letters(len_rnd_txt)
        text2 = gen_random_letters(len_rnd_txt)
        s += match_perc(text1, text2)
    s /= cnt_rnd_txt
    print("Длина текста: {0}".format(len_rnd_txt))
    print("Количество совпадений: {0}".format(count_common_letters(text1, text2)))
    print("Процент совпадений: {0}".format(s))


def randomw():
    print("5. Два текста из случайных слов.")
    s = 0
    for _ in range(cnt_rnd_txt):
        text1 = gen_random_words(len_rnd_txt)
        text2 = gen_random_words(len_rnd_txt)
        s += match_perc(text1, text2)
    s /= cnt_rnd_txt
    print("Длина текста: {0}".format(len_rnd_txt))
    print("Количество совпадений: {0}".format(count_common_letters(text1, text2)))
    print("Процент совпадений: {0}".format(s))


full_of_sense()
sense_and_randoml()
sense_and_randomw()
randoml()
randomw()