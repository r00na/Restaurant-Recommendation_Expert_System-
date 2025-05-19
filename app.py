from experta import KnowledgeEngine, Rule, Fact, Field
from flask import Flask, render_template, request

class CuisineFact(Fact):
    pass

class DiningPreferenceFact(Fact):
    pass

class RestaurantRecommendationEngine(KnowledgeEngine):
    @Rule(CuisineFact(cuisine='Jordanian'))
    def recommend_jordanian(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Bait Al-Mansaf Albadawi',
            'description': 'Traditional Jordanian Mansaf with its distinctive flavor, along with various dishes like Zarb meat, Sambousek, Mandi, and more.',
            'phone': '+962796444135',
            'branches': 'Tabarbour - Mushagil Circle',
            'rating': '4.3'
        }))

    @Rule(CuisineFact(cuisine='Jordanian',price='mid-range', ambiance='family', special_features='nothing'))
    def recommend_jordanian(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Mansaf Shrrbha Restaurant',
            'description': 'serves authentic Jordanian Mansaf with Jameed and fresh meat, along with various dessert dishes such as Nabulsi Knafeh.',
            'phone': '0798730202',
            'branches': 'Seventh Circle - Al Az bin Abdul Salam Street',
            'rating': '4.4'
        }))

    @Rule(CuisineFact(cuisine='Jordanian',wifi='yes', ambiance='family'))
    def recommend_jordanian(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Qaser-Aldeyafah Restaurant',
            'description': 'serves the distinctive Jordanian Mansaf dish with fresh meat and chicken, along with many other specialty dishes like Szechuan chicken, chicken in cream sauce, and more.',
            'phone': '065531456',
            'branches': 'Al Madinah Al Munawarah Street',
            'rating': '4.2'
        }))

    @Rule(CuisineFact(cuisine='Jordanian', hours ='lunch', family_friendly ='yes', area = 'downtown', ambiance='family'
))
    def recommend_jordanian(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Al Quds Restaurant',
            'description': 'Al Quds Restaurant serves a variety of dishes such as Mansaf, Mandi, Maglouba, Freekeh, Ouzi, Kabsa, grills, assorted desserts, and more.',
            'phone': '064630168',
            'branches': 'Downtown - King Hussein Street',
            'rating': '4.0'
        }))

    @Rule(CuisineFact(price='mid-range', area='downtown', hours = 'breakfast' , ambiance='family' 
))
    def recommend_jordanian(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Snack 22 Restaurant',
            'description': 'Restaurant offers a variety of dishes including burgers, fries, spleen sandwiches, liver sandwiches, cocktails, and assorted beverages.',
            'phone': '064625733',
            'branches': 'Downtown - Basman Street',
            'rating': '4.0'
        }))
 
    @Rule(CuisineFact(cuisine='pizza', wifi='yes', hours ='lunch', ambiance='family'
))
    def recommend_italian(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Pizza El Rais',
            'description': 'Managed by an Italian chef, serving the best original Italian-flavored pizzas. Famous for its thick-crust pizzas and also offers other Lebanese dishes like manakeesh, as well as pasta and a variety of salads.',
            'phone': '+962798209994',
            'branches': 'Al Bayader, Wadi Al Seer',
            'rating': '4.5 (Social Media), 4.0 (Delivery Apps)'
        }))

    @Rule(CuisineFact(cuisine='eastern dishes', hours = 'dinner', wifi='yes', family_friendly ='yes', price='budget', special_features= 'rooftop view' ))
    def recommend_chinese(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Levant Restaurant',
            'description': 'Levant Restaurant offers a variety of Armenian and Eastern dishes such as kashlama, lula kebab, mesouf bulgur, talar kebab, shawarma, saj, grilled meats, kofta, and more. ',
            'phone': '+962796609000',
            'branches': 'Third Circle - Methqal Al Fayez Street',
            'rating': '4.6'
        }))

    @Rule(CuisineFact(cuisine='western dishes', special_features='live music', wifi='yes', family_friendly ='yes'))
    def recommend_indian(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Mijana Restaurant & Cafe',
            'description': 'Mijana Restaurant & Cafe offers a variety of Western and Eastern dishes such as Mexican beef fajitas, chicken escalope, arayes, grilled kibbeh, shish tawook, and more. ',
            'phone': '+962799381474',
            'branches': 'Jabal Amman - Ahmad bin Tulun Street',
            'rating': '4.5'
        }))

    @Rule(CuisineFact(cuisine='pizza', outdoor_seating = 'no', ambiance = 'family', wifi = 'yes' 
))
    def recommend_japanese(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Pizza Sqrd',
            'description': 'Pizza Sqrd offers a variety of delicious pizzas with a unique basil flavor, as well as other dishes like pasta and cannoli.',
            'phone': '0799687773',
            'branches': 'Seventh Circle',
            'rating': '5.0 (Social Media), 4.2 (Delivery Apps)'
        }))

    @Rule(CuisineFact(cuisine='seafood', area = 'downtown', hours = 'lunch'
))
    def recommend_lebanese(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Smakji Seafood',
            'description': 'Smakji Seafood offers a variety of seafood dishes such as stuffed and oven-grilled sea bream, grilled sea bream, grilled fillet, Sayadiyah rice with sea bream, and more. ',
            'phone': '0776685783',
            'branches': 'Downtown - King Talal Street',
            'rating': '4.4'
        }))

    @Rule(CuisineFact(cuisine='seafood', area = 'downtown', hours = 'lunch', ambiance = 'casual'
))
    def recommend_mexican(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Ocean Fresh Fish',
            'description': 'Ocean Fresh Fish offers a variety of seafood dishes including grilled salmon, sea bass, grilled sea bream, sushi, Provencal shrimp, and more. ',
            'phone': '0797661100',
            'branches': 'Khalda, Abdali, Marka, Tabrbour,  Sweifieh, Muqabalain, Marj Al Hamam, Seventh Circle, Al Madinah Al Munawarah Street',
            'rating': '4.3'
        }))

    @Rule(DiningPreferenceFact(cuisine='shawarma', price='mid-range' 
))
    def recommend_budget(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Shawarma Reem',
            'description': 'Offers a variety of shawarma types, including beef and chicken shawarma, with multiple branches in Amman.',
            'phone': '+96265601517',
            'branches': 'Al Madinah Al Munawarah Street, Seventh Circle, Dabouq, Jubaiha, Sweifieh, Restaurant Street',
            'rating': '4.7'
        }))

    @Rule(DiningPreferenceFact(price='mid-range', hours= 'dinner'
))
    def recommend_mid_range(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'AlMousalli Shawarma',
            'description': 'AlMousalli Shawarma offers a variety of shawarma types, including beef shawarma, chicken shawarma, Italian shawarma, Aleppo shawarma, and many appetizers and sides.',
            'phone': '065601517',
            'branches': 'Al Madinah Al Munawarah Street, Seventh Circle, Dabouq, Jubaiha, Sweifieh',
            'rating': '4.7'
        }))

    @Rule(DiningPreferenceFact(hours = 'breakfast', authentic= 'yes', area = 'west amman', ambiance='family' 
))
    def recommend_high_end(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Ka3keh 3l Mashi',
            'description': 'Ka3keh 3l Mashi offers a wide variety of pastries such as manakish, pizza, and diverse sandwiches. It is particularly known for its traditional Ka3keh sandwiches, which makes it a popular breakfast spot in the Seventh Circle area.',
            'phone': '065858774 / 0795858774',
            'branches': 'Seventh Circle, Princess Sumaya Street, behind Sultan Centere',
            'rating': '4.0'
        }))

    @Rule(DiningPreferenceFact(hours = 'breakfast'
))
    def recommend_high_end(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Pizza and Manaqeesh Terghalli',
            'description': 'Pizza and Manaqeesh Terghalli is renowned for its assorted manakish and pizza dishes. The mixed cheese manakish is a customer favorite. They also offer egg with turkey and cheese manakish, rolls, and various Jordanian dishes.',
            'phone': '0790904466',
            'branches': 'Seventh Circle, Al Sahl area, Masoud bin Saad Street, behind Cosmo Seventh Circle, next to the Space Institute',
            'rating': '5.0'
        }))

    @Rule(DiningPreferenceFact(cuisine='falafel', area='downtown', hours = 'breakfast', ambiance='family'
 ))
    def recommend_downtown(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Hashem Restaurant',
            'description': 'Hashem Restaurant is one of the oldest and most prestigious traditional restaurants in Amman, renowned for serving delicious breakfast meals, including falafel, fava beans, hummus, fried potatoes, and various appetizers. ',
            'phone': '064353373',
            'branches': 'Downtown',
            'rating': '4.5'
        }))

    @Rule(DiningPreferenceFact(area='west_amman', price = 'mid-range'
))
    def recommend_west_amman(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Fakhreldin Restaurant',
            'description': 'Fakhreldin Restaurant specializes in offering a variety of dishes including local lamb grills, scaloppini, grilled and fried fish, numerous appetizers, and soft drinks. The restaurant also serves various desserts such as Lebanese Nights, Muhalabiya, and Halawat Al-Jibn.',
            'phone': '+962797711177  ',
            'branches': 'Jabal Amman, 2nd Circle',
            'rating': '4.5'
        }))
  
    @Rule(DiningPreferenceFact(ambiance='casual' ))
    def recommend_casual(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'La Capitale Restaurant',
            'description': 'La Capitale is known for offering all types of grills, shawarma, spiced rice, stuffed grape leaves, and more. The restaurant also features a variety of side dishes, salads, pickles, and different kinds of natural juices and beverages.',
            'phone': '+962065505555  ',
            'branches': 'Amman, Four Seasons Hotel  ',
            'rating': '4.5'
        }))

    @Rule(DiningPreferenceFact(ambiance='fine_dining', special_features = 'live music'))
    def recommend_fine_dining(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Abdoun Khashouka',
            'description': 'This restaurant is known for its diverse menu, including various casseroles, manakish, natural juices, and soft drinks. Popular dishes include chicken liver, shakshuka, and makdous.',
            'phone': '+962770121211  ',
            'branches': 'Abdoun, Saad Shamout Street, beside Housing Bank Park, Dabouq, Ikram Street, beside Starbucks, Building No. 30  ',
            'rating': '4.5'
        }))
  
    @Rule(DiningPreferenceFact(outdoor_seating='yes' , special_features='nothing'
))
    def recommend_outdoor_seating(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Blue Fig',
            'description': 'Offers outdoor seating with a variety of international dishes.',
            'phone': '+962 7 9092 8800',
            'branches': 'Abdoun',
            'rating': '4.4'
        }))

    @Rule(DiningPreferenceFact(special_features='live music'
))
    def recommend_authentic(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Sufra Restaurant',
            'description': 'Authentic Jordanian cuisine with a variety of traditional dishes.',
            'phone': '+962 6 461 1468',
            'branches': 'Jabal Amman',
            'rating': '4.7'
        }))


    @Rule(DiningPreferenceFact(special_features='rooftop_view'))
    def recommend_rooftop_view(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Cantaloupe Gastro Pub',
            'description': 'Offers a rooftop view with a variety of international dishes.',
            'phone': '07 7000 0717',
            'branches': 'Jabal Amman',
            'rating': '4.3'
        }))

    @Rule(DiningPreferenceFact(special_features='vegan'))
    def recommend_vegan(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Vegan Spectrum',
            'description': 'Restaurant with a selection of vegan dishes including a pasta bowl, quinoa tabouleh, and a selection of cakes. Dine in, pick up, or delivery. Everything is prepared fresh, from appetizers to main courses. Also serves desserts. ',
            'phone': '+962-772437625',
            'branches': 'Al-Besharah St, Amman, Jordan',
            'rating': '4.0'
        }))

    @Rule(DiningPreferenceFact(hours='dinner' 
))
    def recommend_late_night(self):
        self.declare(Fact(recommended_restaurant={
            'name': 'Brisket Amman',
            'description': 'Brisket Amman is renowned for serving grilled chicken, grilled meats, and burgers. The restaurant is known for its high-quality food and reasonable prices.',
            'phone': '+962799506020  ',
            'branches': 'Amman, Abdullah Bin Masoud Street  ',
            'rating': '4.5'
        }))

def recommend_restaurant(preferences):
    engine = RestaurantRecommendationEngine()
    engine.reset()

    for key, value in preferences.items():
        if key == 'cuisine':
            engine.declare(CuisineFact(cuisine=value))
        else:
            engine.declare(DiningPreferenceFact(**{key: value}))

    engine.run()
    for fact in engine.facts.values():
        if isinstance(fact, Fact) and 'recommended_restaurant' in fact:
            return fact['recommended_restaurant']
    return None

def ask_preferences():
    preferences = {}
    preferences['cuisine'] = input("What type of cuisine are you in the mood for? (Jordanian, Italian, pizza, seafood, eastern dishes, western dishes, shawarma, falafel): ")
    preferences['price'] = input("What is your price range? (budget, mid-range): ")
    preferences['area'] = input("Which area do you prefer? (downtown, west amman, east amman): ")
    preferences['ambiance'] = input("What type of ambiance do you prefer? (casual, fine dining, family): ")
    preferences['special_features'] = input("Do you have any special features in mind? (live music, rooftop view, vegan, nothing): ")
    preferences['family_friendly'] = input("Are you looking for a family-friendly restaurant? (yes or no): ")
    preferences['wifi'] = input("Do you need Wi-Fi access? (yes or no): ")
    preferences['hours'] = input("Do you have a specific dining time in mind? (breakfast, lunch, dinner): ")
    

    return preferences


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        preferences = {
            'cuisine': request.form['cuisine'],
            'price': request.form['price'],
            'area': request.form['area'],
            'ambiance': request.form['ambiance'],
            'special_features': request.form['special_features'],
            'family_friendly': request.form['family_friendly'],
            'wifi': request.form['wifi'],
            'hours': request.form['hours']
        }
        recommended_restaurant = recommend_restaurant(preferences)
        return render_template('result.html', restaurant=recommended_restaurant)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)