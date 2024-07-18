import os, time
from func import get_wrlz, tem_size, cls, opendir, is_mcworld, get_folder_size, get_width

hr, vers = '=' * tem_size(0), ['正式版', '预览版']         # 常量1
title, prompt = '基岩版存档管理器', '输入选项后回车确定：' # 常量2
size_l, name_l, ls, dtd_vers, wds = 0, 0, [], [], [[], []] # 变量：list, msize_lengths, lname_lengths

for i in [0, 1]: # 将已安装版本信息写入dtd_vers和dtd_str (dtd: detected)
	try:
		if os.path.isdir(get_wrlz(i)):
			wds[i] = os.listdir(f'{get_wrlz(i)}')
			dtd_vers.append(i)
	except: print(f'{vers[i]} not found!')
if len(dtd_vers) == 1: dtd_str = vers[dtd_vers[0]]         # '正式版' | '预览版'
elif len(dtd_vers) == 2: dtd_str = f'{vers[0]}、{vers[1]}' # '正式版、预览版'
for i in dtd_vers:                                         # 将全部MCBE存档信息存储到ls列表
	for w in wds[i]:
		if is_mcworld(f'{get_wrlz(i)}\\{w}') == True:
			with open(f'{get_wrlz(i)}\\{w}\\levelname.txt', 'r', encoding = 'UTF-8') as l:
				name = fname = l.readline() # levelname, fullname
				if get_width(name) > 16:
					while get_width(name) > 13: name = name[:-1]
					name += '...'
			timestamp = os.path.getmtime(f'{get_wrlz(i)}\\{w}\\level.dat')     # timestamp
			mtime = time.strftime('%Y/%m/%d %H:%M', time.localtime(timestamp)) # modified_time (str)
			byte = get_folder_size(f'{get_wrlz(i)}\\{w}')                      # Byte size (int)
			if byte < 1048576: size = round(byte / 10485.76) / 100             # MB_size (num)
			else: size = round(byte / 104857.6) / 10                           # MB_size (num)
			ls.append([i, w, int(timestamp), mtime, byte, size, name, fname])  # list
for i in range(1, len(ls)): # 按照修改时间冒泡降序
	for j in range(0, len(ls) - i): # https://www.runoob.com/w3cnote/bubble-sort.html
		if ls[j][2] < ls[j + 1][2]: ls[j], ls[j + 1] = ls[j + 1], ls[j]
for i in ls:
	idex_l = max(len(str(len(ls))), 4)
	name_l = max(name_l, get_width(i[6]), 4)
	size_l = max(size_l, len(str(i[5])))

def list_all():
	cls()
	os.system(f'title {title} - {len(ls)}个存档')
	# print(f'// [版本,文件夹,时间戳,修改,B体积,MB体积,短名,完整名]\n{ls}') # DEBUG
	if dtd_vers == []:
		print(f'''{title} - 存档列表\n{hr}\n未检测到任何com.mojang，布什戈门？来找彩蛋的？
安装MCBE：          https://mcappx.com
购买Minecraft：     https://www.xbox.com/zh-CN/games/store/minecraft-java-bedrock-edition-for-pc/9NXP44L49SHJ
MCLauncher使用教程：https://github.com/UMSCJK/MCLauncher-tutorial
''')
	elif len(ls) == 0: print(f'{title} - 检测到：{dtd_str}\n{hr}\n未检测到存档！错误代码：雪豹')
	else:
		world_ls = ''
		for i in range(0, len(ls)):
			idex_s = ' ' * (idex_l - len((str(i + 1))))
			name_s = ' ' * (name_l - get_width(ls[i][6]))
			size_s = ' ' * (size_l - len(str(ls[i][5])))
			world_ls += f'| {idex_s}{i + 1} | {vers[ls[i][0]]} | {ls[i][6]}{name_s}'
			world_ls += f' | {ls[i][1]} | {size_s}{ls[i][5]} MB | {ls[i][3]} |\n'
		print(f'''╭{'─' * (idex_l + name_l + size_l + 54)}╮
| {title} - 检测到：{dtd_str}{' ' * (idex_l + size_l + name_l - len(dtd_vers) * 8 + 28)}|
├─{'─' * (idex_l - 4)}─────┬────────┬─────{'─' * (name_l - 4)}─┬──────────────┬─{'─' * (size_l - 1)}─────┬──────────────────┤
| {' ' * (idex_l - 4)}编号 |  版本  | 名称{' ' * (name_l - 4)} | 存档文件夹名 | {' ' * (size_l - 1)}大小 | 修改时间         |
| {'-' * (idex_l - 4)}---: | :----: | :---{'-' * (name_l - 4)} | ------------ | {'-' * (size_l - 1)}---: | ---------------- |
{world_ls}├─{'─' * idex_l}─┴────────┴─────{'─' * (name_l - 4)}─┴──────────────┴─{'─' * (size_l - 1)}─────┴──────────────────┤
| 选项列表 【o】打开正式版存档;【编号】查看存档信息，如：3{' ' * (idex_l + name_l + size_l - 4)} |
|【0】退出;【p】打开预览版存档;【编号+e】导出存档， 如：2e{' ' * (idex_l + name_l + size_l - 4)} |
╰{'─' * (idex_l + name_l + size_l + 54)}╯\n''')
		sel = input(prompt)
		if sel == '0': exit()
		elif sel.lower() == 'o': opendir(get_wrlz(0)); os.system('title 已打开正式版文件夹！'); time.sleep(2); list_all()
		elif sel.lower() == 'p': opendir(get_wrlz(1)); os.system('title 已打开预览版文件夹！'); time.sleep(2); list_all()
		elif sel.lower() in ['op', 'po']:
			opendir(get_wrlz(0)); opendir(get_wrlz(1)); os.system('title 已打开双版本文件夹！'); time.sleep(2); list_all()
		elif sel.isdigit() == True:
			if int(sel) <= len(ls):
				show_info(int(sel) - 1)
			else:
				print(f'存档编号无效！'); time.sleep(2); list_all()
		elif sel[-1] == 'e' and sel[:-1].isdigit() == True:
			sel = sel[:-1] # TODO：导出指定存档
			if int(sel) <= len(ls): print(f'这里要导出{ls[int(sel) - 1][7]}为mcworld！'); time.sleep(2); list_all()
			else: print(f'存档编号无效！'); time.sleep(2); list_all()
		else: print('无效输入！'); time.sleep(2); list_all()

def show_info(i): # TODO：完善显示信息
	cls()
	print(f'存档信息：{ls[i][7]}')
	sel = input(prompt)
	if sel == '0': list_all()

list_all()