#Ejercicios de Diccionarios
#1
print("Introduce hotel name")
name = input()
while True:
    try:
        print("Introduce hotel stars")
        stars = int(input())
        if stars <= 0:
            print("The number cannot less or equal 0")
        if stars > 5:
            print("The maximum numbers of stars is 5")
        if stars > 0 and stars <= 5:
            break
    except:
            print("Introduce a valid value")
hotel_info = {
    "hotel_name": name,
    "hotel_stars": stars,
    "hotel_room": []
}
while True:
    while True:
        try:
            print("////////////////////////")
            print("Introduce hotel room to consult")
            print("If you want to exit type",f"{'"Yes"'}")
            print("////////////////////////")
            room_num_user_input = input()
            room_num = int(room_num_user_input)
            room_num_str = ""
            if room_num <= 0:
                print("The number cannot less or equal to 0")
            if room_num > 10:
                print("There is not more than 10 rooms")
            if room_num > 0 and room_num <= 10:
                break
        except:
                room_num_str = room_num_user_input.strip().lower()
                if room_num_str == "yes":
                    break
                else:
                    print("Introduce a valid value")
    
    if room_num_str == "yes":
        print("You left the program successfully")
        break
    else:
        if room_num <= 5:
            if 1 <= room_num <= 3:
                room_price = 40
            else:
                room_price = 50
            floor = "1st floor"
            room_num_data = str("Room number "+f"{room_num}")
        else:
            if 6 <= room_num <= 8:
                room_price = 75
            else:
                room_price = 100
            floor = "2nd floor"
            room_num_data = str("Room number "+f"{room_num}")
        rooms = {"floor": floor,
            "price": room_price,
            "room_num": room_num_data}
        hotel_info["hotel_room"].clear()
        hotel_info["hotel_room"].append(rooms)
        print("////////////////////////")
        print("Hotel name:", hotel_info["hotel_name"])
        print("Hotel stars:", hotel_info["hotel_stars"])
        print("////////////////////////")
        print("Room info")
        for room_data in hotel_info["hotel_room"]:
            for key,display_room_data in room_data.items():
                if display_room_data == room_price:
                    print("Room price:",f"{room_price}"+"$")
                else:
                    print(display_room_data)
        print("////////////////////////")