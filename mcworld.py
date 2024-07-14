import os, time, math
from func import get_wrlz, tem_size, cls, is_mcworld, get_folder_size, bubble

hr, input_info = '=' * tem_size(0), '输入选项编号后回车确定：' # 常量
ls, msize_lens, wds = [], [], [os.listdir(f'{get_wrlz(0)}'), os.listdir(f'{get_wrlz(1)}')] # 变量

cls()

# 将全部MCBE存档信息存储到ls列表
for i in [0, 1]: # 正式版、预览版
	for w in wds[i]:
		if is_mcworld(f'{get_wrlz(i)}\\{w}') == True:
			with open(f'{get_wrlz(i)}\\{w}\\levelname.txt', 'r', encoding = 'UTF-8') as l:
				lname = l.readline()                                       # 存档名称
			timestamp = os.path.getmtime(f'{get_wrlz(i)}\\{w}\\level.dat') # 时间戳
			time_struct = time.localtime(timestamp)                        # 修改时间 (time_struct)
			mtime = time.strftime('%Y/%m/%d %H:%M', time_struct)           # 修改时间 (字符串)
			bsize = get_folder_size(f'{get_wrlz(i)}\\{w}')                 # 存档大小 (字节)
			if bsize < 1048576: msize = round(bsize / 10485.76) / 100      # 存档大小 (兆字节)
			else: msize = round(bsize / 104857.6) / 10
			ls.append([i, w, math.floor(timestamp), mtime, bsize, msize, lname])
			msize_lens.append(len(str(msize)))

# 按照修改时间冒泡排序 (降序，新的在前) https://www.runoob.com/w3cnote/bubble-sort.html
for i in range(1, len(ls)):
	for j in range(0, len(ls) - i):
		if ls[j][2] < ls[j + 1][2]:
			ls[j], ls[j + 1] = ls[j + 1], ls[j]

def demo(): # debug: print wds_ls
	cls()
	print('demo: [版本, 文件夹名, 修改时间戳, 修改时间, 字节体积, 兆字节体积, 存档名称]')
	for i in range(0, len(ls)): print(f'{i}: {ls[i]}')
	input(f'注: 按照修改时间戳降序，0和1: 正式版和预览版，ls: {ls}')
# demo() # debug

def list_all():
	cls()
	print(f'基岩版存档管理器\n{hr}')
	for i in range(0, len(ls)): print(f'| {' ' * (len(str(len(ls))) - len((str(i + 1))))}{i + 1} | {['正式版', '预览版'][ls[i][0]]} | {ls[i][1]} | {ls[i][3]} | {' ' * (bubble(msize_lens)[0] - len(str(ls[i][5])))}{ls[i][5]}MB | {ls[i][6]}')

list_all()
