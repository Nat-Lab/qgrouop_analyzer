### qgroup-analyzer ###
---

`qgroup-analyzer` is a simple tool written in BaSH helps you analyze your QQ groups. It requires [jq](https://stedolan.github.io/jq/) to run.

### How to use? ###

You will need to dump your groups infomation first. To do this, log in to [QQ Groups's Website](http://qun.qq.com), then navigate to [member management page](http://qun.qq.com/member.html). Open developer console, Get cookie by doing `alert(document.cookie)`, for bkn, you can get it by pasting following code into console:

```javascript
for (var e = $.cookie("skey"), t = 5381, n = 0, o = e.length; o > n; ++n) t += (t << 5) + e.charAt(n).charCodeAt(); 
alert(2147483647 & t);
```

Once you obtained the cookie and bkn, do: 

```
$ export COOKIE=".... your cookie ...." 
$ export bkn="... your bkn ..."
$ ./qgroup_info_dump
```

And now the script will dump all your groups informations. When dump finished, you should get:

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

You can now play it with `qgroup_analyzer`. As you hava got all JSON data, you can also do your own analysis.

### License ###

MIT License
