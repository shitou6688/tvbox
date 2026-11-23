import json
base=json.load(open("config.json",encoding="utf-8"))

a=dict(base); a["spider"]="https://raw.githubusercontent.com/shitou6688/tvbox/main/jar/new.jar"
json.dump(a,open("config_jar_gh.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)

b=dict(base); b["spider"]="https://www.modelscope.cn/datasets/qwer1234561476/jumo/resolve/master/new.jar"
json.dump(b,open("config_jar_ms.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("ok")
