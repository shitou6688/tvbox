import json, glob, os

rows = []
for f in sorted(glob.glob("*.json")):
    try:
        j = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    sp = str(j.get("spider", "") or "")
    sites = j.get("sites", []) or []
    popup = any("popup.jar" in str(s.get("jar", "")) for s in sites)
    if not sp:
        tag = "空 -> 不加载 jar"
    elif "new.jar" in sp and "modelscope" in sp:
        tag = "new.jar(魔搭)"
    elif "new.jar" in sp and "github" in sp:
        tag = "new.jar(GitHub)"
    elif "new.jar" in sp:
        tag = "new.jar(Gitee)"
    else:
        tag = sp[:34]
    rows.append((f, len(sites), tag, "有" if popup else "无"))

w = max(len(r[0]) for r in rows) if rows else 10
print("%-*s %6s  %-22s %s" % (w, "文件", "站点", "spider", "popup.jar"))
print("-" * (w + 45))
for r in rows:
    print("%-*s %6d  %-22s %s" % (w, r[0], r[1], r[2], r[3]))
