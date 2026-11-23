import json
src=json.load(open("config_lite.json",encoding="utf-8"))
out={
  "spider": "",
  "sites": [s for s in src["sites"] if str(s.get("type"))=="1"],
  "parses": [],
  "lives": [
    {"name":"电视狗","type":0,"url":"https://zb.7778.uk/starlink.m3u","epg":""},
    {"name":"电视狗","type":0,"url":"https://zb.7778.uk","epg":""}
  ]
}
json.dump(out,open("config_clean_nojar.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("config_clean_nojar.json  sites=%d lives=%d spider=%r"%(len(out["sites"]),len(out["lives"]),out["spider"]))
print("站点:", ", ".join(s["name"] for s in out["sites"]))
