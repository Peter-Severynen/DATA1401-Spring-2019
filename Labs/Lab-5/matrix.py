import random
import math

#helper functions
def transposeM(m):
    return map(list,zip(*m))

def calcMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def calcDet(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    det = 0
    for c in range(len(m)):
        det += ((-1)**c)*m[0][c]*calcDet(calcMinor(m,0,c))
    return det

#part 6a functions
def inv(m):
    det = calcDet(m)
    if len(m) == 2:
        return [[m[1][1]/det, -1*m[0][1]/det],
                [-1*m[1][0]/det, m[0][0]/det]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = calcMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * calcDet(minor))
            #print cofactorRow
        cofactors.append(cofactorRow)
    cofactors = transposeM(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/det
    return cofactors      

class matrix():
    def __init__(self, M=[[1,0,0],[0,1,0],[0,0,1]]):
        #constructor that I can pass a 2D list into
            self.M = M
        
    #part 2a functions
    def constant(self,n,m,c):
        self.M = []
        for i in range(m):
            self.M.append([])
            for j in range(n):
                self.M[i].append(c)
        #return self

    #part 2b functions
    def zeros(self,n,m, c=0):
        self.M = []
        for i in range(m):
            self.M.append([])
            for j in range(n):
                self.M[i].append(c)

    def ones(self,n,m, c=1):
        self.M = []
        for i in range(m):
            self.M.append([])
            for j in range(n):
                self.M[i].append(c)
    
    def randomMatrix(self,n,m, c=0):
        self.M = []
        for i in range(m):
            self.M.append([])
            for j in range(n):
                self.M[i].append(random.randint(1,10))

   #part 2c functions
    def eye(self,n):
        self.M = []
        for i in range(n):
            self.M.append([])
            for j in range(n):
                if(i==j):
                    self.M[i].append(1)
                else:
                    self.M[i].append(0)
        #return self.M

    #part 3a functions
    def shape(self):
        size = []
        ctr = 0 #if shape finds a row that has the wrong number of columns, then it increments the invalid count
        m = len(self.M)
        n = len(self.M[0])
        for i in range(0,m):
            if len(self.M[i]) != n:
                ctr+=1
        if ctr > 0:
            return False
        else:
            size.append(n)
            size.append(m)
            return size
        
    #part 3b functions
    def row(self,n):
        out = []
        dim = self.shape()
        col = dim[0]
        row = dim[1]
        #print "self.M[n] is:"+str(self.M[n])
        if n > row:
            print "Row index is out-of-bounds!"
            out.append(None)
        else:
            return self.M[n]

    def column(self,n):
        out = []
        dim = self.shape()
        col = dim[0]
        row = dim[1]
        if n > col:
            print "Column index is out-of-bounds!"
            out.append(None)
        else:
            for i in range(0,row):
                for j in range(0,col):
                    if j == n:
                        out.append(self.M[i][j])
        return out
    
    #part 3c functions
    def mat_copy(l,n,m):
        a = []
        for i in range(n):
            a.append([])
            for j in range(m):
                    a[i].append(l[j]) #TODO fix bug
        return a

    def block(self, n_0, n_1, m_0, m_1):
        out_1 = []
        out_2 = [1]
        out_2_num_col = (n_1-n_0)+1 #the output matrix's number of columns
        out_2_num_row = (m_1-m_0)+1 #the output matrix's number of rows
        dim = self.shape()
        print dim
        col = dim[0]
        row = dim[1]
        if n_1 > col or m_1 > row:
            print "Column index is out-of-bounds!"
            out_1.append(None)
        else:
            for i in range(0,row):
                for j in range(0,col):
                    if i >= m_0 and i <= m_1:
                        if j >= n_0 and j <= n_1:
                            out_1.append(self.M[i][j])
        out_2[0] = out_1
        return out_2
    
    #part 4a functions
    def transpose(self):
        temp = [[self.M[j][i] for j in range(len(self.M))] for i in range(len(self.M[0]))]
        self.M = temp
    
    #part 4b, 4e functions
    def multiply(self, c, m, n):
        out = []
        #if c is zero, perform scalar multiplication on the internal matrix self.M
        if (type(c) == int and c!= 0):
            #perform scalar multiplication
            dim = self.shape()
            n = dim[0]
            m = dim[1]
            for i in range(m):
                for j in range(n):
                     self.M[i][j] = self.M[i][j]*c
        #if c is 1, perform element-wise multiplication on the 2 input matrices
        #if (type(c) == int and c!= 0):
        #    out = [[self.M[i][j]*n[i][j] for j in range(len(n[0]))] for i in range(len(n))]
        #    self.M = out
        else:
            #perform matrix multiplication
            out = []
            for i in range(0,len(m)):
                temp=[]
                for j in range(0,len(n[0])):
                    sum1 = 0
                    for k in range(0,len(m[0])):
                        sum1 += m[i][k]*n[k][j]
                    temp.append(sum1)
                out.append(temp)
        return out
    
    #part 4c functions
    def add(self, N):
        out = [[self.M[i][j]+N.M[i][j] for j in range(len(N.M[0]))] for i in range(len(self.M))]
        self.M = out
        return self
    
    #part 4d functions
    def sub(self, N):
        out = [[self.M[i][j]+(N.M[i][j]*-1) for j in range(len(N.M[0]))] for i in range(len(self.M))]
        self.M = out
        return self
    
    #part 4g functions
    def outer(self, B):
        out = []
        self.transpose()
        out = self.multiply(0,self.M,B)
        return out

class vector(matrix):
    def __init__(self):
        matrix.__init__(self)
    
    #part 4g functions
    def dot(self, A,B):
        out = 0
        for i,j in zip(A,B):
            out += i*j
        return out

    
    #part 5a functions
    def norm(self, M,i,p=1):
        out = 0
        if i == 1:
            #compute 1-norm
            sum_1 = 0
            for j in range(0,len(M)):
                sum_1 += abs(M[j])
            out = sum_1
        elif i == 2:
            #compute 2-norm
            sum_2 = 0
            for j in range(0,len(M)):
                x_squared = M[j] ** 2
                sum_2 += x_squared
            out = math.sqrt(sum_2)
        elif i == 3:
            #string = raw_input("Enter p")
            #p = float(string)
            #compute p-norm
            sum_3 = 0
            for j in range(0,len(M)):
                abs_x = abs(M[j])
                abs_x_to_the_p = abs_x**(p)
                sum_3 += abs_x_to_the_p
                out = sum_3 ** (1/float(p))

        elif i == 4:
            #compute infinity-norm
            current_max = 0
            for j in range(0,len(M)):
                if M[j] > current_max:
                    current_max = M[j]
            out = current_max
        return out
    
