from tabulate import tabulate

# function of assigning the different names to each destination register 
def destAlloc(ARF, RRF, dest, srcRegister1, srcRegister2, operation):
    # first finding a non reused register in RRF 
    address = -1 
    for i in range(16):
        if(RRF[i][2] == 0):
            address = i 
            break  
    if address >= 0 :   
        #  according to the operation updating the value of register in Renamed register file 
        if operation == '+' :
            RRF[address][0]  = srcRegister1+ srcRegister2
        elif operation == '-' :
            RRF[address][0]  = srcRegister1- srcRegister2
        elif operation == '*' :
            RRF[address][0]  = srcRegister1* srcRegister2
        elif operation == '/' :
            RRF[address][0]  = srcRegister1 / srcRegister2   
        elif operation == '&' :
            RRF[address][0]  = srcRegister1 & srcRegister2   
        elif operation == '|' :
            RRF[address][0]  = srcRegister1 | srcRegister2   
        elif operation == '<<' :
            RRF[address][0]  = srcRegister1 << srcRegister2   
        elif operation == '>>' :
            RRF[address][0]  = srcRegister1 >> srcRegister2   
        elif operation == '>' :
            RRF[address][0]  = srcRegister1 > srcRegister2 
        elif operation == '<' :
            RRF[address][0]  = srcRegister1 < srcRegister2   
        elif operation == '^' :
            RRF[address][0]  = srcRegister1 ^ srcRegister2     
        # updating the valid and busy bit 
        RRF[address][2] = 1 
        RRF[address][1] = 1 
        # updating the  tag value in ARF 
        ARF[dest][2] = address 
        # updating the busy value of ARF 
        ARF[dest][1] = 1 

    else :
        print("none register is free")




# when all instruction completed then updating the register value in ARF from the RRF 
def registerUpdate(ARF, RRF):
    for i in range(16):
        # we have update the  value of only those register in ARF whose busy bit is 1 
        if ARF[i][1] == 1: 
            ARF[i][0] = RRF[ARF[i][2]][0] 
            # changing the busy bit in ARF 
            ARF[i][1] =  0 
            # chaning the busy bit in RRF 
            RRF[ARF[i][2]][2] = 0 # because this register is now free to use 
            # changing the valid bit into RRF
            RRF[ARF[i][2]][1] = 0  




# function of taking values of register from source 
def sourceOperandRead(ARF, RRF, source):
    if ARF[source][1] == 0 :
        # our operand is exist in ARF 
        return ARF[source][0]
    elif  ARF[source][1] == 1 :
        if RRF[ARF[source][2]][1] == 1 :
            # it means that valid bit is 1 so our operand exist in RRF 
            return   RRF[ARF[source][2]][0] 
        else :
            # previous instrcution is not executed, returning the address of that register 
            return ARF[source][2] 
        



# ARF = Architectural Register file 
ARF = []
# ARF have 3 columns 
# first column of ARF denotes the data of ith address register data  
# second column of ARF denotes the data of ith address is in the ARF or RRF 
# third column of ARF denotes the if the data of register in the RRF then which address this data exist 
# there are 16 register in ARF and RRF 
# intilizing the register starting values in ARF 
for i in range(16):
    row = []
    for j in range(3):
        if j==0 :
            row.append(i+j)
        else :
            row.append(0)
       
    ARF.append(row)


RRF = [] 
# RRF = Rename Register file 
# RRF also have three columns 
# first column of RRF denotes the data of ith address register data  (data)
# second column  of RRF denotes that value of data stored or not in this address (valid)
# third coloumn denotes that this register is already used or not (Busy)
for i in range(16):
    row = []
    for j in range(3):
        row.append(0)

    RRF.append(row)

#  printing starting  values  of register  files 
print("Initial values of Register files: ")
# display ARF and RRF as tables in parallel
headers_arf = ["Register-data", "busy", "Tag"]
headers_rrf = ["Register-data", "Valid", "Busy"]
table_arf = tabulate(ARF, headers=headers_arf, tablefmt="pretty", numalign="center")
table_rrf = tabulate(RRF, headers=headers_rrf, tablefmt="pretty", numalign="center")

# split the tables into rows and add a gap between columns
rows_arf = table_arf.split("\n")
rows_rrf = table_rrf.split("\n")
rows_combined = []
for i in range(len(rows_arf)):
    row_combined = rows_arf[i] + " " * 5 + rows_rrf[i]
    rows_combined.append(row_combined)

# print the combined table
print("\n".join(rows_combined))


# taking a example to show the code 
""" performing these three instruction 
R1, R2, R3  is register number 2nd, 3rd, 4th in ARF 
R1 <=  R2 +R3 
R3 <= R1 - R2 
R3 <= R2*R1 
"""
# by address taking source values from ARF using sourceOperandRead function 
# In first instruction R2 and R3 are source registers 
# so finding the values of R2 and R3 
R2 = sourceOperandRead(ARF, RRF, 2) 
R3 = sourceOperandRead(ARF, RRF, 3) 
# using the destAlloc function doing addition operation and updating values in Register-files 

destAlloc(ARF, RRF, 1, R2, R3, '+')
# printing register files after all three instruction is done 

print("Displaying the contents of the register files after completing the first instruction:")

# display ARF and RRF as tables in parallel
headers_arf = ["Register-data", "busy", "Tag"]
headers_rrf = ["Register-data", "Valid", "Busy"]
table_arf = tabulate(ARF, headers=headers_arf, tablefmt="pretty", numalign="center")
table_rrf = tabulate(RRF, headers=headers_rrf, tablefmt="pretty", numalign="center")

# split the tables into rows and add a gap between columns
rows_arf = table_arf.split("\n")
rows_rrf = table_rrf.split("\n")
rows_combined = []
for i in range(len(rows_arf)):
    row_combined = rows_arf[i] + " " * 5 + rows_rrf[i]
    rows_combined.append(row_combined)

# print the combined table
print("\n".join(rows_combined))


# finding the source register R1 and R2 for SUB instruction 
# by address taking source values from ARF using sourceOperandRead function 

R1 = sourceOperandRead(ARF, RRF, 1) 
R2 = sourceOperandRead(ARF, RRF, 2) 
# using the destAlloc function doing subtract operation and updating values in Register-files 

destAlloc(ARF, RRF, 3, R1, R2, '-')
# printing register files after all three instruction is done 

print("Displaying the contents of the register files after completing the first two instruction:")

# display ARF and RRF as tables in parallel
headers_arf = ["Register-data", "busy", "Tag"]
headers_rrf = ["Register-data", "Valid", "Busy"]
table_arf = tabulate(ARF, headers=headers_arf, tablefmt="pretty", numalign="center")
table_rrf = tabulate(RRF, headers=headers_rrf, tablefmt="pretty", numalign="center")

# split the tables into rows and add a gap between columns
rows_arf = table_arf.split("\n")
rows_rrf = table_rrf.split("\n")
rows_combined = []
for i in range(len(rows_arf)):
    row_combined = rows_arf[i] + " " * 5 + rows_rrf[i]
    rows_combined.append(row_combined)

# print the combined table
print("\n".join(rows_combined))



# finding the source register R2 and R3 for SUB instruction 
# finding values by address taking source values from ARF using sourceOperandRead function 

R1 = sourceOperandRead(ARF, RRF, 1) 
R2 = sourceOperandRead(ARF, RRF, 2) 
# using the destAlloc function doing multiplication operation and updating values in Register-files 

destAlloc(ARF, RRF, 3, R1, R2, '*')
# printing register files before updating  the  values  in ARF 
print("Displaying the contents of the register files after all instructions have finished:")
# display ARF and RRF as tables in parallel
headers_arf = ["Register-data", "busy", "Tag"]
headers_rrf = ["Register-data", "Valid", "Busy"]
table_arf = tabulate(ARF, headers=headers_arf, tablefmt="pretty", numalign="center")
table_rrf = tabulate(RRF, headers=headers_rrf, tablefmt="pretty", numalign="center")

# split the tables into rows and add a gap between columns
rows_arf = table_arf.split("\n")
rows_rrf = table_rrf.split("\n")
rows_combined = []
for i in range(len(rows_arf)):
    row_combined = rows_arf[i] + " " * 5 + rows_rrf[i]
    rows_combined.append(row_combined)

# print the combined table
print("\n".join(rows_combined))

# calling the register update function 
registerUpdate(ARF, RRF) 

# printing register files after all three instruction is done 

print("Displaying the final contents of the register files:")

# display ARF and RRF as tables in parallel
headers_arf = ["Register-data", "busy", "Tag"]
headers_rrf = ["Register-data", "Valid", "Busy"]
table_arf = tabulate(ARF, headers=headers_arf, tablefmt="pretty", numalign="center")
table_rrf = tabulate(RRF, headers=headers_rrf, tablefmt="pretty", numalign="center")

# split the tables into rows and add a gap between columns
rows_arf = table_arf.split("\n")
rows_rrf = table_rrf.split("\n")
rows_combined = []
for i in range(len(rows_arf)):
    row_combined = rows_arf[i] + " " * 5 + rows_rrf[i]
    rows_combined.append(row_combined)

# print the combined table
print("\n".join(rows_combined))
