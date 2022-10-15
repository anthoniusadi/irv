# int 16bit   2byte
# dibagi 100
from os import sep
from numpy import size

import matplotlib.pyplot as plt
import numpy as np

file_out= open("out2.txt", "w",encoding="latin-1")
def decode_tostring(payload):
    return payload.decode('latin-1').encode('ascii', errors='xmlcharrefreplace').decode('ascii')
# with open("binary_contoh", "rb") as file:
#     data = file.read(69)

# datastring = str(data)
# print(type(data))
# print(data.decode('utf-8'))
# lines = []
# for line in data:
#     lines.append(line.decode('utf-8'))
file = open("binary_contoh", "rb")
lines = []
byte = file.read(2)
y = []
while byte:
    # print(byte)
    byte = file.read(2)
    data_y = int.from_bytes(byte, "big", signed=True) / 100
    print(data_y)
    lines.append(byte.decode('latin-1'))
    # print(lines)
    tmp = byte.decode('latin-1')
    # print(type(tmp))
    # lines.append(str(tmp))    
    # for item in lines:
    y.append(data_y)

    data = file_out.write(str(data_y))
    # print(type(data))
a = 'k o t p u t o j q t t w v s p k o x o y k k x k y t n k r l j p 3 Ê ’nÿºÿ×ÿÐ ›ÿø ) + $ ¬ R ÿÞ — K  ê ë È v ×_üÿÒÿÇ   ? Z ~ ~ y M › — j 0 q  ’ p ª ‡ J 4 ˆ a _ Œ ~ r } l € ‚ ‚ † d q P x q o q H j c u w ƒ x { p „ x x i q l o w | z n p t | { l j q g p t k w g j q r l u j t q l t n l w w r i y l y j y j s q t t i t x l x n w w t q l u l g s j y n p t o j u s k t w t w n w } t k t s l o q n k n r l t s u v t t r p s r q p t r i u i q t p t n u k s k v u r w m o w v y p u m p o t k v p x q n p q o v w p t l t n s l v v i z o r i q l m u u n n i k t ~ u h l q v h v p t m x f w k m w n m p q t t w l v q p r k n r w w f r o s q x i v t o r l m i x p z v t p s m n v n w j q s q o j z s s y y h q r u t o n m n s o u m v m p t l u j n { t l p o k x u k z h p t u m u u n p q t f p x l y p k j'
# b = 'k o t p u t o j q t t w v s p k o x o y k k x k y t n k r l j p 3 Ê ’nÿºÿ×ÿÐ ›ÿø ) + $ ¬ R ÿÞ — K  ê ë È v ×_üÿÒÿÇ   ? Z ~ ~ y M › — j 0 q  ’ p ª ‡ J 4 ˆ a _ Œ ~ r } l € ‚ ‚ † d q P x q o q H j c u w ƒ x { p „ x x i q l o w | z n p t | { l j q g p t k w g j q r l u j t q l t n l w w r i y l y j y j s q t t i t x l x n w w t q l u l g s j y n p t o j u s k t w t w n w } t k t s l o q n k n r l t s u v t t r p s r q p t r i u i q t p t n u k s k v u r w m o w v y p u m p o t k v p x q n p q o v w p t l t n s l v v i z o r i q l m u u n n i k t ~ u h l q v h v p t m x f w k m w n m p q t t w l v q p r k n r w w f r o s q x i v t o r l m i x p z v t p s m n v n w j q s q o j z s s y y h q r u t o n m n s o u m v m p t l u j n { t l p o k x u k z h p t u m u u n p q t f p x l y p k j'
b = 'k o t p u t o j q t t w v s p k o x o y k k x k y t n k r l j p 3 Ê ’nÿºÿ×ÿÐ ›ÿø ) + $ ¬ R ÿÞ — K  ê ë È v ×_üÿÒÿÇ   ? Z ~ ~ y M › — j 0 q  ’ p ª ‡ J 4 ˆ a _ Œ ~ r } l € ‚ ‚ † d q P x q o q H j c u w ƒ x { p „ x x i q l o w | z n p t | { l j q g p t k w g j q r l u j t q l t n l w w r i y l y j y j s q t t i t x l x n w w t q l u l g s j y n p t o j u s k t w t w n w } t k t s l o q n k n r l t s u v t t r p s r q p t r i u i q t p t n u k s k v u r w m o w v y p u m p o t k v p x q n p q o v w p t l t n s l v v i z o r i q l m u u n n i k t ~ u h l q v h v p t m x f w k m w n m p q t t w l v q p r k n r w w f r o s q x i v t o r l m i x p z v t p s m n v n w j q s q o j z s s y y h q r u t o n m n s o u m v m p t l u j n { t l p o k x u k z h p t u m u u n p q t f p x l y p k j'
if a==b:
    print('true')
else:
    print('false')
print(f'max data y : {max(y)}, PANJANG DATA : {len(y)}')
# print(x)
# print(len(x))
x = np.arange(len(y))
plt.title("plotting")
plt.xlabel('samples')
plt.ylabel('amplitudes')
# plt.yticks(y)
plt.plot(x, y)
  
plt.show()