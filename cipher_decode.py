import string
chars = string.ascii_letters
cph_str = "RAEanEY.Xkh, 23fs3 3X5Q5 Q3E XZZfsfvH RAEaSQvsx 5XeksE sXcE, Xa leE5cvO QXkE cX2a fQ5 UEkkfQ cEAHXO8EaQ vZQEk kEvHfNfah fQ 3vc iEEa 5EskEQHO 3vsxEc Q2X 2EEx5 vhX.l3E 5fQE 3v5 v5xEc e5Ek5 QX kEYfE2 kEsEaQ sX88fQ5 QX Q3Efk AkX4EsQ5 QX 8vxE 5ekE Q3EO cXa’Q sXaQvfa vaO ivsxcXXkEc Xk XQ3Ek 8vHfsfXe5 sXcE.B5 2EHH v5 iEfah 3X8E QX RAEaSQvsx'5 iHeEAkfaQ5, RAEanEY 3X5Q5 v ae8iEk XZ XQ3Ek UfQ-iv5Ec kEAX5fQXkfE5 AkEQQO 8es3 vHXah Q3E HfaE5 XZ UfQLei vac 5f8fHvk 5XeksE-3X5Qfah XeQZfQ5. GQ e5E5 UXXhHE-iefHQ UEkkfQ QX AkXYfcEc v 2Ei-iv5Ec EaYfkXa8EaQ ZXk QEv85 QX kEYfE2 Evs3 XQ3Ek5' 2Xkx, vAAkXYE Xk cEaO s3vahE5 QX sXcE iv5E5, vac XQ3Ek2f5E sXHHviXkvQE Xa AkXhkv88fah AkX4EsQ5."
key_dic = {'a': 'v', 'b': 'i', 'c': 's', 'd': 'c', 'e': 'E', 'f': 'Z', 'g': 'h', 'h': '3', 'i': 'f', 'j': '4', 'k': 'x', 'l': 'H', 'm': '8', 'n': 'a', 'o': 'X', 'p': 'A', 'q': 'P', 'r': 'k', 's': '5', 't': 'Q', 'u': 'e', 'v': 'Y', 'w': '2', 'x': 'D', 'y': 'O', 'z': 'N', 'A': 'B', 'B': 'y', 'C': '0', 'D': 'n', 'E': 'm', 'F': 't', 'G': 'U', 'H': 'L', 'I': 'G', 'J': 'C', 'K': 'I', 'L': '1', 'M': 'o', 'N': 'W', 'O': 'R', 'P': 'M', 'Q': '9', 'R': 'K', 'S': 'S', 'T': 'l', 'U': 'T', 'V': 'q', 'W': 'z', 'X': 'r', 'Y': 'j', 'Z': 'F', '0': 'b', '1': '6', '2': 'J', '3': 'p', '4': 'V', '5': '7', '6': 'w', '7': 'd', '8': 'u', '9': 'g'}
rev_dic = {}
str_cph = ""

for k,v in key_dic.items():
    rev_dic[v] = k
#print(rev_dic)

for i in cph_str:
    if i in rev_dic:
        str_cph += rev_dic[i]
    if i not in rev_dic.keys():
        str_cph += i
print(str_cph)
