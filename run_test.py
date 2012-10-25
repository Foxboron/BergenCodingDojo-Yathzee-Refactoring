import sys
import os
import nose

def main():
    sys.path.insert(0, os.path.dirname(os.getcwd()))
    nose.main()
    exit(0)

if __name__ == '__main__':
    main()
