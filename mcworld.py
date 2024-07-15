import os, time, math
from func import get_wrlz, tem_size, cls, opendir, is_mcworld, get_folder_size, get_str_width

hr, vers, input_info = '=' * tem_size(0), ['正式版', '预览版'], '输入选项后回车确定：' # 常量
ls, msize_l, lname_l, dtd_vers, wds = [], [], [], [], [[], []] # 变量

for i in [0, 1]: # 将已安装版本信息写入dtd_vers和dtd_str (detected_versions, dtd_string)
	try:
		if os.path.isdir(get_wrlz(i)):
			wds[i] = (os.listdir(f'{get_wrlz(i)}'))
			dtd_vers.append(i) # [] | [0] | [1] | [0, 1]
	except: print(f'{vers[i]} not found!') # 没用
if len(dtd_vers) == 1: dtd_str = vers[dtd_vers[0]] # '正式版' | '预览版'
elif len(dtd_vers) == 2: dtd_str = f'{vers[0]}、{vers[1]}' # '正式版、预览版'

cls()

# 将全部MCBE存档信息存储到ls列表
for i in dtd_vers:
	for w in wds[i]:
		if is_mcworld(f'{get_wrlz(i)}\\{w}') == True:
			with open(f'{get_wrlz(i)}\\{w}\\levelname.txt', 'r', encoding = 'UTF-8') as l:
				lname = fname = l.readline()                                   # levelname, fullname
				if get_str_width(lname) > 16:
					while get_str_width(lname) > 13: lname = lname[:-1]
					lname += '...'
			timestamp = os.path.getmtime(f'{get_wrlz(i)}\\{w}\\level.dat')     # timestamp
			mtime = time.strftime('%Y/%m/%d %H:%M', time.localtime(timestamp)) # modified_time (str)
			bsize = get_folder_size(f'{get_wrlz(i)}\\{w}')                     # Byte size (int)
			if bsize < 1048576: msize = round(bsize / 10485.76) / 100          # MB_size (num)
			else: msize = round(bsize / 104857.6) / 10                         # MB_size (num)
			ls.append([i, w, math.floor(timestamp), mtime, bsize, msize, lname, fname]) # list
			msize_l.append(len(str(msize)))                                    # MB_size_lengths
			lname_l.append(get_str_width(lname))                               # levelname_lengths

# 按照修改时间冒泡排序 (降序，新的在前) https://www.runoob.com/w3cnote/bubble-sort.html
for i in range(1, len(ls)):
	for j in range(0, len(ls) - i):
		if ls[j][2] < ls[j + 1][2]: ls[j], ls[j + 1] = ls[j + 1], ls[j]

def list_all():
	cls()
	os.system(f'title 基岩版存档管理器 - {len(ls)}个存档')
	if not len(dtd_vers) in [1, 2]:
		print(f'基岩版存档管理器 - 存档列表\n{hr}\n没检测到com.mojang，后面还要加一堆提示QAQ\n')
	else:
		wds_list = ''
		for i in range(0, len(ls)):
			index_s = ' ' * (len(str(len(ls))) - len((str(i + 1))) + 2)
			lname_s = ' ' * (max(lname_l) - get_str_width(ls[i][6]))
			msize_s = ' ' * (max(msize_l) - len(str(ls[i][5])))
			if len(ls) < 10: index_s = ' ' * 3
			wds_list += f'| {index_s}{i + 1} | {vers[ls[i][0]]} | {ls[i][6]}{lname_s} | {ls[i][1]} | {msize_s}{ls[i][5]} MB | {ls[i][3]} |\n'
		print(f'''╭{'─' * (max(msize_l) + max(lname_l) + 58)}╮
| 基岩版存档管理器 - 检测到：{dtd_str}{' ' * (max(msize_l) + max(lname_l) - len(dtd_vers) * 8 + 32)}|
├──────┬────────┬─────{'─' * (max(lname_l) - 4)}─┬──────────────┬─{'─' * (max(msize_l) - 1)}─────┬──────────────────┤
| 编号 |  版本  | 名称{' ' * (max(lname_l) - 4)} | 存档文件夹名 | {' ' * (max(msize_l) - 1)}大小 | 修改时间         |
| ---: | :----: | :---{'-' * (max(lname_l) - 4)} | ------------ | {'-' * (max(msize_l) - 1)}---: | ---------------- |
{wds_list}├──────┴────────┴─{'─' * max(lname_l)}─┴──────────────┴─{'─' * (max(msize_l) - 1)}─────┴──────────────────┤
|     选项列表  【o】打开正式版存档文件夹；【编号】查看存档详细信息，如：3 {' ' * (max(msize_l) + max(lname_l) - 16)}|
|【0】退出程序；【p】打开预览版存档文件夹；【编号+e】导出为mcworld， 如：2e{' ' * (max(msize_l) + max(lname_l) - 16)}|
╰{'─' * (max(msize_l) + max(lname_l) + 58)}╯''')

		sel = input(input_info)
		if sel == '0': exit()
		elif sel == 'o': opendir(get_wrlz(0)); os.system('title 已打开正式版文件夹！'); time.sleep(2); list_all()
		elif sel == 'p': opendir(get_wrlz(1)); os.system('title 已打开预览版文件夹！'); time.sleep(2); list_all()
		else: print('无效输入！'); time.sleep(2); list_all()

# def demo(): # debug: print ls
# 	cls(); info = ''
# 	for i in range(0, len(ls)): info += f'{i}: {ls[i]}\n'
# 	print(f'dtd_vers: {dtd_vers}\n\nwds: {wds}\n\ndemo: [版本, 文件夹名, 修改时间戳, 修改时间, 字节体积, 兆字节体积, 存档短名, 存档完整名称]\n{info}// 注: 按照修改时间戳降序，0和1: 正式版和预览版\n\nls: {ls}\n')
# demo() # debug

list_all()