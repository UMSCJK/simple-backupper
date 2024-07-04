import os, time
from functions import comp, getTime, temSize, cls, folder, readJSON

cfg = readJSON('config.json')
def main():
	cls()
	print(f'文件夹备份工具\n{'=' * temSize(0)}')
	for i in cfg:
		print(f'''{i}: {cfg[i]['info']}
    备份路径：{cfg[i]['bdir']}\n''')
	print(f'0: 退出程序 (Ctrl+C)\n{'=' * temSize(0)}')
	sel = input('输入选项编号后回车确定：')
	if sel == '0': exit()
	elif sel in cfg:
		options(sel)
	main()

def options(i):
	cls()
	print(f'''{cfg[i]['info']}
{'=' * temSize(0)}
原始路径：{cfg[i]['path']}
备份预览：{cfg[i]['bdir']}\{cfg[i]['head']}_{getTime(12)}.{cfg[i]['form']}
{'=' * temSize(0)}
1：开始备份
2：打开原目录
0：返回主界面
{'=' * temSize(0)}''')
	sel = input('输入选项编号后回车确定：')
	if sel == '0': main()
	elif sel == '1':
		if not os.path.exists(cfg[i]['bdir']): os.makedirs(cfg[i]['bdir'])
		comp(f'{cfg[i]['bdir']}\{cfg[i]['head']}_{getTime(12)}.{cfg[i]['form']}', cfg[i]['path'])
		time.sleep(1)
		ifolder(i)
	elif sel == '2':
		folder(cfg[i]['path'])
		options(i)

def ifolder(i):
	cls()
	print(f'''{cfg[i]['info']}：备份完成
{'=' * temSize(0)}
1：打开备份所在文件夹
0：返回主界面
{'=' * temSize(0)}''')
	sel = input('输入选项编号后回车确定：')
	if sel == '0': main()
	elif sel == '1': folder(cfg[i]['bdir'])
	main()
main()