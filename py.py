# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------



# first import the method ABCmeta and abstractclassmethod 

from abc import ABCMeta ,abstractclassmethod



class lang(metaclass= ABCMeta): # using ABCmeta in the class


    @abstractclassmethod #using the abstractclassmethod in the def in the class 
    def lang_name(self):

        pass

    @abstractclassmethod
    def lang_opp(self):

        pass

    ### new we have to function must add for any method in class or any class inheritance the ABCmeta class

class python(lang):

    def lang_name(self):

        return f"- python -"


    def lang_opp(self):

        return f"- yes -"
    

class java(lang):

    def lang_name(self):

        return f"- java -"


    def lang_opp(self):

        return f"- no -"
    
one = java()

print(one.lang_name())


print(one.lang_opp())


## what happend if lang_opp in jave ?

## there is error gone output for => TypeError: Can't instantiate abstract class java with abstract method lang_opp