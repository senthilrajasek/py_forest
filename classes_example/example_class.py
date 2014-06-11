import sys

class ExampleClass:
    """An example class"""
    config_data = { "url" : "http://www.python.org",
            "port" : "8080",
            "db_host" : "localdb.abccorp.net",
            "db_port" : "143",
            "db_user" : "reader",
            "db_password" : "reader"
            }

    def __init__(self, db_host):
        if db_host:
            self.config_data['db_host'] = db_host

    def example_function( self ):
        return "This is an example function."

def main():
    print ExampleClass.config_data
    print ExampleClass.__doc__
    print ExampleClass.config_data['db_host']
    print ExampleClass('localdb2.abccorp.net').config_data['db_host']
    print ExampleClass.config_data['db_host']
    print ExampleClass.example_function 
    print ExampleClass(None).example_function


if __name__ == '__main__':
    sys.exit( main() )

