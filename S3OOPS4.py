"""
    Types of Inheritance
    1. Single Level
    2. Multi Level
    3. Hierarchy
    4. Multiple
    5. Hybrid
"""

#  Single Level
class Product:
    pass

class TV(Product):
    pass

#Multi Level
class LEDTV(TV):
    pass

# Hierarchy
class PlasmaTV(TV):
    pass

# Multiple
class LocationTracker:
    pass

class InternetTracker:
    pass

class App(LocationTracker, InternetTracker):
    pass