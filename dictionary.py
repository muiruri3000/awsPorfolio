dogFeatures = {
    'name' : 'bosco',
    'breed':'German Shepherd',
    'color': 'brown'
}

dogFeatures["legs"] = 4
dogFeatures["tail"] = 1
dogFeatures["fav_food"] = 'meatballs'

print("the following are dog features")

for key,value in dogFeatures.items():
    print(f"{key} : {value}")
