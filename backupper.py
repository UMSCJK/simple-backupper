import os
from func import comp, get_ojng, get_time, tem_size, cls, opendir, read_json, write_json, cfg_ok

hr, input_info = '=' * tem_size(0), '输入选项编号后回车确定：'
default_cfg = {
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
		"path": get_ojng(0)
	},
	"3": {
		"info": "Minecraft预览版",
		"bdir": ".\\Backups",
		"head": "MCPV",
		"form": "zip",
		"path": get_ojng(1)
	}
}

def main():
	cls()
	global cfg; cfg = read_json('config.json')
	print(f'文件夹备份工具\n{hr}')
	for i in cfg: print(f'''{i}: {cfg[i]['info']}\n    备份路径：{cfg[i]['bdir']}\n''')
	print(f'0: 退出程序 (Ctrl+C)\n{hr}')
	sel = input(input_info)
	if sel == '0': exit()
	elif sel in cfg: options(sel)
	else: main()

def options(i):
	cls()
	print(f'''{cfg[i]['info']}\n{hr}\n原始路径：{cfg[i]['path']}
备份预览：{cfg[i]['bdir']}\{cfg[i]['head']}_{get_time(12)}.{cfg[i]['form']}\n{hr}
1：开始备份\n2：打开原目录\n0：返回主界面\n{hr}''')
	sel = input(input_info)
	if sel == '0': main()
	elif sel == '2': opendir(cfg[i]['path']); options(i)
	elif sel == '1':
		if not os.path.exists(cfg[i]['bdir']): os.makedirs(cfg[i]['bdir'])
		comp(f'{cfg[i]['bdir']}\{cfg[i]['head']}_{get_time(12)}.{cfg[i]['form']}', cfg[i]['path'])
		ifolder(i)
	else: options(i)

def ifolder(i):
	cls()
	print(f'''{cfg[i]['info']}：备份完成\n{hr}\n1：打开备份所在文件夹\n0：返回主界面\n{hr}''')
	sel = input(input_info)
	if sel == '0': main()
	elif sel == '1': opendir(cfg[i]['bdir'])
	else: ifolder(i)

def cfg_err():
	cls()
	print(f'''配置文件损坏！\n{hr}\n1：修复并继续\n2：打开config.json\n0：退出\n{hr}''')
	sel = input(input_info)
	if sel == '0': exit()
	elif sel == '1': write_json('config.json', default_cfg); main()
	elif sel == '2': os.system('start config.json'); cfg_err()
	else: cfg_err()

if not os.path.isfile('config.json'): write_json('config.json', default_cfg); main()
elif cfg_ok('config.json') == False: cfg_err()
else: main()