import os
from functions import comp, getOjng, getTime, temSize, cls, folder, readJSON, writeJSON, cfgOK

inputInfo = '输入选项编号后回车确定：'
defaultConfig = {
	"1": {
		"info": "PVZ杂交版",
		"bdir": ".\\Backups",
		"head": "pvzHE",
		"form": "7z",
		"path": "C:\\ProgramData\\PopCap Games\\PlantsVsZombies\\pvzHE\\yourdata"
	},
	"2": {
		"info": "Minecraft基岩版",
		"bdir": ".\\Backups",
		"head": "MCBE",
		"form": "zip",
		"path": getOjng(0)
	},
	"3": {
		"info": "Minecraft预览版",
		"bdir": ".\\Backups",
		"head": "MCPV",
		"form": "zip",
		"path": getOjng(1)
	}
}

def main():
	cls()
	global cfg; cfg = readJSON('config.json')
	print(f'文件夹备份工具\n{'=' * temSize(0)}')
	for i in cfg: print(f'''{i}: {cfg[i]['info']}\n    备份路径：{cfg[i]['bdir']}\n''')
	print(f'0: 退出程序 (Ctrl+C)\n{'=' * temSize(0)}')
	sel = input(inputInfo)
	if sel == '0': exit()
	elif sel in cfg: options(sel)
	else: main()

def options(i):
	cls()
	print(f'''{cfg[i]['info']}\n{'=' * temSize(0)}\n原始路径：{cfg[i]['path']}\n备份预览：{cfg[i]['bdir']}\{cfg[i]['head']}_{getTime(12)}.{cfg[i]['form']}\n{'=' * temSize(0)}\n1：开始备份\n2：打开原目录\n0：返回主界面\n{'=' * temSize(0)}''')
	sel = input(inputInfo)
	if sel == '0': main()
	elif sel == '2': folder(cfg[i]['path']); options(i)
	elif sel == '1':
		if not os.path.exists(cfg[i]['bdir']): os.makedirs(cfg[i]['bdir'])
		comp(f'{cfg[i]['bdir']}\{cfg[i]['head']}_{getTime(12)}.{cfg[i]['form']}', cfg[i]['path'])
		ifolder(i)
	else: options(i)

def ifolder(i):
	cls()
	print(f'''{cfg[i]['info']}：备份完成\n{'=' * temSize(0)}\n1：打开备份所在文件夹\n0：返回主界面\n{'=' * temSize(0)}''')
	sel = input(inputInfo)
	if sel == '0': main()
	elif sel == '1': folder(cfg[i]['bdir'])
	else: ifolder(i)

def cfgErr():
	cls()
	print(f'''配置文件损坏！\n{'=' * temSize(0)}\n1：修复并继续\n2：打开config.json\n0：退出\n{'=' * temSize(0)}''')
	sel = input(inputInfo)
	if sel == '0': exit()
	elif sel == '1': writeJSON('config.json', defaultConfig); main()
	elif sel == '2': os.system('start config.json'); cfgErr()
	else: cfgErr()

if not os.path.isfile('config.json'): writeJSON('config.json', defaultConfig); main()
elif cfgOK('config.json') == False: cfgErr()
else: main()