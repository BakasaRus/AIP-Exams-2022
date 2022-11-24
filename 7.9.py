# . - один любой символ
# .* - несколько любых символов (в т.ч. 0)
# \. - точка

import re

files = [
    'pbpyb.ttf', 'iteaat.cua', 'wbkea23.tot',
    'pybegea.ast', 'spapyb12.ty', 'ppydinaup.cbp',
    'papydin.bca', 'cbblea.dbt', 'papydin2.cat',
    'papyb.ppt'
]

masks = [
    re.compile(r'p.*y.*\..*'),
    re.compile(r'.*py.*\.с.*'),
    re.compile(r'.*p.*pyb.*\..*'),
    re.compile(r'.*p.*py\..*t.*'),
    re.compile(r'.*d.*\..*b.*'),
    re.compile(r'.*p.*y.*\..*'),
    re.compile(r'.*a.*2.*\..*t.*'),
    re.compile(r'.*a.*y.*\..*'),
]

for mask in masks:
    count = 0
    for file in files:
        if mask.match(file):
            count += 1
    print(count)
