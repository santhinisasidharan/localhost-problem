from flask import Flask
app = Flask(__name__)

app.route('/')
app.route('restaurants')
def  showRestaurants():
    '"This page will show all my restaurants"'

app.route('/retaurant/new')
def  newRestaurant():
     '"This page will be for making a new restaurant"'

app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant():
    '"This page is used to edit a restaurant"'

app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant():
     '"This page is used to delete a restaurant "'

app.route('/restaurant/<int:restaurant_id>')
app.route('/restaurant/<int:restaurant_id/menu>')
def showMenu():
     '"This page is used to show menu items in a restaurant"'

app.route('/restaurant/<int:restaurant_id/menu/new>')
def newMenuItem():
     '"This page is used to add new menu items in a restaurant"'

app.route('/restaurant/<int:restaurant_id/menu/menu_id/edit>')
def editMenuItem():
     '"This page is used to edit menu items in a restaurant"'

app.route('/restaurant/<int:restaurant_id/menu/menu_id/delete>')
def deleteMenuItem():
     '"This page is used to show menu items in a restaurant'''



if __name__ =='__main__':
    app.debug =True
    app.run(host = '0.0.0.0', port = 8080)
