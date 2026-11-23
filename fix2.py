import json
KEEP="http://118.89.172.248:8025/jar/zb.php"
f="config_clean_nojar.json"
j=json.load(open(f,encoding="utf-8"))
print("原 lives:",[l["name"] for l in j.get("lives",[])])
j["lives"]=[{"name":"平台直播","type":0,"url":KEEP,"epg":""}]
json.dump(j,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("新 lives:",[l["name"] for l in j["lives"]])
print()
for x in ("config_ultra.json","config_master.json","config_clean_nojar.json"):
    k=json.load(open(x,encoding="utf-8"))
    print("%-26s sites=%-3d lives=%d %s" % (x,len(k["sites"]),len(k["lives"]),[l["name"] for l in k["lives"]]))
