import ephem

planets_names = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

planets_ephem = {
  "sun": ephem.Sun(),
  "moon": ephem.Moon(),
  "mercury": ephem.Mercury(),
  "venus":ephem.Venus(),
  "mars": ephem.Mars(),
  "jupiter": ephem.Jupiter(),
  "saturn": ephem.Saturn(),
  "uranus": ephem.Uranus(),
  "neptune": ephem.Neptune(),
  "pluto": ephem.Pluto()
                 }
