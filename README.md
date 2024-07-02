# gameDataMgr

## 简介

- 简易游戏数据管理程序
- 适用于MCBE的`com.mojang`、PVZ杂交版的`yourdata`等，支持自定义目录
- 使用7-Zip实现基本压缩解压操作

## 功能

- 读取配置文件：每一个游戏（备份项目）的：
  - 名称
  - 备份文件名开头
  - 原目录
  - 备份目录
  - 压缩格式（zip或7z等）
- 打开指定目录
- 备份指定目录
- 还原指定目录
- 记录操作日志
- 列出备份列表