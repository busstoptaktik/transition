import sys

# dict-of-strings
Mennesker = {
    'asmei':   'Aslak Meister',
    'nho':     'Henrik Olsen',
    'kjbri':   'Kjeld Brixen',
    'lrh':     'Lars Hole',
    'kreve':   'Kristian Evers',
    'krkel':   'Kristian Keller',
    'majws':   'Majbritt Westring Sørensen',
    'meweb':   'Mette Weber',
    'taphs':   'Tanya Pheiffer Sunding',
    'thokn':   'Thomas Knudsen',
    'pn':      'Palle Nielsen',
    'rmort':   'Rene Thyregod Andsbjerg',
    'extern':  'Udenfor GRF',           # Elvis, Helle, Steen, PW, morbo, ...
}

# dict-of-strings
Opgaver = {
#    Kaldenavn      Beskrivelse
    'plugin':      'Færdiggør QGIS-plugin til observationshåndtering',
    'kons':        'Konsolidering af de mange FIRE repos til en samlet kodebase',

    'ilægning':    'Generel data-ilægningsfunktionalitet',
    'ilæg_niv':    'Ilægning af resultater af almindelig højdenetsvedligeholdelse',
    'ilæg_5D':     'Ilægning af 5D-kontrolberegninger',
    'ilæg_GNSS':   'Ilægning af {ugentlige?} GNSS-beregninger',

    'valdetest':   'Opsæt Valde-testmiljø der udstiller Helles mellemtabeller',
    'kontrol':     'Stikprøvekontrol af Databasemigrering',

    'test_mark':   'Afprøvning og tilretning af alm beregningsfunktionalitet, FIRE-mark',
    'materiale':   'Udarbejdelse af kursusmateriale',
    'kursus':      'Afholdelse af kursus i beregning og databaseanvendelse',
    'videnstrans': 'Vidensoverdragelse omkring systemhåndtering',
    'tilpasning':  'Tilpasning af eksisterende kode, udvikling af ny funktionalitet',
}

# dict-of-strings
Tovholdere = {
    'plugin':      'thokn',
    'ilægning':    'kreve',
    'videnstrans': 'kreve',
    'kursus':      'majws',
}

# dict-of-sets
Afhængigheder = {
#    Opgave        Afhængigheder
    'plugin':      {},
    'ilægning':    {},

    'ilæg_niv':    {'ilægning'},
    'ilæg_5D':     {'ilæg_niv'},
    'ilæg_GNSS':   {'ilægning'},

    'valdetest':   {'extern'},
    'kontrol':     {'valdetest'},

    'test_mark':   {'ilæg_niv'},
    'materiale':   {'test_mark'},
    'kursus':      {'materiale'},
    'videnstrans': {},
    'tilpasning':  {'kons'}
}

# dict-of-sets
Personafhængigheder = {
#    Opgave        Personafhængigheder
    'plugin':      {'thokn'},
    'ilægning':    {'kreve', 'thokn'},

    'ilæg_niv':    {'asmei'},
    'ilæg_5D':     {'asmei'},
    'ilæg_GNSS':   {'meweb'},

    'valdetest':   {'kreve', 'extern'},
    'kontrol':     {'krkel', 'nho', 'lrh'},

    'test_mark':   {'thokn', 'majws', 'kjbri'},
    'materiale':   {'majws', 'kjbri', 'thokn'},
    'kursus':      {'materiale'},
    'videnstrans': {'kreve', 'lrh', 'extern'},
    'tilpasning':  {'taphs', 'kreve', 'majws', 'thokn'},
    'kons':        {'kreve'},
    'kursus':      {'thokn', 'kreve', 'majws', 'asmei', 'kjbri', 'nho', 'pn', 'rmort', 'lrh'}
}



#------------------------------------------------------------------------------
class plugin:
#------------------------------------------------------------------------------
    """Færdiggør QGIS-plugin til observationshåndtering

    osv. osv. (længere beskrivelse her)
    osv. osv. (længere beskrivelse her)"""
    pass
#------------------------------------------------------------------------------
class kons:
#------------------------------------------------------------------------------
    """Konsolidering af de mange FIRE repos til en samlet kodebase"""
    pass
#------------------------------------------------------------------------------
class ilægning:
#------------------------------------------------------------------------------
    """Generel data-ilægningsfunktionalitet"""
    pass
#------------------------------------------------------------------------------
class ilæg_niv:
#------------------------------------------------------------------------------
    """Ilægning af resultater af almindelig højdenetsvedligeholdelse"""
    pass
#------------------------------------------------------------------------------
class ilæg_5D:
#------------------------------------------------------------------------------
    """Ilægning af 5D-kontrolberegninger"""
    pass
#------------------------------------------------------------------------------
class ilæg_GNSS:
#------------------------------------------------------------------------------
    """Ilægning af {ugentlige?} GNSS-beregninger"""
    pass
#------------------------------------------------------------------------------
class valdetest:
#------------------------------------------------------------------------------
    """Opsæt Valde-testmiljø der udstiller Helles mellemtabeller"""
    pass
#------------------------------------------------------------------------------
class kontrol:
#------------------------------------------------------------------------------
    """Stikprøvekontrol af Databasemigrering"""
    pass
#------------------------------------------------------------------------------
class test_mark:
#------------------------------------------------------------------------------
    """Afprøvning og tilretning af alm beregningsfunktionalitet, FIRE-mark"""
    pass
#------------------------------------------------------------------------------
class materiale:
#------------------------------------------------------------------------------
    """Udarbejdelse af kursusmateriale"""
    pass
#------------------------------------------------------------------------------
class kursus:
#------------------------------------------------------------------------------
    """Afholdelse af kursus i beregning og databaseanvendelse"""
    pass
#------------------------------------------------------------------------------
class videnstrans:
#------------------------------------------------------------------------------
    """Vidensoverdragelse omkring systemhåndtering"""
    pass
#------------------------------------------------------------------------------
class tilpasning:
#------------------------------------------------------------------------------
    """Tilpasning af eksisterende kode, udvikling af ny funktionalitet"""
    pass



def banner(text):
    print (80*'-')
    print (text)
    print (80*'-')

if 'opgaver' in sys.argv[1:] or len(sys.argv)<2:
    banner('Opgaver')
    for o in Opgaver:
        print(f"{o:12}  {Opgaver[o]}")

if 'mennesker' in sys.argv[1:] or len(sys.argv)<2:
    banner('Opgaveallokering pr. humanoide')
    for m in Mennesker:
        # print(f"{m:5}  {Mennesker[m]}")
        tasks = set()
        for pa in Personafhængigheder:
            if m in Personafhængigheder[pa]:
                tasks |= {pa}
        print(f"{m:12} {tasks}")

for arg in sys.argv[1:]:
    if arg in Opgaver and  arg in globals():
        banner(arg)
        print(globals()[arg].__doc__)

# med venlig hilsen...
if 'idiot' in sys.argv[1:]:
    print('klaphat!')
