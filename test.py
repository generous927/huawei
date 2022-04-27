'''
字符串最后一个单词的长度
描述
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。
输出描述：
输出一个整数，表示输入字符串最后一个单词的长度。
'''

# while True:
#     try:
#         print(len(input().split(sep=' ')[-1]))
#     except:
#         break

'''
计算某字符出现次数
描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）
数据范围：1≤n≤1000 
输入描述：
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。
输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）
'''

# s = input("").upper()
# j = input("").upper()
# print(s.count(j))

'''
明明的随机数
描述
明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
数据范围： 1≤n≤1000，输入的数字大小满足1≤val≤500 
输入描述：
第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表明明生成的随机数。 具体格式可以参考下面的"示例"。
输出描述：
输出多行，表示输入数据处理后的结果
'''

# while True:
#     try:
#         n = input()
#         ta = []
#         for i in range(int(n)):
#             ta.append(int(input()))
#         uniq = set(ta)
#         for j in sorted(uniq):
#             print(j)
#     except:
#         break

'''
字符串分隔
描述
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)
输出描述：
依次输出所有分割后的长度为8的新字符串
'''

# while True:
#     try:
#         l = input()
#         for i in range(0, len(l), 8):
#             print("{0:0<8s}".format(l[i:i+8]))
#     except:
#         break

'''
进制转换
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
数据范围：保证结果在1≤n≤2^{31}-1 
输入描述：
输入一个十六进制的数值字符串。
输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
'''

# while True:
#     try:
#         s=input()
#         print(int(s,16))
#     except:
#         break

'''
质数因子
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
数据范围：1≤n≤2×10^{9}+14 
输入描述：
输入一个整数
输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
'''

# num = int(input())
# def func(num):
#     prime_num = 1
#     for i in range(2, int(num ** 0.5 + 2)):
#         if num % i == 0:
#             prime_num = 0
#             b = int(num / i)
#             print(str(i), end=' ')
#             func(b)
#             break
#     if prime_num == 1:
#         print(str(num), end=' ')
# func(num)

'''
取近似值
描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
数据范围：保证输入的数字在 32 位浮点数范围内
输入描述：
输入一个正浮点数值
输出描述：
输出该数值的近似整数值
'''

# a = float(input())
# print(int(a) + 1 if a % 1 >= 0.5 else int(a))

'''
合并表记录
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
提示:
0 <= index <= 11111111
1 <= value <= 100000
输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开
输出描述：
输出合并后的键值对（多行）
'''

# b = {}
# a = int(input())
# c = set()
# for i in range(a):
#     contents = input().split(" ")
#     key = int(contents[0])
#     value = int(contents[1])
#     if key not in c:
#         c.add(key)
#         b[key] = value
#     else:
#         b[key] = b[key] + value
# result = sorted(b.keys(), reverse=False)
# for key in result:
#     print(key, b[key])

'''
提取不重复的整数
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
数据范围：1≤n≤10^8  
输入描述：
输入一个int型整数
输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
'''

# a=input()
# a=a[::-1]
# y=''
# for i in a:
#     if i not in y:
#         y=y+i
# print(y)

'''
字符个数统计
描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串 abaca 而言，有 a、b、c 三种不同的字符，因此输出 3 。
数据范围：1≤n≤500 
输入描述：
输入一行没有空格的字符串。
输出描述：
输出输入字符串 中范围在(0~127，包括0和127)字符的种数。
'''

# import sys
#
# a = sys.stdin.readline().strip()
# words = ''
# for i in a:
#     if i not in words and ord(i) >= 0 and ord(i) <= 127:
#         words += i
# print(len(words))


'''
数字颠倒
描述
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
数据范围：0≤n≤2^{30}-1 
输入描述：
输入一个int整数
输出描述：
将这个整数以字符串的形式逆序输出
'''

# a =  input()
# str(a)
# print(a[::-1])


'''
字符串反转
描述
接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
输入描述：
输入一行，为一个只包含小写字母的字符串。
输出描述：
输出该字符串反转后的字符串。
'''

# def backword(str1):
#     slen = len(str1)
#     sstr = ""
#     for i in range(slen):
#         sstr = sstr + str1[slen - i - 1]
#     return sstr
#
#
# inputstr = input()
# if inputstr.isalpha() and inputstr.islower():
#     print(backword(inputstr))


'''
句子逆序
描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
数据范围：输入的字符串长度满足1≤n≤1000 
注意本题有多组输入
输入描述：
输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母。
输出描述：
得到逆序的句子
'''


# def func():
#     try:
#         number_list = input().strip().split(' ')
#         number_list.reverse()
#         print(' '.join(number_list))
#     except:
#         pass
#
#
# if __name__ == "__main__":
#     func()

'''
字符串排序
描述
给定n个字符串，请对n个字符串按照字典序排列。
数据范围：1≤n≤1000,字符串长度满足1≤len≤100 
输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述：
数据输出n行，输出结果为按照字典序排列的字符串。
'''

# import sys
# num=int(sys.stdin.readline().strip())
# ll=list()
# for i in range(num):
#     ll.append(sys.stdin.readline().strip())
# ll.sort(key=str)
# for item in ll:
#     print(item)

'''
求int型正整数在内存中存储时1的个数
描述
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
数据范围：保证在 32 位整型数字范围内
输入描述：
 输入一个整数（int类型）
输出描述：
 这个数转换成2进制后，输出1的个数
'''

# print(bin(int(input())).count('1'))


'''
购物单
描述
王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。
王强查到了每件物品的价格（都是 10 元的整数倍），而他只有 N 元的预算。除此之外，他给每件物品规定了一个重要度，用整数 1 ~ 5 表示。他希望在花费不超过 N 元的前提下，使自己的满意度达到最大。
满意度是指所购买的每件物品的价格与重要度的乘积的总和，假设设第ii件物品的价格为v[i]v[i]，重要度为w[i]w[i]，共选中了kk件物品，编号依次为j_1,j_2,...,j_k，
则满意度为：v[j_1]*w[j_1]+v[j_2]*w[j_2]+ … +v[j_k]*w[j_k]v[j_k] （其中 * 为乘号）
请你帮助王强计算可获得的最大的满意度。
输入描述：
输入的第 1 行，为两个正整数N，m，用一个空格隔开：
（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
输出描述：
输出一个正整数，为张强可以获得的最大的满意度。
'''

# import collections
# import functools
#
# n, m = map(int, input().strip().split())
# v = [0] * m
# p = [0] * m
# q = [0] * m
# d = collections.defaultdict(list)
# for i in range(m):
#     temm = list(map(int, input().strip().split()))
#     v[i], p[i], q[i] = temm[0], temm[1], temm[2] - 1
#     if q[i] != -1:
#         d[q[i]].append(i)
# dn = collections.defaultdict(list)
# for k in d.keys():
#     dn[k].append([v[k], v[k] * p[k]])
#     for i in d[k]:
#         dn[k].append([v[i] + v[k], v[i] * p[i] + v[k] * p[k]])
#     if len(d[k]) == 2:
#         dn[k].append([v[d[k][0]] + v[k] + v[d[k][1]], v[d[k][0]] * p[d[k][0]] + v[k] * p[k] + v[d[k][1]] * p[d[k][1]]])
# for i in range(m):
#     if i not in d and q[i] == -1:
#         dn[i].append([v[i], v[i] * p[i]])
# k = list(dn.keys())
#
#
# @functools.cache
# def f(i, j):
#     if j < 0: return 0
#     if i < 0: return 0
#     res = f(i - 1, j)
#     for v, vp in dn[k[i]]:
#         if v > j: continue
#         res = max(res, f(i - 1, j - v) + vp)
#     return res
#
#
# print(f(len(k) - 1, n))

'''
坐标移动
描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+A10=（-10,0）
+S20=(-10,-20)
+W10=(-10,-10)
+D30=(20,-10)
+x=无效
+A1A=无效
+B10A11=无效
+一个空不影响
+ A10  =  (10,-10)
结果 （10， -10）
数据范围：每组输入的字符串长度满足1≤n≤10000  ，坐标保证满足-2^{31}≤x,y≤2^{31}-1 ，且数字部分仅含正数
输入描述：
一行字符串
输出描述：
最终坐标，以逗号分隔
'''

# string = input()
#
# str_list = string.split(';')
# d = {}
# for item in str_list:
#     if len(item) > 1 and item[0] in list('ADSW') and item[1:].isdecimal():
#         d[item[0]] = d.get(item[0], 0) + int(item[1:])
# x, y = (d['D'] - d['A']), (d['W'] - d['S'])
# print('%d,%d' % (x, y))

'''
识别有效的IP地址和掩码并进行分类统计
描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
所有的IP地址划分为 A,B,C,D,E五类
A类地址从1.0.0.0到126.255.255.255;
B类地址从128.0.0.0到191.255.255.255;
C类地址从192.0.0.0到223.255.255.255;
D类地址从224.0.0.0到239.255.255.255；
E类地址从240.0.0.0到255.255.255.255
私网IP范围是：
从10.0.0.0到10.255.255.255
从172.16.0.0到172.31.255.255
从192.168.0.0到192.168.255.255
子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
（注意二进制下全是1或者全是0均为非法子网掩码）
注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的
输入描述：
多行字符串。每行一个IP地址和掩码，用~隔开。
请参考帖子https://www.nowcoder.com/discuss/276处理循环输入的问题。
输出描述：
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
'''

# import sys
#
# a_type = [1 << 24, (127 << 24) - 1]
# b_type = [128 << 24, (192 << 24) - 1]
# c_type = [192 << 24, (224 << 24) - 1]
# d_type = [224 << 24, (240 << 24) - 1]
# e_type = [240 << 24, (1 << 32) - 1]
#
# p1 = [10 << 24, (11 << 24) - 1]
# p2 = [(172 << 24) + (16 << 16), (172 << 24) + (32 << 16) - 1]
# p3 = [(192 << 24) + (168 << 16), (192 << 24) + (169 << 16) - 1]
#
#
# def parse_mask(mask):
#     chunks = mask.split('.')
#     if len(chunks) != 4:
#         return 1
#     val = 0
#     for c in chunks:
#         if len(c) == 0:
#             return 1
#         val = val * 256 + int(c)
#     if val == 0 or val == 0xffffffff:
#         return 1
#     prev = 0
#     while val > 0:
#         cur = val & 1
#         if cur == 0 and prev == 1:
#             return 1
#         prev = cur
#         val = (val >> 1)
#     return 0
#
#
# def parse_addr(addr):
#     chunks = addr.split('.')
#     if len(chunks) != 4:
#         return (5, 0)
#     val = 0
#     for c in chunks:
#         if len(c) == 0:
#             return (5, 0)
#         val = val * 256 + int(c)
#     if val >= a_type[0] and val <= a_type[1]:
#         if val >= p1[0] and val <= p1[1]:
#             return (0, 1)
#         else:
#             return (0, 0)
#     if val >= b_type[0] and val <= b_type[1]:
#         if val >= p2[0] and val <= p2[1]:
#             return (1, 1)
#         else:
#             return (1, 0)
#     if val >= c_type[0] and val <= c_type[1]:
#         if val >= p3[0] and val <= p3[1]:
#             return (2, 1)
#         else:
#             return (2, 0)
#     if val >= d_type[0] and val <= d_type[1]:
#         return (3, 0)
#     if val >= e_type[0] and val <= e_type[1]:
#         return (4, 0)
#
#     return (-1, 0)
#
#
# # A, B, C, D, E, error, private,
# cnts = [0, 0, 0, 0, 0, 0, 0]
#
# for line in sys.stdin.readlines():
#     (addr, mask) = line.strip().split('~')
#     (t, p) = parse_addr(addr)
#     c = parse_mask(mask)
#     if c == 1 and t != -1:
#         cnts[5] += 1
#     elif t >= 0:
#         cnts[t] += 1
#         if p > 0:
#             cnts[6] += 1
#
# cnts = [str(x) for x in cnts]
# print(' '.join(cnts))


'''
简单错误记录
描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理：
1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是“相同”的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。也就是说，哪怕不同路径下的文件，如果它们的名字的后16个字符相同，也被视为相同的错误记录
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准
数据范围：错误记录数量满足1≤n≤100  ，每条记录长度满足1≤len≤100 
输入描述：
每组只包含一个测试用例。一个测试用例包含一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。
输出描述：
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：
'''

# err_list = []
# cnt_list = []
#
# while True:
#     try:
#         s = input().split(' ')
#         f = s[0].split('\\')[-1]
#         item = f'{f[-16:]} {s[1]}'
#         try:
#             i = err_list.index(item)
#             cnt_list[i] += 1
#         except ValueError:
#             err_list.append(item)
#             cnt_list.append(1)
#     except Exception:
#         break
#
# for i in range((len(err_list) - 8) if len(err_list) > 8 else 0, len(err_list)):
#     print(err_list[i], cnt_list[i])


'''
密码验证合格程序
描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的不含公共元素的子串重复 （注：其他符号不含空格或换行）
数据范围：输入的字符串长度满足1≤n≤100 
输入描述：
一组字符串。
输出描述：
如果符合要求输出：OK，否则输出NG
'''

# while True:
#     try:
#
#         line = input()
#         a = 0
#         b = 0
#         c = 0
#         d = 0
#         flag = True
#         for i in line:
#             if i.isdigit():
#                 a = 1
#             elif i.islower():
#                 b = 1
#             elif i.isupper():
#                 c = 1
#             else:
#                 d = 1
#         for j in range(len(line) - 3):
#             if line.count(line[j:j + 3]) > 1:
#                 flag = False
#         if len(line) > 8 and (a + b + c + d) >= 3 and flag:
#             print("OK")
#         else:
#             print("NG")
#     except:
#         break


'''
简单密码
描述
现在有一种密码变换算法。
九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
数字和其它的符号都不做变换。
数据范围： 输入的字符串长度满足1≤n≤100 
输入描述：
输入一组密码，长度不超过100个字符。
输出描述：
输出密码变换后的字符串
'''


# while True:
#     e=[]
#     try:
#         s = list(input())
#         for i in s:
#             if i>="A" and i <="Z":
#                 t=chr((ord(i)+33))
#                 if t>'z':
#                     t='a'
#                 e.append(t)
#             elif i>="a" and i <="c":
#                  e.append('2')
#             elif i>="d" and i <="f":
#                  e.append('3')
#             elif i>="g" and i <="i":
#                  e.append('4')
#             elif i>="j" and i <="l":
#                  e.append('5')
#             elif i>="m" and i <="o":
#                  e.append('6')
#             elif i>="p" and i <="s":
#                  e.append('7')
#             elif i>="t" and i <="v":
#                  e.append('8')
#             elif i>="w" and i <="z":
#                  e.append('9')
#             else :
#                  e.append(i)
#         print("".join(e))
#     except:
#         break


'''
汽水瓶
描述
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
数据范围：输入的正整数满足1≤n≤100 
注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。
输入描述：
输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。n=0 表示输入结束，你的程序不应当处理这一行。
输出描述：
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。
'''

# while True:
#     try:
#         a=int(input())
#         if a!=0:
#             print (a//2)
#         else:
#             pass
#     except:
#         break

'''
删除字符串中出现次数最少的字符
描述
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
数据范围：输入的字符串长度满足1≤n≤20 ，保证输入的字符串中仅出现小写字母
输入描述：
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。
输出描述：
删除字符串中出现次数最少的字符后的字符串。
'''

# while True:
#     try:
#         aaa = list(input())
#         b = list(set(aaa))
#         c=[]
#         for i in b:
#             c.append(aaa.count(i))
#         for i in range(len(c)):
#             if c[i] == min(c):
#                 while b[i] in aaa:aaa.remove(b[i])
#         print("".join(aaa))
#     except:
#         break

'''
合唱队
描述
N位同学站成一排，音乐老师要请最少的同学出列，使得剩下的 K 位同学排成合唱队形。
设K位同学从左到右依次编号为 1，2…，K ，他们的身高分别为T_1,T_2,…,T_K，
若存在i(1≤i≤K) 使得T_1<T_2<......<T_{i-1}<T_i
且 T_i>T_{i+1}>......>T_K ，则称这KK名同学排成了合唱队形。
通俗来说，能找到一个同学，他的两边的同学身高都依次严格降低的队形就是合唱队形。
例子： 
123 124 125 123 121 是一个合唱队形
123 123 124 122不是合唱队形，因为前两名同学身高相等，不符合要求
123 122 121 122不是合唱队形，因为找不到一个同学，他的两侧同学身高递减。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等
数据范围：1≤n≤3000 
输入描述：
用例两行数据，第一行是同学的总数 N ，第二行是 N 位同学的身高，以空格隔开
输出描述：
最少需要几位同学出列
'''

# import bisect
# def max_order(lists):
#     list_num = []
#     list_max = []
#     for i in lists:
#         local = bisect.bisect_left(list_num, i)
#         if local == len(list_num):
#             list_num.append(i)
#             list_max.append(local+1)
#         else:
#             list_num[local] = i
#             list_max.append(local+1)
#     return list_max
# while True:
#     try:
#         people_num = int(input())
#         height_list = list(map(int, input().split()))
#         result_1 = max_order(height_list)
#         result_2 = max_order(height_list[::-1])[::-1]
#         print(people_num - max(map(sum, zip(result_1, result_2))) + 1)
#     except BaseException as er:
#         #print("fault line is", er.__traceback__.tb_lineno)
#         break


'''
数据分类处理
描述
信息社会，有海量的数据需要分析处理，比如公安局分析身份证号码、 QQ 用户、手机号码、银行帐号等信息及活动记录。
采集输入大数据和分类规则，通过大数据分类处理程序，将大数据分类输出。
数据范围：1≤I,R≤100  ，输入的整数大小满足0≤val≤2^{31}-1 
输入描述：
﻿一组输入整数序列I和一组规则整数序列R，I和R序列的第一个整数为序列的个数（个数不包含第一个整数）；整数范围为0~(2^31)-1，序列个数不限
输出描述：
﻿从R依次中取出R<i>，对I进行处理，找到满足条件的I： 
I整数对应的数字需要连续包含R<i>对应的数字。比如R<i>为23，I为231，那么I包含了R<i>，条件满足 。 
按R<i>从小到大的顺序:
(1)先输出R<i>； 
(2)再输出满足条件的I的个数； 
(3)然后输出满足条件的I在I序列中的位置索引(从0开始)； 
(4)最后再输出I。 
附加条件： 
(1)R<i>需要从小到大排序。相同的R<i>只需要输出索引小的以及满足条件的I，索引大的需要过滤掉 
(2)如果没有满足条件的I，对应的R<i>不用输出 
(3)最后需要在输出序列的第一个整数位置记录后续整数序列的个数(不包含“个数”本身)
序列I：15,123,456,786,453,46,7,5,3,665,453456,745,456,786,453,123（第一个15表明后续有15个整数） 
序列R：5,6,3,6,3,0（第一个5表明后续有5个整数） 
输出：30, 3,6,0,123,3,453,7,3,9,453456,13,453,14,123,6,7,1,456,2,786,4,46,8,665,9,453456,11,456,12,786
说明：
30----后续有30个整数
3----从小到大排序，第一个R<i>为0，但没有满足条件的I，不输出0，而下一个R<i>是3
6--- 存在6个包含3的I 
0--- 123所在的原序号为0 
123--- 123包含3，满足条件 
'''

# try:
#     while True:
#         l1=input().split()[1:]
#         l2=list(map(int,input().split()))[1:]
#         l2=list(set(l2))
#         l2.sort()
#         res=[]
#         l2=list(map(str,l2))
#         for i in range(len(l2)):
#             ans =[]
#             for j in range(len(l1)):
#                 if l2[i] in l1[j]:
#                     ans.append(str(j))
#                     ans.append(l1[j])
#             if ans:
#                 res.append(l2[i])
#                 res.append(str(len(ans)//2))
#                 res +=ans
#         ss = str(len(res))+' '+' '.join(res)
#         print(ss)
# except:
#     pass


'''
字符串排序
描述
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
数据范围：输入的字符串长度满足1≤n≤1000 
输入描述：
输入字符串
输出描述：
输出字符串
'''

# while True:
#     try:
#         a=input()
#         #构造两个列表，一个列表用来放全字母的字符串2，另外一个列表取出来
#         char=[] #构造一个列表用来存放字符串
#         res=[False]*len(a)#构造一个列表用来记住非字母的位置
#         for i,v in enumerate(a):
#             if v.isalpha(): #如果全是字母则放入char中
#                 char.append(v)
#             else:
#                 res[i]=v
#         #然后对char进行排序
#         char.sort(key=lambda c:c.lower())
#         #重构,在res中的false项中放入char
#         for i,v in enumerate(res):
#             if not v:
#                 res[i]=char[0]
#                 char.pop(0)
#         print(''.join(res))
#     except:
#         break

'''
查找兄弟单词
描述
定义一个单词的“兄弟单词”为：交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如： ab 和 ba 是兄弟单词。 ab 和 ab 则不是兄弟单词。
现在给定你 n 个单词，另外再给你一个单词 x ，让你寻找 x 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。
数据范围：1≤n≤1000 ，输入的字符串长度满足1≤len(str)≤10 ，1≤k<n 
输入描述：
输入只有一行。 先输入字典中单词的个数n，再输入n个单词作为字典单词。 然后输入一个单词x 最后后输入一个整数k
输出描述：
第一行输出查找到x的兄弟单词的个数m 第二行输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。
'''

# while True:
#     try:
#         ss=input().split()
#         n=int(ss[0])
#         dict=ss[1:n+1]
#         s=ss[-2]
#         m=int(ss[-1])
#         a=[]
#         for i in dict:
#             if len(i)==len(s) and i!=s and sorted(i)==sorted(s):
#                 a.append(i)
#         print(len(a))
#         if a and m<=len(a):
#             print(sorted(a)[m-1])
#     except:
#         break


'''
素数伴侣
描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，
如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。
输入:
有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。
输出:
输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。
数据范围：1≤n≤100，输入的数据大小满足2≤val≤30000 
输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数
输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。
'''


# def prime_judge(n):
#     m = int(n ** 0.5) + 2
#     for i in range(3, m, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# def group_lst(lst):  ##分奇偶
#     a, b = [], []
#     for i in lst:
#         if int(i) % 2 == 0:
#             a.append(int(i))
#         else:
#             b.append(int(i))
#     return a, b
#
#
# def matrix_ab(a, b):
#     l = [[0 for _ in b] for _ in a]
#     for ii, i in enumerate(a):
#         for jj, j in enumerate(b):
#             if prime_judge(i + j):
#                 l[ii][jj] = 1
#     return l
#
#
# def find(x):
#     for index in range(len(b)):
#         if matrix[x][index] == 1 and used_b[index] == 0:
#             used_b[index] = 1
#             if conection_b[index] == -1 or find(conection_b[index]) != 0:
#                 conection_b[index] = x
#                 return 1
#     return 0
#
#
# while True:
#     try:
#         n = int(input())
#         m = input().split(' ')
#         a, b = group_lst(m)
#         matrix = matrix_ab(a, b)
#         conection_b = [-1 for _ in range(len(b))]
#         count = 0
#         for i in range(len(a)):
#             used_b = [0 for _ in range(len(b))]
#             if find(i):
#                 count += 1
#         print(count)
#     except:
#         break

'''
字符串加解密
描述
对输入的字符串进行加解密，并输出。
加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
解密方法为加密的逆过程。
数据范围：输入的两个字符串长度满足1≤n≤1000，保证输入的字符串都是只由大小写字母或者数字组成
输入描述：
第一行输入一串要加密的密码
第二行输入一串加过密的密码
输出描述：
第一行输出加密后的字符
第二行输出解密后的字符
'''

# while True:
#     try:
#         a = input()
#         b = input()
#         m = []
#         n = []
#         for c in a:
#             c = str(c)
#             if c == 'Z':
#                 c = 'a'
#             elif c == 'z':
#                 c = 'A'
#             elif c.islower():
#                 c = chr(ord(c)+1).upper()
#             elif c.isupper():
#                 c = chr(ord(c)+1).lower()
#             elif c == '9':
#                 c = '0'
#             elif c.isdigit():
#                 c = str(int(c) + 1)
#             m.append(c)
#         print(''.join(m))
#         for c in b:
#             c = str(c)
#             if c == 'a':
#                 c = 'Z'
#             elif c == 'A':
#                 c = 'z'
#             elif c.islower():
#                 c = chr(ord(c.upper())-1)
#             elif c.isupper():
#                 c = chr(ord(c.lower())-1)
#             elif c == '0':
#                 c = '9'
#             elif c.isdigit():
#                 c = str(int(c) - 1)
#             n.append(c)
#         print(''.join(n))
#     except:
#         break


'''
字符串合并处理
描述
按照指定规则对输入的字符串进行处理。
详细描述：
第一步：将输入的两个字符串str1和str2进行前后合并。如给定字符串 "dec" 和字符串 "fab" ， 合并后生成的字符串为 "decfab"
第二步：对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标的意思是字符在字符串中的位置。注意排序后在新串中仍需要保持原来的奇偶性。
例如刚刚得到的字符串“decfab”，分别对下标为偶数的字符'd'、'c'、'a'和下标为奇数的字符'e'、'f'、'b'进行排序（生成 'a'、'c'、'd' 和 'b' 、'e' 、'f'），
再依次分别放回原串中的偶数位和奇数位，新字符串变为“abcedf”
第三步：对排序后的字符串中的'0'~'9'、'A'~'F'和'a'~'f'字符，需要进行转换操作。
转换规则如下：
对以上需要进行转换的字符所代表的十六进制用二进制表示并倒序，然后再转换成对应的十六进制大写字符（注：字符 a~f 的十六进制对应十进制的10~15，大写同理）。
如字符 '4'，其二进制为 0100 ，则翻转后为 0010 ，也就是 2 。转换后的字符为 '2'。
如字符 ‘7’，其二进制为 0111 ，则翻转后为 1110 ，对应的十进制是14，转换为十六进制的大写字母为 'E'。
如字符 'C'，代表的十进制是 12 ，其二进制为 1100 ，则翻转后为 0011，也就是3。转换后的字符是 '3'。
根据这个转换规则，由第二步生成的字符串 “abcedf” 转换后会生成字符串 "5D37BF"。
数据范围：输入的字符串长度满足1≤n≤100 
输入描述：
样例输入两个字符串，用空格隔开。
输出描述：
输出转化后的结果。
'''

hex_num = ['0', '1', '2', '3',
           '4', '5', '6', '7',
           '8', '9', 'a', 'b',
           'c', 'd', 'e', 'f',
           'A', 'B', 'C', 'D',
           'E', 'F']


# def helper(s):
#     ten = int(s, 16)
#     bc = format(ten, 'b').rjust(4, '0')
#     bc = list(bc)
#     bc.reverse()
#     ten = int(''.join(bc), 2)
#     hc = format(ten, 'x')
#     return hc.upper()
#
#
# while True:
#     try:
#         a, b = input().strip().split()
#         res = list(a + b)
#         res[::2] = sorted(res[::2])
#         res[1::2] = sorted(res[1::2])
#         for i in range(len(res)):
#             if res[i] in hex_num:
#                 res[i] = helper(res[i])
#         print(''.join(res))
#     except EOFError:
#         break

'''
单词倒排
描述
对字符串中的所有单词进行倒排。
说明：
1、构成单词的字符只有26个大写或小写英文字母；
2、非构成单词的字符均视为单词间隔符；
3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4、每个单词最长20个字母；
数据范围：字符串长度满足1≤n≤10000 
输入描述：
输入一行，表示用来倒排的句子
输出描述：
输出句子的倒排结果
'''

# while True:
#     try:
#         out_arr = []
#         in_arr = input()
#         for i in in_arr:
#             if not i.isalpha():
#                 in_arr = in_arr.replace(i,' ')
#         for j in in_arr.split():
#             out_arr.append(j)
#         print(" ".join(out_arr[::-1]))
#     except:
#         break

'''
密码截取
描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
数据范围：字符串长度满足1≤n≤2500 
输入描述：
输入一个字符串（字符串的长度不超过2500）
输出描述：
返回有效密码串的最大长度
'''

# while True:
#     try:
#         s = input()
#         n = len(s)
#         single_center, double_center = [1]*n, [0]*n
#         for i in range(1,n):
#             j = 0
#             while j < min(i, n-i-1):
#                 j += 1
#                 if s[i-j]==s[i+j]:
#                     single_center[i] += 2
#                 else:
#                     break
#         for i in range(1,n-1):
#             j = 0
#             flag = True
#             while j < min(i, n-i-2):
#                 j += 1
#                 if s[i] == s[i+1]:
#                     if flag:
#                         double_center[i] = 2
#                         flag = False
#                     if s[i-j] == s[i+1+j]:
#                         double_center[i] += 2
#                     else:
#                         break
#                 else:
#                     break
#         print(max(max(single_center), max(double_center)))
#     except:
#         break


'''
整数与IP地址间的转换
描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
数据范围：保证输入的是合法的 IP 序列
输入描述：
输入 
1 输入IP地址
2 输入10进制型的IP地址
输出描述：
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址
'''

# while 1:
#     try:
#         a=list(map(int,input().split('.')))
#         b=int(input())
#         c=''
#         for i in a:
#             s=bin(i)[2:]
#             while (len(s)<8):
#                 s='0'+s
#             c += s
#         print(int(c,2))
#         b=bin(b)[2:]
#         while (len(b)<32):
#             b= '0'+b
#         print(str(int(b[0:8],2))+'.'+str(int(b[8:16],2))+'.'+str(int(b[16:24],2))+'.'+str(int(b[24:32],2)))
#     except:
#         break


'''
图片整理
描述
Lily上课时使用字母数字图片教小朋友们学习英语单词，每次都需要把这些图片按照大小（ASCII码值从小到大）排列收好。请大家给Lily帮忙，通过代码解决。
Lily使用的图片使用字符"A"到"Z"、"a"到"z"、"0"到"9"表示。
数据范围：每组输入的字符串长度满足1≤n≤1000 
输入描述：
一行，一个字符串，字符串中的每个字符表示一张Lily使用的图片。
输出描述：
Lily的所有图片按照从小到大的顺序输出
'''

# while True:
#     try:
#         print(''.join(sorted(input())))
#     except:
#         break


'''
蛇形矩阵
描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
输入描述：
输入正整数N（N不大于100）
输出描述：
输出一个N行的蛇形矩阵。
'''

# while True:
#     try:
#         num = int(input())
#         for i in range(num):
#             if i == 0:
#                 res = [(x+2)*(x+1)//2 for x in range(num)]
#             else:
#                 res = [x - 1 for x in res[1:]]
#             print(' '.join(map(str, res)))
#     except:
#         break


'''
字符串加密
描述
有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：首先，选择一个单词作为密匙，如TRAILBLAZERS。
如果单词中包含有重复的字母，只保留第1个，将所得结果作为新字母表开头，并将新建立的字母表中未出现的字母按照正常字母表顺序加入新字母表。如下所示：
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y (实际需建立小写字母的字母表，此字母表仅为方便演示）
上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，信息中的每个字母被固定于顶上那行，并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。
因此，使用这个密匙， Attack AT DAWN (黎明时攻击)就会被加密为Tpptad TP ITVH。
请实现下述接口，通过指定的密匙和明文得到密文。
数据范围：1≤n≤100 ，保证输入的字符串中仅包含小写字母
输入描述：
先输入key和要加密的字符串
输出描述：
返回加密后的字符串
'''

# while True:
#     try:
#         s = str(input().strip())
#         jiami = str(input().strip())
#         new_key = ''
#         for i in s:
#             if i.lower() not in new_key:
#                 new_key += i
#         std = 'abcdefghijklmnopqrstuvwxyz'
#         old = ''
#         for i in std:
#             if i not in new_key:
#                 old += i
#         new_s = new_key + old
#         dic = {}
#         for i, j in zip(std, new_s):
#             dic[i] = j
#         res = ''
#         for i in jiami:
#             if i.islower():
#                 res += dic[i]
#             elif i.isupper():
#                 res += str(dic[o]).upper()
#             else:
#                 res += i
#         print(res)
#     except:
#         break


'''
统计每个月兔子的总数
描述
有一种兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子。
例子：假设一只兔子第3个月出生，那么它第5个月开始会每个月生一只兔子。
一月的时候有一只兔子，假如兔子都不死，问第n个月的兔子总数为多少？
数据范围：输入满足1≤n≤31 
输入描述：
输入一个int型整数表示第n个月
输出描述：
输出对应的兔子总数
'''

# while True:
#     try:
#         n = int(input())
#         num = 0
#         num1 = 0
#         num2 = 0
#         for i in range(n):
#             num += num2
#             num2 = num1
#             if num == 0 and num2 == 0:
#                 num1 = 1
#             elif num == 0 and num2 == 1:
#                 num1 = 0
#             else:
#                 num1 = num
#         print(num + num1 + num2)
#
#     except:
#         break

'''
求小球落地5次后所经历的路程和第5次反弹的高度
描述
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
数据范围：输入的小球初始高度满足1≤n≤1000 ，且保证是一个整数
输入描述：
输入起始高度，int型
输出描述：
分别输出第5次落地时，共经过多少米以及第5次反弹多高。
注意：你可以认为你输出保留六位或以上小数的结果可以通过此题。
'''

# while 1:
#     try:
#         num = int(input())
#         print(num*2.875)
#         print((num/32))
#     except:
#         break


'''
判断两个IP是否属于同一子网
描述
IP地址是由4个0-255之间的整数构成的，用"."符号相连。
二进制的IP地址格式有32位，例如：10000011，01101011，00000011，00011000;每八位用十进制表示就是131.107.3.24
子网掩码是用来判断任意两台计算机的IP地址是否属于同一子网络的根据。
子网掩码与IP地址结构相同，是32位二进制数，由1和0组成，且1和0分别连续，其中网络号部分全为“1”和主机号部分全为“0”。
你可以简单的认为子网掩码是一串连续的1和一串连续的0拼接而成的32位二进制数，左边部分都是1，右边部分都是0。
利用子网掩码可以判断两台主机是否中同一子网中。
若两台主机的IP地址分别与它们的子网掩码进行逻辑“与”运算（按位与/AND）后的结果相同，则说明这两台主机在同一子网中。
示例：
IP 地址　 192.168.0.1
子网掩码　 255.255.255.0
转化为二进制进行运算：
IP 地址　  11000000.10101000.00000000.00000001
子网掩码　11111111.11111111.11111111.00000000
AND运算   11000000.10101000.00000000.00000000
转化为十进制后为：
192.168.0.0
IP地址　 192.168.0.254
子网掩码　 255.255.255.0
转化为二进制进行运算：
I P 地址　11000000.10101000.00000000.11111110
子网掩码  11111111.11111111.11111111.00000000
AND运算  11000000.10101000.00000000.00000000
转化为十进制后为：
192.168.0.0
通过以上对两台计算机IP地址与子网掩码的AND运算后，我们可以看到它运算结果是一样的。均为192.168.0.0，所以这二台计算机可视为是同一子网络。
输入一个子网掩码以及两个ip地址，判断这两个ip地址是否是一个子网络。
若IP地址或子网掩码格式非法则输出1，若IP1与IP2属于同一子网络输出0，若IP1与IP2不属于同一子网络输出2。
注:
有效掩码与IP的性质为：
1. 掩码与IP每一段在 0 - 255 之间
2. 掩码的二进制字符串前缀为网络号，都由‘1’组成；后缀为主机号，都由'0'组成
输入描述：
3行输入，第1行是输入子网掩码、第2，3行是输入两个ip地址
题目的示例中给出了三组数据，但是在实际提交时，你的程序可以只处理一组数据（3行）。
输出描述：
若IP地址或子网掩码格式非法则输出1，若IP1与IP2属于同一子网络输出0，若IP1与IP2不属于同一子网络输出2
'''

# while 1:
#     try:
#         mask = list(map(int, input().split('.')))
#         ip1 = list(map(int, input().split('.')))
#         ip2 = list(map(int, input().split('.')))
#         f = True
#         for i in range(len(mask)):
#             if mask[i] not in range(256) or ip1[i] not in range(256) or ip2[i] not in range(256):
#                 f = False
#                 break
#             if i<len(mask)-1 and mask[i] < mask[i+1]:
#                 f = False
#                 break
#         t1,t2= [],[]
#         if f:
#             for i in range(len(mask)):
#                 t1.append(mask[i]&ip1[i])
#                 t2.append(mask[i]&ip2[i])
#             if t1==t2:
#                 print(0)
#             else: print(2)
#         else: print(1)
#     except:break


'''
统计字符
描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
数据范围：输入的字符串长度满足1≤n≤1000 
输入描述：
输入一行字符串，可以有空格
输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数
'''

# while True:
#     try:
#         sentence = input()
#         word, space, digit, other = 0, 0, 0, 0
#         for i in sentence:
#             if i.isalpha():
#                 word += 1
#             elif i == ' ':
#                 space += 1
#             elif i.isdigit():
#                 digit += 1
#             else:
#                 other += 1
#         print(word)
#         print(space)
#         print(digit)
#         print(other)
#     except:
#         break

'''
称砝码
描述
现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
注：
称重重量包括 0
数据范围：每组输入数据满足1≤n≤10,1≤m_i≤2000，1≤x_i≤10 
输入描述：
对于每组测试数据：
第一行：n --- 砝码的种数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])
输出描述：
利用给定的砝码可以称出的不同的重量数
'''

# while True:
#     try:
#         n = int(input())
#         m = list(map(int, input().split()))
#         x = list(map(int, input().split()))
#
#         res = [0]
#         for i in range(n):
#             tmp = [m[i] * j for j in range(x[i] + 1)]
#             res = list(set(a + b for a in tmp for b in res))
#         print(len(res))
#     except:
#         break

'''
学英语
描述
Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：
具体规则如下:
1.在英语读法中三位数字看成一整体，后面再加一个计数单位。从最右边往左数，三位一单位，例如12,345 等
2.每三位数后记得带上计数单位 分别是thousand, million, billion.
3.公式：百万以下千以上的数 X thousand X, 10亿以下百万以上的数：X million X thousand X, 10 亿以上的数：X billion X million X thousand X. 每个X分别代表三位数或两位数或一位数。
4.在英式英语中百位数和十位数之间要加and，美式英语中则会省略，我们这个题目采用加上and，百分位为零的话，这道题目我们省略and
下面再看几个数字例句：
22: twenty two
100:  one hundred
145:  one hundred and forty five
1,234:  one thousand two hundred and thirty four
8,088:  eight thousand (and) eighty eight (注:这个and可加可不加，这个题目我们选择不加)
486,669:  four hundred and eighty six thousand six hundred and sixty nine
1,652,510:  one million six hundred and fifty two thousand five hundred and ten
说明：
数字为正整数，不考虑小数，转化结果为英文小写；
保证输入的数据合法
关键字提示：and，billion，million，thousand，hundred。
数据范围：1≤n≤2000000 
输入描述：
输入一个long型整数
输出描述：
输出相应的英文写法
'''

# num1 = ['zero','one','two','three','four','five','six',
#        'seven','eight','nine','ten','eleven','twelve',
#        'thirteen','fourteen','fifteen','sixteen',
#        'seventeen','eighteen','nineteen']
# num2 = [0,0,'twenty','thirty','forty','fifty','sixty',
#        'seventy','eighty','ninety']
# # 100以内转英文
# def n2w(n):
#     if n > 0:
#         if n < 20:
#             word.append(num1[n])
#         else:
#             word.append(num2[n//10])
#             if n%10 != 0:
#                 word.append(num1[n%10])
# # 1000以内转英文
# def hun(n):
#     if n >= 100:
#         word.append(num1[n//100])
#         word.append('hundred')
#         if n % 100 != 0:
#             word.append('and')
#     n2w(n%100)
# while True:
#     try:
#         n = int(input())
#     except:
#         break
#     else:
#         word = []
#         a = n % 1000  # 个十百位
#         b = (n//1000) % 1000  # 个十百千
#         c = (n//1000000) % 1000  #个十百m
#         d = n // 1000000000    # 个十百b
#         if d > 0:
#             hun(d)
#             word.append('billion')
#         if c > 0 :
#             hun(c)
#             word.append('million')
#         if b > 0:
#             hun(b)
#             word.append('thousand')
#         if a > 0 :
#             hun(a)
#         print(' '.join(word))

'''
迷宫问题
描述
定义一个二维数组 N*M ，如 5 × 5 数组下所示：
int maze[5][5] = {
0, 1, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 1, 0,
};
它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的路线。入口点为[0,0],既第一格是可以走的路。
数据范围：2≤n,m≤10，输入的内容只包含0≤val≤1 
输入描述：
输入两个整数，分别表示二维数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。
输出描述：
左上角到右下角的最短路径，格式如样例所示。
'''

# maze = []
# maze_visit = []
# myStack = []
# move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# N, M = 0, 0
#
#
# def DFS(x, y):
#     if x < 0 or x >= N or y < 0 or y >= M:
#         return False
#     if maze_visit[x][y] == True:
#         return False
#     if maze[x][y] == 1:
#         return False
#     maze_visit[x][y] = True
#     if x == N - 1 and y == M - 1:
#         myStack.append((x, y))
#         return True
#     for m in move:
#         next_x = x + m[0]
#         next_y = y + m[1]
#         if DFS(next_x, next_y):
#             myStack.append((x, y))
#             return True
#     return False
#
#
# while True:
#     try:
#         maze = []
#         maze_visit = []
#         myStack = []
#         N, M = map(int, input().split())
#         for i in range(N):
#             row = input().split()
#             maze.append([int(num) for num in row])
#             maze_visit.append([False] * len(row))
#         # print(N, M)
#         # print(maze)
#         # print(maze_visit)
#         DFS(0, 0)
#         myStack = myStack[::-1]
#         for row in myStack:
#             print('(' + str(row[0]) + ',' + str(row[1]) + ')')
#     except:
#         break


'''
Sudoku
描述
问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，并且满足每一行、每一列、每一个3X3粗线宫内的数字均含1-9，并且不重复。
例如：
输入
输出
数据范围：输入一个 9*9 的矩阵
输入描述：
包含已知数字的9X9盘面数组[空缺位以数字0表示]
输出描述：
完整的9X9盘面数组
'''


# def check(matrix, row, col, value):
#     """
#     检测在(row,col)放value是否合适
#     1.每行含1-9,不含重复值value
#     2.每列含1-9,不含重复值value
#     3.3*3区块含1-9,不含重复值value
#     """
#     # 检测每行
#     for j in range(9):
#         if matrix[row][j] == value:
#             return False
#     # 检测每列
#     for i in range(9):
#         if matrix[i][col] == value:
#             return False
#     # 检测元素所在3*3区域
#     area_row = (row // 3) * 3
#     area_col = (col // 3) * 3
#     for i in range(area_row, area_row + 3):
#         for j in range(area_col, area_col + 3):
#             if matrix[i][j] == value:
#                 return False
#     return True
#
#
# def solveSudoku(matrix, count=0):
#     """
#     遍历每一个未填元素，遍历1-9替换为合适的数字
#     """
#     if (count == 81):  # 递归出口
#         return True
#     # 行优先遍历
#     row = count // 9  # 行标
#     col = count % 9  # 列标
#     if matrix[row][col] != 0:  # 已填充
#         return solveSudoku(matrix, count=count + 1)
#     else:  # 未填充
#         for i in range(1, 10):
#             if check(matrix, row, col, i):  # 找到可能的填充数
#                 matrix[row][col] = i
#                 if solveSudoku(matrix, count=count + 1):  # 是否可完成
#                     return True  # 可完成
#                 # 不可完成
#                 matrix[row][col] = 0  # 回溯
#         return False  # 不可完成
#
#
# while True:
#     try:
#         matrix = []
#         for i in range(9):
#             matrix.append([int(i) for i in input().split(' ')])  # 多维列表输入
#         solveSudoku(matrix)
#         for i in range(9):
#             print(' '.join(map(str, matrix[i])))
#     except:
#         break


'''
名字的漂亮度
描述
给出一个字符串，该字符串仅由小写字母组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个字符串，计算每个字符串最大可能的“漂亮度”。
本题含有多组数据。
数据范围：输入的名字长度满足1≤n≤10000 
输入描述：
第一行一个整数N，接下来N行每行一个字符串
输出描述：
每个字符串可能的最大漂亮程度
'''

# while True:
#     try:
#         a= int(input())
#         s=[]
#         for i in range(0, a):
#             s.append(input().lower())
#         for each in s:
#             sum1=0
#             c=26
#             count=[]
#             for i in list(set(each)):
#                 count.append(each.count(i))
#                 count=sorted(count,reverse=1)
#
#             for i in count:
#                 sum1+=int(i)*c
#                 c-=1
#             print(sum1)
#     except:
#         break


'''
截取字符串
描述
输入一个字符串和一个整数 k ，截取字符串的前k个字符并输出
数据范围：字符串长度满足1≤n≤1000,1≤k≤n 
输入描述：
1.输入待截取的字符串
2.输入一个正整数k，代表截取的长度
输出描述：
截取后的字符串
'''

# while True:
#     try:
#         a,b=input(),input()
#         print(a[:int(b)])
#
#     except:
#         break


'''
从单向链表中删除指定值的节点
描述
输入一个单向链表和一个节点的值，从单向链表中删除等于该值的节点，删除后如果链表中无节点则返回空指针。
链表的值不能重复。
构造过程，例如输入一行数据为:
6 2 1 2 3 2 5 1 4 5 7 2 2
则第一个参数6表示输入总共6个节点，第二个参数2表示头节点值为2，剩下的2个一组表示第2个节点值后面插入第1个节点值，为以下表示:
1 2 表示为
2->1
链表为2->1
3 2表示为
2->3
链表为2->3->1
5 1表示为
1->5
链表为2->3->1->5
4 5表示为
5->4
链表为2->3->1->5->4
7 2表示为
2->7
链表为2->7->3->1->5->4
最后的链表的顺序为 2 7 3 1 5 4
最后一个参数为2，表示要删掉节点为2的值
删除 结点 2
则结果为 7 3 1 5 4
数据范围：链表长度满足1≤n≤1000 ，节点中的值满足0≤val≤10000 
测试用例保证输入合法
输入描述：
输入一行，有以下4个部分：
1 输入链表结点个数
2 输入头结点的值
3 按照格式插入各个结点
4 输入要删除的结点的值
输出描述：
输出一行
输出删除结点后的序列，每个数后都要加空格
'''

# while True:
#     try:
#         string = list(map(int, input().split()))
#         link = []  # 链表
#         link.append(string[1])  # 表头
#         for i in range(1, string[0]):
#             link.insert(link.index(string[2 * i + 1]) + 1, string[2 * i])
#
#         link.remove(string[-1])
#         print(' '.join(map(str, link)))
#     except:
#         break


'''
四则运算
描述
输入一个表达式（用字符串表示），求这个表达式的值。
保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。
数据范围：表达式计算结果和过程中满足|val|≤1000，字符串长度满足1≤n≤1000 
输入描述：
输入一个算术表达式
输出描述：
得到计算结果
'''

# print(eval(input().replace('{','(').replace('}',')').replace('[','(').replace(']',')')))

'''
输出单向链表中倒数第k个结点
描述
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。
链表结点定义如下：
struct ListNode
{
    int m_nKey;
    ListNode* m_pNext;
};
正常返回倒数第k个结点指针，异常返回空指针.
要求：
(1)正序构建链表;
(2)构建后要忘记链表长度。
数据范围：链表长度满足1≤n≤1000，k≤n，链表中数据满足 0≤val≤10000 
本题有多组样例输入。
输入描述：
输入说明
1 输入链表结点个数
2 输入链表的值
3 输入k的值
输出描述：
输出一个整数
'''

# while True:
#     try:
#         num = int(input())
#         in_st = input().strip()
#         k = int(input())
#         mi_st = in_st.split(' ')
#         if k == 0:
#             print(0)
#         else:
#             print(mi_st[num-k])
#     except:
#         break

'''
计算字符串的编辑距离
描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。
许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家 Levenshtein 提出的，故又叫 Levenshtein Distance 。
例如：
字符串A: abcdefg
字符串B: abcdef
通过增加或是删掉字符 ”g” 的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。
要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。
数据范围：给定的字符串长度满足1≤len(str)≤1000 
输入描述：
每组用例一共2行，为输入的两个字符串
输出描述：
每组用例输出一行，代表字符串的距离
'''

# def compare(a,b):
#     m,n=len(a),len(b)
#     dp=list(range(n+1))
#     for i in range(1,m+1):
#         pre=dp[::]
#         dp[0]=i
#         for j in range(1,n+1):
#             if a[i-1]==b[j-1]:
#                 dp[j]=pre[j-1]
#             else:
#                 dp[j]=min(pre[j],pre[j-1],dp[j-1])+1
#     return dp[-1]
# while True:
#     try:
#         a=input()
#         b=input()
#         if a=='' or b=='':
#             print(abs(len(a)-len(b)))
#         else:
#             print(compare(a,b))
#     except:
#         break

'''
描述
以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数、左上角数和右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。
求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出3，输入2则输出-1。
数据范围：1≤n≤10^9
输入描述：
输入一个int整数
输出描述：
输出返回的int值
'''

# while True:
#     try:
#         n=int(input())
#         res=-1
#         if n<=2:
#             res=-1
#         elif n%2==1:
#             res=2
#         elif n%4==0:
#             res=3
#         else:
#             res=4
#         print(res)
#     except:
#         break
#找规律


'''
表达式求值
描述
给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过 100 ，合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。
数据范围：运算过程中和最终结果均满足∣val∣≤2^{31}-1 ，即只进行整型运算，确保输入的表达式合法
输入描述：
输入算术表达式
输出描述：
计算出结果值
'''

# while True:
#     try:
#         n = input()
#         print(eval(n))
#     except:
#         break

'''
挑7
描述
输出 1到n之间 的与 7 有关数字的个数。
一个数与7有关是指这个数是 7 的倍数，或者是包含 7 的数字（如 17 ，27 ，37 ... 70 ，71 ，72 ，73...）
数据范围：1≤n≤30000 
输入描述：
一个正整数 n 。( n 不大于 30000 )
输出描述：
一个整数，表示1到n之间的与7有关的数字个数。
'''

# N=30000
# M=len(str(N))-2
# def getCountOfSeven(n):
#     sevenList=[]
#     # 7的倍数
#     for i in range(7,n+1,7):
#         sevenList.append(i)
#     # 个位是7
#     for i in range(7,n+1,10):
#         sevenList.append(i)
#     # 十位是7、百位是7、千位是7……
#     for a in [10**i for i in range(M)]:
#         for flag in [(80+100*j)*a for j in range(N//(100*a))]:
#             tmp=n+1 if n<flag else flag
#             for i in range(flag-10*a,tmp):
#                 sevenList.append(i)
#     sevenList=list(set(sevenList))
#     return len(sevenList)
#
# while True:
#     try:
#         print(getCountOfSeven(int(input().strip())))
#     except:
#         break


'''
完全数计算
描述
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
输入n，请输出n以内(含n)完全数的个数。
数据范围：1≤n≤5×10^{5}
输入描述：
输入一个数字n
输出描述：
输出不超过n的完全数的个数
'''

# while True:
#     try:
#         a=int(input())
#         print(len(list(filter(lambda x: x < a, [6, 28, 496, 8128]))))
#     except:
#         break

'''
高精度整数加法
描述
输入两个用字符串 str 表示的整数，求它们所表示的数之和。
数据范围：1≤len(str)≤10000 
输入描述：
输入两个字符串。保证字符串只含有'0'~'9'字符
输出描述：
输出求和后的结果
'''

# while True:
#     try:
#         x1 = int(input())
#         x2 = int(input())
#         print(x1+x2)
#     except:
#         break


'''
输入n个整数，输出其中最小的k个
描述
输入n个整数，找出其中最小的k个整数并按升序输出
本题有多组输入样例
数据范围1≤n≤1000，输入的整数满足1≤val≤10000 
输入描述：
第一行输入两个整数n和k
第二行输入一个整数数组
输出描述：
从小到大输出最小的k个整数，用空格分开。
'''

# while True:
#     try:
#         m,n=map(int,input().split(" "))
#         num=list(map(int,input().split()))
#         num.sort()
#         print(" ".join(map(str,num[:n])))
#     except:
#         break

'''
找出字符串中第一个只出现一次的字符
描述
找出字符串中第一个只出现一次的字符
数据范围：输入的字符串长度满足1≤n≤1000 
输入描述：
输入一个非空字符串
输出描述：
输出第一个只出现一次的字符，如果不存在输出-1
'''

# while True:
#     try:
#         a = input()
#         for i in a:
#             if a.count(i) == 1:
#                 print(i)
#                 break
#         else:print(-1)
#     except:break

'''
查找组成一个偶数最接近的两个素数
描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。
数据范围：输入的数据满足4≤n≤1000 
输入描述：
输入一个大于2的偶数
输出描述：
从小到大输出两个素数
'''

# while True:
#     try:
#         def zhishu(x):
#             for i in range(2,x//2+1):
#                 if x%i == 0:
#                     return False
#                     break
#             else:
#                 return True
#         n = int(input().strip())
#         list1 = []
#         for i in range(n//2,n):
#             if zhishu(i) and zhishu(n-i):
#                 list1.append(i)
#                 list1.append(n-i)
#             else:
#                 continue
#         print(list1[1])
#         print(list1[0])
#     except:
#         break

'''
放苹果
描述
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。
数据范围:0≤m≤10，1≤n≤10。
输入描述：
输入两个int整数
输出描述：
输出结果，int型
'''


# def f(m, n):
#     if m == 0 or n == 1:
#         return 1
#     if m < n:
#         return f(m, m)
#     else:
#         return (f(m, n - 1) + f(m - n, n))
#
#
# while True:
#     try:
#         m, n = map(int, input().split())
#         print(f(m, n))
#
#     except:
#         break


'''
查找输入整数二进制中1的个数
描述
输入一个正整数，计算它在二进制下的1的个数。
注意多组输入输出！！！！！！
数据范围：1≤n≤2^{31}-1
输入描述：
输入一个整数
输出描述：
计算整数二进制中1的个数
'''

# while True:
#     try:
#         print(bin(int(input())).count('1'))
#     except:
#         break


'''
DNA序列
描述
一个 DNA 序列由 A/C/G/T 四个字母的排列组合组成。 G 和 C 的比例（定义为 GC-Ratio ）
是序列中 G 和 C 两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，这个比例非常重要。因为高的 GC-Ratio 可能是基因的起始点。
给定一个很长的 DNA 序列，以及限定的子串长度 N ，请帮助研究人员在给出的 DNA 序列中从左往右找出 GC-Ratio 最高且长度为 N 的第一个子串。
DNA序列为 ACGT 的子串有: ACG , CG , CGT 等等，但是没有 AGT ， CT 等等
数据范围：字符串长度满足1≤n≤1000 ，输入的字符串只包含 A/C/G/T 字母
输入描述：
输入一个string型基因序列，和int型子串的长度
输出描述：
找出GC比例最高的子串,如果有多个则输出第一个的子串
'''

# while True:
#     try:
#         a=input()
#         n=int(input())
#         g=0
#         index=0
#         for i in range(0,len(a)-n+1):
#             GC = a.count('G',i,i+n) + a.count('C',i,i+n)
#             if GC > g:
#                 g = GC
#                 index = i
#         print(a[index:index+n])
#     except:
#         break

'''
MP3光标位置
描述
MP3 Player因为屏幕较小，显示歌曲列表的时候每屏只能显示几首歌曲，用户要通过上下键才能浏览所有的歌曲。为了简化处理，假设每屏只能显示4首歌曲，光标初始的位置为第1首歌。
现在要实现通过上下键控制光标移动来浏览歌曲列表，控制逻辑如下：
歌曲总数<=4的时候，不需要翻页，只是挪动光标位置。
光标在第一首歌曲上时，按Up键光标挪到最后一首歌曲；光标在最后一首歌曲时，按Down键光标挪到第一首歌曲。
其他情况下用户按Up键，光标挪到上一首歌曲；用户按Down键，光标挪到下一首歌曲。
2. 歌曲总数大于4的时候（以一共有10首歌为例）：
特殊翻页：屏幕显示的是第一页（即显示第1 – 4首）时，
光标在第一首歌曲上，用户按Up键后，屏幕要显示最后一页（即显示第7-10首歌），同时光标放到最后一首歌上。
同样的，屏幕显示最后一页时，光标在最后一首歌曲上，用户按Down键，屏幕要显示第一页，光标挪到第一首歌上。
一般翻页：屏幕显示的不是第一页时，光标在当前屏幕显示的第一首歌曲时，用户按Up键后，屏幕从当前歌曲的上一首开始显示，
光标也挪到上一首歌曲。光标当前屏幕的最后一首歌时的Down键处理也类似。
其他情况，不用翻页，只是挪动光标就行。
数据范围：命令长度1≤s≤100 ，歌曲数量1≤n≤150 
进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n) 
输入描述：
输入说明：
1 输入歌曲数量
2 输入命令 U或者D
输出描述：
输出说明
1 输出当前列表
2 输出当前选中歌曲
'''

# while True:
#     try:
#         num = int(input())
#         command = input()
#         head, tail, i = 1, 4, 1
#         if (num <= 4):
#             for ci in command:
#                 if (ci == 'U'):
#                     if i == 1:
#                         i = num
#                     else:
#                         i -= 1
#                 else:
#                     if i == num:
#                         i = 1
#                     else:
#                         i += 1
#             head, tail = 1, num
#         else:
#             for ci in command:
#                 if (ci == 'U'):
#                     if i == 1:
#                         i = num
#                         head, tail = num - 3, num
#                     else:
#                         i -= 1
#                         if i < head:
#                             head, tail = i, i + 3
#                 else:
#                     if i == num:
#                         i = 1
#                         head, tail = 1, 4
#                     else:
#                         i += 1
#                         if i > tail:
#                             head, tail = i - 3, i
#         ans = list(range(head, tail + 1))
#         print(' '.join(str(j) for j in ans))
#         print(i)
#     except:
#         break

'''
查找两个字符串a,b中的最长公共子串
描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
数据范围：字符串长度1≤length≤300 
进阶：时间复杂度：O(n^3)，空间复杂度：O(n)
输入描述：
输入两个字符串
输出描述：
返回重复出现的字符
'''

# while True:
#     try:
#         str1=input()
#         str2=input()
#         n = 0
#         s = ''
#         if len(str1)>len(str2):
#             str1,str2 = str2, str1
#         for i in range(len(str1)+1):
#             if str1[i-n:i] in str2:
#                 s = str1[i-n:i]
#                 n +=1
#         print(s)
#     except:
#         break


'''
配置文件恢复
描述
有6条配置命令，它们执行的结果分别是：
 命令                    执行
reset	            reset what
reset board	        board fault
board add	        where to add
board delete        no board at all
reboot backplane	impossible
backplane abort	    install first
he he	            unknown command
注意：he he不是命令。
为了简化输入，方便用户，以“最短唯一匹配原则”匹配（注：需从首字母开始进行匹配）：
1、若只输入一字串，则只匹配一个关键字的命令行。例如输入：r，根据该规则，匹配命令reset，执行结果为：reset what；输入：res，根据该规则，匹配命令reset，执行结果为：reset what；
2、若只输入一字串，但匹配命令有两个关键字，则匹配失败。例如输入：reb，可以找到命令reboot backpalne，但是该命令有两个关键词，所有匹配失败，执行结果为：unknown command
3、若输入两字串，则先匹配第一关键字，如果有匹配，继续匹配第二关键字，如果仍不唯一，匹配失败。
例如输入：r b，找到匹配命令reset board 和 reboot backplane，执行结果为：unknown command。
例如输入：b a，无法确定是命令board add还是backplane abort，匹配失败。
4、若输入两字串，则先匹配第一关键字，如果有匹配，继续匹配第二关键字，如果唯一，匹配成功。例如输入：bo a，确定是命令board add，匹配成功。
5、若输入两字串，第一关键字匹配成功，则匹配第二关键字，若无匹配，失败。例如输入：b addr，无法匹配到相应的命令，所以执行结果为：unknow command。
6、若匹配失败，打印“unknown command”
注意：有多组输入。
数据范围：数据组数：1≤t≤800 ，字符串长度1≤s≤20 
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
输入描述：
多行字符串，每行字符串一条命令
输出描述：
执行结果，每条命令输出一行
'''


# while True:
#     try:
#         m=input().strip().split()
#         key=["reset","reset board","board add","board delete","reboot backplane","backplane abort"]
#         value=["reset what","board fault","where to add","no board at all","impossible","install first"]
#         #不建字典，用列表的方式避免了双层循环，如果实在要用列表，直接用dict(zip（list1,list2）)合成字典都行.
#         if len(m)<1 or len(m)>2:   #判断当输入为小于1个或者输入大于2个字符串时，不符合命令，就报未知命令
#             print("unknown command")
#         elif len(m)==1:   #当输入一个字符串
#             if m[0]==key[0][:len(m[0])]:  #这里才是解决这个题的最佳思想，利用切片的思想来匹配
#                 print(value[0])
#             else:
#                 print("unknown command")
#         else:
#             index=[]
#             for i in range(1,len(key)): #这里把所有原始命令遍历，如果这里写成(len(key)+1),也就是1..6，那么下面的key[i]要改成k[i-1]才符合逻辑
#                 a=key[i].split() #将具体的一个KEY分割成两部分
#                 if m[0]==a[0][:len(m[0])] and m[1]==a[1][:len(m[1])]:  #然后去匹配被分割的key,这里不可能有reset这种单独的，因为上面条件已经限制了。
#                     index.append(i)  #符合条件就把这个位置入列表
#             if len(index)!=1:
#                 print("unknown command")
#             else:
#                 print(value[index[0]]) #输出对应的value值
#     except:
#         break


'''
24点游戏算法
描述
给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,运算符仅允许出现在两个数字之间,本题对数字选取顺序无要求，但每个数字仅允许使用一次，且需考虑括号运算
此题允许数字重复，如3 3 4 4为合法输入，此输入一共有两个3，但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作。
输入描述：
读入4个[1,10]的整数，数字允许重复，测试用例保证无异常数字。
输出描述：
对于每组案例，输出一行表示能否得到24点，能输出true，不能输出false
'''

# import sys
#
#
# def func(nums, tar):
#     if len(nums) == 1: return nums[0] == tar
#     # 注意各种计算顺序都要考虑
#     for i in range(len(nums)):
#         nums = nums[1:] + [nums[0]]
#         if func(nums[1:], tar + nums[0]) or func(nums[1:], tar - nums[0]) or func(nums[1:], tar * nums[0]) or func(
#                 nums[1:], tar / nums[0]):
#             return True
#     return False
#
#
# for line in sys.stdin:
#     nums = list(map(int, line.strip().split()))
#     print(str(func(nums, 24)).lower())

'''
成绩排序
描述
给定一些同学的信息（名字，成绩）序列，请你将他们的信息按照成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。
例示：
jack      70
peter     96
Tom       70
smith     67
从高到低  成绩
peter     96
jack      70
Tom       70
smith     67
从低到高
smith     67
jack      70
Tom       70
peter     96
注：0代表从高到低，1代表从低到高
数据范围：人数：1≤n≤200 
进阶：时间复杂度：O(nlogn)，空间复杂度：O(n) 
输入描述：
第一行输入要排序的人的个数n，第二行输入一个整数表示排序的方式，之后n行分别输入他们的名字和成绩，以一个空格隔开
输出描述：
按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开
'''

# while True:
#     try:
#         num = int(input())
#         flag = False if int(input().strip()) == 1 else True
#         out = []
#         for i in range(num):
#             info = input().split()
#             out.append((info[0], int(info[1])))
#         for j in sorted(out, key=lambda x: x[1], reverse=flag):
#             print(j[0], j[1])
#
#
#     except:
#         break


'''
矩阵乘法
描述
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C。这个矩阵的每个元素是由下面的公式决定的
矩阵的大小不超过100*100
输入描述：
第一行包含一个正整数x，代表第一个矩阵的行数
第二行包含一个正整数y，代表第一个矩阵的列数和第二个矩阵的行数
第三行包含一个正整数z，代表第二个矩阵的列数
之后x行，每行y个整数，代表第一个矩阵的值
之后y行，每行z个整数，代表第二个矩阵的值
输出描述：
对于每组输入数据，输出x行，每行z个整数，代表两个矩阵相乘的结果
'''

# while True:
#     try:
#         x = int(input())
#         y = int(input())
#         z = int(input())
#         a = []
#         b = []
#         for i in range(x):
#             a.append(list(map(int, input().split())))
#         for i in range(y):
#             b.append(list(map(int, input().split())))
#         res = [[] for i in range(x)]
#         b = list(zip(*b))
#         for i in range(x):
#             for j in range(z):
#                 sums = [n1*n2 for n1, n2 in zip(a[i], b[j])]
#                 res[i].append(sum(sums))
#         for line in res:
#             print(' '.join(map(str, line)))
#     except:
#         break


'''
矩阵乘法计算量估算
描述
矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：
A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵
计算A*B*C有两种顺序：((AB)C)或者(A(BC))，前者需要计算15000次乘法，后者只需要3500次。
编写程序计算不同的计算顺序需要进行的乘法次数。
数据范围：矩阵个数：1≤n≤15 ，行列数：1≤row_i,col_i≤100 ，保证给出的字符串表示的计算顺序唯一。
进阶：时间复杂度：O(n) ，空间复杂度：O(n) 
输入描述：
输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则
计算的法则为一个字符串，仅由左右括号和大写字母（'A'~'Z'）组成，保证括号是匹配的且输入合法！
输出描述：
输出需要进行的乘法次数
'''

# while True:
#     try:
#         n = int(input())
#         arr = []
#         order = []
#         res = 0
#         for i in range(n):
#             arr.append(list(map(int, input().split())))
#         f = input()
#         for i in f:
#             if i.isalpha():
#                 order.append(arr[ord(i) - 65])
#             elif i == ')' and len(order) >= 2:
#                 a = order.pop()
#                 b = order.pop()
#                 res += b[0] * b[1] * a[1]
#                 order.append([b[0], a[1]])
#         print(res)
#     except:
#         break


'''
字符串通配符
描述
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
？：匹配1个字符
注意：匹配时不区分大小写。
输入：
通配符表达式；
一组字符串。
输出：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
数据范围：字符串长度100\1≤s≤100 
进阶：时间复杂度：O(n^2)，空间复杂度：O(n)
输入描述：
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串
输出描述：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
'''

# import re
# while True:
#     try:
#         a,b = input().strip().lower(),input().strip().lower()
#         a=a.replace('?','\w{1}').replace('.','\.').replace('*','\w*')
#         c=re.findall(a,b)
#         if b in c and len(c)==1:
#             print('true')
#         else:
#             print('false')
#     except:
#         break
#