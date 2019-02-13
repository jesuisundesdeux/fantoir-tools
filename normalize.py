#!/bin/python
# -*- coding: UTF-8 -*-

# 2019 - Bruno Adele <brunoadele@gmail.com> #JeSuisUnDesDeux team

# https://www.data.gouv.fr/s/resources/fichier-fantoir-des-voies-et-lieux-dits/community/20150512-103719/Descriptif_FANTOIR.pdf

import os
import shutil
from collections import OrderedDict

# Replace word
def replace_words(words, text):
    for word in iter(words):
        for search in words[word]:
            if text.find(search)==0:
                # Begin word
                text = text.replace(search,word)  
            else:
                search = " %(search)s" % locals()
                text = text.replace(search,word)

    text = text.strip()

    return text

# Normalize text content, remove symbols
def normalize(text):
    text = text.replace("-"," " )
    text = text.replace("'"," ")
    text = text.replace("\""," ")
    text = text.replace("/"," ")
    text = " ".join(text.split())
    text = replace_words(REPLACE_WORDS,text)

    return text

REPLACE_WORDS = {
    ' ':['D ','DE ', 'LA ','DU '],
    }

TYPE_VOIE = {
    "ACH": "ANCIEN CHEMIN",
    "AER": "AERODROME",
    "AERG": "AEROGARE",
    "AGL": "AGGLOMERATION",
    "AIRE": "AIRE",
    "ALL": "ALLEE",
    "ANGL": "ANGLE",
    "ARC": "ARCADE",
    "ART": "ANCIENNE ROUTE",
    "AUT": "AUTOROUTE",
    "AV": "AVENUE",
    "BASE": "BASE",
    "BD": "BOULEVARD",
    "BER": "BERGE",
    "BORD": "BORD",
    "BRE": "BARRIERE",
    "BRG": "BOURG",
    "BRTL": "BRETELLE",
    "BSN": "BASSIN",
    "CAE": "CARRIERA",
    "CALL": "CALLE,CALLADA",
    "CAMI": "CAMIN",
    "CAMP": "CAMP",
    "CAN": "CANAL",
    "CAR": "CARREFOUR",
    "CARE": "CARRIERE",
    "CASR": "CASERNE",
    "CC": "CHEMIN COMMUNAL",
    "CD": "CHEMIN DEPARTEMENTAL",
    "CF": "CHEMIN FORESTIER",
    "CHA": "CHASSE",
    "CHE": "CHEMIN",
    "CHEM": "CHEMINEMENT",
    "CHL": "CHALET",
    "CHP": "CHAMP",
    "CHS": "CHAUSSEE",
    "CHT": "CHATEAU",
    "CHV": "CHEMIN VICINAL",
    "CITE": "CITE",
    "CIVE": "COURSIVE",
    "CLOS": "CLOS",
    "CLR": "COULOIR",
    "COIN": "COIN",
    "COL": "COL",
    "COR": "CORNICHE",
    "CORO": "CORON",
    "COTE": "COTE",
    "COUR": "COUR",
    "CPG": "CAMPING",
    "CR": "CHEMIN RURAL",
    "CRS": "COURS",
    "CRX": "CROIX",
    "CTR": "CONTOUR",
    "CTRE": "CENTRE",
    "DARS": "DARSE,DARCE",
    "DEVI": "DEVIATION",
    "DIG": "DIGUE",
    "DOM": "DOMAINE",
    "DRA": "DRAILLE",
    "DSC": "DESCENTE",
    "ECA": "ECART",
    "ECL": "ECLUSE",
    "EMBR": "EMBRANCHEMENT",
    "EMP": "EMPLACEMENT",
    "ENC": "ENCLOS",
    "ENV": "ENCLAVE",
    "ESC": "ESCALIER",
    "ESP": "ESPLANADE",
    "ESPA": "ESPACE",
    "ETNG": "ETANG",
    "FD": "FOND",
    "FG": "FAUBOURG",
    "FON": "FONTAINE",
    "FOR": "FORET",
    "FORT": "FORT",
    "FOS": "FOSSE",
    "FRM": "FERME",
    "GAL": "GALERIE",
    "GARE": "GARE",
    "GBD": "GRAND BOULEVARD",
    "GPL": "GRANDE PLACE",
    "GR": "GRANDE RUE",
    "GREV": "GREVE",
    "HAB": "HABITATION",
    "HAM": "HAMEAU",
    "HIP": "HIPPODROME",
    "HLE": "HALLE",
    "HLG": "HALAGE",
    "HLM": "HLM",
    "HTR": "HAUTEUR",
    "ILE": "ILE",
    "ILOT": "ILOT",
    "IMP": "IMPASSE",
    "JARD": "JARDIN",
    "JTE": "JETEE",
    "LAC": "LAC",
    "LEVE": "LEVEE",
    "LICE": "LICES",
    "LIGN": "LIGNE",
    "LOT": "LOTISSEMENT",
    "MAIL": "MAIL",
    "MAIS": "MAISON",
    "MAR": "MARCHE",
    "MARE": "MARE",
    "MAS": "MAS",
    "MNE": "MORNE",
    "MRN": "MARINA",
    "MTE": "MONTEE",
    "NTE": "NOUVELLE ROUTE",
    "PAE": "PETITE AVENUE",
    "PARC": "PARC",
    "PAS": "PASSAGE",
    "PASS": "PASSE",
    "PCH": "PETIT CHEMIN",
    "PCHE": "PORCHE",
    "PHAR": "PHARE",
    "PIST": "PISTE",
    "PKG": "PARKING",
    "PL": "PLACE",
    "PLA": "PLACA",
    "PLAG": "PLAGE",
    "PLAN": "PLAN",
    "PLCI": "PLACIS",
    "PLE": "PASSERELLE",
    "PLN": "PLAINE",
    "PLT": "PLATEAU",
    "PNT": "POINTE",
    "PONT": "PONT",
    "PORQ": "PORTIQUE",
    "PORT": "PORT",
    "POST": "POSTE",
    "POT": "POTERNE",
    "PROM": "PROMENADE",
    "PRT": "PETITE ROUTE",
    "PRV": "PARVIS",
    "PTA": "PETITE ALLEE",
    "PTE": "PORTE",
    "PTR": "PETITE RUE",
    "PTTE": "PLACETTE",
    "QUA": "QUARTIER",
    "QUAI": "QUAI",
    "RAC": "RACCOURCI",
    "REM": "REMPART",
    "RES": "RESIDENCE",
    "RIVE": "RIVE",
    "RLE": "RUELLE",
    "ROC": "ROCADE",
    "RPE": "RAMPE",
    "RPT": "ROND POINT",
    "RTD": "ROTONDE",
    "RTE": "ROUTE",
    "RUE": "RUE",
    "RUET": "RUETTE",
    "RUIS": "RUISSEAU",
    "RULT": "RUELLETTE",
    "RVE": "RAVINE",
    "SAS": "SAS",
    "SEN": "SENTIER",
    "SQ": "SQUARE",
    "STDE": "STADE",
    "TER": "TERRE",
    "TOUR": "TOUR",
    "TPL": "TERRE PLEIN",
    "TRA": "TRAVERSE",
    "TRAB": "TRABOULE",
    "TRN": "TERRAIN",
    "TRT": "TERTRE",
    "TSSE": "TERRASSE",
    "TUN": "TUNNEL",
    "VAL": "VAL",
    "VALL": "VALLON,VALLEE",
    "VC": "VOIE COMMUNALE",
    "VCHE": "VIEUX CHEMIN",
    "VEN": "VENELLE",
    "VGE": "VILLAGE",
    "VIA": "VIA",
    "VIAD": "VIADUC",
    "VIL": "VILLE",
    "VLA": "VILLA",
    "VOIE": "VOIE",
    "VOIR": "VOIRIE",
    "VOUT": "VOUTE",
    "VOY": "VOYEUL",
    "VTE": "VIEILLE ROUTE",
    "ZA": "ZA",
    "ZAC": "ZAC",
    "ZAD": "ZAD",
    "ZI": "ZI",
    "ZONE": "ZONE",
    "ZUP": "ZUP"
}

fantoir_file="FANTOIR0119"
dcom = dict()
alldatas = OrderedDict()

# Reset datas folder
shutil.rmtree('datas',ignore_errors=True)
os.mkdir('datas')

# Analyze FANTOIR datas
with open(fantoir_file, 'rb') as textfile:
    for rawline in textfile:
        line = rawline.decode('UTF-8')
        sizeline = len(line)
        if sizeline<90:
            # Initial record

            # 1 11 10 X FILLER
            # 12 36 25 X Libellé du centre de production du fichier
            # 37 44 8 X Date de situation du fichier2 AAAAMMJJ
            # 45 52 8 X Date de production du fichie
            filler = line[0:11]
            centre =  line[11:36]
            datesitu =  line[36:44]
            dateprod =  line[44:52]
        elif sizeline<=90:
            # Check if departement/direction record exists
            filler =  line[3:11]
            if "        " in str(filler):
                # 1 2 2 X Code département
                # 3 3 1 X Code direction
                # 4 11 8 X FILLER
                # 12 41 30 X Libellé Direction        
                cdep = line[0:2].strip()
                cdir =  line[2:3].strip()
                libelle =  line[11:41].strip()

                if cdir!="0" and cdep=="97":
                    codedep = "%(cdep)s%(cdir)s" % locals()
                else:
                    codedep = "%(cdep)s" % locals()
                
                if codedep not in alldatas:
                    alldatas[codedep] = {
                        'name': libelle,
                        'towns': {
                        }
                    }
                    depname = "%(codedep)s - %(libelle)s" % locals()
                    print ("Analyze %(depname)s" % locals())

            else:
                # Town record
                # 1 2 2 X Code département
                # 3 3 1 X Code direction
                # 4 6 3 X Code commune
                # 7 10 4 X FILLER
                # 11 11 1 X Clé RIVOLI Contrôle la validité de COMM
                # 12 41 30 X Libellé Commune
                # 42 42 1 X FILLER
                # 43 43 1 X Type de la commune N : rurale, R : recensée
                # 44 45 2 X FILLER
                # 46 46 1 X Caractère RUR 3 : pseudo-recensée, blanc sinon
                # 47 49 3 X FILLER
                # 50 50 1 X Caractère de population blanc si < 3000 hab, * sinon
                # 51 52 2 X FILLER
                # 53 59 7 9 Population réelle
                # 60 66 7 9 Population à part
                # 67 73 7 9 Population fictive
                # 74 74 1 X Caractère d’annulation Q : annulation avec transfert
                # 75 81 7 9 Date d’annulation
                # 82 88 7 9 Date de création de l’article
                cdep = line[0:2].strip()
                cdir =  line[2:3].strip()
                ccom =  line[3:6].strip()
                crivo = line[10:11].strip()
                lcom = line[11:41].strip()
                tcom = line[42:43].strip()
                crur =  line[45:46].strip()
                cpol = line[49:50].strip()
                prel = line[52:59].strip()
                ppart = line[59:66].strip()
                pfict = line[66:73].strip()
                cann = line[73:74].strip()
                dann = line[74:81].strip()
                dcre = line[81:88].strip()

                if cdir!="0" and cdep=="97":
                    codedep = "%(cdep)s%(cdir)s" % locals()
                else:
                    codedep = "%(cdep)s" % locals()

                if ccom in alldatas[codedep]['towns']:
                    print("ERREUR: lcom")
                    sys.exit()

                lcleanname = lcom.replace('/','')
                alldatas[codedep]['towns'][ccom] = { 
                    'name': lcom,
                    'cleanname': lcleanname,
                    'streets': [] 
                }
        else:
            # Street record
            # 1 2 2 X Code département
            # 3 3 1 X Code direction
            # 4 6 3 X Code commune
            # 7 10 4 X FILLER
            # 11 11 1 X Clé RIVOLI Contrôle la validité de COMM
            # 12 41 30 X Libellé Commune
            # 42 42 1 X FILLER
            # 43 43 1 X Type de la commune N : rurale, R : recensée
            # 44 45 2 X FILLER
            # 46 46 1 X Caractère RUR 3 : pseudo-recensée, blanc sinon
            # 47 49 3 X FILLER
            # 50 50 1 X Caractère de population blanc si < 3000 hab, * sinon
            # 51 52 2 X FILLER
            # 53 59 7 9 Population réelle
            # 60 66 7 9 Population à part
            # 67 73 7 9 Population fictive
            # 74 74 1 X Caractère d’annulation Q : annulation avec transfert
            # 75 81 7 9 Date d’annulation
            # 82 88 7 9 Date de création de l’article
            # 89 150 42 X FILLER
            # DESCRIPTION FICHIER FANTOIR DES VOIES ET LIEUX-DITS PAGE
            # DE FICHIER 10
            # 3.4. Enregistrement Voie
            # DEB FIN LGR NAT DESCRIPTION OBSERVATION
            # 1 2 2 X Code département
            # 3 3 1 X Code direction
            # 4 6 3 X Code commune
            # 7 10 4 X Identifiant de la voie dans la commune
            # 11 11 1 X Clé RIVOLI
            # 12 15 4 X Code nature de voie
            # 16 41 26 X Libellé voie
            # 42 42 1 X FILLER
            # 43 43 1 X Type de la commune N : rurale, R : recensée
            # 44 45 2 X FILLER
            # 46 46 1 X Caractère RUR 3 : pseudo-recensée, blanc sinon
            # 47 48 2 X FILLER
            # 49 49 1 X Caractère de voie 1 : privée, 0 : publique
            # 50 50 1 X Caractère de population blanc si < 3000 hab, * sinon
            # 51 59 9 X FILLER
            # 60 66 7 9 Population à part
            # 67 73 7 9 Population fictive
            # 74 74 1 X Caractère d’annulation O : sans transfert, Q : avec
            # 75 81 7 9 Date d’annulation
            # 82 88 7 9 Date de création de l’article
            # 89 103 15 X FILLER
            # 104 108 5 X Code identifiant MAJIC de la voie
            # 109 109 1 X Type de voie
            # 1 : voie
            # 2 : ensemble immobilier
            # 3 : lieu-dit
            # 4 :pseudo-voie
            # 5 : voie provisoire
            # 110 110 1 X Caractère du lieu-dit 1 : lieu-dit bâti, 0 sinon
            # 111 112 2 X FILLER
            # 113 120 8 X
            # Dernier mot entièrement alphabétique du
            # libellé de la voie
            # 121 150 30 X FILLER
            cdep = line[0:2].strip()
            cdir =  line[2:3].strip()
            ccom =  line[3:6].strip()
            crivo = line[10:11].strip()
            nvoie = line[11:15].strip()
            lstreet = line[15:41].strip()
            tcom = line[42:43].strip()
            crur =  line[45:46].strip()
            cpol = line[49:50].strip()
            prel = line[52:59].strip()
            ppart = line[59:66].strip()
            pfict = line[66:73].strip()
            cann = line[73:74].strip()
            dann = line[74:81].strip()
            dcre = line[81:88].strip()
            cmajic = line[103:108].strip()
            tvoie = line[108:109].strip()
            cdit = line[109:110].strip()
            dmot = line[112:120].strip()

            if cdep != "99":
                lstreet_norm = normalize(lstreet)
                voie=""
                if nvoie in TYPE_VOIE:
                    voie=TYPE_VOIE[nvoie]

                if cdir!="0" and cdep=="97":
                    codedep = "%(cdep)s%(cdir)s" % locals()
                else:
                    codedep = "%(cdep)s" % locals()

                alldatas[codedep]['towns'][ccom]['streets'].append("%(cdep)s;%(cdir)s;%(ccom)s;%(crivo)s;%(nvoie)s;%(voie)s;%(lstreet)s;%(lstreet_norm)s;%(tcom)s;%(crur)s;%(cpol)s;%(prel)s;%(ppart)s;%(pfict)s;%(cann)s;%(dann)s;%(dcre)s;%(cmajic)s;%(tvoie)s;%(cdit)s;%(dmot)s\n" % locals())

# Init README template
shutil.copyfile("README_template.md", "README.md")
with open("README.md", 'a') as docfile:
    docfile.write("## Statistique par departement\n\n")

    docfile.write("| Departement | Nb villes | nb rues |\n")
    docfile.write("|-------------|-----------|---------|\n")

    allnbtowns = 0
    allnbstreets = 0

    # Generate csv file
    for codedep in alldatas:
        # Create folder
        depname = alldatas[codedep]['name']
        repname = normalize(depname)
        path = "datas/%(codedep)s-%(repname)s" %locals()
        os.makedirs(path)

        nbtowns = len(alldatas[codedep]['towns']) 
        allnbtowns += len(alldatas[codedep]['towns'])
        nbstreets = 0
        for codetown in alldatas[codedep]['towns']:
            nbstreets += len(alldatas[codedep]['towns'][codetown]['streets'])
            allnbstreets += len(alldatas[codedep]['towns'][codetown]['streets'])

            # Save normalized streets to file
            filename = "%s/%s-%s.csv" % (path,codetown,normalize(alldatas[codedep]['towns'][codetown]['name']))
            with open(filename, 'w') as townfile:
                export = "cdep;cdir;ccom;crivo;nvoie;voie;lstreet;lstreet_norm;tcom;crur;cpol;prel;ppart;pfict;cann;dann;dcre;cmajic;tvoie;cdit;dmot\n"
                townfile.write(export)

                for street in alldatas[codedep]['towns'][codetown]['streets']:
                    townfile.write(street)

        docfile.write("| %s - %s | %s | %s |\n" % (codedep, alldatas[codedep]['name'],nbtowns,nbstreets))
        # docfile.write("* **%s - %s**\n" % (codedep, alldatas[codedep]['name']))
        # docfile.write("  * Nombre de communes   : %s\n" % nbtowns)
        # docfile.write("  * Nombre d'adresses    : %s\n" % nbstreets)

    docfile.write("## Statistique totale\n")
    docfile.write("  * Nombre de communes   : %s\n" % allnbtowns)
    docfile.write("  * Nombre d'adresses    : %s\n" % allnbstreets)