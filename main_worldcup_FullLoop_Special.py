# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:22:00 2018

@author: PeerapongE
"""
import random
import operator
import itertools as it
import matplotlib.pyplot as plt
#list of ranking of country in Group#A






def Cal_Chance(Score_A,Score_B):
    Sum_Score  = Score_A + Score_B
    Fraction_A = Score_A / Sum_Score
    Fraction_B = Score_B / Sum_Score
    
    Draw_Fraction = min(Fraction_A, Fraction_B)/3
    
    A_Win = Fraction_A - Draw_Fraction
    Draw  = Draw_Fraction * 2
    B_Win = Fraction_B - Draw_Fraction
    
    Chance_List = [A_Win, Draw, B_Win]
    
    return Chance_List


# Google: Pytyon random between 0 and 1
# https://stackoverflow.com/questions/33359740/random-number-between-0-and-1-in-python

def Cal_Result(Chance_List):
    
    A_Win_Cut = Chance_List[0]
    Draw_Cut  = Chance_List[0] + Chance_List[1]
    
    Rand = random.uniform(0, 1)
    if Rand < A_Win_Cut:
        Result = 'A'
    elif Rand < Draw_Cut:
        Result = 'Draw'
    else :
        Result = 'B'
        
    return Result
    

def Cal_Win_Country(Country_A, Country_B, CountryFIFA):
    
    
    Chance_List = Cal_Chance(CountryFIFA[Country_A], CountryFIFA[Country_B])
    
    Result = Cal_Result(Chance_List)
    # Interpret the result
    if Result == 'A':
        Victory = Country_A
    if Result == 'B':
        Victory = Country_B
    if Result == 'Draw':
        Victory = 'Draw'
    return Victory


CountryFIFA  = {
'Belgium':1727,
'France':1726,
'Brazil':1676,
'Croatia':1634,
'England':1631,
'Portugal':1614,
'Uruguay':1609,
'Switzerland':1599,
'Spain':1591,
'Denmark':1589,
'Argentina':1582,
'Colombia':1575,
'Chile':1565,
'Sweden':1560,
'Netherlands':1560,
'Germany':1558,
'Mexico':1540,
'Italy':1539,
'Wales':1525,
'Poland':1518,
'Peru':1518,
'Austria':1509,
'Senegal':1505,
'Romania':1501,
'United States':1497,
'Tunisia':1493,
'Slovakia':1483,
'Ukraine':1482,
'Iran':1481,
'Serbia':1481,
'Venezuela':1478,
'Paraguay':1476,
'Republic of Ireland':1474,
'Bosnia-Herzegovina':1472,
'Northern Ireland':1465,
'Costa Rica':1464,
'Iceland':1452,
'Scotland':1446,
'Turkey':1443,
'Morocco':1440,
'Australia':1436,
'Czech Republic':1435,
'Greece':1428,
'Nigeria':1427,
'Montenegro':1427,
'Bulgaria':1425,
'Norway':1425,
'Russia':1424,
'Congo DR':1420,
'Japan':1414,
'Hungary':1412,
'Ghana':1412,
'Korea Republic':1405,
'Jamaica':1404,
'Cameroon':1394,
'Egypt':1393,
'Ecuador':1382,
'Finland':1378,
'Bolivia':1374,
'Albania':1372,
'Burkina Faso':1371,
'Slovenia':1369,
'Honduras':1369,
'Mali':1363,
"Côte d'Ivoire":1356,
'Guinea':1354,
'Algeria':1347,
'FYR Macedonia':1343,
'Saudi Arabia':1335,
'El Salvador':1327,
'Panama':1326,
'Cape Verde Islands':1325,
'South Africa':1325,
'Syria':1322,
'Uganda':1320,
'China PR':1317,
'Belarus':1317,
'Canada':1314,
'UAE':1309,
'Curaçao':1306,
'Lebanon':1296,
'Oman':1295,
'Zambia':1292,
'Congo':1280,
'Gabon':1277,
'Luxembourg':1276,
'Cyprus':1276,
'Iraq':1271,
'Georgia':1269,
'Israel':1265,
'Kyrgyzstan':1264,
'Trinidad and Tobago':1260,
'Qatar':1258,
'Benin':1257,
'Uzbekistan':1251,
'Estonia':1242,
'India':1240,
'Faroe Islands':1238,
'Palestine':1236,
'Vietnam':1229,
'Mauritania':1222,
'Armenia':1222,
'Haiti':1219,
'Libya':1217,
'Kenya':1210,
'Madagascar':1209,
'Azerbaijan':1206,
'Niger':1205,
'Korea DPR':1196,
'Jordan':1196,
'Namibia':1191,
'Central African Republic':1180,
'Bahrain':1178,
'Zimbabwe':1175,
'Sierra Leone':1172,
'Philippines':1171,
'Mozambique':1167,
'Thailand':1160,
'Kazakhstan':1159,
'Tajikistan':1158,
'Guinea-Bissau':1158,
'New Zealand':1157,
'Togo':1136,
'Chinese Taipei':1134,
'Angola':1131,
'Antigua and Barbuda':1126,
'Sudan':1120,
'Turkmenistan':1120,
'Nicaragua':1119,
'Malawi':1115,
'Kosovo':1113,
'Latvia':1112,
'Andorra':1111,
'Lithuania':1111,
'Yemen':1106,
'St. Kitts and Nevis':1105,
'Rwanda':1094,
'Tanzania':1087,
'Myanmar':1085,
'Burundi':1085,
'Hong Kong':1078,
'Swaziland':1078,
'Comoros':1076,
'Solomon Islands':1073,
'Botswana':1071,
'Lesotho':1069,
'Afghanistan':1068,
'Equatorial Guinea':1063,
'Guatemala':1061,
'Liberia':1051,
'Ethiopia':1049,
'Maldives':1046,
'Suriname':1037,
'Dominican Republic':1036,
'New Caledonia':1036,
'Mauritius':1022,
'Tahiti':1020,
'Kuwait':1018,
'Indonesia':1003,
'Belize':1002,
'Nepal':1001,
'Barbados':998,
'Vanuatu':996,
'South Sudan':994,
'Singapore':991,
'Gambia':986,
'Malaysia':985,
'Papua New Guinea':984,
'Fiji':981,
'Moldova':979,
'St. Lucia':976,
'Cambodia':970,
'Grenada':968,
'Cuba':963,
'Chad':956,
'Bermuda':952,
'Guyana':951,
'Dominica':950,
'Puerto Rico':948,
'St. Vincent / Grenadines':946,
'Liechtenstein':937,
'Malta':926,
'Macao':925,
'Laos':923,
'São Tomé e Príncipe':920,
'Bhutan':917,
'Aruba':916,
'Mongolia':915,
'Seychelles':911,
'Cook Islands':908,
'American Samoa':908,
'Guam':907,
'Bangladesh':907,
'Gibraltar':905,
'Brunei':903,
'Timor-Leste':900,
'Samoa':896,
'Djibouti':896,
'Pakistan':888,
'Montserrat':887,
'Sri Lanka':886,
'US Virgin Islands':881,
'Cayman Islands':874,
'Tonga':868,
'Eritrea':868,
'Somalia':868,
'British Virgin Islands':867,
'Turks and Caicos Islands':864,
'Anguilla':864,
'Bahamas':858,
'San Marino':854,
}

#User input here, the country name must be consistent with CountryFIFA dictionary

Country_List = ['Bahrain', 'Thailand', 'India', 'UAE'] # GroupA
#Country_List = ['Portugal', 'Spain', 'Morocco', 'Iran'] # GroupB
#Country_List = ['France', 'Australia', 'Peru', 'Denmark'] # GroupC
#Country_List = ['Argentina', 'Iceland', 'Croatia', 'Nigeria'] # GroupD
#Country_List = ['Brazil', 'Switzerland', 'Costa Rica', 'Serbia'] # GroupE
#Country_List = ['Germany', 'Mexico', 'Sweden', 'South Korea'] # GroupF
#Country_List = ['Belgium', 'Panama', 'Tunisia', 'England'] # GroupG
#Country_List = ['Poland', 'Senegal', 'Colombia', 'Japan'] # GroupH


NumSim = 10000 # Number of simulation runs

Country_Point_Zero = {}

#Initialize the dict
for Country in Country_List :
    Country_Point_Zero[Country] = 0

CountryAverage = Country_Point_Zero.copy()

Match_All_List = list(it.combinations(Country_List, 2))


Qualified_List = [] #A list to collect qualified country (2 teams) for 2nd round
Leader_List = [] #A List to collect winner from the group

for i in range(0,NumSim):
    
    CountryPoint = Country_Point_Zero.copy()
    # All Matches - 1 to 6
    
    for Match_Competition in Match_All_List :
        Country_A = Match_Competition[0]
        Country_B = Match_Competition[1]

        Winner = Cal_Win_Country(Country_A, Country_B, CountryFIFA)

        if Winner in CountryFIFA :
            CountryPoint[Winner]   = CountryPoint[Winner] + 3
        else :
            CountryPoint[Country_A] = CountryPoint[Country_A] + 1
            CountryPoint[Country_B] = CountryPoint[Country_B] + 1

    # Completed, summarize the result
    
    print(CountryPoint)

    Sorted_Country = sorted(CountryPoint.items(), key=operator.itemgetter(1))
    print(Sorted_Country)

    #Country name sorted
    Pass1  = Sorted_Country[3][0]
    Pass2  = Sorted_Country[2][0]
    Pass3  = Sorted_Country[1][0]
    Pass4  = Sorted_Country[0][0]
    
    # Sorted Score
    Score1 = Sorted_Country[3][1]
    Score2 = Sorted_Country[2][1]
    Score3 = Sorted_Country[1][1]
    Score4 = Sorted_Country[0][1]
    
    # Collect data with correction on same score sorted, will honor team with better FIFA score
    
    # Collect Qualified_List
    #collect both leader the 1st runner-up
    
    Qualified_List.append(Pass1) # First collect the leader
    
    if Score2 != Score3 : # The runner-up might have conflict with the 3rd
        Qualified_List.append(Pass2)
    else :
        if CountryFIFA[Pass2] >= CountryFIFA[Pass3]:
            Qualified_List.append(Pass2)
        else :
            Qualified_List.append(Pass3)
        
        
    # Collect Leader_List
    if Score1 != Score2 :
        Leader_List.append(Pass1) # Collect only the leader
    else :
        if CountryFIFA[Pass1] >= CountryFIFA[Pass2]:
            Leader_List.append(Pass1)
        else :
            Leader_List.append(Pass2)
    

    CountryAverage[Pass1] += Score1 / NumSim
    CountryAverage[Pass2] += Score2 / NumSim    
    CountryAverage[Pass3] += Score3 / NumSim
    CountryAverage[Pass4] += Score4 / NumSim

# Calculate Chance
Quanlified_Chance = [0,0,0,0]
Leader_Chance     = [0,0,0,0]

for i in range(0,len(Country_List)):
    Quanlified_Chance[i] = Qualified_List.count(Country_List[i])/NumSim
    Leader_Chance[i]     = Leader_List.count(Country_List[i])/NumSim

print('----------Summary for Qualifier---------')
Country = Country_List[0]
print('Chance of ' + Country + ' to proceed next round is ' + str(Qualified_List.count(Country)/NumSim))
Country = Country_List[1]
print('Chance of ' + Country + ' to proceed next round is ' + str(Qualified_List.count(Country)/NumSim))
Country = Country_List[2]
print('Chance of ' + Country + ' to proceed next round is ' + str(Qualified_List.count(Country)/NumSim))
Country = Country_List[3]
print('Chance of ' + Country + ' to proceed next round is ' + str(Qualified_List.count(Country)/NumSim))

print('----------Summary for Winner---------')

Country = Country_List[0]
print('Chance of ' + Country + ' to win the group is ' + str(Leader_List.count(Country)/NumSim))
Country = Country_List[1]
print('Chance of ' + Country + ' to win the group is ' + str(Leader_List.count(Country)/NumSim))
Country = Country_List[2]
print('Chance of ' + Country + ' to win the group is ' + str(Leader_List.count(Country)/NumSim))
Country = Country_List[3]
print('Chance of ' + Country + ' to win the group is ' + str(Leader_List.count(Country)/NumSim))

#Visualization
plt.bar(range(len(Country_List)),Leader_Chance,tick_label=Country_List)
plt.ylabel('Prob')
plt.title('Chance of Winning the Group')
plt.savefig('Winning the group.png')
plt.show()

plt.bar(range(len(Country_List)),Quanlified_Chance,tick_label=Country_List)
plt.ylabel('Prob')
plt.title('Chance of Quanlify to next round')
plt.savefig('Quanlify to next round.png')
plt.show()

print('----------Summary for Predicted Score Table---------')
print(CountryAverage)
