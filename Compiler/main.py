import argparse

'''
Content principal compiler routines
'''
# todo make the compiler
# todo please use venv while make the compiler
def main():
    '''
    the principal routine
    :return: nothing
    :rtype: None
    '''
    # todo look for string split in multiline instructions and scape chars
    parser = argparse.ArgumentParser(description='get a cool script living in some path and return the \
                                        program\'s mips script')

    parser.add_argument('path', nargs=1, help='the cool script path')

    args = parser.parse_args()

    # make something with var(args)[path]
    print(vars(args)['path'])

main()
