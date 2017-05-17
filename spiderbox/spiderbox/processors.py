# -*- coding: utf-8 -*

#
class SaveDates( object ):

    def __init__( self, separator=u' '):
        self.separator = separator

    def __call__( self, values ):
        dates = None
        if 0 < len( values ):
            value = values[0]
            dates = { 'begin_date': '', 'end_date': '', 'label': value }
        return dates

class SaveSingle( object ):

    def __init__( self, separator=u' '):
        self.separator = separator

    def __call__( self, values ):
        value = None
        if 0 < len( values ):
            value = values[0].replace( ' - ', '' )
        return value

class Ucfirst(object):

    def __init__(self, separator=u' '):
        self.separator = separator

    def __call__(self, values):
        value = None
        if 0 < len( values ):
            value = values[0]
        return value
#

class TakeSecond(object):

    def __init__( self, separator=u' ' ):
        self.separator = separator
        self.nth = TakeNth( nth=1 )

    def __call__( self, values ):
        return self.nth( values )

class TakeNth(object):

    def __init__( self, separator=u' ', nth=0 ):
        self.separator = separator
        self.nth = nth

    def __call__( self, values ):
        value = None
        id_value = self.nth
        if self.nth <  len( values ):
            value = values[self.nth]

        return value

class TakeDates( object ):

    def __init__( self, separator=u' ' ):
        self.separator = separator

    def __call__( self, values ):
        if 0 < len( values ):
            value = values[0]
        else:
            value = None
        return value
