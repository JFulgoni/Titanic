import data_helper
__author__ = 'johnfulgoni'

def main():
    header, data = data_helper.get_train()
    print header
    print data[0]

if __name__=="__main__":
    main()