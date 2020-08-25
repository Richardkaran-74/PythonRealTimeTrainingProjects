
def main():
    #f = open('File text1.txt','w+')
    #f = open('File text1.txt','a')
    f = open('File text1.txt', 'r')

    #for i in range(10):
     #   f.write('This is line:'+str(i)+'\r\n')

    #f.close()
    if f.mode == 'r':
        contents = f.read()
    print(contents)



if __name__ == '__main__':
    main()
