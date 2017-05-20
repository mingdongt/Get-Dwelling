from django import forms

CENSUS_YEAR_CHOICES = (
    (
        'All',
        (
            ('All', 'All'),
        )
    ),
    (
        '2002-2006',
        (
            (range(2002, 2006 + 1), '2002-2016'),
            (2002, '2002'),
            (2003, '2003'),
            (2004, '2004'),
            (2005, '2005'),
            (2006, '2006'),
        ),
    ),
    (
        '2007-2011',
        (
            (range(2007, 2011 + 1), '2007-2011'),
            (2007, '2007'),
            (2008, '2008'),
            (2009, '2009'),
            (2010, '2010'),
            (2011, '2011'),
        ),
    ),
    (
        '2012-2016',
        (
            (range(2012, 2016 + 1), '2012-2016'),
            (2012, '2012'),
            (2013, '2013'),
            (2014, '2014'),
            (2015, '2015'),
            (2016, '2016'),
        ),
    ),
)

CLUE_SMALL_AREA_CHOICES = (
    ('All', 'All'),
    ('Carlton', 'Carlton'),
    ('Docklands', 'Docklands'),
    ('East Melbourne', 'East Melbourne'),
    ('Kensington', 'Kensington'),
    ('Melbourne (CBD)', 'Melbourne (CBD)'),
    ('Melbourne (Remainder)', 'Melbourne (Remainder)'),
    ('North Melbourne', 'North Melbourne'),
    ('Parkville', 'Parkville'),
    ('Port Melbourne', 'Port Melbourne'),
    ('South Yarra', 'South Yarra'),
    ('Southbank', 'Southbank'),
    ('West Melbourne (Industrial)', 'West Melbourne (Industrial)'),
    ('West Melbourne (Residential)', 'West Melbourne (Residential)'),
)

DWELLING_TYPE_CHOICES = (
        ('All', 'All'),
        ('House/Townhouse', 'House/Townhouse'),
        ('Residential Apartments', 'Residential Apartments'),
        ('Student Apartments', 'Student Apartments'),
)

DIMENSION_CHOICES= (
    ('Census Year', 'Census Year'),
    ('CLUE Small Area', 'CLUE Small Area'),
    ('Dwelling Type', 'Dwelling Type'),
)


class AnalyzeInputForm(forms.Form):

    census_year_range = forms.MultipleChoiceField(
        label="Census Year Range:",
        choices=CENSUS_YEAR_CHOICES,
        required=False,
    )
    clue_small_area = forms.MultipleChoiceField(
        label="CLUE Small Area:",
        choices=CLUE_SMALL_AREA_CHOICES,
        required=False,
    )
    dwelling_type = forms.MultipleChoiceField(
        label="Dwelling Type:",
        choices=DWELLING_TYPE_CHOICES,
        required=False,
    )
    dwelling_number_min = forms.IntegerField(
        min_value=1,
        required=False,
    )
    dwelling_number_max = forms.IntegerField(
        max_value=1000,
        required=False,
    )
    search_street_address = forms.CharField(
        required=False,
        label="Search Street Address:",
    )

    row = forms.ChoiceField(
        required=True,
        choices=DIMENSION_CHOICES,
    )
    column = forms.ChoiceField(
        required=True,
        choices=DIMENSION_CHOICES
    )
    aggregation_function = forms.ChoiceField(
        required=True,
        choices=(
            ('Sum', 'Sum'),
            ('Maximum', 'Maximum'),
            ('Minimum', 'Minimum'),
            ('Average', 'Average'),
            ('Median', 'Median'),
            ('Count', 'Count'),
        )
    )


