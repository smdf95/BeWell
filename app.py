from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from forms import MoodForm, NegativeForm, PositiveForm, Relief, GratitudeForm, LoginForm, RegistrationForm
from datetime import date
import requests






app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'  # Store session data on the server's filesystem
app.config['SESSION_PERMANENT'] = False  # Session data is not permanent
app.config['SESSION_USE_SIGNER'] = True
app.config["SECRET_KEY"] = "mysecretkey"

Session(app)

response = requests.get("https://zenquotes.io/api/random/")

json_data = response.json()

def get_quote():
    quote = json_data[0]['q']
    return quote

quote = get_quote()

def get_author():
    author = json_data[0]['a']
    return author

author = get_author()




gratitude_journal = {
    1: {
        "date": "20/09",
        "name": "Shane",
        "gratitude": "I am grateful for the sunny weather!",
    }
}

resource_list = [
    {
        "id": 0,
        "name": "Leaves on a Stream",
        "symptoms": "rumination, worry, sadness",
        "url": "",
        "images": "https://p1.pxfuel.com/preview/521/721/196/leaves-water-reflection-color-colorful-nature.jpg",
        "description": "Leaves on a Stream is a short guided meditation that's designed to help us step away from our thoughts and watch as they come and go. This helps stop us from getting swept up and lost in our thoughts.",
        "extra_description": "This can be practiced everyday, and is a great way of learning that your thoughts are temporary, and often non-factual.",
        "sources": '<li><a href="https://insighttimer.com/">Insight Timer</a> is a free meditation app with tons of free meditations to choose from.</li><li><a href="https://www.headspace.com/">Headspace</a> is a subscription based app that offers great meditations that can be useful for beginners.</li><li><a href="https://youtube.com/">YouTube</a> and <a href="https://soundcloud.com/">SoundCloud</a> are also great sources for free meditations.'
    },
    {
        "id": 1,
        "name": "Breathing Exercises",
        "symptoms": "tension, shortness of breath, agitation, irritation, restlessness, rumination, worry",
        "url": "",
        "images": "https://c0.wallpaperflare.com/preview/163/438/524/yoga-pose-peace-zen.jpg",
        "description": "Breathing exercises help the body and mind relax and only take a few minutes. They can be done anywhere and are a great way of soothing stress and anxiety.",
        "extra_description": "We all know how to breathe. Breathing exercises help us breathe with focus and intent, while helping the body and mind find a state of calm."
    },
    {
        "id": 2,
        "name": "Mindfulness Meditation",
        "symptoms": "rumination, agitation, irritation, restlessness, worry, sadness",
        "url": "",
        "images": "https://feelgoodpal.com/blog/health-benefits-of-meditation/feature_hua7828a6576614f61d7673755ec2289a2_107633_1200x1200_fill_q100_box_smart1.jpg",
        "description": "Mindfulness meditation fosters present-moment awareness, helping us understand our thoughts and emotions without judgment, promoting inner clarity and calm.",
        "extra_description": "Whether you decide to sit down and practice for 10 minutes or you prefer to practice while going about your day, mindfulness meditation is a great way to help you manage stress and anxiety.",
        "sources": '<li><a href="https://insighttimer.com/">Insight Timer</a> is a free meditation app with tons of free meditations to choose from.</li><li><a href="https://www.headspace.com/">Headspace</a> is a subscription based app that offers great meditations that can be useful for beginners.</li><li><a href="https://youtube.com/">YouTube</a> and <a href="https://soundcloud.com/">SoundCloud</a> are also great sources for free meditations.'

    },
    {
        "id": 3,
        "name": "Mindfulness Body-Scan",
        "symptoms": "tension, rumination, agitation, irritation, restlessness, worry",
        "url": '<iframe width="60%" height="120px" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/712155895&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;">',
        "images": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBtZmeb21b0I747rlirauftr7KNAMlDXNdww&usqp=CAU",
        "description": "Body scan meditation guides us through a gentle exploration of the body, bringing attention to each part. This practice promotes relaxation and heightened bodily awareness.",
        "extra_description": "Like most mindful practices, body scans can be done whenever and wherever you are. For maximum relaxation however, lying down on a bed while practicing is best.",
        "sources": '<li><a href="https://insighttimer.com/">Insight Timer</a> is a free meditation app with tons of free meditations to choose from.</li><li><a href="https://www.headspace.com/">Headspace</a> is a subscription based app that offers great meditations that can be useful for beginners.</li><li><a href="https://youtube.com/">YouTube</a> and <a href="https://soundcloud.com/">SoundCloud</a> are also great sources for free meditations.',
        

    },
    {
        "id": 4,
        "name": "Listen to Music",
        "symptoms": "agitation, irritation, sadness",
        "url": "",
        "images": "https://images.pexels.com/photos/6399/woman-girl-technology-music.jpg",
        "description": "Listening to music is a therapeutic experience that can soothe the mind, alleviate stress, and elevate emotions, providing a refreshing break from daily routines.",
        "extra_description": "Listening to empowering or happy music can shift our perspective to view our situation in a different light."

    },
    {
        "id": 5,
        "name": "Walk",
        "symptoms": "tension, shortness of breath, agitation, restlessness, worry",
        "url": "",
        "images": "https://feelgoodpal.com/blog/can-you-lose-weight-by-walking-an-hour-a-day/feature_huaf75c49c3661eb37ef38a46188171d60_551648_1200x1200_fill_q100_box_smart1.jpg",
        "description": "Walking is a simple yet effective way to reconnect with nature, alleviate tension, and invigorate both body and mind, promoting overall well-being.",
        "extra_description": "It is a cost-efficient, yet powerful tool for combatting stress, anxiety, and depression. If walking is not a viable option for you, just simply being outside can help clear our mind and reconnect with the present moment."

    },
    {
        "id": 6,
        "name": "Yoga",
        "symptoms": "tension, shortness of breath, agitation, irritation, restlessness, worry",
        "url": "",
        "images": "https://www.madisonlibrary.org/sites/default/files/2022-11/yoga.jpg",
        "description": "Yoga combines physical postures, mindful breathing, and meditation to enhance flexibility, strength, and inner peace, fostering a harmonious balance between body and soul.",
        "extra_description": "It can be done in a class or at home. There are hundreds of free videos available on YouTube with enough variety to suit your needs. Yoga can be done in bed or in a chair, so it is a great resource for most individuals."

    },
    {
        "id": 7,
        "name": "Journaling",
        "symptoms": "agitation, irritation, rumination, worry, sadness",
        "url": "",
        "images": "https://freerangestock.com/sample/120817/close-up-of-hand-writing-on-a-notebook.jpg",
        "description": "Journaling is a reflective practice that encourages self-expression, emotional processing, and self-discovery, offering a valuable outlet for thoughts and feelings.",
        "extra_description": "Simply writing whatever comes to mind can help us unload the burden of our stress and offer us a new perspective on the situation. It can free us from endless rumination and help us to connect with our inner self."

    },
    {
        "id": 8,
        "name": "4x4 Breathing",
        "symptoms": "tension, shortness of breath, agitation, irritation, restlessness, rumination, worry",
        "url": "",
        "images": "https://www.loghouse.ie/wp-content/uploads/2022/01/How-to-build-a-Meditation-room-at-home.jpg",
        "description": "4x4 breathing, also known as box breathing, involves inhaling for 4 seconds, holding for 4 seconds, exhaling for 4 seconds, and pausing for 4 seconds between breaths, promoting relaxation and stress reduction.",
        "extra_description": "It is a simple, yet scientifically proven breathing technique that can help you to reduce stress and anxiety. It is a great way to step outside of your thoughts and focus on your breath."

    },
    {
        "id": 9,
        "name": "Mindful Colouring",
        "symptoms": "tension, agitation, irritation, restlessness, rumination, worry, sadness",
        "url": "",
        "images": "https://www.stockvault.net/data/2016/09/28/211357/preview16.jpg",
        "description": "Mindful colouring is a meditative practice that involves focusing on colouring intricate patterns or images with full attention, helping to calm the mind and reduce stress.",
        "extra_description": "Mindful colouring books are like colouring books for adults. It allows us to become immersed in a creative process, which has been found to be incredibly helpful for our mental health."
    },
    {
        "id": 10,
        "name": "Read a Book",
        "symptoms": "agitation, irritation, restlessness, rumination, worry",
        "url": "",
        "images": "https://live.staticflickr.com/65535/51097799939_30a167fc22_b.jpg",
        "description": "Reading a book can help you relax, clear your mind, and boost your mood. It can also help you fall asleep quicker.",
        "extra_description": "Reading has been found to be a great resource for stress relief and relaxation."
    }
]


accounts = [
    {
        "id": 0,
        "username": "admin",
        "password": "test123"
    }
]



with app.test_request_context():
    print("Before clearing session:")
    print(session)
    session.clear()
    session['logged_in'] = False
    session['user'] = None
    print("After initializing session:")
    print(session)

@app.route('/redirect_login')
def redirect_login():
    session['previous_page'] = request.referrer
    return redirect(url_for('login'))

@app.route('/redirect_register')
def redirect_register():
    session['previous_page'] = request.referrer
    return redirect(url_for('register'))

@app.route('/redirect_logout')
def redirect_logout():
    session['previous_page'] = request.referrer
    return redirect(url_for('login'))

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    

    form = MoodForm()
    negative_form = NegativeForm()
    positive_form = PositiveForm()
    
    negative_mood = negative_form.neg_selection.data
    if negative_form.validate_on_submit():
        if negative_mood == "Yes":
            print(negative_mood)
            return redirect(url_for("relief"))
    
    
    
    if positive_form.validate_on_submit():
        print("okay")
        if positive_form.pos_selection.data == "Yes":
            print(positive_form.pos_selection.data)
            return redirect(url_for("gratitude"))
    else:
        print("Oops")

    return render_template("index.html", form=form, negative_form=negative_form, positive_form=positive_form, quote=quote, author=author)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' not in session:
        session['logged_in'] = False

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        for account in accounts:
            if account['username'] == username and account['password'] == password:
                session['logged_in'] = True
                session['user'] = account['id']
                previous_page = session.get('previous_page')
                print("previous_page:", previous_page)
                if previous_page:
                    return redirect(previous_page)
                else:
                    return redirect(url_for('index'))
        # If no matching account is found, return an error message
        return render_template('login.html', form=form, error='Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.username.data in accounts:
            return redirect(url_for("login"))
        else:
            accounts.append({
                "id": len(accounts),
                "username": form.username.data,
                "password": form.password.data
            })
            session['logged_in'] = True
            session['user'] = len(accounts) - 1
            previous_page = session.get('previous_page')
            print("previous_page:", previous_page)
            if previous_page:
                return redirect(previous_page)
            else:
                return redirect(url_for('index'))
    return render_template("register.html", form=form)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session['user'] = None
    previous_page = session.get('previous_page')
    print("previous_page:", previous_page)
    if previous_page:
        return redirect(previous_page)
    else:
        return redirect(url_for('index'))

@app.route('/resources/')
def resources():

    return render_template("resources.html", resource_list=resource_list)

@app.route('/resource/<id>')
def resource_info(id):
    return render_template("resource_info.html", resource=resource_list[int(id)], id=id)


@app.route("/gratitude", methods=['GET', 'POST'])
def gratitude():
    form = GratitudeForm()
    username = session.get('user')
    current_date = date.today()
    formatted_date = current_date.strftime("%d/%m")
    if form.validate_on_submit():
        key = len(gratitude_journal) + 1
        id = username
        name = accounts[username]['username']
        gratitude = form.gratitude.data

        gratitude_journal[key] = {
            "id": id,
            "date": formatted_date,
            "name": name,
            "gratitude": gratitude
        }

        return redirect(url_for("gratitude"))
    
    return render_template('gratitude.html', gratitude_journal=gratitude_journal, form=form)




@app.route('/delete/<int:key>')
def delete(key):
    if key in gratitude_journal:
        del gratitude_journal[key]
        return redirect(url_for("gratitude"))
        
        

filtered_items = []  

@app.route("/relief", methods=['GET', 'POST'])
def relief():
    form = Relief()
    global filtered_items

    if request.method == 'POST':
        if form.validate_on_submit():
            selected_feelings = form.relief.data

            filtered_items = []

            for resource in resource_list:
                if any(feeling.lower() in resource["symptoms"].lower() for feeling in selected_feelings):
                    filtered_items.append({
                        "id": resource["id"],
                        "name": resource["name"],
                        "images": resource["images"],
                        "url": resource["url"],
                        "symptoms": resource["symptoms"],
                        "description": resource["description"]
                    })

            return render_template('relief_resources.html', filtered_items=filtered_items, selected_feelings=selected_feelings)

    return render_template('relief.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)