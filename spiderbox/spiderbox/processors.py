# -*- coding: utf-8 -*

#

class SaveMulti( object ):

    def __init__( self, separator=u' '):
        self.separator = separator

    def __call__( self, values ):
        print len( values )
        if len( values ) == 0:
            value = list()
        elif not values[0]:
            value = list()
        else:
            value = values
        return value

class SaveSingle( object ):

    def __init__( self, separator=u' '):
        self.separator = separator

    def __call__( self, values ):
        value = ''
        if 0 < len( values ):
            value = values[0].replace( ' - ', '' )
        return value

class Ucfirst(object):

    def __init__(self, separator=u' '):
        self.separator = separator

    def __call__(self, values):
        value = ''
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
        value = ''
        id_value = self.nth
        print values
        if self.nth <  len( values ):
            value = values[self.nth]

        return value

class TakeEventUrl( object ):

    def __init__( self, separator=u' ' ):
        self.separator = separator

    def __call__( self, values ):
        print 'VALUES------------------------------------->'
        print values
        return values

class TakePays( object ):
    """
    Transforme l'image drapeau en une valeur fr,be,... désignant le pays
    """

    def __init__( self, separator=u' ' ):
        self.separator = separator

    def __call__( self, values ):
        pays = ''

        if len( values ) == 1:
            tmp = values[0]
            pays = tmp.split( '/' )[1].split( '.' )[0]

            if pays == 'fr':
                pays = 'France'
            elif pays == 'be':
                pays = 'Belgique'
            else:
                pays = ''

        return pays

#
class ShowMe( object ):

    def __init__( self, separator=u' ', nth=0 ):
        self.separator = separator

    def __call__( self, values ):
        print '**************<DEBUG**************'
        print values
        for  value in values:
            print 'value %s' % ( value )
        print '***************DEBUG>**************'
        return values
