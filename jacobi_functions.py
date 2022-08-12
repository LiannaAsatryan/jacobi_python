from matrix import *
EPSILION = 0.00001

#this function reads the matrix from the input file and returns the matrix object
def read_input():
    i_file = open("input.txt", 'r')
    input_list = i_file.read().split()
    m = matrix(int(input_list[0]))
    k = 1
    for i in range(m.get_rows()):
        for j in range(m.get_cols()):
            m.set(i, j, float(input_list[k]))
            k = k + 1
    i_file.close()
    return m

#this function reads data from the golden file
def read_golden():
    g_file = open("golden.txt", 'r')
    golden_list = g_file.read().split()
    g_file.close()
    return golden_list

def jacobi(m):
    if(m.diag_dominant == False):
        return None
    else:
        rows = m.get_rows()
        cols = rows + 1
        previous = []
        x = []
        for i in range(rows):
            x.append(0)
        converge = False
        while(converge == False):
            previous = x
            for i in range(rows):
                sum = 0
                for j in range(rows):
                    sum += m.get(i, j) * previous[j]
                sum -= (m.get(i, i) * previous[i])
                x[i] = (m.get(i, rows) - sum) / m.get(i, i)
            converge = True
            for i in range(rows):
                if(abs(x[i] - previous[i]) > EPSILION):
                    converge = false
                    break
        return x


#this function writes the given list or a message into the output file
def write_in_file(list_name):
    o_file = open("output.txt", 'w')
    if(check_input()):
        if(list_name == None):
            o_file.write("no dominant")
        else:
            for item in list_name:
                item = float("{0:.7f}".format(item))
                o_file.write(str(item))
                if(item != list_name[len(list_name)-1]):
                    o_file.write(' ')
    else:
        o_file.write("wrong imput")
    o_file.close()

#this function compares two lists and returns true if they are similiar
def cmp_lists(list1, list2):
    if(len(list1) != len(list2)):
        return False
    for i in range(len(list1)):
        if( float("{0:.5f}".format(float(list1[i]))) !=  float("{0:.5f}".format(float(list2[i])))):
            return False
    return True

#this function checks a string is a float number
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#this function returns true if the input is accurate, and returns false otherwise
def check_input():
    i_file = open("input.txt", 'r')
    input_list = i_file.read().split()
    if(input_list[0].isdigit() == False):
        i_file.close()
        return False
    if(len(input_list) != int(input_list[0]) * (int(input_list[0])+1)+1):
        i_file.close()
        return False
    for i in range(len(input_list)):
        if(isfloat(input_list[i]) == False):
            i_file.close()
            return False
    i_file.close()
    return True


