MARK_SAFE=0
MARK_DEATH=1
MARK_BIRTH=2
MARK_NONE=None

class Game(object):
    def __init__(self,x,y,fields=None):
       self.max_x = x
       self.max_y = y
       self.fields = fields

    def get_field(self,x,y):
       if not 0 <= x < self.max_x:
           return False
       if not 0 <= y < self.max_y:
           return False

       i = x + self.max_x * y 
       return int(self.fields[i])

    def set_field(self,x,y,value):
       i = x + self.max_x * y
       self.fields[i]=value


    def check_field(self,x,y):
        num = self.around_me(x,y)
        if  self.get_field(x,y)==1:
            if num == 1:
                return MARK_DEATH
            elif num == 2 or num == 3 :
                return MARK_SAFE
            elif num >= 4:
                return MARK_DEATH 
            else:
                return MARK_NONE

        if  self.get_field(x,y)==0:
            if num == 3:
                return MARK_BIRTH
            else:
                return MARK_NONE
    
    def check_field_all(self):
        tmp_list = []
        for y in range(0,self.max_y):
            for x in range(0,self.max_x):
               tmp_list.append(self.check_field(x,y))
        self.marks=tmp_list

    def update_field(self,x,y):
       self.get_field(x,y)
       mark = self.marks[x+self.max_x*y]
       if mark == MARK_DEATH:
           self.set_field(x,y,0)
       if mark == MARK_BIRTH:
           self.set_field(x,y,1)

    def update_field_all(self):
        for x in range(0,self.max_x):
            for y in range(0,self.max_y):
                self.update_field(x,y)
 
    def around_me(self,x,y):
        tmp_list = [
            int(self.get_field(x-1,y-1)),
            int(self.get_field(x,y-1)),
            int(self.get_field(x+1,y-1)),
            int(self.get_field(x-1,y)),
            int(self.get_field(x+1,y)),
            int(self.get_field(x-1,y+1)),
            int(self.get_field(x,y+1)),
            int(self.get_field(x+1,y+1))
        ]
        return sum(tmp_list)

    def disp_marks(self):
        l = self.marks
        tmp_l = []
        for y in range(0,self.max_y):
            for x in range(0,self.max_x):
                tmp_l.append(str(l[x+y*self.max_x]))
            tmp_l.append('\n')
        print ''.join(tmp_l)

    def disp(self):
        l = self.fields
        for y in range(0,self.max_y):
            line = ''
            for x in range(0,self.max_x):
               line += str(self.get_field(x,y))
            print(line)
        print('----------')
