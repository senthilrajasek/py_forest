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
    def example_function():
        return "This is an example function."

def main():
    print ExampleClass.config_data
    print ExampleClass.example_function 
    print ExampleClass.__doc__
    print ExampleClass.config_data['db_host']


if __name__ == '__main__':
    sys.exit( main() )

