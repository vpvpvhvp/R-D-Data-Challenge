#!/usr/bin/env python3
 
import time, random
import math
from collections import deque

f = open('CAN_Dataset.txt','r')

a = []
count = 0
amount = 0
avg = 0
dos_flag = 0
dos_p = 0
sumfor_avg = 0 
training_flag = 0
fuzzy_flag = 0
fuzzy_token = 0
fuzzy_ids = {'test' : 0}
Window_Size = 40
Jump_Size = 50
colorMap = ["g", "r", "b", "y"]

def abs_min(a, b):
    if(a < 0):
        a = a * -1

    if(b < 0):
        b = b * -1

    if(a < b):
        return a
    return b

def max(a, b):
    if(a > b):
        return a
    return b

def training():

    global training_flag, count, sumfor_avg, avg, fuzzy_ids
    
    training_flag = 1

    avg = 708
    fuzzy_ids = {'1200': 0, '344': 1, '345': 1, '346': 1, '347': 1, '340': 1, '341': 1, '342': 1, '343': 1, '348': 1, '349': 1, '298': 1, '299': 1, '296': 1, '297': 1, '294': 1, '295': 1, '292': 1, '293': 1, '290': 1, '291': 1, '270': 1, '271': 1, '272': 0, '273': 1, '274': 1, '275': 1, '276': 1, '277': 1, '278': 1, '279': 1, '1004': 1, '108': 1, '109': 1, '102': 1, '103': 1, '100': 1, '101': 1, '106': 1, '107': 1, '104': 1, '105': 1, '1213': 1, '1655': 1, '99': 1, '98': 1, '91': 1, '90': 1, '93': 1, '92': 1, '95': 1, '94': 1, '97': 1, '96': 1, '1623': 1, '1622': 1, '1621': 1, '1620': 1, '1627': 1, '1626': 1, '1625': 1, '1624': 1, '1629': 1, '1628': 1, '559': 1, '558': 1, '555': 1, '554': 1, '557': 1, '556': 1, '551': 1, '550': 1, '553': 1, '552': 1, '1199': 1, '1198': 1, '1191': 1, '1190': 1, '1193': 1, '1192': 1, '1195': 1, '1194': 1, '1197': 1, '1196': 1, '1177': 1, '1176': 1, '1175': 1, '1174': 1, '1173': 1, '1172': 1, '1171': 1, '1170': 1, '1179': 1, '1178': 1, '1007': 1, '510': 1, '513': 1, '1285': 1, '1284': 1, '1287': 1, '1286': 1, '1281': 1, '1280': 1, '1283': 1, '1282': 1, '1003': 1, '879': 1, '1289': 1, '1288': 1, '514': 1, '1579': 1, '1578': 1, '689': 1, '688': 0, '1573': 1, '1572': 1, '687': 1, '1000': 1, '681': 1, '680': 1, '683': 1, '1574': 1, '623': 1, '622': 1, '621': 1, '873': 1, '620': 1, '627': 1, '1222': 1, '1221': 1, '624': 1, '1371': 1, '406': 1, '1373': 1, '1372': 1, '1375': 1, '1374': 1, '1377': 1, '400': 1, '1379': 1, '1378': 1, '452': 1, '409': 1, '408': 1, '453': 1, '454': 1, '455': 1, '456': 1, '457': 1, '379': 1, '378': 1, '647': 1, '371': 1, '370': 1, '373': 1, '372': 1, '375': 1, '374': 1, '377': 1, '376': 1, '1244': 1, '393': 1, '392': 1, '391': 1, '390': 1, '397': 1, '396': 1, '395': 1, '394': 1, '399': 0, '398': 1, '1246': 1, '245': 1, '244': 1, '247': 1, '246': 1, '241': 1, '240': 1, '243': 1, '242': 1, '249': 1, '248': 1, '179': 1, '178': 1, '177': 1, '176': 1, '175': 1, '174': 1, '173': 1, '172': 1, '171': 1, '170': 1, '656': 1, '1503': 1, '1500': 1, '1501': 1, '652': 1, '653': 1, '1504': 1, '651': 1, '1364': 1, '1115': 1, '1362': 1, '1618': 1, '1619': 1, '1616': 1, '1617': 1, '1614': 1, '1615': 1, '1612': 1, '1613': 1, '1610': 1, '1611': 1, '1142': 1, '1143': 1, '1140': 1, '1141': 1, '1146': 1, '1147': 1, '1144': 1, '1145': 1, '1148': 1, '1149': 1, '692': 1, '1547': 1, '1544': 1, '1545': 1, '696': 1, '697': 1, '694': 1, '1541': 1, '698': 1, '699': 1, '1548': 1, '1549': 1, '542': 1, '543': 1, '540': 1, '541': 1, '546': 1, '547': 1, '544': 0, '545': 1, '548': 1, '549': 1, '761': 1, '414': 1, '415': 1, '416': 1, '417': 1, '410': 1, '411': 1, '412': 1, '413': 1, '1384': 1, '1385': 1, '1386': 1, '1387': 1, '1380': 1, '419': 1, '1382': 1, '1383': 1, '368': 1, '369': 1, '366': 1, '367': 1, '364': 1, '365': 1, '362': 1, '363': 1, '360': 1, '361': 1, '380': 1, '381': 1, '382': 1, '383': 1, '384': 1, '385': 1, '386': 1, '387': 1, '388': 1, '389': 1, '1077': 1, '258': 1, '259': 1, '252': 1, '253': 1, '250': 1, '251': 1, '256': 1, '257': 1, '254': 1, '255': 1, '168': 1, '169': 1, '164': 1, '165': 1, '166': 1, '167': 1, '160': 0, '161': 0, '162': 1, '163': 1, '1090': 1, '1091': 1, '1093': 1, '670': 1, '671': 1, '1609': 1, '1608': 1, '1601': 1, '1600': 1, '1603': 1, '1602': 1, '1605': 1, '1604': 1, '1607': 1, '1606': 1, '809': 0, '808': 1, '803': 1, '802': 1, '801': 1, '800': 1, '807': 1, '806': 1, '805': 1, '804': 1, '608': 0, '1159': 1, '1158': 1, '1155': 1, '1154': 1, '1157': 1, '1156': 1, '1151': 1, '1150': 1, '1153': 1, '1152': 1, '1555': 1, '58': 1, '1551': 1, '1550': 1, '1553': 1, '1552': 1, '59': 1, '1554': 1, '1557': 1, '1556': 1, '1559': 1, '54': 1, '57': 1, '56': 1, '51': 1, '50': 1, '53': 1, '52': 0, '537': 1, '55': 1, '535': 1, '534': 1, '533': 1, '532': 1, '531': 1, '1558': 1, '539': 1, '538': 1, '536': 1, '429': 1, '428': 1, '1399': 1, '1398': 1, '1397': 1, '420': 1, '1395': 1, '1394': 1, '425': 1, '424': 1, '1391': 1, '426': 1, '530': 1, '853': 1, '229': 1, '228': 1, '227': 1, '226': 1, '225': 1, '224': 1, '223': 1, '222': 1, '221': 1, '220': 1, '151': 1, '150': 1, '153': 1, '152': 1, '155': 1, '154': 1, '157': 1, '156': 1, '159': 1, '158': 1, '1293': 1, 'test': 1, '1256': 1, '690': 1, '1525': 1, '1526': 1, '818': 1, '0': 0, '1527': 1, '810': 1, '811': 1, '812': 1, '813': 1, '814': 1, '815': 1, '816': 1, '817': 1, '1522': 1, '1523': 1, '1490': 1, '1491': 1, '1492': 1, '1493': 1, '1494': 1, '1495': 1, '1496': 1, '1497': 1, '1498': 1, '1499': 1, '423': 1, '422': 1, '1393': 1, '1392': 1, '427': 1, '1390': 1, '1128': 1, '1129': 1, '1120': 1, '1121': 1, '1122': 1, '1123': 1, '1124': 1, '1125': 1, '1126': 1, '1127': 1, '524': 1, '525': 1, '526': 1, '527': 1, '1018': 1, '1019': 1, '522': 1, '523': 1, '1014': 1, '1015': 1, '1016': 1, '1017': 1, '1010': 1, '1011': 1, '1012': 1, '1013': 1, '1234': 1, '1235': 1, '1236': 1, '1237': 1, '1230': 1, '1231': 1, '1232': 1, '1233': 1, '1238': 1, '1239': 1, '438': 1, '439': 1, '436': 1, '437': 1, '434': 1, '435': 1, '432': 1, '433': 1, '430': 1, '431': 1, '238': 1, '239': 1, '234': 1, '235': 1, '236': 1, '237': 1, '230': 1, '231': 1, '232': 1, '233': 1, '1': 1, '146': 1, '147': 1, '144': 1, '145': 1, '142': 1, '143': 1, '140': 1, '141': 1, '148': 1, '149': 1, '123': 1, '939': 1, '938': 1, '933': 1, '932': 1, '931': 1, '930': 1, '937': 1, '936': 1, '935': 1, '934': 1, '829': 1, '828': 1, '825': 1, '824': 1, '827': 1, '826': 1, '821': 1, '820': 1, '823': 1, '822': 1, '1483': 1, '1482': 1, '1481': 1, '1480': 1, '1487': 1, '1486': 1, '1485': 1, '1484': 1, '1489': 1, '1488': 1, '797': 1, '796': 1, '795': 1, '794': 1, '793': 1, '792': 1, '791': 1, '790': 0, '799': 1, '798': 1, '1270': 1, '613': 1, '1272': 1, '1139': 1, '1138': 1, '1133': 1, '1132': 1, '1131': 1, '1130': 1, '1137': 1, '1136': 1, '1135': 1, '1134': 1, '1276': 1, '1277': 1, '519': 1, '518': 1, '1009': 1, '1008': 1, '511': 1, '1006': 1, '1005': 1, '512': 1, '515': 1, '1002': 1, '1001': 1, '516': 1, '1227': 1, '1226': 1, '1225': 1, '1224': 1, '1223': 1, '626': 1, '625': 1, '1220': 1, '629': 1, '628': 1, '1229': 1, '1228': 1, '2': 1, '11': 1, '10': 1, '13': 1, '12': 1, '15': 1, '14': 1, '17': 1, '16': 1, '19': 1, '18': 1, '201': 1, '200': 1, '203': 1, '202': 1, '205': 1, '204': 1, '207': 1, '206': 1, '209': 1, '208': 1, '685': 1, '684': 1, '1571': 1, '686': 1, '1577': 1, '1576': 1, '1575': 1, '682': 1, '928': 1, '929': 1, '920': 1, '921': 1, '922': 1, '923': 1, '924': 1, '925': 1, '926': 1, '927': 1, '832': 1, '833': 1, '830': 1, '831': 1, '836': 1, '837': 1, '834': 1, '835': 1, '838': 1, '839': 1, '3': 1, '784': 1, '785': 1, '786': 1, '787': 1, '780': 1, '781': 1, '782': 1, '783': 1, '788': 1, '789': 1, '60': 1, '61': 1, '62': 1, '63': 1, '64': 1, '65': 1, '66': 0, '67': 0, '68': 0, '69': 1, '407': 1, '1588': 1, '1589': 1, '1370': 1, '1582': 1, '1583': 1, '1580': 1, '1581': 1, '1586': 1, '405': 1, '1584': 1, '1585': 1, '1038': 1, '404': 1, '508': 1, '509': 1, '1032': 1, '507': 1, '1030': 1, '505': 1, '502': 1, '503': 1, '500': 1, '402': 1, '1212': 1, '631': 1, '632': 1, '1211': 1, '1216': 1, '635': 1, '636': 1, '1215': 1, '638': 1, '639': 1, '1218': 1, '1219': 1, '465': 1, '1106': 1, '1455': 1, '1104': 1, '1457': 1, '1450': 1, '1451': 1, '1100': 1, '1101': 1, '1458': 1, '1459': 1, '1108': 1, '1570': 1, '216': 1, '217': 1, '214': 1, '215': 1, '212': 1, '213': 1, '210': 1, '211': 1, '218': 1, '219': 1, '4': 1, '919': 1, '918': 1, '915': 1, '914': 0, '917': 1, '916': 1, '911': 1, '910': 1, '913': 1, '912': 1, '458': 1, '847': 1, '846': 1, '845': 1, '844': 1, '843': 1, '842': 1, '841': 1, '840': 1, '849': 1, '848': 0, '663': 1, '1587': 1, '662': 1, '1039': 1, '753': 1, '752': 1, '751': 1, '750': 1, '757': 1, '756': 1, '755': 1, '754': 1, '759': 1, '758': 1, '1595': 1, '506': 1, '1597': 1, '1596': 1, '1591': 1, '1590': 1, '1593': 1, '1033': 1, '1599': 1, '1598': 1, '1025': 1, '1024': 1, '1027': 1, '1031': 1, '1021': 1, '1020': 1, '1023': 1, '1022': 1, '1036': 1, '1029': 1, '1028': 1, '1037': 1, '1034': 1, '501': 1, '605': 1, '630': 1, '607': 1, '606': 1, '1209': 1, '1208': 1, '603': 1, '602': 1, '1205': 1, '1204': 1, '1207': 1, '1206': 1, '609': 1, '1210': 1, '1203': 1, '1202': 1, '633': 1, '634': 1, '1217': 1, '1214': 1, '637': 1, '1447': 1, '1446': 1, '1445': 1, '1444': 1, '5': 1, '1442': 0, '1441': 1, '1440': 0, '1119': 1, '1118': 1, '1351': 1, '1449': 1, '1448': 1, '1350': 1, '461': 1, '1356': 1, '463': 1, '489': 1, '488': 1, '487': 1, '486': 1, '485': 1, '1354': 1, '483': 1, '482': 1, '481': 1, '480': 1, '695': 1, '199': 1, '198': 1, '195': 1, '194': 1, '197': 1, '196': 1, '191': 1, '190': 1, '193': 1, '192': 1, '1454': 1, '1107': 1, '1456': 1, '1105': 1, '1102': 1, '1103': 1, '1452': 1, '1453': 1, '902': 1, '903': 1, '900': 1, '901': 1, '906': 1, '907': 1, '904': 1, '905': 1, '908': 1, '909': 1, '1109': 1, '854': 1, '855': 1, '856': 1, '857': 1, '850': 1, '851': 1, '852': 1, '819': 1, '858': 1, '859': 1, '6': 1, '740': 1, '741': 1, '742': 1, '743': 1, '744': 1, '745': 1, '746': 1, '747': 1, '748': 1, '749': 1, '1050': 1, '1051': 1, '1052': 1, '1053': 1, '1054': 1, '1055': 1, '1056': 1, '1057': 1, '1058': 1, '1059': 1, '1278': 1, '1279': 1, '618': 1, '619': 1, '612': 1, '1271': 1, '610': 1, '611': 1, '616': 1, '617': 1, '614': 1, '615': 1, '1472': 1, '1473': 1, '1470': 1, '1471': 1, '1476': 1, '1477': 1, '1474': 1, '1475': 1, '1478': 1, '1479': 1, '1304': 1, '1305': 1, '1306': 0, '1307': 1, '1300': 1, '1301': 1, '1302': 1, '1303': 0, '1308': 1, '1309': 1, '498': 1, '499': 1, '494': 1, '495': 1, '496': 1, '497': 0, '490': 1, '491': 1, '492': 1, '493': 1, '24': 0, '25': 1, '26': 1, '27': 1, '20': 1, '21': 1, '22': 1, '23': 1, '28': 1, '29': 1, '7': 1, '972': 1, '591': 1, '590': 1, '1085': 1, '592': 1, '1083': 1, '594': 1, '977': 1, '976': 1, '975': 1, '974': 1, '973': 1, '1081': 1, '971': 1, '970': 1, '596': 1, '979': 1, '978': 1, '182': 1, '183': 1, '180': 1, '181': 1, '186': 1, '187': 1, '184': 1, '185': 1, '188': 1, '189': 1, '869': 1, '868': 1, '861': 1, '860': 1, '863': 1, '862': 1, '865': 1, '864': 1, '867': 1, '866': 1, '883': 1, '882': 1, '881': 1, '880': 0, '887': 1, '886': 1, '885': 1, '884': 1, '889': 1, '888': 1, '775': 1, '774': 1, '777': 1, '776': 1, '771': 1, '770': 1, '773': 1, '772': 1, '779': 1, '778': 1, '77': 1, '76': 1, '75': 1, '74': 1, '73': 1, '72': 1, '71': 1, '70': 1, '79': 1, '78': 1, '1043': 1, '1042': 1, '1041': 1, '1040': 1, '1047': 1, '1046': 1, '1045': 1, '1044': 1, '1049': 1, '1048': 1, '1680': 0, '1269': 1, '1268': 1, '669': 1, '668': 1, '667': 1, '1262': 1, '665': 1, '664': 1, '1267': 1, '1266': 0, '1265': 0, '1264': 0, '421': 1, '1469': 1, '1468': 1, '1465': 1, '1464': 1, '1467': 1, '1466': 1, '1461': 1, '1460': 1, '1463': 1, '1462': 1, '1317': 1, '1316': 1, '1315': 1, '1314': 1, '1313': 1, '1311': 1, '1310': 1, '1319': 1, '1318': 1, '528': 1, '464': 1, '529': 1, '319': 1, '318': 1, '313': 1, '312': 1, '311': 1, '310': 1, '317': 1, '316': 1, '315': 1, '314': 1, '443': 1, '1334': 1, '1337': 1, '440': 1, '447': 1, '446': 1, '1333': 1, '1332': 1, '403': 1, '1521': 1, '280': 1, '964': 1, '965': 1, '966': 1, '967': 1, '960': 1, '961': 1, '962': 1, '963': 1, '401': 1, '968': 1, '969': 1, '286': 1, '1241': 1, '878': 1, '1240': 1, '876': 1, '877': 1, '874': 1, '875': 1, '872': 1, '1243': 1, '870': 1, '871': 1, '1242': 1, '9': 1, '1245': 1, '1532': 1, '890': 1, '891': 1, '892': 1, '893': 1, '894': 1, '895': 1, '896': 1, '897': 1, '898': 0, '899': 1, '1530': 1, '1249': 1, '1248': 1, '641': 1, '768': 1, '769': 1, '762': 1, '763': 1, '760': 1, '640': 1, '766': 1, '767': 1, '764': 1, '765': 1, '1078': 1, '1079': 1, '1076': 1, '1535': 1, '1074': 1, '1075': 1, '1072': 1, '1073': 1, '1070': 1, '1071': 1, '1678': 1, '1679': 1, '1674': 1, '1675': 1, '1676': 1, '1677': 1, '1670': 1, '1671': 1, '1672': 1, '1673': 1, '1094': 1, '1095': 1, '1096': 1, '1097': 1, '678': 1, '679': 1, '1092': 1, '1534': 1, '674': 1, '675': 1, '676': 1, '677': 1, '1098': 1, '1099': 1, '672': 0, '673': 1, '1533': 1, '1418': 1, '1419': 1, '1410': 1, '1411': 1, '1412': 1, '1413': 1, '1414': 1, '1415': 0, '1416': 1, '1417': 1, '1322': 1, '1323': 1, '1320': 1, '1321': 1, '1326': 1, '1327': 1, '1324': 1, '1325': 1, '1328': 1, '1329': 1, '1531': 1, '1524': 1, '1257': 1, '1254': 1, '1255': 1, '1520': 0, '1253': 1, '1250': 1, '1251': 1, '1528': 1, '1529': 1, '1258': 1, '1259': 1, '308': 1, '309': 1, '300': 1, '301': 1, '302': 1, '303': 1, '304': 1, '305': 1, '306': 1, '307': 1, '473': 1, '471': 1, '959': 1, '958': 1, '951': 1, '950': 1, '953': 1, '952': 1, '955': 1, '954': 1, '957': 1, '956': 1, '477': 1, '1263': 1, '666': 1, '504': 1, '1261': 1, '1260': 1, '719': 1, '718': 1, '717': 1, '716': 1, '715': 1, '714': 1, '713': 1, '712': 1, '711': 1, '710': 1, '661': 1, '660': 1, '1069': 1, '1068': 1, '1061': 1, '1060': 1, '1063': 1, '1062': 1, '1065': 1, '1064': 1, '1067': 1, '1066': 1, '1669': 1, '1668': 1, '1667': 1, '1666': 1, '1665': 1, '1664': 1, '1663': 1, '1662': 1, '1661': 1, '1660': 1, '1087': 0, '1086': 1, '593': 1, '1084': 1, '595': 1, '1082': 1, '597': 1, '1080': 1, '599': 1, '598': 1, '1089': 1, '1088': 0, '1409': 1, '1408': 1, '1403': 1, '1402': 1, '1401': 1, '1400': 1, '1407': 1, '1406': 1, '1405': 1, '1404': 1, '1546': 1, '449': 1, '448': 1, '1339': 1, '1338': 1, '693': 1, '1335': 1, '442': 1, '441': 1, '1336': 1, '1331': 1, '1330': 1, '445': 1, '444': 1, '691': 1, '1542': 1, '1543': 1, '39': 1, '38': 1, '1540': 1, '33': 1, '32': 1, '31': 1, '30': 1, '37': 1, '36': 1, '35': 1, '34': 1, '1537': 1, '1536': 1, '643': 1, '642': 1, '645': 1, '644': 1, '1247': 1, '646': 1, '649': 1, '648': 1, '1539': 1, '1538': 1, '339': 0, '338': 1, '335': 1, '334': 1, '337': 1, '336': 1, '331': 1, '330': 1, '333': 1, '332': 1, '8': 1, '948': 1, '949': 1, '946': 1, '947': 1, '944': 1, '945': 1, '942': 1, '943': 1, '940': 1, '941': 1, '133': 1, '132': 1, '131': 1, '130': 1, '137': 1, '136': 1, '135': 1, '134': 1, '139': 1, '138': 1, '2010': 1, '708': 1, '709': 1, '704': 0, '705': 1, '706': 1, '707': 1, '700': 1, '701': 1, '702': 1, '703': 1, '88': 1, '89': 1, '82': 1, '83': 1, '80': 0, '81': 1, '86': 1, '87': 1, '84': 1, '85': 1, '1658': 1, '1659': 1, '1652': 1, '1653': 1, '1650': 1, '1651': 1, '1656': 1, '1657': 1, '1654': 1, '1389': 1, '586': 1, '587': 1, '584': 1, '585': 1, '582': 1, '583': 1, '580': 1, '581': 1, '588': 1, '589': 1, '1633': 1, '1436': 1, '1437': 1, '1434': 1, '1435': 0, '1432': 1, '1433': 1, '1430': 1, '1431': 1, '418': 1, '1438': 1, '1439': 1, '1349': 0, '1348': 1, '459': 1, '450': 1, '451': 1, '1342': 1, '1343': 1, '1344': 1, '1345': 1, '1346': 1, '1347': 1, '517': 1, '1502': 1, '657': 1, '654': 1, '655': 1, '1506': 1, '1507': 1, '650': 1, '1505': 1, '1508': 0, '1509': 1, '658': 1, '659': 1, '1292': 1, '1376': 1, '322': 1, '323': 1, '320': 1, '321': 1, '326': 1, '327': 1, '324': 1, '325': 1, '328': 1, '329': 1, '1340': 1, '1594': 1, '1341': 1, '1592': 1, '995': 1, '994': 1, '997': 1, '996': 1, '991': 1, '990': 1, '992': 1, '999': 1, '998': 1, '120': 1, '121': 1, '122': 1, '1026': 1, '124': 1, '125': 1, '126': 1, '127': 1, '128': 0, '129': 0, '520': 1, '521': 1, '1645': 1, '1644': 1, '1647': 1, '1646': 1, '1641': 1, '1640': 1, '1643': 1, '1642': 1, '1396': 1, '1649': 1, '1648': 1, '1252': 1, '579': 1, '578': 1, '604': 1, '573': 1, '572': 1, '571': 1, '570': 1, '577': 1, '576': 1, '575': 1, '574': 1, '601': 1, '600': 1, '1421': 1, '1420': 1, '1423': 1, '1422': 1, '1425': 1, '1424': 1, '1427': 1, '1426': 1, '1429': 1, '1428': 1, '731': 1, '730': 1, '733': 1, '732': 1, '735': 1, '734': 1, '737': 1, '736': 1, '739': 1, '738': 1, '1359': 1, '1358': 1, '469': 1, '468': 1, '1353': 1, '1352': 1, '467': 1, '466': 1, '1357': 1, '460': 1, '1355': 1, '462': 1, '1273': 1, '1519': 1, '1518': 1, '1515': 1, '1514': 1, '1517': 1, '1516': 1, '1511': 1, '1510': 1, '1513': 1, '1512': 1, '1275': 1, '357': 0, '356': 0, '355': 1, '354': 1, '353': 1, '352': 1, '351': 1, '350': 1, '359': 1, '358': 1, '1111': 1, '1110': 1, '1113': 1, '289': 1, '288': 0, '1112': 1, '281': 1, '1443': 1, '283': 1, '282': 1, '285': 1, '284': 1, '287': 1, '1114': 1, '1117': 1, '1116': 1, '263': 1, '262': 1, '261': 1, '260': 1, '267': 1, '266': 1, '265': 1, '264': 1, '269': 1, '268': 1, '1290': 1, '1291': 1, '1564': 1, '1565': 1, '1566': 1, '1567': 1, '988': 1, '989': 1, '982': 1, '983': 1, '980': 1, '981': 1, '986': 1, '987': 1, '984': 1, '985': 1, '115': 1, '114': 1, '117': 1, '116': 1, '111': 1, '110': 1, '113': 1, '112': 1, '119': 1, '118': 1, '1388': 1, '1035': 1, '1630': 1, '1631': 1, '1632': 1, '484': 1, '1634': 1, '1635': 1, '1636': 1, '1637': 1, '1638': 1, '1639': 1, '568': 1, '569': 1, '560': 1, '561': 1, '562': 1, '563': 1, '564': 1, '565': 1, '566': 1, '567': 1, '1188': 1, '1189': 1, '1186': 1, '1187': 1, '1184': 1, '1185': 1, '1182': 1, '1183': 1, '1180': 1, '1181': 1, '726': 1, '727': 1, '724': 1, '725': 1, '722': 1, '723': 1, '720': 1, '721': 1, '728': 1, '729': 1, '1164': 1, '1165': 1, '1166': 1, '1167': 1, '1160': 1, '1161': 1, '1162': 1, '1163': 1, '1168': 1, '1169': 1, '472': 1, '48': 1, '49': 1, '46': 1, '47': 1, '44': 1, '45': 1, '42': 1, '43': 1, '40': 1, '41': 1, '1568': 1, '1569': 1, '1298': 1, '1299': 1, '1560': 1, '1561': 1, '1562': 1, '1563': 1, '1296': 0, '1297': 1, '1294': 1, '1295': 1, '1360': 1, '1361': 1, '1381': 1, '1201': 0, '1366': 1, '1367': 1, '470': 1, '1365': 1, '476': 1, '1363': 1, '474': 1, '475': 1, '478': 1, '479': 1, '1368': 1, '1369': 1}

def DoS_Attack_Detect(i, Window_Size, threshold):

    global a,count,amount,avg,dos_flag,dos_p,sumfor_avg,training_flag

    i_id = int(i.split()[3],16)

    i_time = i.split()[1]

    if( dos_flag == 0 ):
        count = count + 1
        if(training_flag == 0):
            sumfor_avg += i_id
            avg = sumfor_avg / count

    if( count < Window_Size ):
        a.append(int(i_id))

    else:
        try: 
            a[Window_Size-1] = int(i_id)
        except:
            a.append(i_id)          

    amount += i_id

    if( count >= Window_Size ):

        if(dos_flag == 1):
            if(amount / Window_Size > avg * threshold):
                dos_p -= 1
            else:
                dos_p = 0

            if(dos_p < Window_Size*-2.5):
                
                dos_flag = 0
                dos_p = 0



        if(amount / Window_Size < avg * threshold and dos_flag == 0 and count > 1000):
            dos_flag = 1
            dos_p = 0

        amount -= a[0]
        a[0:Window_Size-1] = a[1:Window_Size]

def Fuzzy_Attack_Detect(i,fuzzy_window_size):

    global fuzzy_ids, fuzzy_flag, fuzzy_token

    i_id = int(i.split()[3],16)
    i_id = str(i_id)

    if(fuzzy_ids[i_id] == 1):

        fuzzy_token = fuzzy_window_size
        fuzzy_flag = 1

    else:

        fuzzy_token -= 1

    if(fuzzy_token <= 0):

        fuzzy_flag = 0

class RealtimePlot:
    def __init__(self, axes, max_entries = 50000):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)
        self.maxY = 0
        self.minY = 1000000
        self.axes = axes
        self.max_entries = max_entries
        self.lineplot, = axes.plot([], [], "g.")
        self.axes.set_autoscaley_on(True)

    def add(self, x, y, flag):
        print x,y,flag
        if(y > self.maxY): self.maxY = y
        if(y < self.minY): self.minY = y
        self.axis_x.append(x)
        self.axis_y.append(y)
        self.lineplot.set_data(self.axis_x, self.axis_y)
        self.axes.set_xlim(self.axis_x[0], self.axis_x[-1] + 1e-15)
        self.lineplot.set_color(colorMap[flag])
        self.axes.set_ylim(self.minY-30, self.maxY+30)
        self.axes.relim(); self.axes.autoscale_view()

    def animate(self, figure, callback, interval = 50):
        import matplotlib.animation as animation
        def wrapper(frame_index):
            self.add(*callback(frame_index))
            self.axes.relim(); self.axes.autoscale_view()
            return self.lineplot
        animation.FuncAnimation(figure, wrapper, interval=interval)

def main():
    from matplotlib import pyplot as plt
    training()
    fig, axes = plt.subplots()
    display = RealtimePlot(axes)
    lines = f.readlines()
    sT = lines[0].split()[1]
    xT = 0
    PC = 0
    flag = 0
    for i in lines:
        PC = PC + 1
        DoS_Attack_Detect(i, 40, 0.6)
        Fuzzy_Attack_Detect(i, 10)
        if(dos_flag == 1): flag = flag | 1
        if(fuzzy_flag == 1): flag = flag | 2
        if(float(i.split()[1]) - float(sT) > 0.1):
            display.add(xT, PC, flag)
            plt.pause(0.001)
            sT = i.split()[1]
            xT = xT + 0.1
            PC = 0
            flag = 0

if __name__ == "__main__": main()