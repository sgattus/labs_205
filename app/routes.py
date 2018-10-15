from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, AnimalForm
from app.models import User
from app.models import Animal,Habitat,Location,AnimalToHabitat


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/animal/<name>')
@login_required
def animal(name):
   # your code here
   form = AnimalForm()
   a = Animal.query.filter_by(name=name).first()
   p= AnimalToHabitat.query.filter_by(animalID=a.id).first()
   if p is None:
       h=""
       l=""
       loc=l
   # pp=AnimalToHabitat.query.filter_by(animalID=a.id).all()
   else:
       h=Habitat.query.filter_by(id=p.habitatID).first()
       l=Location.query.filter_by(id=h.id).first()
       if l is None:
           #l=""
           #loc=l
           a = Animal.query.filter_by(name=name).first()
           p = AnimalToHabitat.query.filter_by(animalID=a.id).first()
           h = Habitat.query.filter_by(id=p.habitatID).first()
           l = Location.query.filter_by(id=h.locationID).first()
           loc = l.continent
       else:
           loc = l.continent

   pp = AnimalToHabitat.query.filter_by(animalID=a.id).all()

   habitats = {'username': 'sonya'}

   all_animals = Habitat.query.all()
   posts = list()
   for hh in pp:

       posts.append({'animals': {'username': Habitat.query.filter_by(id=hh.habitatID).first()},
                     })



   if form.validate_on_submit():
       title = form.username.data

   else:
       title = a.name

   if form.validate_on_submit():
       flash('Animal was created {}'.format(
           form.username.data))

   if form.validate_on_submit():
       picture = 'https://myelitedetail.us/images/drawn-animal-extinct-animal/drawn-animal-extinct-animal-20.jpg'
   else:

       picture = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" \
                 "Zanzibar_Leopard_2.JPG/800px-Zanzibar_Leopard_2.JPG"

   if form.validate_on_submit():
       bio = form.animalBio.data
   else:
       bio = a.bio

   if form.validate_on_submit():
       extermination = form.extermination.data
   else:
       extermination = a.extinction
       hab=posts
       #loc=l.continent








   return render_template("animal.html", b=bio, e=extermination, p=picture, t=title,h=hab,l=loc,animals=all_animals,posts=posts)


@app.route('/animals', methods=['GET', 'POST'])
@login_required
def animals():
    animals = {'username': 'sonya'}
    all_animals = Animal.query.all()
    a1=Animal.query.get(1)
    i=1
    posts = list()
    for a in all_animals:
        posts.append({ 'animals': {'username': a}
                      })



    return render_template('animals.html', title='Artist Page', animals=all_animals, posts=posts, a1=a1)


@app.route('/create_bio_page', methods=['GET', 'POST'])
@login_required
def create():
    form = AnimalForm()
    if request.method == 'POST':
        flash('Animal was created {}'.format(form.name.data))

        a1 = Animal(name=form.name.data, bio=form.animalBio.data, extinction=form.extermination.data, year=form.year.data)
        #L = Location(continent=form.location.data)
        db.session.add(a1)
        #db.session.add(L)
        db.session.commit()
        #L1 = Location.query.filter_by(continent=form.location.data).first()
        #A1 = Animal.query.filter_by(name=form.name.data).first()

        #h1 = Habitat(name=form.animalBehavior.data, climate='bees', food='food', locationID=L1.id)
        #db.session.add(h1)
        #db.session.commit()
        #hh = Habitat.query.filter_by(name=form.animalBehavior.data).first()
        #a2h = AnimalToHabitat(animalID=A1.id, habitatID=hh.id)
        #db.session.add(a2h)
        #db.session.commit()

        return redirect(url_for('animals'))
    return render_template('create_bio_page.html',  title='Sign In', form=form)

@app.route('/create_location', methods=['GET', 'POST'])
@login_required
def create_location():
    form = AnimalForm()
    if request.method == 'POST':
        flash('Location was created {}'.format(form.location.data))

        L = Location(continent=form.location.data)
        db.session.add(L)
        db.session.commit()


        return redirect(url_for('animals'))
    return render_template('create_location.html',  title='Sign In', form=form, sloc=form.sLocation)

@app.route('/create_habitat', methods=['GET', 'POST'])
@login_required
def create_habitat():
    form = AnimalForm()
    form.sLocation.choices = [(row.id, row.continent) for row in Location.query.all()]
    form.sAnimal.choices = [(rowA.id, rowA.name) for rowA in Animal.query.all()]
    L= Location.query.filter_by(id=form.sLocation.data).first()
    if request.method == 'POST':
        flash('Habitat was created {}'.format(form.location.data))

        H = Habitat(name=form.habitatName.data,climate=form.climate.data,food=form.climate.data,locationID=L.id)

        db.session.add(H)
        db.session.commit()

        posts = list()
        for a in form.sAnimal.data:
            A = Animal.query.filter_by(id=a).first()
            posts.append(a)
            a2h = AnimalToHabitat(animalID=A.id,habitatID=H.id)
            db.session.add(a2h)
            db.session.commit()


        return redirect(url_for('animals'))
    return render_template('create_habitat.html',  title='Sign In', form=form, sloc=form.sLocation)


@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")
   # clear all data from all tables
   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()

   a1 = Animal(name="Zanzibar Leopard", bio="The Zanzibar Leopard is an African leopard. Its origin lies in Unguja Island of Zanzibar Archipelago. These leopards were believed to be part of local witch craft. In 2008 the leopard was considered extinct due to prejudices from local hunters. In the 1990s a conservation effort was made to try to restore leopards. Sadly it seems that these creatures are no more...", extinction="The extermination of the Zanzibar Leopard was cultivated by local farmers convinced these animals were kept by witches and trained to harass the local farmers by their owners. The belief swept across the Island tha leopards could be trained to do the evil bidding of those performing witchcraft. The beautiful cats were considered vermin. The problem began in the 20th century when the human populous and agricultural encroached on the habitat of the Zanzibar Leopard. The Zanzibar revolution of 1964 ws a combo of an anti-witchcraft and anti-leopard campaign founded by a witch seeker that ultimately led to the near extinction of the Zanzibar Leopard.",year=1990)
   a2= Animal(name="Quagga",bio="The Quagga looks like a cross between a horse and a zeebra. The head down to the neck is striped and the rest is a brown coat.",extinction="The animal was hunted to death around the 1870's and in the last died off in Europe in the 1880s. This this creature is a sub-speices of the plains zeebra there is breeding going on to try to reproduce this creature back into existence.",year=1900)
   a3= Animal(name="Formosan Clouded Leopard",bio="The Formosan Clouded Leopard is a subspecies of the Clouded Leopard Species. Its tail is one-half the length of a regular clouded leopard. It is the second biggest carnivore of the Jade Mountain region.",extinction= "With these creatures being such big hunters themselves they were sadly hunted to extinction.",year=1980)
   a4=Animal(name="Dodo",bio="an extinct flightless bird that was endemic to the island of Mauritius east of Madagascar in the Indian Ocean.",extinction="Dutch sailors ate the beast to extinction after finding that the bird was incredibly easy to catch due to the fact it had no fear of humans.", year=1660)
   a5=Animal(name="Tasmanian Tiger",bio="A shy nocturnal animal and similar in appearance to a dog (but with a stiff tail and abdominal pouch)",extinction="There extinction is attributed to competition from Aboriginal Australians and invasive dingoes", year=1936)
   db.session.add(a1)
   db.session.add(a2)
   db.session.add(a3)
   db.session.add(a4)
   db.session.add(a5)
   db.session.commit()

   h1= Habitat(name="forest",climate="island",food="hoofstock",locationID=1)
   h2=Habitat(name="plains",climate="savannah",food="grass",locationID=1)
   h3=Habitat(name="mountain",climate="tropical",food="goats",locationID=3)
   h4=Habitat(name="wetlands",climate="wet",food="kangaroos",locationID=4)
   db.session.add(h1)
   db.session.add(h2)
   db.session.add(h3)
   db.session.add(h4)



   db.session.commit()

   a2h1= AnimalToHabitat(animalID=1,habitatID=1)
   a2h2=AnimalToHabitat(animalID=2,habitatID=2)
   a2h3=AnimalToHabitat(animalID=3,habitatID=3)
   a2h4=AnimalToHabitat(animalID=4,habitatID=1)
   a2h5=AnimalToHabitat(animalID=5,habitatID=4)
   a2h6=AnimalToHabitat(animalID=5,habitatID=1)
   a2h7=AnimalToHabitat(animalID=1,habitatID=3)
   db.session.add(a2h1)
   db.session.add(a2h2)
   db.session.add(a2h3)
   db.session.add(a2h4)
   db.session.add(a2h5)
   db.session.add(a2h6)
   db.session.add(a2h7)
   db.session.commit()

   L1=Location(continent="Africa")
   L2=Location(continent="North America")
   L3=Location(continent="Asia")
   L4=Location(continent="Australia")
   db.session.add(L1)
   db.session.add(L2)
   db.session.add(L3)
   db.session.add(L4)
   db.session.commit()
   return render_template('home.html', title='Home')