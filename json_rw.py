import json
def readJSON(f): # 读取JSON文件，返回文件数据
	with open(f, "r", encoding="UTF-8") as file:
		json_str = file.read()
		return json.loads(json_str)
def writeJSON(f, data): # 将指定数据写入指定JSON文件
	with open(f, "w", encoding="UTF-8") as file:
		json.dump(data, file, ensure_ascii=False, indent='\t')
jsonData = readJSON("example_config.json")
print(jsonData)
# writeJSON("test.json", jsonData)