#import the class we want to inheritate from
from chef import Chef

#create the new class calling the father class
class ChineseChef(Chef):

    def make_fried_rice(self):
        print ("The chef makes fried rice")

    #overwrite the inheritated function to change it!!
    def make_special_dish(self):
        print ("The chef makes orange chiken")