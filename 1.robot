*** Settings ***
Library  main.py

*** Test Cases ***
Reverse
    [Documentation]
    ...
    ${coordinate}=  reverse  ${59.7027541}  ${30.379206}
    Should Be Equal  ${coordinate}  Полковая улица, София, Пушкин, Санкт-Петербург, Северо-Западный федеральный округ, 196603, Россия


Geocode
    [Documentation]
    ...
    ${address}=  geocode  Полковая улица  Санкт-Петербург  Россия
    Should Be Equal  ${address}  59.7027541 30.379206