def encode(m, s):
    table = []
    stringtable = ""
    tls = []
    stringtable = s
    for i in range(5):
        table.append([])
        for e in range(5):
            table[i].append(stringtable[e + i * 5])
    i = 1
    try:
        while(i < len(m)):
            tls.append([m[i-1],m[i]])
            i+=2
    except:
        return("your string must be an even number of characters")
    table.append(table[0])
    print(table)
    colum0 = -500
    colum1 = 500
    r0w = -500
    r1w = 500
    for i in range(len(tls)):
        if tls[i][0] == tls[i][1]:
            tls[i][1] == "X"
        else:
            boolean = True
            for row in range(5):
                if table[row].count(tls[i][0]) == 1 and table[row].count(tls[i][1]) == 1 and boolean:
                    print('rows same')
                    tls[i][0] = table[row + 1][table[row].index(tls[i][0])]
                    tls[i][1] = table[row + 1][table[row].index(tls[i][1])]
                    print(tls[i])
                    boolean = False
                else:
                    for column in range(5):
                        if table[row][column] == tls[i][0]:
                            colum0 = column
                            r0w = row
                        if table[row][column] == tls[i][1]:
                            colum1 = column
                            r1w = row
# check this part because it's in the for statement make sure it makes sense
                        if colum0 == colum1 and boolean:
                            print('columns same')
                            boolean = False
                            tls[i][0] = table[r0w][(colum0 + 1) % 5]
                            tls[i][1] = table[r1w][(colum1 + 1) % 5]
                            print(tls[i])
            if colum1 != colum0 and boolean:
                print(colum1, " and ", colum0)
                tls[i][0] = table[r0w][colum1]
                tls[i][1] = table[r1w][colum0]
                print(tls[i], "step 3", table[r0w][colum1], table[r1w][colum0], "\n")
    finalstwing = ""
    for i in range(len(tls)):
        finalstwing += ''.join(tls[i])
        print('--' + finalstwing)
    return(finalstwing)
def decode(m, s):
    table = []
    stringtable = ""
    tls = []
    stringtable = s
    for i in range(5):
        table.append([])
        for e in range(5):
            table[i].append(stringtable[e + i * 5])
    i = 1
    try:
        while(i < len(m)):
            tls.append([m[i-1],m[i]])
            i+=2
    except:
        return("your string must be an even number of characters")
    table.append(table[0])
    print(table)
    for i in range(len(tls)):
        colum0 = -500
        colum1 = 500
        r0w = -500
        r1w = 500
        boolean = True
        for row in range(5):
            if table[row].count(tls[i][0]) == 1 and table[row].count(tls[i][1]) == 1 and boolean:
                print('rows same')
                tls[i][0] = table[row - 1][table[row].index(tls[i][0])]
                tls[i][1] = table[row - 1][table[row].index(tls[i][1])]
                print(tls[i])
                boolean = False
            else:
                for column in range(5):
                    if table[row][column] == tls[i][0]:
                        colum0 = column
                        r0w = row
                        print(tls[i][0], ' ', r0w, ' ', colum0)
                    if table[row][column] == tls[i][1]:
                        colum1 = column
                        r1w = row
                        print(tls[i][1], ' ', r1w, ' ', colum1)
# check this part because it's in the for statement make sure it makes sense
                    if colum0 == colum1 and boolean:
                        print('columns same ', tls[i], 'column0, 1 == ', colum0, ' ', colum1)
                        boolean = False
                        tls[i][0] = table[r0w][(colum0 - 1)]
                        tls[i][1] = table[r1w][(colum1 - 1)]
                        print(tls[i])
        if colum1 != colum0 and boolean:
            print(colum1, " and ", colum0)
            tls[i][0] = table[r0w][colum1]
            tls[i][1] = table[r1w][colum0]
            print(tls[i], "step 3", table[r0w][colum1], table[r1w][colum0], "\n")
    finalstwing = ""
    for i in range(len(tls)):
        finalstwing += ''.join(tls[i])
        print('--' + finalstwing)
    return(finalstwing)
"""
def samerowencode(letters):
    for i in range(5):
        if table[i].count(letters[0]) == 1 and table[i].count(letters[1]) == 1:
            return(table[i].index(
                
                
def samerowdecode(letters):
"""
