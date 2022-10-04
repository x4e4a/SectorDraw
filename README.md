# SectorDraw
Little Function that draws 120 Degree Sectors

Sector Plotting Function

Vincenty's Direct Calculation used to generate a 120 Degree Sector similar to that of a Cell Phone Sector.

Given Starting Point (Lat, Long), Azimuth (Direction), Distance (in Miles), Starts from Start Point, Creates the first point as -60 Degrees from Azimuth (half a sector) at the specified distance. Then increments through all 120 Degrees of the sector, Arriving at +60 degrees from the azimuth, the function completes the Sector by returning to the Start Point. (Cell Phone Sectors are typically 120 degrees)

Function was used years ago to estimate locations in records. Other examples in Vincenty's Calculations and Haversine Formulas seemed to focus on determining the distance between two known locations.

Can be easily modified for other uses.
Examples include:
  - Location data with estimated accuracy measurements (distance can be modified)
  - Sector sizes larger/smaller than 120 Degrees (Sectors > or < 120 Degrees)


