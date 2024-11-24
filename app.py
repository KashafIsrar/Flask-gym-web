from flask import Flask, render_template

app = Flask(__name__)


services = [
        {
            'title': 'Personal Trainer',
            'description': 'Get one-on-one coaching with our experienced trainers to achieve your fitness goals faster.',
            'image': 'img/service1.jpg',
            'alt': 'Personal Trainer Image',
            'button_text': 'Learn More',
            'link': '#'
        },
        {
            'title': 'Free WiFi',
            'description': 'Stay connected with our high-speed WiFi while you work out or relax in our lounge.',
            'image': 'img/service1.jpg',
            'alt': 'Free WiFi Image',
            'button_text': 'Learn More',
            'link': '#'
        },
        {
            'title': 'Friendly Environment',
            'description': 'Enjoy working out in a welcoming, motivating, and judgment-free space.',
            'image': 'img/service1.jpg',
            'alt': 'Friendly Environment Image',
            'button_text': 'Learn More',
            'link': '#'
        }
    ]

memberships = [
        {
            'title': 'Personal Trainer',
            'description': 'Modern Equipment.',
            'image': 'img/membership.webp',
            'alt': 'Personal Trainer Image',
            'button_text': 'Learn More',
            'link': '#'
        },
        {
            'title': 'Free WiFi',
            'description': 'Variety og group classes',
            'image': 'img/membership.webp',
            'alt': 'Free WiFi Image',
            'button_text': 'Learn More',
            'link': '#'
        },
        {
            'title': 'Friendly Environment',
            'description': 'Expert Personal Trainers',
            'image': 'img/membership.webp',
            'alt': 'Friendly Environment Image',
            'button_text': 'Learn More',
            'link': '#'
        }
    ]

@app.route('/')
def home():
    return render_template('index.html', services=services)

@app.route('/about')
def about():

    return render_template('about.html', services=services)

@app.route('/membership')
def membership():
    return render_template('membership.html', memberships=memberships)

if __name__ == '__main__':
    app.run(debug=True)
