 # -*- coding: utf-8 -*-
"""CMPSC132 - Homework 1.py

I have included that code snippets for the <a href= "https://runestone.academy/runestone/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html">PSADS book below</a>. You need to extend the code in order to meet the criteria listed at the end of the chapter.
"""
def gcd(m, n):
      while m % n != 0:
        m, n = n, m % n
      return n
  
def int_to_fraction(x):
  if type(x) == int:
    return Fraction(x, 1)
  elif type(x) == Fraction:
    return x
  else:
    raise TypeError("Must be an int/Fraction")

class Fraction:
    def __init__(self, top, bottom):
        cmmn = gcd(top, bottom)
        self.num = top // cmmn
        self.den = bottom // cmmn
        

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)


  
    def __sub__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den \
        - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    def __gt__(self, other_fraction):
      return (self.num * other_fraction.den > other_fraction.num * self.den)

    def __ge__(self, other_fraction):
      return (self.num * other_fraction.den >= other_fraction.num * self.den)

    def __lt__(self, other_fraction):
      return (self.num * other_fraction.den < other_fraction.num * self.den)

    def __le__(self, other_fraction):
      return (self.num * other_fraction.den <= other_fraction.num * self.den)

    def __ne__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num != second_num

    def __repr__(self):
      return self.__str__()

    def __radd__(self, left):
      """
      print(f"self: {self}")
      print(f"left: {left}")
      """
      return self + left
      #return None
      
    def __repr__(self):
      return self.__str__()

    def get_num(self):
      return self.num
    def get_den(self):
      return self.den
      
    def show(self):
        print(self.__str__())

x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2, 3)
print(x + y)
assert x + y == Fraction(7,6)
print(x == y)

"""# COMPLETE THE FRACTION CLASS
<a href= "https://runestone.academy/runestone/books/published/pythonds3/Introduction/Exercises.html"> You can also find these questions in the book. </a><br>
1. Implement the simple methods get\\_num and get\\_den that will return the numerator and denominator of a fraction.

2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the \\_\\_add\\_\\_ function no longer needs to reduce. Make the necessary modifications.

3. Implement the remaining simple arithmetic operators (\\_\\_sub\\_\\_, \\_\\_mul\\_\\_, and \\_\\_truediv\\_\\_).

4. Implement the remaining relational operators (\\_\\_gt\\_\\_, \\_\\_ge\\_\\_, \\_\\_lt\\_\\_, \\_\\_le\\_\\_, and \\_\\_ne\\_\\_).

5. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer, the constructor should raise an exception.

6. In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.

7. Research the \\_\\_radd\\_\\_ method. How does it differ from \\_\\_add\\_\\_? When is it used? Implement \\_\\_radd\\_\\_.

8. Repeat the last question but this time consider the \\_\\_iadd\\_\\_ method.

9. Research the \\_\\_repr\\_\\_ method. How does it differ from \\_\\_str\\_\\_? When is it used? Implement \\_\\_repr\\_\\_.
"""

#Test 1
x.get_num()
assert x.get_num() == 1
y.get_den()
assert y.get_den() == 3

# Test 2
z = Fraction(3,6)
print(z)  #should be 1/2
assert z == Fraction(1,2)

# Test 3
# __sub__
z = x-y
print(z)
assert z == Fraction(-1,6)
# __mul__
z = x*y
print(z)
assert z == Fraction(1,3)
# __truediv__
# from __future__ import division  #this might need to be imported
z = x/y
print(z)
assert z == Fraction(3,4)

# Test 4
# __gt__
assert (x > y) is False
# __ge__
assert (x >= y) is False
# __lt__
assert (x < y) is True
# __le__
assert (x <= y) is True
# __ne__
assert (x != y) is True

#Test 5
try:
    alpha = Fraction(1.2,2.2)
except:
    print('that doesn\'t work!')

#Test 6
beta = Fraction(3, -5)
print(beta)
print(beta.get_num())
print(beta.get_den())
assert beta == Fraction(-3, 5)

#Test 7 radd
print(x + 1)
print(1 + x)
assert (x + 1) == Fraction(3,2)
assert (1 + x) == Fraction(3,2)

#Test 8 iadd
for i in range(y.get_den()):
    x += i
    print(x)
assert x ==  Fraction(7,2)


"""# LOGIC GATE PROBLEM
Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy. How much additional coding did you need to do?

The most simple arithmetic circuit is known as the half adder. Research the simple half-adder circuit. Implement this circuit.

Now extend that circuit and implement an 8-bit full adder."""

#

''''

#class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


#class BinaryGate(LogicGate):

    def __init__(self,n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


#class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        # a = self.getPinA()
        # b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

#class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        #a = self.getPinA()
        #b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

#class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


#class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

#class XORGate(BinaryGate): 
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    def performGateLogic(self):
      #return self.pinA ^ self.pinB
      return(self.pinA and not self.pinB) or (not (self.pinA and self.pinB))  


#class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def __init__(self, lbl):
        self.name = lbl
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

'''
class LogicGate:

    def __init__(self, lbl):
        self.name = lbl
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, lbl):
        super(BinaryGate, self).__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    #Programmatically set value
    def set_a(self,a):
        self.pin_a = a
    def set_b(self,b):
        self.pin_b = b
    #Grab values from the user
    def set_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter pin A input for gate " + self.get_label() + ": "))
    def set_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter pin B input for gate " + self.get_label() + ": "))
    # Call to set both pins with user data
    def set_pins(self):
        self.pin_a = self.set_pin_a()
        self.pin_b = self.set_pin_b()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
    
    def get_pin_a(self):
        return self.pin_a
    
    def get_pin_b(self):
        return self.pin_b


class ANDGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        assert self.pin_a != () and self.pin_b != ()
        return((self.pin_a and self.pin_b))  

class ORGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class XORGate(BinaryGate): 
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        return((self.pin_a or self.pin_b) and not(self.pin_a and self.pin_b))  

class UnaryGate(LogicGate):

    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin
            

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NOTGate(UnaryGate):

    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class NANDGate(ANDGate):
    
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class NORGate(ORGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(fgate.get_output())

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def adder(a,b,c=0):
  #define all gates
  xor1= XORGate("xor1")
  xor2= XORGate("xor2")
  and1= ANDGate("and1")
  and2= ANDGate("and2")
  or1= ORGate("or1")
  # set all input values
  xor1.pin_a = a
  xor1.pin_b = b  
  and2.pin_a = a
  and2.pin_b = b
  and1.pin_b = c
  xor2.pin_b = c
  #now set the connectors
  ca = Connector(xor1, xor2)
  cb = Connector(xor1, and1)
  
  cc = Connector(and1, or1)
  cd = Connector(and2, or1)
  
  #NATE: Make sure the outputs are correct to match the schematic
  # https://en.wikipedia.org/wiki/Adder_(electronics)
  return int(or1.perform_gate_logic()), int(xor2.perform_gate_logic())
 
#testing loop     
#single full adder
##Testing Loop
c= 0
for a in [0,1]:
  for b in [0,1]:
    carry,s = adder(a,b,c)
    print(a,b,carry,s)

c= 0
for a in [1,10]:
  for b in [1,10]:
    carry,s = adder(a,b,c)
    print(a,b,carry,s)
    
def one_bit_adder_tests():
  """

When you run this function, the output should look similar to below. 

  0 + 0 = 0 1
  0 + 1 = 0 1
  1 + 0 = 0 1
  1 + 1 = 1 0
  """
  c = 0
  for a in [0,1]:
    for b in [0,1]:
      c, s = adder(a,b,c)
      print(f"{a}+{b} = {c}{s}")
  return None

one_bit_adder_tests()
  
def eight_bit_adder(a, b, c = 0):

    total = []

    reversed_a = list(reversed(a))

    reversed_b = list(reversed(b))

    for i in range(8):

        c, s = adder(int(reversed_a[i]), int(reversed_b[i]), c)

        total.insert(0, s)

    return c, total




def nth_bit_adder(a, b, c = 0):

    total = []

    last = len(a)

    reversed_a = list(reversed(a))

    reversed_b = list(reversed(b))

    for i in range(last):

        c, s = adder(int(reversed_a[i]), int(reversed_b[i]), c)

        total.insert(0, s)

    return c, total






input1 = "10101010"

input2 = "01010101"

output = eight_bit_adder(input1, input2)

print(output)


input1 = "00000001"

input2 = "01111111"

output = eight_bit_adder(input1, input2)

print(output)
    
#g1 = AndGate("G1")
#g2 = AndGate("G2")
#g3 = OrGate("G3")
#g4 = NotGate("G4")
#c1 = Connector(g1,g3)
#c2 = Connector(g2,g3)
#c3 = Connector(g3,g4)
#print(g4.getOutput())



"""
Write test cases for adding together a one-bit number, repeat for two-bit numbers. 
How do you expand this adding to be used for n-bits? 
"""

"A: If adding based on the length of the number you should be able to go to the nth as long as both numbers are the same size. "
