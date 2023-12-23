## Истина

### Что нужно сделать:

# К вам попал зашифрованный текст, означающий большую истину для многих программистов на Python.
# Напишите программу, которая реализует алгоритм дешифровки этого текста.
# Расшифруйте текст с помощью своей программы.

# `vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip`

text = ('vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm '
        'fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj '
        'uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj '
        'vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu '
        'zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV '
        'mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq '
        'up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz '
        'pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( '
        'i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui '
        'iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb '
        'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO '
        'bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip')


alphabet_lower = [chr(i) for i in range(97, 123)]
alphabet_upper = [chr(i) for i in range(65, 91)]

alphabet = ''.join(alphabet_upper) + ''.join(alphabet_lower)

inter_text = []
for i_word in text.split():
    new_word = ''
    for sym in i_word:
        if sym in alphabet:
            index = alphabet.index(sym)
            new_word += alphabet[index - 1]
        else:
            new_word += sym
    inter_text.append(new_word)

result = []
key = 3
for j_word in inter_text:
    shift = key % len(j_word)
    res_word = j_word[-shift:] + j_word[:-shift]
    result.append(res_word)
    if '/' in j_word:
        key += 1

new_text = ' '.join(result)

new_text = new_text.replace('/ ', '.\n')
new_text = new_text.replace('(', "'")
new_text = new_text.replace('-', ',')
new_text = new_text.replace('..', '--')
new_text = new_text.replace('+', '*')
new_text = new_text.replace('"', '!')


print('Зашифрованное сообщение:\n')
print(new_text)