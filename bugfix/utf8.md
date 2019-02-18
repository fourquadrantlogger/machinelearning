
# bug
```
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 64: ordinal not in range(128)
```

# fix
```
import sys
reload(sys)
sys.setdefaultencoding('utf8')
```
