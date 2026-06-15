from datetime import datetime, timedelta

def predict_eta(departure_str,distance_km,speed=60):

    depart = datetime.strptime(departure_str,"%Y-%m-%d %H:%M:%S")
    hours = distance_km / speed
    eta = depart + timedelta(hours=hours)

    return eta