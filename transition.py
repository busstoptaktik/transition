import sys

# dict-of-strings
Mennesker = {
    'asmei':   'Aslak Meister',
    'erlys':   'Erik Lysdal',
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

    'elfle':   'Elvis Flesborg',
    'hefel':   'Helle Feldthaus',
    'stsuu':   'Steen Suurballe',
    'pw':      'Peter West-Nielsen',
    'morbo':   'Morten Romanow Bøgemose',
}

# dict-of-strings
Opgaver = {
#    Kaldenavn      Beskrivelse
    'plugin':      'Færdiggør QGIS-plugin til observationshåndtering',
    'kons':        'Konsolidering af de mange FIRE repos til en samlet kodebase',
    'målerCD':     'Hvilke dele af (det der engang hed) MålerCDen, skal FIREgenskabes?',

    'ilægning':    'Generel data-ilægningsfunktionalitet',
    'ilæg_niv':    'Ilægning af resultater af almindelig højdenetsvedligeholdelse',
    'ilæg_5D':     'Ilægning af 5D-kontrolberegninger',
    'ilæg_GNSS':   'Ilægning af {ugentlige?} GNSS-beregninger',

    'valdetest':   'Opsæt Valde-testmiljø der udstiller Helles mellemtabeller',
    'kontrol':     'Stikprøvekontrol af Databasemigrering',

    'kons':        'Konsolidering af kodebasen',
    'ka_forb':     'Forberedelse af kode- og arkitekturintroworkshop',
    'ka_intro':    'Kode- og arkitekturintroworkshop',
    'test_mark':   'Afprøvning og tilretning af alm beregningsfunktionalitet, FIRE-mark',
    'materiale':   'Udarbejdelse af kursusmateriale',
    'kursus':      'Afholdelse af kursus i beregning og databaseanvendelse',
    'tilpasning':  'Tilpasning af eksisterende kode, udvikling af ny funktionalitet',
    'udstilling':  'Inkrementel opdatering af udstillingsdata i GDBank',
    'videnstrans': 'Vidensoverdragelse omkring systemhåndtering',
}

Afsluttede = {
    'valdetest',
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
    'målerCD':     {},

    'ilæg_niv':    {'ilægning'},
    'ilæg_5D':     {'ilæg_niv'},
    'ilæg_GNSS':   {'ilægning'},

    'valdetest':   {},
    'kontrol':     {'valdetest'},

    'kons':        {},
    'ka_forb':     {'kons'},
    'ka_intro':    {'ka_forb'},
    'test_mark':   {'ilæg_niv'},
    'materiale':   {'test_mark'},
    'kursus':      {'materiale'},
    'videnstrans': {'udstilling'},
    'tilpasning':  {'kons'},
    'udstilling':  {'kontrol', 'ilægning'},
}

# dict-of-sets
Personafhængigheder = {
#    Opgave        Personafhængigheder
    'plugin':      {'thokn'},
    'ilægning':    {'kreve', 'thokn'},
    'målerCD':     {'nho', 'majws', 'thokn'},

    'ilæg_niv':    {'asmei'},
    'ilæg_5D':     {'asmei'},
    'ilæg_GNSS':   {'meweb'},

    'valdetest':   {'kreve', 'elfle'},
    'kontrol':     {'krkel', 'nho', 'lrh'},

    'kons':        {'kreve'},
    'ka_forb':     {'kreve', 'thokn'},
    'ka_intro':    {'kreve', 'thokn', 'majws', 'taphs', 'asmei', 'lrh'},
    'test_mark':   {'thokn', 'majws', 'kjbri'},
    'materiale':   {'majws', 'kjbri', 'thokn'},
    'kursus':      {'thokn', 'kreve', 'majws', 'asmei', 'kjbri', 'nho', 'pn', 'rmort', 'lrh', 'erlys'},
    'videnstrans': {'hefel', 'kreve', 'lrh', 'morbo', 'thokn', 'pw'},
    'tilpasning':  {'taphs', 'kreve', 'majws', 'thokn'},
    'udstilling':  {'hefel', 'kreve', 'morbo', 'thokn', 'stsuu'},
}


#------------------------------------------------------------------------------
class plugin:
#------------------------------------------------------------------------------
    """Færdiggør QGIS-plugin til observationshåndtering

    osv. osv. (længere beskrivelse her)
    osv. osv. (længere beskrivelse her)
    """

    pass

#------------------------------------------------------------------------------
class kons:
#------------------------------------------------------------------------------
    """Konsolidering af de mange FIRE repos til en samlet kodebase"""

    pass

#------------------------------------------------------------------------------
class målerCD:
#------------------------------------------------------------------------------
    """Hvilke dele af (det der engang hed) MålerCDen, skal FIREgenskabes?

    Bl.a. laver Henrik en SQLite-fil med "lokaloversigt. Hvad er der ellers?
    """

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



def banner(text=""):
    print (80*'-')
    print (text)
    if text != "":
        print (80*'-')
    else:
        print ()

if 'opgaver' in sys.argv[1:] or len(sys.argv)<2:
    banner('Opgaver')
    for o in Opgaver:
        if o not in Afsluttede:
            print(f"{o:12}  {Opgaver[o]}")
    banner()
    banner('Afsluttede opgaver')
    for o in Opgaver:
        if o in Afsluttede:
            print(f"{o:12}  {Opgaver[o]}")
    banner()

if 'mennesker' in sys.argv[1:] or len(sys.argv)<2:
    banner('Opgaveallokering pr. humanoide')
    for m in Mennesker:
        # print(f"{m:5}  {Mennesker[m]}")
        tasks = set()
        for pa in Personafhængigheder:
            if m in Personafhængigheder[pa] and pa not in Afsluttede:
                tasks |= {pa}
        if (len(tasks) > 0):
            print(f"{m:12} {tasks}")
    banner()

for arg in sys.argv[1:]:
    if arg in Opgaver and  arg in globals():
        banner(arg)
        print(globals()[arg].__doc__)
    banner()

# med venlig hilsen...
if 'idiot' in sys.argv[1:]:
    print('klaphat!')
