"""
BONUS: Opening and writing to filesystem
"""
def filewrite(file_name):
    f = open(file_name, 'a')  # Open the file with name file_name in append mode
    f.write('This is a sentence that follows a new line\n This is another new line.')
    f.close()

def fileread(file_name):
    fw = open(file_name, 'r')
    lines = fw.readlines()
    for line in lines:
        print(line)
    fw.close()

if __name__ == '__main__':
    filewrite('sample.txt')

    fileread('sample.txt')
