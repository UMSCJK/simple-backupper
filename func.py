import os, time, json
def comp(f, d): os.system(f'7z a {f} \'{d}\\**\'') # Compress
def extr(f, d): os.system(f'7z x {f} -o{d} -aoa') # Extract
def get_ojng(v): return f'{os.environ.get('LocalAppData')}\\Packages\\Microsoft.Minecraft{['UWP', 'WindowsBeta'][v]}_8wekyb3d8bbwe\\LocalState\\games\\com.mojang'
def get_wrlz(v): return f'{get_ojng(v)}\\minecraftWorlds'
def get_time(d): return time.strftime('%Y%m%d%H%M%S')[0:d]
def tem_size(i): return [os.get_terminal_size().columns, os.get_terminal_size().lines][i]
def cls(): os.system('cls')
def opendir(p): os.system(f'explorer {p}')
def read_json(f): # Read & return JSON file data
	with open(f, 'r', encoding = 'UTF-8') as file:
		json_str = file.read()
		return json.loads(json_str)
def write_json(f, data): # Write data into JSON file
	with open(f, 'w', encoding = 'UTF-8') as file:
		json.dump(data, file, ensure_ascii=False, indent='\t')
def cfg_ok(f): # 若配置文件异常则返回False
	try:
		ok_ct, tot_ct, cfg, items = 0, 0, read_json(f), ['info', 'bdir', 'head', 'form', 'path']
		for c in cfg:
			for i in items:
				try:
					if cfg[c][i]: ok_ct += 1
				except: print(f'{f}: [{c}][{i}]缺失！')
			tot_ct += len(items)
		if ok_ct == tot_ct: return True
		else: return False
	except: return False
def is_mcworld(path):
	err_num, required_files = 0, ['levelname.txt', 'level.dat', 'level.dat_old']
	for f in required_files:
		err_num += (not os.path.isfile(f'{path}\\{f}'))
	err_num += (not os.path.isdir(f'{path}\\db'))
	return (err_num == 0)
def get_folder_size(folder_path):
	total_size = 0
	for path, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(path, file)
			total_size += os.path.getsize(file_path)
	return total_size
# https://geek-docs.com/python/python-ask-answer/236_python_very_quickly_getting_total_size_of_folder.html
def bubble(arr):
	for i in range(1, len(arr)):
		for j in range(0, len(arr) - i):
			if arr[j] < arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
# https://www.runoob.com/w3cnote/bubble-sort.html

# comp('1.zip', getOjng(0))
# extr('1.zip', '.\\t')
# print(f'Release: {getOjng(0)}\nPreview: {getOjng(1)}')
# print(getTime(12))
# print(f'Width:  {temSize(0)}\nHeight: {temSize(1)}')
# cls()
# jsonData = readJSON('example_config.json')
# print(jsonData)
# writeJSON('test.json', jsonData)
# cfgOK('config.json')
# print(is_mcworld(f'{get_wrlz(1)}\\PDpWPodkHVA='))
# print(get_folder_size(f'{get_wrlz(1)}\\PDpWPodkHVA='))