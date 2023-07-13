import time

red_man = "RED MAN 🔴 🚶"
green_man = "GREEN MAN 🟢 🚶"

red_light = "RED LIGHT 🔴 🚦"
amber_light = "AMBER LIGHT 🟠 🚦"
green_light = "GREEN LIGHT 🟢 🚦"

man_colour = red_man
traffic_light_colour = green_light

print(f"Pedestrians: {man_colour}\nTraffic: {traffic_light_colour}\n")
button_press = input("Press button (y/n)? ")

if button_press == "y":
    traffic_light_colour = amber_light
    print(f"Pedestrians: {man_colour}\nTraffic: {traffic_light_colour}\n")
    time.sleep(4)
    traffic_light_colour = red_light
    print(f"Pedestrians: {man_colour}\nTraffic: {traffic_light_colour}\n")
    time.sleep(2)
    man_colour = green_man
    print(f"Pedestrians: {man_colour}\nTraffic: {traffic_light_colour}\n")

