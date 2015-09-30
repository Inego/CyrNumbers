__author__ = 'Inego'

import re

vowels = ('а', 'я', 'э', 'е', 'ы', 'и', 'о', 'ё', 'у', 'ю')

rare = ('х', 'ц', 'ч', 'ш', 'щ')

voiceless = ('к', 'п', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')

NO_OBSCENE = True


def bad_A(p, grp, grqty, prev):
    if grp < 0:
        return True
    return False


def bad_B(p, grp, grqty, prev):
    if (prev in voiceless or
                NO_OBSCENE and p == 'е'  # убираем нецензурщину
        ):
        return True
    return False


def bad_V(p, grp, grqty, prev):
    return False


def bad_G(p, grp, grqty, prev):
    if grp == 1 and grqty == 0:
        return True

    return False


def bad_D(p, grp, grqty, prev):
    if (grp == 1 and grqty == 0 and not prev in ('в', 'г', 'ж', 'з')
        or prev in voiceless):
        return True

    return False


def bad_YE(p, grp, grqty, prev):
    return False


def bad_YO(p, grp, grqty, prev):
    if prev in ('а', 'я', 'э', 'е', 'ё', 'ю', 'ж', 'ц', 'ч', 'ш', 'щ'):
        return True

    return False


def bad_ZH(p, grp, grqty, prev):
    return False


def bad_Z(p, grp, grqty, prev):
    return False


def bad_I(p, grp, grqty, prev):
    if grp < 0:
        return True
    return False


def bad_K(p, grp, grqty, prev):
    return False


def bad_L(p, grp, grqty, prev):
    return False


def bad_M(p, grp, grqty, prev):
    if (grqty == 0 and grp > 0 and not prev in ('вжстш')
        or grp > 0 and prev in 'пч'):
        return True
    return False


def bad_N(p, grp, grqty, prev):
    if (grp == 2 and prev in ('н', 'щ')):
        return True

    return False


def bad_O(p, grp, grqty, prev):
    return False


def bad_P(p, grp, grqty, prev):
    if (grp > 0 and prev in 'дщ'):
        return True
    return False


def bad_R(p, grp, grqty, prev):
    return False


def bad_S(p, grp, grqty, prev):
    if (grp > 0 and prev in ('т')
        or prev == 'к' and grp == 2 and not p[-2:-1] in 'влмнр'):
        return True
    return False


def bad_T(p, grp, grqty, prev):
    if grp > 0 and prev in 'д':
        return True
    return False


def bad_U(p, grp, grqty, prev):
    return False


def bad_F(p, grp, grqty, prev):
    return False


def bad_H(p, grp, grqty, prev):
    return False


def bad_TS(p, grp, grqty, prev):
    if grp > 0:
        if (grqty == 0
            or not prev in ('в', 'м', 'н', 'р')):
            return True
    return False


def bad_CH(p, grp, grqty, prev):
    if (grp > 0 and prev in 'д'
        or grp > 1 and prev in 'м'):
        return True
    return False


def bad_SH(p, grp, grqty, prev):
    if p:
        if grqty == 0 and not prev in ('к', 'п') and not prev in vowels:
            return True

    return False


def bad_SCH(p, grp, grqty, prev):
    if p:
        if not prev in ('б', 'м', 'п', 'щ') and not prev in vowels:
            return True

    return False


def bad_Y(p, grp, grqty, prev):
    if (not p
        or prev in vowels
        or prev in ('ж', 'ч', 'ш', 'щ')):
        return True

    return False


def bad_E(p, grp, grqty, prev):
    return False


def bad_YU(p, grp, grqty, prev):
    if prev in ('ж', 'х', 'ц', 'ч', 'ш', 'щ'):
        return True

    return False


def bad_YA(p, grp, grqty, prev):
    return False


class Letter:
    def __init__(self, letter, is_vowel, bad, fcy):
        self.letter = letter
        self.is_vowel = is_vowel
        self.bad = bad
        self.penalty = 55414481 - fcy

        letter_dict[letter] = self


def init_letters():
    global _A
    global _B
    global _V
    global _G
    global _D
    global _YE
    global _YO
    global _ZH
    global _Z
    global _I
    global _K
    global _L
    global _M
    global _N
    global _O
    global _P
    global _R
    global _S
    global _T
    global _U
    global _F
    global _H
    global _TS
    global _CH
    global _SH
    global _SCH
    global _Y
    global _E
    global _YU
    global _YA

    global letter_dict

    letter_dict = {}

    _A = Letter('а', True, bad_A, 40487008)
    _B = Letter('б', False, bad_B, 8051767)
    _V = Letter('в', False, bad_V, 22930719)
    _G = Letter('г', False, bad_G, 8564640)
    _D = Letter('д', False, bad_D, 15052118)
    _YE = Letter('е', True, bad_YE, 42691213)
    _YO = Letter('ё', True, bad_YO, 184928)
    _ZH = Letter('ж', False, bad_ZH, 4746916)
    _Z = Letter('з', False, bad_Z, 8329904)
    _I = Letter('и', True, bad_I, 37153142)
    _K = Letter('к', False, bad_K, 17653469)
    _L = Letter('л', False, bad_L, 22230174)
    _M = Letter('м', False, bad_M, 16203060)
    _N = Letter('н', False, bad_N, 33838881)
    _O = Letter('о', True, bad_O, 55414481)
    _P = Letter('п', False, bad_P, 14201572)
    _R = Letter('р', False, bad_R, 23916825)
    _S = Letter('с', False, bad_S, 27627040)
    _T = Letter('т', False, bad_T, 31620970)
    _U = Letter('у', True, bad_U, 13245712)
    _F = Letter('ф', False, bad_F, 1335747)
    _H = Letter('х', False, bad_H, 4904176)
    _TS = Letter('ц', False, bad_TS, 2438807)
    _CH = Letter('ч', False, bad_CH, 7300193)
    _SH = Letter('ш', False, bad_SH, 3678738)
    _SCH = Letter('щ', False, bad_SCH, 1822476)
    _Y = Letter('ы', True, bad_Y, 9595941)
    _E = Letter('э', True, bad_E, 1610107)
    _YU = Letter('ю', True, bad_YU, 3220715)
    _YA = Letter('я', True, bad_YA, 10139085)


class Number:
    def __init__(self, number, letters):
        self.number = number
        self.letters = letters

        for l in letters:
            l.number = number


def init_numbers():
    global num_list

    num_list = [
        Number('0', [_N, _A, _SH]),
        Number('1', [_V, _I, _Z]),
        Number('2', [_B, _YE, _TS]),
        Number('3', [_L, _YA, _ZH]),
        Number('4', [_H, _O, _R]),
        Number('5', [_G, _U, _S]),
        Number('6', [_P, _YO, _CH]),
        Number('7', [_M, _E, _F]),
        Number('8', [_D, _Y, _SCH]),
        Number('9', [_T, _YU, _K])]

    global num_dict

    num_dict = dict((x.number, x) for x in num_list)


init_letters()
init_numbers()


def remove_nondigits(s):
    p = re.compile('\D')

    return p.sub('', s)


def suggest_letter(s, idx, grp, prevstr, grqty, prev, curr_score, best):
    '''
    grp: 0 = no preceding, negative: vowels, positive: consonants
    '''

    n_char = s[idx]

    n = num_dict[n_char]

    for l in n.letters:
        # print(l.letter)

        if best.score and curr_score + l.penalty > best.score:
            continue

        if (grqty == 0 and l.letter == prev):
            continue

        if l.is_vowel:
            if grp < -1:
                continue

            newgrp = (0 if grp > 0 else grp) - 1
            newgrqty = (grqty + 1 if grp > 0 else grqty)


        else:
            if (grp > 2
                or grp == 2 and (l.letter in 'бгдзпшщ' or prevstr.endswith(l.letter + l.letter))
                or grp > 0 and l.letter in rare and prev in rare
                or grp > 1 and l.letter == prev):
                continue

            newgrp = (0 if grp < 0 else grp) + 1
            newgrqty = (grqty + 1 if grp < 0 else grqty)

        if (l.bad(prevstr, grp, grqty, prev)):
            continue

        newprevstr = prevstr + l.letter

        if idx < len(s) - 1:
            suggest_letter(s, idx + 1, newgrp, newprevstr, newgrqty, l.letter, curr_score + l.penalty, best)

        else:

            if newgrp > 2:
                last_three = newprevstr[-3:]
                if (not 'р' in last_three
                    and not last_three.endswith('ск')
                    and not last_three.endswith('ст')):
                    continue

            if newgrp == 2:
                if prev == l.letter:
                    if l.letter in ('т'):
                        continue
                if l.letter == 'м' and not prev in ('з', 'р'):
                    continue
                if l.letter == 'п' and not prev in 'лмр':
                    continue

            if best.score is None or curr_score + l.penalty < best.score:
                best.score = curr_score + l.penalty
                best.words = []

            best.words.append(newprevstr)



            # print(n)


class Winner:
    def __init__(self):
        self.score = None
        self.words = []


def suggest(s):
    clear_s = remove_nondigits(s)

    best = Winner()

    suggest_letter(clear_s, 0, 0, '', 0, None, 0, best)

    for w in best.words:
        print(w)


def check_word(s):
    n = ''

    for l in s:
        n += letter_dict[l].number

    suggest(n)


suggest('0123456789')
