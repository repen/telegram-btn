"""
This program is dedicated to the public domain under the CC0 license.
"""
import re

class Controller:
    def __init__(self):
        pass

    def __route(self, command):
        model = Models()
        func = model.get_model( command )
        message = func()
        return message

    def route(self, command):
        message = self.__route( command )
        return message


    def __controller(self):
        pass    

    def controller(self):
        self.__controller()


class Models:
    def __init__(self):
        self.models = {}
        self.methods =  [ x.replace("_", "") for x in dir( self ) if re.search(r"^_[^_]", x) ]

    def _menu(self):
        return ("Main menu", [self.methods] )

    def _about(self):
        return ("[text](http://example.com) \nAbout info", [ self.methods ])

    def _contact(self):
        return ("Contact info", [ self.methods ])

    def _home(self):

        return ("Home info", [ self.methods, ["Menu"] ])

    def _map(self):
        return ("google map", [ self.methods ])

    def get_model(self, route):
        result = lambda : ("", [ self.methods ]) 
        if route in self.methods:
           result = getattr( self, "_" + route )
        
        return result

if __name__ == '__main__':
    controller = Controller()
    text, menu = controller.route("about")
