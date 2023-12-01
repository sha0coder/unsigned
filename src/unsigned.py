
class Unsigned64:

    def __init__(self, val=0):
        self.val = self.__fix(val)

    def __fix(self, val):
        if val < 0:
            val += 2**64
        return val & 0xffffffffffffffff

    def sub(self, n):
        self.val = (self.val - n.val) & 0xffffffffffffffff

    def add(self, n):
        self.val = (self.val + n.val) & 0xffffffffffffffff

    def ror(self, n):
        n = n % 64 
        self.val = (self.val >> n | self.val << (64 - n)) & 0xffffffffffffffff

    def rol(self, n):
        n = n % 64 
        self.val = (self.val << n | self.val >> (64 - n)) & 0xffffffffffffffff

    def or_op(self, n):
        self.val = self.val | n.val

    def not_op(self):
        self.val = ~self.val & 0xffffffffffffffff

    def neg(self):
        self.val = (-self.val) & 0xffffffffffffffff

    def xor(self, n):
        self.val = self.val ^ n.val

    def and_op(self, n):
        self.val = self.val & n.val

    def shl(self, n): 
        self.val = (self.val << n) & 0xffffffffffffffff

    def shr(self, n): 
        self.val = (self.val >> n) & 0xffffffffffffffff

    def hex(self):
        return hex(self.val)

    def __eq__(self, n):
        return self.val == n.val

    def __str__(self):
        return str(self.val)



class Unsigned32:

    def __init__(self, val=0):
        self.val = self.__fix(val)

    def __fix(self, val):
        if val < 0:
            val += 2**32
        return val & 0xffffffff

    def sub(self, n):
        self.val = (self.val - n.val) & 0xffffffff

    def add(self, n):
        self.val = (self.val + n.val) & 0xffffffff

    def ror(self, n):
        n = n % 32 
        self.val = (self.val >> n | self.val << (32 - n)) & 0xffffffff

    def rol(self, n):
        n = n % 32 
        self.val = (self.val << n | self.val >> (32 - n)) & 0xffffffff

    def or_op(self, n):
        self.val = self.val | n.val

    def not_op(self):
        self.val = ~self.val & 0xffffffff

    def neg(self):
        self.val = (-self.val) & 0xffffffff

    def xor(self, n):
        self.val = self.val ^ n.val

    def and_op(self, n):
        self.val = self.val & n.val

    def shl(self, n): 
        self.val = (self.val << n) & 0xffffffff

    def shr(self, n): 
        self.val = (self.val >> n) & 0xffffffff

    def hex(self):
        return hex(self.val)

    def __eq__(self, n):
        return self.val == n.val

    def __str__(self):
        return str(self.val)


class Unsigned16:

    def __init__(self, val=0):
        self.val = self.__fix(val)

    def __fix(self, val):
        if val < 0:
            val += 2**16
        return val & 0xffff

    def sub(self, n):
        self.val = (self.val - n.val) & 0xffff

    def add(self, n):
        self.val = (self.val + n.val) & 0xffff

    def ror(self, n):
        n = n % 16 
        self.val = (self.val >> n | self.val << (16 - n)) & 0xffff

    def rol(self, n):
        n = n % 16 
        self.val = (self.val << n | self.val >> (16 - n)) & 0xffff

    def or_op(self, n):
        self.val = self.val | n.val

    def not_op(self):
        self.val = ~self.val & 0xffff

    def neg(self):
        self.val = (-self.val) & 0xffff

    def xor(self, n):
        self.val = self.val ^ n.val

    def and_op(self, n):
        self.val = self.val & n.val

    def shl(self, n): 
        self.val = (self.val << n) & 0xffff

    def shr(self, n): 
        self.val = (self.val >> n) & 0xffff

    def hex(self):
        return hex(self.val)

    def __eq__(self, n):
        return self.val == n.val

    def __str__(self):
        return str(self.val)


class Unsigned8:

    def __init__(self, val=0):
        self.val = self.__fix(val)

    def __fix(self, val):
        if val < 0:
            val += 2**8
        return val & 0xff

    def sub(self, n):
        self.val = (self.val - n.val) & 0xff

    def add(self, n):
        self.val = (self.val + n.val) & 0xff

    def ror(self, n):
        n = n % 8 
        self.val = (self.val >> n | self.val << (8 - n)) & 0xff

    def rol(self, n):
        n = n % 8 
        self.val = (self.val << n | self.val >> (8 - n)) & 0xff

    def or_op(self, n):
        self.val = self.val | n.val

    def not_op(self):
        self.val = ~self.val & 0xff

    def neg(self):
        self.val = (-self.val) & 0xff

    def xor(self, n):
        self.val = self.val ^ n.val

    def and_op(self, n):
        self.val = self.val & n.val

    def shl(self, n): 
        self.val = (self.val << n) & 0xff

    def shr(self, n): 
        self.val = (self.val >> n) & 0xff

    def hex(self):
        return hex(self.val)

    def __eq__(self, n):
        return self.val == n.val

    def __str__(self):
        return str(self.val)



class Signed32:

    def __init__(self, val=0):
        self.val = self.__fix(val)

    def __fix(self, val):
        val = val & 0xffffffff
        if val == 0x80000000:
            return val
        if val & 0x80000000:
            val -= 0x100000000
        return val

    def sub(self, n):
        self.val = self.__fix(self.val - n.val)

    def add(self, n):
        self.val = self.__fix(self.val + n.val)

    def ror(self, n):
        n = n % 32
        self.val = self.__fix((self.val & 0xffffffff) >> n | (self.val & 0xffffffff) << (32 - n))

    def rol(self, n):
        n = n % 32
        self.val = self.__fix((self.val << n) & 0xffffffff | (self.val >> (32 - n)))

    def or_op(self, n):
        self.val = self.__fix(self.val | n.val)

    def not_op(self):
        self.val = self.__fix(~self.val)

    def neg(self):
        self.val = self.__fix(-self.val)

    def xor(self, n):
        self.val = self.__fix(self.val ^ n.val)

    def and_op(self, n):
        self.val = self.__fix(self.val & n.val)

    def shl(self, n):
        self.val = self.__fix(self.val << n)

    def shr(self, n):
        self.val = self.__fix(self.val >> n)

    def hex(self):
        return hex(self.val)

    def __eq__(self, n):
        return self.val == n.val


class Signed64:

    def __init__(self, val=0):
        self.val = self.__fix(val)

    def __fix(self, val):
        val = val & 0xffffffffffffffff
        if val == 0x8000000000000000:
            return val
        if val & 0x8000000000000000:
            val -= 0x10000000000000000
        return val

    def sub(self, n):
        self.val = self.__fix(self.val - n.val)

    def add(self, n):
        self.val = self.__fix(self.val + n.val)

    def ror(self, n):
        n = n % 64
        self.val = self.__fix((self.val & 0xffffffffffffffff) >> n | (self.val & 0xffffffffffffffff) << (64 - n))

    def rol(self, n):
        n = n % 64
        self.val = self.__fix((self.val << n) & 0xffffffffffffffff | (self.val >> (64 - n)))

    def or_op(self, n):
        self.val = self.__fix(self.val | n.val)

    def not_op(self):
        self.val = self.__fix(~self.val)

    def neg(self):
        self.val = self.__fix(-self.val)

    def xor(self, n):
        self.val = self.__fix(self.val ^ n.val)

    def and_op(self, n):
        self.val = self.__fix(self.val & n.val)

    def shl(self, n):
        self.val = self.__fix(self.val << n)

    def shr(self, n):
        self.val = self.__fix(self.val >> n)

    def hex(self):
        return hex(self.val)

    def __eq__(self, n):
        return self.val == n.val

    def __str__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)


class Signed16:

    def __init__(self, val=0):
        self.val = self.__fix(val)

    def __fix(self, val):
        val = val & 0xffff
        if val == 0x8000:
            return val
        if val & 0x8000:
            val -= 0x10000
        return val

    def sub(self, n):
        self.val = self.__fix(self.val - n.val)

    def add(self, n):
        self.val = self.__fix(self.val + n.val)

    def ror(self, n):
        n = n % 16
        self.val = self.__fix((self.val & 0xffff) >> n | (self.val & 0xffff) << (16 - n))

    def rol(self, n):
        n = n % 16
        self.val = self.__fix((self.val << n) & 0xffff | (self.val >> (16 - n)))

    def or_op(self, n):
        self.val = self.__fix(self.val | n.val)

    def not_op(self):
        self.val = self.__fix(~self.val)

    def neg(self):
        self.val = self.__fix(-self.val)

    def xor(self, n):
        self.val = self.__fix(self.val ^ n.val)

    def and_op(self, n):
        self.val = self.__fix(self.val & n.val)

    def shl(self, n):
        self.val = self.__fix(self.val << n)

    def shr(self, n):
        self.val = self.__fix(self.val >> n)

    def hex(self):
        return hex(self.val)

    def __eq__(self, n):
        return self.val == n.val

    def __str__(self):
        return str(self.val)


class Signed8:

    def __init__(self, val=0):
        self.val = self.__fix(val)

    def __fix(self, val):
        val = val & 0xff
        if val == 0x80:
            return val
        if val & 0x80:
            val -= 0x100
        return val

    def sub(self, n):
        self.val = self.__fix(self.val - n.val)

    def add(self, n):
        self.val = self.__fix(self.val + n.val)

    def ror(self, n):
        n = n % 8
        self.val = self.__fix((self.val & 0xff) >> n | (self.val & 0xff) << (8 - n))

    def rol(self, n):
        n = n % 8
        self.val = self.__fix((self.val << n) & 0xff | (self.val >> (8 - n)))

    def or_op(self, n):
        self.val = self.__fix(self.val | n.val)

    def not_op(self):
        self.val = self.__fix(~self.val)

    def neg(self):
        self.val = self.__fix(-self.val)

    def xor(self, n):
        self.val = self.__fix(self.val ^ n.val)

    def and_op(self, n):
        self.val = self.__fix(self.val & n.val)

    def shl(self, n):
        self.val = self.__fix(self.val << n)

    def shr(self, n):
        self.val = self.__fix(self.val >> n)

    def hex(self):
        return hex(self.val)

    def __eq__(self, n):
        return self.val == n.val

    def __str__(self):
        return str(self.val)       



def tests():
    x = Unsigned32(0xffffffffffff)
    assert(x.hex() == '0xffffffff')

    x = Unsigned32(-2)
    assert(x.hex() == '0xfffffffe')

    a = Unsigned32(2)
    b = Unsigned32(0)
    b.sub(a)
    assert(b.hex() == '0xfffffffe')

    c = Unsigned32(0xfffffffe)
    assert(b == c)

    a = Unsigned32(1)
    b = Unsigned32(0xffffffff)

    b.add(a)
    assert(b.hex() == '0x0')

    assert Unsigned32(0xffffffffffff).hex() == '0xffffffff' 
    assert Unsigned32(-1).hex() == '0xffffffff' 
    assert Unsigned32(10).hex() == '0xa' 

    a = Unsigned32(1)
    b = Unsigned32(0xffffffff)
    b.add(a)
    assert b.hex() == '0x0'

    a = Unsigned32(2)
    b = Unsigned32(0)
    b.sub(a)
    assert b.hex() == '0xfffffffe'

    a = Unsigned32(0xf0f0f0f0)
    b = Unsigned32(0x0f0f0f0f)
    a.and_op(b)
    assert a.hex() == '0x0'

    a = Unsigned32(0xf0f0f0f0)
    b = Unsigned32(0x0f0f0f0f)
    a.or_op(b)
    assert a.hex() == '0xffffffff'

    a = Unsigned32(0xf0f0f0f0)
    a.not_op()
    assert a.hex() == '0xf0f0f0f'

    a = Unsigned32(1)
    a.shl(31)
    assert a.hex() == '0x80000000'

    a = Unsigned32(0x80000000)
    a.shr(31)
    assert a.hex() == '0x1'

    assert Signed32(0x7fffffff).hex() == '0x7fffffff' 
    assert Signed32(-0x80000000).hex() == '0x80000000'
    assert Signed32(10).hex() == '0xa' 
    assert Signed32(-10).hex() == '-0xa'

    a = Signed32(1)
    b = Signed32(0x7fffffff)
    b.add(a)
    assert b.hex() == '0x80000000'

    a = Signed32(1)
    b = Signed32(-0x80000000)
    b.sub(a)
    assert b.hex() == '0x7fffffff' 

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

    

tests()
