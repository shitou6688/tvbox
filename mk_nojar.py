import json, collections
j=json.load(open("config_lite.json",encoding="utf-8"))
# 只留 CMS 采集站，去掉 spider 与直播，用于判定启动等待来源
k={"spider":"", "sites":[s for s in j["sites"] if str(s.get("type"))=="1"], "parses":[], "lives":[]}
json.dump(k,open("config_nojar.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("config_nojar.json sites=",len(k["sites"]),"lives=",len(k["lives"]),"spider=",repr(k["spider"]))
