def swapFileData():
    file1 = input("Name of the first file")
    file2 = input("Name of the second file")
    
    data_a = open(file1, 'r')
    data_a_read = data_a.read()
    
    data_b = open(file2, 'r')
    data_b_read = data_b.read()

    data_a_write = open(file1, 'w')
    data_a_write.write(data_b_read)

    data_b_write = open(file2, 'w')
    data_b_write.write(data_a_read)

swapFileData()
    
