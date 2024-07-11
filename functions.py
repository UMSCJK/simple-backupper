import os, time, json
def comp(f, d): os.system(f"7z a {f} \"{d}\\**\"") # Compress
def extr(f, d): os.system(f"7z x {f} -o{d} -aoa") # Extract
def getOjng(v): return f"{os.environ.get("LocalAppData")}\\Packages\\Microsoft.Minecraft{["UWP", "WindowsBeta"][v]}_8wekyb3d8bbwe\\LocalState\\games\\com.mojang"
def getTime(d): return time.strftime("%Y%m%d%H%M%S")[0:d]
def temSize(i): return [os.get_terminal_size().columns, os.get_terminal_size().lines][i]
def cls(): os.system('cls')
def folder(p): os.system(f'explorer {p}')
def readJSON(f): # Read & return JSON file data
	with open(f, "r", encoding="UTF-8") as file:
		json_str = file.read()
		return json.loads(json_str)
def writeJSON(f, data): # Write data into JSON file
	with open(f, "w", encoding="UTF-8") as file:
		json.dump(data, file, ensure_ascii=False, indent='\t')
def cfgOK(f): # 若配置文件异常则返回False
	try:
		okCt, totCt, cfg, items = 0, 0, readJSON(f), ['info', 'bdir', 'head', 'form', 'path']
		for c in cfg:
			for i in items:
				try:
					if cfg[c][i]: okCt += 1
				except: print(f'{f}: [{c}][{i}]缺失！')
			totCt += len(items)
		if okCt == totCt: return True
		else: return False
	except: return False
# comp("1.zip", getOjng(0))
# extr("1.zip", ".\\t")
# print(f"Release: {getOjng(0)}\nPreview: {getOjng(1)}")
# print(getTime(12))
# print(f'Width:  {temSize(0)}\nHeight: {temSize(1)}')
# cls()
# jsonData = readJSON("example_config.json")
# print(jsonData)
# writeJSON("test.json", jsonData)
# cfgOK('config.json')