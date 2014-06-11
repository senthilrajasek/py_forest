import sys

def main():
    PROJECT_CONFIG = {
            'url' : 'http://www.python.org',
            'port' : '80',
            'dataset' : 'california_dataset'
            }
    for k in PROJECT_CONFIG:
        print "{0} : {1} ".format(k, PROJECT_CONFIG[k])

if __name__ == '__main__':
    sys.exit( main() )
