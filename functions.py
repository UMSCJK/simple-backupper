import os, time
def comp(f, d): os.system(f"7z a {f} \"{d}\\**\"") # 压缩
def extr(f, d): os.system(f"7z x {f} -o{d} -aoa") # 解压
def getOjng(v): return f"{os.environ.get("LocalAppData")}\\Packages\\Microsoft.Minecraft{["UWP", "WindowsBeta"][v]}_8wekyb3d8bbwe\\LocalState\\games\\com.mojang"
def getTime(d): return time.strftime("%Y%m%d%H%M%S")[0:d]
# comp("1.zip", getOjng(0))
# extr("1.zip", ".\\t")
# print(f"Release: {getOjng(0)}\nPreview: {getOjng(1)}")
# print(getTime(12))