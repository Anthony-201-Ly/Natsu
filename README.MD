
# Problem statement 

See ConUHacks 2025 - Technical Challenge.docx

# To run: 

```
pip install -r requirements.txt
python model-solution-1.py
python model-solution-2.py
```

## Optimized Output Part 1:

```
Number of fires addressed: 28
Number of fires delayed: 4
Total operational costs: $123000
Estimated damage costs from delayed responses: $550000
Fire severity report: {'low': 13, 'medium': 10, 'high': 5}
```

## Ideal Output Part 2:

```
               timestamp  temperature  humidity  wind_speed  precipitation  vegetation_index  human_activity_index  latitude  longitude  fire_risk
1027 2025-02-12 19:00:00         38.0        10          34            0.1                58                    97   44.2365   -72.1486          1
1653 2025-03-10 21:00:00         40.0        10          33            1.4                71                    95   44.4744   -72.3249          1
2345 2025-04-08 17:00:00         34.8        14          33            0.3                78                    76   44.7120   -73.4962          1
2644 2025-04-21 04:00:00         38.9        26          38            1.2                68                    77   44.6803   -73.7414          1
3169 2025-05-13 01:00:00         38.3        28          40            0.7                80                    98   45.3978   -73.6190          1
3477 2025-05-25 21:00:00         35.7        13          40            0.1                60                    86   44.6208   -72.5141          1
3480 2025-05-26 00:00:00         37.4        38          36            0.4                73                    98   45.0179   -73.9177          1
3709 2025-06-04 13:00:00         39.4        31          40            0.7                79                    99   45.5064   -72.1042          1
4520 2025-07-08 08:00:00         34.5        38          37            0.2                75                   100   44.2776   -73.6413          1
4754 2025-07-18 02:00:00         36.1        12          40            0.4                45                    99   45.5842   -72.3524          1
4758 2025-07-18 06:00:00         35.4        28          29            0.4                76                    94   44.4955   -72.5017          1
````