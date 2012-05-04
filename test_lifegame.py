from nose.tools import *
import lifegame as life

class TestGame:
    def setup(self):
        f = [0,1,1,
             0,1,0,
             0,0,0]
        self.g = life.Game(3,3,f) 

    def test_has_fields(self):
        ok_(0<len(self.g.fields))

    def test_get_field(self):
        eq_(1,self.g.get_field(1,1))
        eq_(0,self.g.get_field(0,0))

    def test_around_me(self):
        eq_(2,self.g.around_me(1,1))
        eq_(2,self.g.around_me(0,0))
        eq_(2,self.g.around_me(2,0))
        eq_(2,self.g.around_me(0,1))

class TestCheck(object):         
    def setup(self):
        f = [0,1,1,
             0,1,0,
             0,0,0]
        self.g = life.Game(3,3,f) 

    def test_check_field(self):
        f = [0,1,1,
             0,1,0,
             0,0,0]
        g = life.Game(3,3,f) 
        eq_(life.MARK_NONE , g.check_field(0,0))
        eq_(life.MARK_NONE , g.check_field(0,1))
        eq_(life.MARK_NONE , g.check_field(0,2))
        eq_(life.MARK_SAFE , g.check_field(1,0))
        eq_(life.MARK_SAFE , g.check_field(1,1))
        eq_(life.MARK_NONE , g.check_field(1,2))
        eq_(life.MARK_SAFE , g.check_field(2,0))
        eq_(life.MARK_BIRTH , g.check_field(2,1))
        eq_(life.MARK_NONE , g.check_field(2,2))

    def test_check_field_all(self):
        self.g.check_field_all()
        ok_(0<len(self.g.marks))
        expect = [None,life.MARK_SAFE,life.MARK_SAFE,
                  None,life.MARK_SAFE,life.MARK_BIRTH,
                  None,None,None]
        eq_(expect,self.g.marks)

class TestUpdate(object):
    def setup(self):
        f = [0,1,1,
             0,1,0,
             0,0,0]
        self.g = life.Game(3,3,f) 

    def test_update_field(self):
        self.g.marks = [life.MARK_DEATH ,life.MARK_DEATH ,life.MARK_DEATH ,
                        life.MARK_DEATH ,life.MARK_DEATH ,life.MARK_DEATH ,
                        life.MARK_DEATH ,life.MARK_DEATH ,life.MARK_DEATH ]
        self.g.update_field(1,0)
        eq_(0,self.g.get_field(1,0))

    def test_update_field_all(self):
        self.g.check_field_all()
        self.g.update_field_all()
        eq_(self.g.fields,[0,1,1,0,1,1,0,0,0])

