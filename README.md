# mario kart 8 deluxe multi-objective optimization

_which karts are good_

## just tell me

excerpted efficient results

```
    setup: char/kart/tires/wing                               SL  AC  TL  SA
Wario - P-Wing - Slick - Wario Wing                          (20, 3,  5,  19)
Wario - Splat Buggy - Standard - Wario Wing                  (17, 8,  7,  17)
Waluigi - Varmint - Wooden - Wario Wing                      (14, 10, 12, 15)
Waluigi - Wild Wiggler - Standard - Peach Parasol            (13, 12, 10, 16)
Pink Gold Peach - Wild Wiggler - Roller - Wario Wing         (11, 13, 12, 13)
Toad - Sports Coupe - Wooden - Wario Wing                    (10, 10, 14, 13)
Wendy - Wild Wiggler - Leaf Tyres - Peach Parasol            (5,  17, 15, 9)
Lemmy - Mr Scooty - Leaf Tyres - Peach Parasol               (1,  19, 18, 5)
```

## running it yourself

python 3.6+

```bash
python optimal-karts.py
```

You can change which attributes to include in the calculation by fiddling with
the constants at the bottom of the script.

## credits

data pulled from [MarioWiki.com](https://www.mariowiki.com/Mario_Kart_8_Deluxe_in-game_statistics#Statistics_in_in-game_format) on 2018-09-13

## attributes

```
WG: Weight
AC: Acceleration
ON: On-Road traction
OF: (Off-Road) Traction
MT: Mini-Turbo
SL: Ground Speed
SW: Water Speed
SA: Anti-Gravity Speed
SG: Air Speed
TL: Ground Handling
TW: Water Handling
TA: Anti-Gravity Handling
TG: Air Handling
```
