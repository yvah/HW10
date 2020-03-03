import string

alphabet = string.ascii_lowercase
height = int(input('Высота: '))
width = 4 * height - 3
if 0 < height < 27:
    for i in list(range(height))[::-1] + list(range(1, height)):
        print('-'.join(alphabet[height-1:i:-1] + alphabet[i:height]).center(width, '-'))
