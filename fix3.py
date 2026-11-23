import json
KEEP="http://118.89.172.248:8025/jar/zb.php"
for f in ("config_ultra.json","config_master.json","config_clean_nojar.json"):
    j=json.load(open(f,encoding="utf-8"))
    old=[l.get("name") for l in j.get("lives",[])]
    j["lives"]=[{"name":"平台直播","type":0,"url":KEEP,"epg":""}]
    json.dump(j,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print("%-26s lives %s -> ['平台直播']" % (f, old))
print()
for f in ("config_ultra.json","config_master.json","config_clean_nojar.json"):
    j=json.load(open(f,encoding="utf-8"))
    print("%-26s sites=%-3d lives=%d %s" % (f,len(j["sites"]),len(j["lives"]),[l["name"] for l in j["lives"]]))
