### qgroup-analyzer ###
---

`qgroup-analyzer` 是使用 BaSH 寫成的一個 QQ 群組分析工具。它需要 [jq](https://stedolan.github.io/jq/) 來運行。

### 如何使用？ ###

在使用 `qgroup-analyzer` 前，妳需要先將 QQ 群組與好友數據匯出。使用 `qgroup_info_dump` 就能做到。`qgroup_info_dump` 會從環境變量中讀取 `COOKIE` 和 `bkn`。這些信息是登錄到 QQ API 所需要的憑據。若要獲取這些信息，登陸到[QQ 群](http://qun.qq.com)網站，訪問[成員管理](http://qun.qq.com/member.html)頁。在地址欄輸入 `javascript:alert(document.cookie)` 來獲取 `COOKIE`。在地址欄輸入 `javascript:for (var e = $.cookie("skey"), t = 5381, n = 0, o = e.length; o > n; ++n) t += (t << 5) + e.charAt(n).charCodeAt();alert(2147483647 & t);` 來獲取 `bkn`。

取得這些信息之後，就可以開始匯出數據了：

```
$ export COOKIE="...妳的 COOKIE..." 
$ export bkn="...妳的 bkn..."
$ ./qgroup_info_dump
```

如果一切順利，你會獲得這些 `JSON` 文件。

```
qgroup-analyzer
├── qgroup_analyzer
├── qgroup_info_dump
└── save
    ├── friends.json
    ├── groups
    │   ├── xxxx.json
    │   ├── xxxx.json
    │   ├── xxxx.json
    │   └── ....
    └── groups.json
```

`friends.json` 是妳好友的列表。

`groups.json` 是妳群組的列表。

`groups/%%%%.json` 是單個群組的詳細信息。包括成員、管理員、等級等數據。

現在，你可以使用 `qgroup_analyzer` 來分析妳的群組了，語法是：

```
./qgroup_analyzer <指令> [參數] [參數...]
```

可以使用的指令有（其中，`uin` 代表 QQ ID，`gid` 代表群組 ID。）：

`common_members <gid_a> <gid_b>` 列出在群組 `a` 和群組 `b` 內的共同成員。

`favorite_groups <uin>` 對用戶 `uin` 的群組等級積分進行排行。

`friends_common` 對好友依據他們與妳共同群組的數量進行排行。

`friends_in_group <gid>` 列出群組 `gid` 中的好友。`gid` 代表群組 ID。

`get_all_names <uin>` 列出 `uin` 全部名字。（全部群內的群名片。）

`get_joined <uin>` 列出 `uin` 所加入的群組。

`get_uin <nick/card>` 列出使用指定的群名片，或用戶名的用戶的 `uin`。

`joined_of_group <gid>` 列出 `gid` 的成員所加入的群。

`joined_of_firends` 列出所有好友加入的群。

`popular_groups` 依據群內好友數量，對群進行排行。

`potential_friends <n>` 列出共同群超過 `n` 個，但不是好友的使用者。

`prolog_export <output_filename> <own_uin>` 匯出數據到 `prolog` 文件。`output_filename` 代表要寫入的文件名，`own_uin` 代表自己的 `uin`。`prolog_export` 指令會匯出所有好友關係、群關係。它會使用如下的條件：`member(uin, gid).`，`friend(own_uin, uin).`。例如，要列出所有群之間的成員關係網，可以使用如下的指令：

```
? - member(X,Y),member(X,Z),not(Z==Y),not(X==own_uin).
X = a_uin_of_group_member, 
Y = a_gid_that_uin_joined, 
Z = another_gid_that_uin_joined ;
X = ..., 
Y = ..., 
Z = ... ;
```

`wolfram_graph <output_file> [source_gid <own_uin>]` 生成 wolfram 可以繪製的圖形。`output_file` 代表要寫入的文件名，`source_gid` 是可選參數，用於指定來源組。如果指定了 `source_gid`，則必須指定 `own_uin`（自己的 `uin`）。

在不限定來源 `gid` 時繪製的圖形：

![Sample Graph](https://raw.githubusercontent.com/Nat-Lab/qgrouop_analyzer/doc/sample_map.png)

### License ###

MIT License
