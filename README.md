


# Documentation

```
from unsigned import Unsigned32
a = Unsigned32(-1)
b = Unsigned32(0xffffffff)

assert a == b

a.sub(b)
a.add(b)
a.ror(2)
a.rol(3)
a.or_op(b)
a.not_op()
a.and_op(b)
a.neg()
a.xor(b)
a.shl(2)
a.shr(3)

assert a.hex() == '0x1fffffff'
assert a() == 0x1fffffff
```

```
from unsigned import Signed16
a = Signed16(-1)
b = Signed16(0xffff)

assert a == b

a.sub(b)
a.add(b)
a.ror(2)
a.rol(3)
a.or_op(b)
a.not_op()
a.and_op(b)
a.neg()
a.xor(b)
a.shl(2)
a.shr(3)

assert a.hex() == '-0x1'
```

