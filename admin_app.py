import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'bitlab_telebot_project'
)
# === Функции базам данных =======================================================================
def getAllRestaurants():
    global mydb
    mycursor = mydb.cursor()
    sql = "select * from restaurants"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def getAllFoodTypes():
    global mydb
    mycursor = mydb.cursor()
    sql = "select * from food_types"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def getAllFoods():
    global mydb
    mycursor = mydb.cursor()
    sql = "select f.id, f.name, f.price, f.description, ft.name, r.name " \
          "FROM foods f " \
          "inner join food_types ft ON f.food_type_id = ft.id " \
          "inner join restaurants r ON f.restaurant_id = r.id"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def addRestaurant(name, address):
    global mydb
    mycursor = mydb.cursor()
    sql = "insert into restaurants (id, name, address) values (NULL, %s, %s)"
    val = (name, address)
    mycursor.execute(sql, val)
    mydb.commit()

def addFoodType(nam1):
    global mydb
    mycursor = mydb.cursor()
    nam1 = '"'+nam1+'"'
    sql = "insert into food_types (id, name) values (NULL, " + nam1 + ")"
    mycursor.execute(sql)
    mydb.commit()

def addFood(name, price, discription, type, rest):
    global mydb
    mycursor = mydb.cursor()
    sql = "insert into foods (id, name, price, description, food_type_id, restaurant_id) values (NULL, %s, %s, %s, %s, %s)"
    val = (name, price, discription, type, rest)
    mycursor.execute(sql, val)
    mydb.commit()

def updateRestaurant(rest_id, new_name, new_addres):
    global mydb
    mycursor = mydb.cursor()
    sql = "update restaurants set name=%s, address=%s where id =" + str(rest_id)
    val = (new_name, new_addres)
    mycursor.execute(sql, val)
    mydb.commit()

def updateFoodType(ft_id, new_ft_name):
    global mydb
    nam1 = '"'+new_ft_name+'"'
    mycursor = mydb.cursor()
    sql = "update food_types set name=" + nam1 + " where id=" + str(ft_id)
    mycursor.execute(sql)
    mydb.commit()

def updateFood(f_id, new_f_name, new_f_price, new_f_descr, new_f_type, new_f_rest):
    global mydb
    mycursor = mydb.cursor()
    sql = "update foods set name=%s, price=%s, description=%s, food_type_id=%s, restaurant_id=%s " \
          "where id=" + str(f_id)
    val = (new_f_name, new_f_price, new_f_descr, new_f_type, new_f_rest)
    mycursor.execute(sql, val)
    mydb.commit()

def deleteRestaurant(del_r_id):
    global mydb
    mycursor = mydb.cursor()
    sql = "delete from restaurants where id=" + str(del_r_id)
    mycursor.execute(sql)
    mydb.commit()

def deleteFoodType(del_ft_id):
    global mydb
    mycursor = mydb.cursor()
    sql = "delete from food_types where id=" + str(del_ft_id)
    mycursor.execute(sql)
    mydb.commit()

def deleteFood(del_f_id):
    global mydb
    mycursor = mydb.cursor()
    sql = "delete from foods where id=" + str(del_f_id)
    mycursor.execute(sql)
    mydb.commit()

#================================================================================================
#------------------------------------------------------------------------------------------------
#=== Основное меню приложения ===================================================================
while True:
    print("====== Main menu =====")
    print("[1] LIST of Restaurants")
    print("[2] LIST of FoodTypes")
    print("[3] LIST of Foods")
    print("[4] ADD Restaurant")
    print("[5] ADD FoodType")
    print("[6] ADD Food")
    print("[7] UPDATE Restaurant information")
    print("[8] UPDATE FoodType information")
    print("[9] UPDATE Food information")
    print("[10] DELETE Restaurant")
    print("[11] DELETE FoodType")
    print("[12] DELETE Food")
    print("[0] to EXIT")
    choice = int(input())

    if choice == 1:
        print("==========")
        allRests = getAllRestaurants()
        for rest in allRests:
            print(str(rest[0]) + ") " + rest[1])
    elif choice == 2:
        print("==========")
        all_food_types = getAllFoodTypes()
        for ft in all_food_types:
            print(str(ft[0]) + ") " + ft[1])
    elif choice == 3:
        print("==========")
        foods = getAllFoods()
        for food in foods:
            print(str(food[0])+ ") " + food[1] + " Price: " + str(food[2]) + " Description: " + food[3] +
                  " Type: " + food[4] + " Restaurant: " + food[5])
    elif choice == 4:
        print("==========")
        rest_name = str(input("Insert new restaurant name: "))
        address = str(input("Insert new address: "))
        addRestaurant(rest_name, address)
        print("New restaurant added!")
        print("==========")
    elif choice == 5:
        print("==========")
        type_name = str(input("Insert new food type name: "))
        addFoodType(type_name)
        print("New food type added!")
        print("==========")
    elif choice == 6:
        print("==========")
        food_name = str(input("Insert new food name: "))
        food_price = int(input("Insert new food price: "))
        food_discription = str(input("Insert new food discription: "))
        print("----------")
        all_food_types = getAllFoodTypes()
        for ft in all_food_types:
            print(str(ft[0]) + ") " + ft[1])
        print("----------")
        food_type = int(input("Choose new food type: "))
        print("----------")
        allRests = getAllRestaurants()
        for rest in allRests:
            print(str(rest[0]) + ") " + rest[1])
        print("----------")
        food_rest = int(input("Choose new food restaurant: "))
        addFood(food_name, food_price, food_discription, food_type, food_rest)
        print("New food added!")
        print("==========")
    elif choice == 7:
        print("==========")
        allRests = getAllRestaurants()
        for rest in allRests:
            print(str(rest[0]) + ") " + rest[1])
        print("----------")
        rest_id = int(input("Which restaurant you wanna update, pls choose id: "))
        new_r_name = str(input("Insert new name: "))
        new_r_addres = str(input("Insert new address: "))
        updateRestaurant(rest_id, new_r_name, new_r_addres)
        print("Successfully updated!")
        print("==========")
    elif choice == 8:
        print("==========")
        all_food_types = getAllFoodTypes()
        for ft in all_food_types:
            print(str(ft[0]) + ") " + ft[1])
        print("----------")
        ft_id = int(input("Which food type you wanna update, pls choose id: "))
        new_ft_name = str(input("Insert new name: "))
        updateFoodType(ft_id, new_ft_name)
        print("Successfully updated!")
        print("==========")
    elif choice == 9:
        print("==========")
        foods = getAllFoods()
        for food in foods:
            print(str(food[0]) + ") " + food[1] + " Price: " + str(food[2]) + " Description: " + food[3] +
                  " Type: " + food[4] + " Restaurant: " + food[5])
        print("----------")
        f_id = int(input("Which food you wanna update, pls choose id: "))
        new_f_name = str(input("Insert new name: "))
        new_f_price = int(input("Insert new price: "))
        new_f_descr = str(input("Insert new food discription: "))
        print("----------")
        all_food_types = getAllFoodTypes()
        for ft in all_food_types:
            print(str(ft[0]) + ") " + ft[1])
        print("----------")
        new_f_type = int(input("Choose new food type: "))
        print("----------")
        allRests = getAllRestaurants()
        for rest in allRests:
            print(str(rest[0]) + ") " + rest[1])
        print("----------")
        new_f_rest = int(input("Choose new food restaurant: "))
        updateFood(f_id, new_f_name, new_f_price, new_f_descr, new_f_type, new_f_rest)
        print("Successfully updated!")
        print("==========")
    elif choice == 10:
        print("==========")
        allRests = getAllRestaurants()
        for rest in allRests:
            print(str(rest[0]) + ") " + rest[1])
        print("----------")
        del_r_id = int(input("Which restaurant you wanna delete, choose id: "))
        deleteRestaurant(del_r_id)
        print("Successfull deleted!")
        print("==========")
    elif choice == 11:
        print("==========")
        all_food_types = getAllFoodTypes()
        for ft in all_food_types:
            print(str(ft[0]) + ") " + ft[1])
        print("----------")
        del_ft_id = int(input("Which food type you wanna delete, choose id: "))
        deleteFoodType(del_ft_id)
        print("Successfull deleted!")
        print("==========")
    elif choice == 12:
        print("==========")
        foods = getAllFoods()
        for food in foods:
            print(str(food[0]) + ") " + food[1] + " Price: " + str(food[2]) + " Description: " + food[3] +
                  " Type: " + food[4] + " Restaurant: " + food[5])
        print("----------")
        del_f_id = int(input("Which food you wanna delete, choose id: "))
        deleteFood(del_f_id)
        print("Successfull deleted!")
        print("==========")
    elif choice == 0:
        break
    else:
        print("WRONG INPUT!!!")
#================================================================================================
