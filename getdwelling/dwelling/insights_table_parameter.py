"""This module saves the parameters for insight pages. The reason we hardcoded
it is because the result is constant, so it's unnecessary to generate them 
every time and it will be much faster to load with given parameter compared 
with generating parameters every time.
"""

INSIGHTS_PARAMETER = [
    {
        'order': 1,
        'rows': ['Carlton', 'Docklands', 'East Melbourne', 'Kensington',
                 'Melbourne (CBD)', 'Melbourne (Remainder)', 'North Melbourne',
                 'Parkville', 'Port Melbourne', 'South Yarra', 'Southbank',
                 'West Melbourne (Residential)'],
        'columns': [('Dwelling number', 2006), ('Dwelling number', 2007),
                    ('Dwelling number', 2008), ('Dwelling number', 2009),
                    ('Dwelling number', 2010), ('Dwelling number', 2011),
                    ('Dwelling number', 2012), ('Dwelling number', 2013),
                    ('Dwelling number', 2014), ('Dwelling number', 2015),
                    ('Dwelling number', 2016)],
        'spots': [[0, 0, 1539.0], [0, 1, 1575.0], [0, 2, 1575.0],
                  [0, 3, 1571.0], [0, 4, 1571.0], [0, 5, 1571.0],
                  [0, 6, 1574.0], [0, 7, 1574.0], [0, 8, 1588.0],
                  [0, 9, 1588.0], [0, 10, 1609.0], [1, 0, 20.0], [1, 1, 25.0],
                  [1, 2, 25.0], [1, 3, 28.0], [1, 4, 28.0], [1, 5, 28.0],
                  [1, 6, 96.0], [1, 7, 96.0], [1, 8, 136.0], [1, 9, 136.0],
                  [1, 10, 138.0], [2, 0, 666.0], [2, 1, 667.0], [2, 2, 667.0],
                  [2, 3, 703.0], [2, 4, 703.0], [2, 5, 703.0], [2, 6, 709.0],
                  [2, 7, 709.0], [2, 8, 709.0], [2, 9, 709.0], [2, 10, 717.0],
                  [3, 0, 1848.0], [3, 1, 1848.0], [3, 2, 3000.0],
                  [3, 3, 3000.0], [3, 4, 3000.0], [3, 5, 3024.0],
                  [3, 6, 3024.0], [3, 7, 3042.0], [3, 8, 3042.0],
                  [3, 9, 3050.0], [3, 10, 3050.0], [4, 0, 293.0],
                  [4, 1, 292.0], [4, 2, 303.0], [4, 3, 306.0], [4, 4, 306.0],
                  [4, 5, 308.0], [4, 6, 305.0], [4, 7, 310.0], [4, 8, 310.0],
                  [4, 9, 328.0], [4, 10, 326.0], [5, 0, 13.0], [5, 1, 13.0],
                  [5, 2, 15.0], [5, 3, 15.0], [5, 4, 16.0], [5, 5, 16.0],
                  [5, 6, 16.0], [5, 7, 17.0], [5, 8, 17.0], [5, 9, 16.0],
                  [5, 10, 16.0], [6, 0, 1750.0], [6, 1, 1875.0],
                  [6, 2, 1875.0], [6, 3, 1970.0], [6, 4, 1970.0],
                  [6, 5, 1970.0], [6, 6, 2011.0], [6, 7, 2011.0],
                  [6, 8, 2063.0], [6, 9, 2063.0], [6, 10, 2084.0],
                  [7, 0, 538.0], [7, 1, 729.0], [7, 2, 729.0], [7, 3, 729.0],
                  [7, 4, 747.0], [7, 5, 747.0], [7, 6, 743.0], [7, 7, 743.0],
                  [7, 8, 749.0], [7, 9, 749.0], [7, 10, 753.0], [8, 0, 0],
                  [8, 1, 0], [8, 2, 0], [8, 3, 0], [8, 4, 1.0], [8, 5, 1.0],
                  [8, 6, 1.0], [8, 7, 2.0], [8, 8, 2.0], [8, 9, 2.0],
                  [8, 10, 2.0], [9, 0, 758.0], [9, 1, 758.0], [9, 2, 761.0],
                  [9, 3, 761.0], [9, 4, 761.0], [9, 5, 760.0], [9, 6, 760.0],
                  [9, 7, 758.0], [9, 8, 758.0], [9, 9, 760.0], [9, 10, 760.0],
                  [10, 0, 45.0], [10, 1, 45.0], [10, 2, 44.0], [10, 3, 44.0],
                  [10, 4, 44.0], [10, 5, 50.0], [10, 6, 50.0], [10, 7, 56.0],
                  [10, 8, 56.0], [10, 9, 60.0], [10, 10, 60.0], [11, 0, 578.0],
                  [11, 1, 598.0], [11, 2, 598.0], [11, 3, 612.0],
                  [11, 4, 612.0], [11, 5, 612.0], [11, 6, 619.0],
                  [11, 7, 619.0], [11, 8, 632.0], [11, 9, 632.0],
                  [11, 10, 636.0]],
        'title': 'Count of Dwellings per CLUE small area per Census year '
                 'between 2006 and 2016.',
        'argument': 'The top three areas in Melbourne where have most'
                    ' dwellings are: Kensington , North Melbourne, Carlton. '
                    'And this fact keeps constant in the past 10 years, you '
                    'may would like to find the most livable area from '
                    'these areas.',

    },

    {
        'order': 2,
        'rows': ['2012', '2016', 'New Dwelling Number'],
        'columns': [('Dwelling number', 'Carlton'),
                    ('Dwelling number', 'Docklands'),
                    ('Dwelling number', 'East Melbourne'),
                    ('Dwelling number', 'Kensington'),
                    ('Dwelling number', 'Melbourne (CBD)'),
                    ('Dwelling number', 'Melbourne (Remainder)'),
                    ('Dwelling number', 'North Melbourne'),
                    ('Dwelling number', 'Parkville'),
                    ('Dwelling number', 'Port Melbourne'),
                    ('Dwelling number', 'South Yarra'),
                    ('Dwelling number', 'Southbank'),
                    ('Dwelling number', 'West Melbourne (Residential)')],
        'spots': [[0, 0, 8723], [0, 1, 4246], [0, 2, 3050], [0, 3, 4889],
                  [0, 4, 12476], [0, 5, 953], [0, 6, 6744], [0, 7, 2013],
                  [0, 8, 1], [0, 9, 2682], [0, 10, 7335], [0, 11, 1808],

                  [1, 0, 10527], [1, 1, 6012], [1, 2, 3095], [1, 3, 5210],
                  [1, 4, 19430], [1, 5, 963], [1, 6, 7498], [1, 7, 2529],
                  [1, 8, 2], [1, 9, 2735], [1, 10, 10447], [1, 11, 2594],

                  [2, 0, 1804], [2, 1, 1766], [2, 2, 45], [2, 3, 321],
                  [2, 4, 6954], [2, 5, 10], [2, 6, 754], [2, 7, 516],
                  [2, 8, 1], [2, 9, 53], [2, 10, 3112], [2, 11, 786]],

        'title': 'Dwelling Number per CLUE small area in 2012 and 2016',
        'argument': 'The top three areas in Melbourne where have most'
                    ' new dwellings in the past 5 years are: Melbourne (CBD)'
                    '(6954), Southbank(3112), Carlton(1804). This shows the '
                    'most popular and demanding living areas are around city '
                    'for people in Melbourne in the recent 5 years, which '
                    'reflects the trend of investment and development of real'
                    ' estate in Melbourne.',
    },

    {
        'rows': [''],
        'columns': [
            'Carlton', 'Docklands', 'East Melbourne', 'Kensington',
            'Melbourne (CBD)', 'Melbourne (Remainder)', 'North Melbourne',
            'Parkville', 'Port Melbourne', 'South Yarra', 'Southbank',
            'West Melbourne (Industrial)', 'West Melbourne (Residential)'],
        'spots': [
            [0, 0, 5.0], [0, 1, 66.0], [0, 2, 4.0], [0, 3, 1.0],
            [0, 4, 39.0], [0, 5, 51.0], [0, 6, 3.0], [0, 7, 2.0],
            [0, 8, 1.0], [0, 9, 3.0], [0, 10, 138.0], [0, 11, 1.0],
            [0, 12, 2.0]],
        'title': 'Average of Dwelling number per CLUE small area',
        'argument':'In southbank, the average of dwelling number is extremely'
                   ' higher than that in other areas. It means that it has a'
                   ' demand for dwelling with high capacity. And it is exactly'
                   ' according to its region feature of Southbank which is '
                   'the area where most big businesses host at.',
    },

    {
        'rows': ['Melbourne (CBD)'],
        'columns': [('Dwelling number', 'House/Townhouse'),
                    ('Dwelling number', 'Residential Apartments'),
                    ('Dwelling number', 'Student Apartments')],
        'spots': [[0, 0, 39.0], [0, 1, 280.0], [0, 2, 7.0]],
        'title': 'Count of Records of Dwellings per Dwelling type in Melbourne'
                 ' CBD in 2016',
        'argument': 'In Melbourne CBD, the most dwellings are apartments. It '
                    'indicates the architectural style of city from Victoria '
                    'government in certain level.',
    },

    {
        'rows': [''],
        'columns': [
            "106-116 A'Beckett Street", '108-112 Capel Street',
            '116-118 Little Bourke Street', '116-120 Bouverie Street',
            '117-121 Bouverie Street', '127-133 Leicester Street',
            '127-135 Pelham Street', '137-139 Palmerston Street',
            '139-143 Bouverie Street', '144-146 Queensberry Street',
            '146-148 Victoria Parade', '146-152 Victoria Parade',
            "15-19 O'Connell Street", '157-175 Royal Parade',
            '16-26 Orr Street', '175 Grattan Street', '182-190 The Avenue',
            '19A David Street', '19B David Street', '2 Boundary Road',
            '2-14 Cobden Street', '2-6 High Street', '223 Berkeley Street',
            '238-242 Flinders Street', '24-30 Barkly Place',
            '251-257 Cardigan Street', '266-270 Faraday Street',
            '296-300 Little Lonsdale Street', '3-11 High Street',
            '303-309 Royal Parade', '312-318 La Trobe Street',
            '335-347 Swanston Street', '35-41 Lonsdale Street',
            '38-40 Howard Street', '4-6 High Street', '402-408 Lonsdale Street',
            '408 Lonsdale Street', '42-50 Barry Street', '439-445 Lonsdale Street',
            '46-56 Drummond Street', '462-468 Swanston Street',
            '470-496 Swanston Street', '5-17 Flemington Road',
            '50-58 MacKenzie Street', '51-63 Villiers Street',
            '522-536 Swanston Street', '546-568 Lygon Street',
            '57-65 Drummond Street', '570 Lygon Street',
            '576-606 Lygon Street', '591-593 Elizabeth Street',
            '621A Swanston Street', '71-79 Bouverie Street',
            '740-750 Swanston Street', '75-79 Flemington Road',
            '768-800 Swanston Street', '768-804 Swanston Street',
            '8-14 Vale Street', '864-866 Swanston Street',
            '870-874 Swanston Street', '9-13 Earl Street',
            '97-107 Berkeley Street', '97-115 Berkeley Street'],
        'spots': [[0, 0, 15.0], [0, 1, 8.0], [0, 2, 9.0], [0, 3, 12.0],
                  [0, 4, 14.0], [0, 5, 12.0], [0, 6, 8.0], [0, 7, 12.0],
                  [0, 8, 10.0], [0, 9, 3.0], [0, 10, 2.0], [0, 11, 1.0],
                  [0, 12, 12.0], [0, 13, 15.0], [0, 14, 10.0], [0, 15, 14.0],
                  [0, 16, 3.0], [0, 17, 8.0], [0, 18, 8.0], [0, 19, 8.0],
                  [0, 20, 3.0], [0, 21, 12.0], [0, 22, 12.0], [0, 23, 15.0],
                  [0, 24, 12.0], [0, 25, 3.0], [0, 26, 10.0], [0, 27, 14.0],
                  [0, 28, 8.0], [0, 29, 14.0], [0, 30, 2.0], [0, 31, 15.0],
                  [0, 32, 13.0], [0, 33, 8.0], [0, 34, 2.0], [0, 35, 8.0],
                  [0, 36, 7.0], [0, 37, 12.0], [0, 38, 15.0], [0, 39, 7.0],
                  [0, 40, 12.0], [0, 41, 15.0], [0, 42, 12.0], [0, 43, 6.0],
                  [0, 44, 3.0], [0, 45, 12.0], [0, 46, 15.0], [0, 47, 15.0],
                  [0, 48, 60.0], [0, 49, 15.0], [0, 50, 10.0], [0, 51, 12.0],
                  [0, 52, 7.0], [0, 53, 14.0], [0, 54, 2.0], [0, 55, 2.0],
                  [0, 56, 8.0], [0, 57, 2.0], [0, 58, 10.0], [0, 59, 3.0],
                  [0, 60, 14.0], [0, 61, 2.0], [0, 62, 1.0]
                  ],
        'title': 'Count of Records of Dwelling(Student apartment) per Street '
                 'address',
        'argument':'By simply filtering the student apartment from all '
                   'records, you could actually find the addresses of all '
                   'student apartments in Melbourne. And most of them are in '
                   'Carlton, which is because the two biggest universities in '
                   'Melbourne: Melbourne University and RMIT University are '
                   'hosting in the city. And Carlton is the area between this '
                   'two University. Would you like to find more things '
                   'intersting? Try our analysis tool now!'
    },





]
