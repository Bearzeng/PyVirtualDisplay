from nose.tools import eq_, ok_

from pyvirtualdisplay.display import Display


def test_with():
    with Display(visible=0, size=(800, 600)) as vd:
        ok_(vd.is_alive())
    eq_(vd.return_code, 0)
    ok_(not vd.is_alive())

def test_dpi():
    with Display(backend='xvfb', size=(800, 600), dpi=99) as vd:
        ok_(vd.is_alive())
    eq_(vd.return_code, 0)
    ok_(not vd.is_alive())
