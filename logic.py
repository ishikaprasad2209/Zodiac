from datetime import datetime

def get_zodiac_sign(dob):
    zodiac_dates = [
        ((1, 20), (2, 18), "Aquarius"),
        ((2, 19), (3, 20), "Pisces"),
        ((3, 21), (4, 19), "Aries"),
        ((4, 20), (5, 20), "Taurus"),
        ((5, 21), (6, 20), "Gemini"),
        ((6, 21), (7, 22), "Cancer"),
        ((7, 23), (8, 22), "Leo"),
        ((8, 23), (9, 22), "Virgo"),
        ((9, 23), (10, 22), "Libra"),
        ((10, 23), (11, 21), "Scorpio"),
        ((11, 22), (12, 21), "Sagittarius"),
        ((12, 22), (1, 19), "Capricorn")
    ]

    month, day = dob.month, dob.day
    for start, end, sign in zodiac_dates:
        if (start[0] == month and start[1] <= day) or (end[0] == month and end[1] >= day):
            return sign
    return "Unknown"