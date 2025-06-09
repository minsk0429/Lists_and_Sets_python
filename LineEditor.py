from ArrayList import ArrayList

list = ArrayList()
while True:
    command = input("[Select Menu] i-insert, d-delete, r-revision, p-print, l-load, s-save, q-quit=> ")

    if command == 'i':
        pos = int(input("Input line number: "))
        str = input("Input line content: ")
        list.insert(pos, str)

    elif command == 'd':
        pos = int(input("Delete line number: "))
        list.delete(pos)

    elif command == 'r':
        pos = int(input("Revision line number: "))
        str = input("Revision line content: ");
        list.replace(pos, str)

    elif command == 'p':
        print('Line Editor')
        for line in range(list.size):
            print('[%2d]'%line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q' : exit()

    elif command == 'l':
        filename = 'test.txt'
        infile = open(filename, 'r')
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's':
        filename = 'test.txt'
        outfile = open(filename, 'w')
        len = list.size
        for i in range(len):
            outfile.write(list.getEntry(i) + '\n')
        outfile.close()