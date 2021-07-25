def build_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

print(build_car('subaru', 'outback', color='blue', tow_package=True))
print(build_car('honda', 'civic', color='silver'))
print(build_car('volvo', 'S60 B5 Inscription'))
