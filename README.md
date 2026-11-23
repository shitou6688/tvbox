# 影视仓 干净接口（去卡密）

本仓库是影视仓 / TVBox 的接口配置，**不含任何卡密激活弹窗插件**，直接导入即可用。

## 直接导入的地址

优先用 jsDelivr（国内访问稳定，有 CDN 加速）：

| 版本 | 地址 | 说明 |
|---|---|---|
| **完整版** | `https://cdn.jsdelivr.net/gh/shitou6688/tvbox@main/config.json` | 51 站（23 采集 + 28 插件）+ 3 直播 |
| 精简版 | `https://cdn.jsdelivr.net/gh/shitou6688/tvbox@main/config_lite.json` | 21 个采集站，最省资源 |
| 直播版 | `https://cdn.jsdelivr.net/gh/shitou6688/tvbox@main/config_zb.json` | 完整版 + 2.3 万频道综合直播源 |
| 测试版 | `https://cdn.jsdelivr.net/gh/shitou6688/tvbox@main/config_test.json` | 仅 3 站，用于排查启动卡顿 |

GitHub 原生 raw（国内可能需要代理）：

```
https://raw.githubusercontent.com/shitou6688/tvbox/main/config.json
```

## 各文件说明

| 文件 | 站点数 | 说明 |
|---|---|---|
| `config.json` | 51 | 主配置。23 个 CMS 采集站 + 28 个 csp 插件站，全部实测可达 |
| `config_lite.json` | 21 | 只保留纯接口采集站，无插件依赖，启动最快 |
| `config_zb.json` | 51 + 直播 | 额外挂载 2.3 万频道的综合直播源（`zb.txt` 镜像） |
| `config_test.json` | 3 | 最小配置，用来判断"转圈"是配置问题还是播放器问题 |

## 关于卡密弹窗

原接口（`http://47.96.82.41:5188/config.json`）的第一个站点挂了一个插件包：

```json
"jar": "https://gitee.com/starlinkapi/pan/raw/master/jar/popup.jar?v=25"
```

该插件内含 `com.wb.popup.Popup` 类，会请求卡密服务器 `124.71.19.220` 并在启动时弹出
"请先进行接口验证 / 微信小程序获取验证码"的窗口。本仓库所有配置均已移除该插件，
主 spider（`new.jar`）中也不含此类。

## spider 说明

默认指向作者原 jar：

```
https://gitee.com/starlinkapi/jar/raw/master/jar/new.jar
```

如需完全自主，可改用本仓库备份的 `jar/new.jar`：

```
https://cdn.jsdelivr.net/gh/shitou6688/tvbox@main/jar/new.jar
```

修改 `config.json` 顶部的 `"spider"` 字段即可。注意：28 个 `csp_` 插件站依赖这个 jar，
删掉 `spider` 会导致这些站点全部失效。

## 导入步骤

1. 影视仓 → 设置（齿轮）→ 配置地址
2. 清空原地址，粘贴上表中的链接
3. 确定 → 回首页 → 右上角「清空缓存 / 重新加载配置」
4. 若旧配置仍然生效，先「恢复默认」一次再重新填入

## 常见问题

**启动一直转圈，按返回键出现"跳过loading"**
通常是某个站点接口超时导致首页汇总加载挂住。本仓库已剔除实测死链
（`dbzy.tv`、`apibdzy.com`、`wwzy.tv`、`wolongzyw.com`），并移除了 1.4 MB 的壁纸接口。
若仍出现，请用 `config_test.json` 测试：若最小配置也转圈，则问题在播放器或网络，
与配置内容无关。

**插件站点（热播、韩圈、哔哩等）打不开**
这些站依赖 `spider` 指向的 `new.jar`。若 jar 地址失效，换成本仓库那份备份即可。
