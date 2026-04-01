import folium

def generate_map(path, hospital_loc):
    m = folium.Map(location=path[-1], zoom_start=13)

    # Old path points
    for loc in path[:-1]:
        folium.CircleMarker(loc, radius=3).add_to(m)

    # Current ambulance position
    folium.Marker(
        path[-1],
        popup="Ambulance",
        icon=folium.Icon(color="red")
    ).add_to(m)

    # Hospital
    folium.Marker(
        hospital_loc,
        popup="Hospital",
        icon=folium.Icon(color="green")
    ).add_to(m)

    # Path line
    folium.PolyLine(path, color="blue").add_to(m)

    m.save("map.html")