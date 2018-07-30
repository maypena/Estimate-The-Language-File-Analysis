# May Pena
# This program matches a text to a language based on
# the letters that reapeat the most in the text. 

text = """El hardware inalámbrico no autorizado se puede introducir fácilmente. Los puntos de
acceso inalámbricos son relativamente poco costosos y se implementan fácilmente. Un
equipo de asesores bienintencionado que trabaja en una sala de conferencias podría
instalar un punto de acceso inalámbrico para compartir un solo puerto cableado en la sala.
Un hacker malicioso puede sentarse en un café con un ordenador portátil habilitado para
uso inalámbrico buscando tráfico no cifrado o cifrado con WEP. En ambos casos, se
presentan riesgos inaceptables. Independientemente de si hay un intento malicioso, la
introducción de hardware no autorizado puede comprometer la confidencialidad e
integridad del tráfico de red. Los dispositivos inalámbricos no autorizados pueden
detectarse al examinar físicamente las instalaciones (práctica conocida como “guerra
móvil”), al utilizar escáneres de radiofrecuencia (RF) para determinar la ubicación de los
dispositivos inalámbricos o al usar sistemas diseñados para analizar el tráfico de red para
detectar dispositivos no autorizados. """

text = text.lower()
letters = { "a" : 0, "b" : 0,"c" : 0,"d" : 0,"e" : 0,"f" : 0,"g" : 0,"h" : 0,"i" : 0,
            "j" : 0,"k" : 0,"l" : 0,"m" : 0,"n" : 0,"o" : 0,"p" : 0,"q" : 0,"r" : 0,"s" : 0,
            "t" : 0,"u" : 0,"v" : 0,"w" : 0,"x" : 0,"y" : 0,"z" : 0 }
   
languageStrings = [('Spanish', 'eaosrnidlc'), ('German', 'enisratdhu'),
                   ('French', 'esaitnrulo'),  ('Italian', 'eaionlrtsc'),
                   ('Dutch', 'enatirodsl'), ('Turkish', 'aeinrkdlom'),
                   ('Polish', 'iaeoznscrw'), ('Swedish', 'eantrslido')]

def fuzzyMatch( string1, string2 ):
    '''given two strings of identical length
      (in our case, strings of 10 characters),
      returns the approximate percentage of matching
      between the two, with 100% representing an exact
      match. This function is useful when the strings do not
      match exactly, but are close'''

    if string1 > string2:
        string1, string2 = string2, string1

    sum = 0
    for i in range( len( string1 ) ):
        char = string1[ i ]
        index = string2.find( char )
        if index == -1:
            index = len( string1 )
        editDistance = abs( i-index )
        sum += editDistance
    return (100-sum)

def mfrequent():
    List = []
    List2 = []
    for l in text:
        if l in letters:
            letters[l] = letters[l] + 1

    for key in letters:
        tuples = ( letters[key], key )
        List.append( tuples )

        List.sort()
        List.reverse()

    for t in List[0:10]:
        List2.append( str( t[1] ) )

    string = ''
    for i in List2:
        string = string + i

    return string

def main():
    string1 = mfrequent()
    print( "Most frequent characters:", string1 )
    for Tuple in languageStrings:
        number = fuzzyMatch( string1, Tuple[1] )
        print( "{0:16}: {1:0.2f}% matching".format( Tuple[0],float( number ) ) )
        
main()
