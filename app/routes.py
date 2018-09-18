from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'sonya'}
    welcome = "Extinct Animal Page"
    introduction = "Sadly since the beginning of life, we have lost many interesting species due to extinction." \
                   " This gives you opportunity to read about these fascinating creatures." \


    return render_template('home.html', title='Home', user=user, welcome=welcome, introduction=introduction)


@app.route('/zanzibar_leopard', methods=['GET', 'POST'])
def zanzibar_leopard():
    form = LoginForm()

    if form.validate_on_submit():
        title = form.username.data
    else:
        title = 'zanzibar leopard'

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
        bio = "The Zanzibar Leopard is an African leopard. Its origin lies in Unguja Island of Zanzibar Archipelago." \
          "These leopards were believed to be part of local witch craft. In 2008 the leopard was considered extinct" \
          "due to prejudices from local hunters. In the 1990s a conservation effort was made to " \
          "try to restore leopards. Sadly it seems that these creatures are no more..."

    if form.validate():
        behavior = form.animalBehavior.data
    else:
        behavior = "Very little is known about the behavior of this animal. The last documented sighting was in the 1980s. " \
               "There are only six skins left in the world left of this animal. " \
               "It was much smaller than the average leopard. " \
               "The coat was much lighter and tiny faded spots. There diet consist of fish and live stock. " \
               "These leopards were used to an island climate."

    if form.validate_on_submit():
        extermination = form.extermination.data
    else:
        extermination = "The extermination of the Zanzibar Leopard was cultivated by local farmers convinced" \
                    " these animals were kept by witches and trained to harass the local farmers by their owners." \
                    " The belief swept across the Island tha leopards could be trained to do the evil " \
                    "bidding of those performing witchcraft. The beautiful cats were considered vermin." \
                    " The problem began in the 20th century when the human populous and" \
                    " agricultural encroached on the habitat of the Zanzibar Leopard. " \
                    "The Zanzibar revolution of 1964 ws a combo of an anti-witchcraft and anti-leopard campaign " \
                    "founded by a witch seeker that ultimately led to the near extinction of the Zanzibar Leopard."

    return render_template("zanzibar_leopard.html", b=bio, behavior=behavior, e=extermination, p=picture, t=title)

@app.route('/animals')
def animals():
    animals = {'username': 'sonya'}
    posts = [
        {
            'animals': {'username': 'The Zanzibar Leopard'},
            'links': '/zanzibar_leopard'
        },
        {
            'animals': {'username': 'Quagga'},
            'links': '/zanzibar_leopard'

        },

        {
            'animals': {'username': 'Tasmanian Tiger'},
            'links': '/zanzibar_leopard'

        },

        {
            'animals': {'username': 'Pinta Island Tortoise'},
            'links': '/zanzibar_leopard'

        },

        {
            'animals': {'username': 'Dodo'},
            'links': '/zanzibar_leopard'

        }

    ]

    return render_template('animals.html', title='Artist Page', animals=animals, posts=posts)

@app.route('/create_bio_page', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Animal was created {}'.format(
            form.username.data))
        return redirect(url_for('zanzibar_leopard'))
    return render_template('create_bio_page.html',  title='Sign In', form=form)
