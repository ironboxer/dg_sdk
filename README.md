# dg_sdk

dg_sdk upgrade crypto to pycryptodomex

### install

```bash
pip3 install -r requirements.txt
```

### demo

```bash
pip install git+https://github.com/ironboxer/dg_sdk

export $(xargs < .env)

python3 demo.py
```

### comment

假如你有以下代码

```Python
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
```

pycrypto vs pycryptodome vs pycryptodomex

1. pycrypto 是一个老版本, 已不再维护.
2. pycryptodome 是最新的版本, 可以看作 pycrypto 的"平替".
3. "平替" 的意思是将 pycrypto 替换为 pycryptodome 的时候, "几乎"一行代码都不用改.
4. 只需要把之前的 pycrypto 彻底删除干净, 然后重装 pycryptodome 即可.
5. 但现实世界并没有这么美好, 总是有些特殊处理的地方.
6. 需要特殊处理的地方在这: https://www.pycryptodome.org/src/vs_pycrypto
7. 如果你的项目不幸需要特殊处理, 维护起来会非常麻烦. 各种兼容性问题非常棘手.
8. pycryptodome 的作者 Legrandin 也意识到了这一点, 所以推出了 pycryptodomex .
9. pycryptodomex 可以看作是 pycryptodome 的"平替".
10. 他强制要求你使用 Cryptodome 开头, 上面的代码需要修改为以下的形式.
```Python
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
```
11.  你只需要安装 pycryptodomex 这一个库即可, 其余两个都删除了吧.
12. import this
13. "Explicit is better than implicit."
