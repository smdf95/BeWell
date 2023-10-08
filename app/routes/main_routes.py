from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from app.forms import MoodForm, NegativeForm, PositiveForm, Relief, GratitudeForm, LoginForm, ForgotPasswordForm, ResetPasswordForm, RegistrationForm
from datetime import date
from . import main_bp
import requests


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






resource_list = [
    {
        "id": 0,
        "name": "Leaves on a Stream",
        "symptoms": "rumination, worry, sadness",
        "url": '<iframe width="60%" height="120px" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/194056066&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/dennis-tirch-phd" title="CompassionFocusedTherapy" target="_blank" style="color: #cccccc; text-decoration: none;">CompassionFocusedTherapy</a> · <a href="https://soundcloud.com/dennis-tirch-phd/leaves-on-a-stream" title="Leaves On A Stream" target="_blank" style="color: #cccccc; text-decoration: none;">Leaves On A Stream</a></div>',
        "images": "https://p1.pxfuel.com/preview/521/721/196/leaves-water-reflection-color-colorful-nature.jpg",
        "description": "Leaves on a Stream is a short guided meditation that's designed to help us step away from our thoughts and watch as they come and go. This helps stop us from getting swept up and lost in our thoughts.",
        "extra_description": "This can be practiced everyday, and is a great way of learning that your thoughts are temporary, and often non-factual.",
        "sources": '<li><a href="https://insighttimer.com/" target="blank">Insight Timer</a> is a free meditation app with tons of free meditations to choose from.</li><li><a href="https://www.headspace.com/" target="blank">Headspace</a> is a subscription based app that offers great meditations that can be useful for beginners.</li><li><a href="https://youtube.com/" target="blank">YouTube</a> and <a href="https://soundcloud.com/" target="blank">SoundCloud</a> are also great sources for free meditations.'
    },
    {
        "id": 1,
        "name": "Breathing Exercises",
        "symptoms": "tension, shortness of breath, agitation, irritation, restlessness, rumination, worry",
        "url": '<iframe width="60%" height="120px" frameborder="no" scrolling="no" seamless src="https://player.simplecast.com/eec2e93f-8375-4958-aae6-faf03c76fc92?dark=false"></iframe>',
        "images": "https://c0.wallpaperflare.com/preview/163/438/524/yoga-pose-peace-zen.jpg",
        "description": "Breathing exercises help the body and mind relax and only take a few minutes. They can be done anywhere and are a great way of soothing stress and anxiety.",
        "extra_description": "We all know how to breathe. Breathing exercises help us breathe with focus and intent, while helping the body and mind find a state of calm.",
        "sources": "<li><a href='https://www.breathewithniall.com/wim-hof-method-blog/2021/3/9/10-days-of-breathing' target='blank'>Breathe with Níall</a> offers a free 10-day Breathing exercise program, which is a great way of finding out if breathing exercises are for you.</li><li>You can find lots of videos on <a href='https://www.youtube.com/' target='blank'>YouTube</a> if you don't feel like signing up to a 10-day program.</li>"
    },
    {
        "id": 2,
        "name": "Mindfulness Meditation",
        "symptoms": "rumination, agitation, irritation, restlessness, worry, sadness",
        "url": '',
        "images": "https://feelgoodpal.com/blog/health-benefits-of-meditation/feature_hua7828a6576614f61d7673755ec2289a2_107633_1200x1200_fill_q100_box_smart1.jpg",
        "description": "Mindfulness meditation fosters present-moment awareness, helping us understand our thoughts and emotions without judgment, promoting inner clarity and calm.",
        "extra_description": "Whether you decide to sit down and practice for 10 minutes or you prefer to practice while going about your day, mindfulness meditation is a great way to help you manage stress and anxiety.",
        "sources": '<li><a href="https://insighttimer.com/" target="blank">Insight Timer</a> is a free meditation app with tons of free meditations to choose from.</li><li><a href="https://www.headspace.com/" target="blank">Headspace</a> is a subscription based app that offers great meditations that can be useful for beginners.</li><li><a href="https://youtube.com/" target="blank">YouTube</a> and <a href="https://soundcloud.com/" target="blank">SoundCloud</a> are also great sources for free meditations.'

    },
    {
        "id": 3,
        "name": "Mindfulness Body-Scan",
        "symptoms": "tension, rumination, agitation, irritation, restlessness, worry",
        "url": '<iframe width="60%" height="120px" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/712155895&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;">',
        "images": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBtZmeb21b0I747rlirauftr7KNAMlDXNdww&usqp=CAU",
        "description": "Body scan meditation guides us through a gentle exploration of the body, bringing attention to each part. This practice promotes relaxation and heightened bodily awareness.",
        "extra_description": "Like most mindful practices, body scans can be done whenever and wherever you are. For maximum relaxation however, lying down on a bed while practicing is best.",
        "sources": '<li><a href="https://insighttimer.com/" target="blank">Insight Timer</a> is a free meditation app with tons of free meditations to choose from.</li><li><a href="https://www.headspace.com/" target="blank">Headspace</a> is a subscription based app that offers great meditations that can be useful for beginners.</li><li><a href="https://youtube.com/" target="blank">YouTube</a> and <a href="https://soundcloud.com/" target="blank">SoundCloud</a> are also great sources for free meditations.'
        

    },
    {
        "id": 4,
        "name": "Listen to Music",
        "symptoms": "agitation, irritation, sadness",
        "url": '',
        "images": "https://images.pexels.com/photos/6399/woman-girl-technology-music.jpg",
        "description": "Listening to music is a therapeutic experience that can soothe the mind, alleviate stress, and elevate emotions, providing a refreshing break from daily routines.",
        "extra_description": "Listening to empowering or happy music can shift our perspective to view our situation in a different light.",
        "sources": '<li><a href="https://spotify.com/" target="blank">Spotify</a> is a popular music streaming service with a vast library of songs and playlists for all tastes.</li><li><a href="https://apple.com/music/" target="blank">Apple Music</a> offers a wide selection of songs, albums, and curated playlists, and it is seamlessly integrated with Apple devices.</li><li><a href="https://soundcloud.com/" target="blank">SoundCloud</a> is a free platform where independent artists and musicians share their music, making it a great place to discover new and unique tracks.</li><li><a href="https://youtube.com/" target="blank">YouTube</a> has a vast source of free music videos, live performances, and user-generated playlists. You can find almost any song or music genre on YouTube.</li>'

    },
    {
        "id": 5,
        "name": "Walk",
        "symptoms": "tension, shortness of breath, agitation, restlessness, worry",
        "url": '',
        "images": "https://feelgoodpal.com/blog/can-you-lose-weight-by-walking-an-hour-a-day/feature_huaf75c49c3661eb37ef38a46188171d60_551648_1200x1200_fill_q100_box_smart1.jpg",
        "description": "Walking is a simple yet effective way to reconnect with nature, alleviate tension, and invigorate both body and mind, promoting overall well-being.",
        "extra_description": "It is a cost-efficient, yet powerful tool for combatting stress, anxiety, and depression. If walking is not a viable option for you, just simply being outside can help clear our mind and reconnect with the present moment.",
        "sources": '<li><a href="https://www.alltrails.com/" target="_blank">AllTrails</a> provides a vast database of hiking and walking trails, including user reviews and trail maps.</li><li><a href="https://www.walkscore.com/" target="_blank">Walk Score</a> calculates the walkability of a neighborhood, helping you find pedestrian-friendly areas and plan walking routes.</li><li><a href="https://www.mapmywalk.com/" target="_blank">MapMyWalk</a> tracks your walking routes, distance, and calories burned, helping you set and achieve walking goals.</li>'

    },
    {
        "id": 6,
        "name": "Yoga",
        "symptoms": "tension, shortness of breath, agitation, irritation, restlessness, worry",
        "url": '<iframe width="60%" height="350" src="https://www.youtube.com/embed/v7AYKMP6rOE?si=algh5jh6uwLWTbPv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
        "images": "https://www.madisonlibrary.org/sites/default/files/2022-11/yoga.jpg",
        "description": "Yoga combines physical postures, mindful breathing, and meditation to enhance flexibility, strength, and inner peace, fostering a harmonious balance between body and soul.",
        "extra_description": "It can be done in a class or at home. There are hundreds of free videos available on YouTube with enough variety to suit your needs. Yoga can be done in bed or in a chair, so it is a great resource for most individuals.",
        "sources": '<li><a href="https://www.yotube.com/" target="blank">Youtube</a> offers a plethora of free youtube classes ranging in duration and difficulty.<li><a href="https://yogawithadriene.com/" target="blank">Yoga with Adriene</a> offers a vast collection of free yoga classes and tutorials on YouTube, suitable for all levels.</li><li>Want to join a class? check out a list of<a href="https://www.google.com/search?q=yoga+classes+near+me&sca_esv=570601344&sxsrf=AM9HkKlgnBkDCdLKtaXFtN4if5dqggOe3w%3A1696410972665&ei=XC0dZbWYKPKwhbIPxLabkAE&oq=yoga+class&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnlvZ2EgY2xhc3MqAggBMggQABiKBRiRAjIIEAAYgAQYyQMyCBAAGIoFGJIDMggQABiABBiSAzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEizFFAAWMEMcAB4AJABAJgBdaABkAaqAQM5LjG4AQPIAQD4AQHCAgcQIxiKBRgnwgIUEC4YgwEYxwEYsQMY0QMYigUYkQLCAg4QABiKBRixAxiDARiRAsICDRAuGIoFGLEDGIMBGEPCAhEQLhiABBixAxiDARjHARjRA8ICCxAAGIAEGLEDGIMBwgILEC4YigUYsQMYgwHCAggQLhiABBixA8ICCBAAGIAEGLEDwgITEC4YigUYsQMYgwEYxwEY0QMYQ8ICDhAuGIoFGMcBGNEDGJECwgINEAAYigUYsQMYgwEYQ8ICIhAuGIoFGLEDGIMBGMcBGNEDGEMYlwUY3AQY3gQY4ATYAQHCAgsQABiKBRixAxiRAsICChAuGIoFGLEDGEPCAgcQABiKBRhDwgILEC4YgAQYsQMYgwHCAg4QABiABBixAxiDARjJA8ICDhAAGIAEGLEDGIMBGJIDwgIQEAAYigUYsQMYgwEYyQMYQ-IDBBgAIEGIBgG6BgYIARABGBQ&sclient=gws-wiz-serp" target="blank"> yoga classes</a> near you.</li>'

    },
    {
        "id": 7,
        "name": "Journaling",
        "symptoms": "agitation, irritation, rumination, worry, sadness",
        "url": '',
        "images": "https://freerangestock.com/sample/120817/close-up-of-hand-writing-on-a-notebook.jpg",
        "description": "Journaling is a reflective practice that encourages self-expression, emotional processing, and self-discovery, offering a valuable outlet for thoughts and feelings.",
        "extra_description": "Simply writing whatever comes to mind can help us unload the burden of our stress and offer us a new perspective on the situation. It can free us from endless rumination and help us to connect with our inner self.",
        "sources": '<li><a href="https://www.journaling.com/" target="_blank">Journaling.com</a> is a website dedicated to journaling with resources and prompts, and it also offers a platform for digital journaling.</li><li><a href="https://www.journalate.com/" target="_blank">Journalate</a> is an online platform for digital journaling, allowing you to write and reflect privately.</li><li><a href="https://journey.cloud/" target="_blank">Journey</a> is a multi-platform journal app that syncs across devices, offering a private and secure space for journaling.</li>'

    },
    {
        "id": 8,
        "name": "4x4 Breathing",
        "symptoms": "tension, shortness of breath, agitation, irritation, restlessness, rumination, worry",
        "url": '<iframe width="40%" height="280px" class="small_video" src="https://www.youtube.com/embed/bF_1ZiFta-E?si=1QWvdguEyo-gGSDz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
        "images": "https://www.loghouse.ie/wp-content/uploads/2022/01/How-to-build-a-Meditation-room-at-home.jpg",
        "description": "4x4 breathing, also known as box breathing, involves inhaling for 4 seconds, holding for 4 seconds, exhaling for 4 seconds, and pausing for 4 seconds between breaths, promoting relaxation and stress reduction.",
        "extra_description": "It is a simple, yet scientifically proven breathing technique that can help you to reduce stress and anxiety. It is a great way to step outside of your thoughts and focus on your breath."

    },
    {
        "id": 9,
        "name": "Mindful Colouring",
        "symptoms": "tension, agitation, irritation, restlessness, rumination, worry, sadness",
        "url": '',
        "images": "https://www.stockvault.net/data/2016/09/28/211357/preview16.jpg",
        "description": "Mindful colouring is a meditative practice that involves focusing on colouring intricate patterns or images with full attention, helping to calm the mind and reduce stress.",
        "extra_description": "Mindful colouring books are like colouring books for adults. It allows us to become immersed in a creative process, which has been found to be incredibly helpful for our mental health.",
        "sources": '<li><a href="https://www.coloringpagesforadults.net/" target="_blank">Coloring Pages for Adults</a> offers a variety of free printable coloring pages designed specifically for adults for mindful coloring.</li><li><a href="https://www.justcolor.net/" target="_blank">Just Color</a> provides a wide selection of free coloring pages, including intricate and detailed designs perfect for relaxation.</li><li><a href="https://www.coloring-book.info/" target="_blank">Coloring Book Info</a> offers a collection of printable coloring pages featuring various themes, from nature to mandalas.</li><li><a href="https://www.crayola.com/free-coloring-pages" target="_blank">Crayola</a> offer a range of coloring sheets for all ages, with a focus on creativity and mindfulness.</li>'
    },
    {
        "id": 10,
        "name": "Read a Book",
        "symptoms": "agitation, irritation, restlessness, rumination, worry",
        "url": '',
        "images": "https://live.staticflickr.com/65535/51097799939_30a167fc22_b.jpg",
        "description": "Reading a book can help you relax, clear your mind, and boost your mood. It can also help you fall asleep quicker.",
        "extra_description": "Reading has been found to be a great resource for stress relief and relaxation.",
        "sources": '<li><a href="https://www.projectgutenberg.org/" target="_blank">Project Gutenberg</a> offers over 60,000 free eBooks, including many classic literary works.</li><li><a href="https://openlibrary.org/" target="_blank">Open Library</a> is a digital library that provides access to a wide range of books, including rare and out-of-print titles.</li><li><a href="https://www.amazon.com/Kindle-eBooks/b?ie=UTF8&node=154606011" target="_blank">Amazon Kindle Store</a> provides a wide selection of eBooks for Kindle readers and apps.</li><li><a href="https://www.audible.com/" target="_blank">Audible</a> offers a vast collection of audiobooks for those who prefer to listen while reading.</li><li><a href="https://librivox.org/" target="_blank">LibriVox</a> offers free audiobooks of public domain books, read by volunteers from around the world.</li>'
    }
]


accounts = [
    {
        "id": 1,
        "username": "shane",
        "name": "Shane",
        "email": "seaghan.fisher@gmail.com",
        "password": "test123"
    }
]

gratitude_journal = {
    1: {
        "id": 1,
        "date": "20/09",
        "name": "shane",
        "gratitude": "I am grateful for the sunny weather!",
    }
}

filtered_items = []  


@main_bp.before_request
def before_request():
    username = session.get('user')

    if username is None or username < 1 or username > len(accounts):
        session['logged_in'] = False
        session['user'] = 0
    
        

@main_bp.route("/", methods=['GET', 'POST'])
@main_bp.route("/index", methods=['GET', 'POST'])
def index():

    form = MoodForm()
    negative_form = NegativeForm()
    positive_form = PositiveForm()
    
    negative_mood = negative_form.neg_selection.data
    if negative_form.validate_on_submit():
        if negative_mood == "Yes":
            print(negative_mood)
            return redirect(url_for("main.relief"))
    
    
    
    if positive_form.validate_on_submit():
        if positive_form.pos_selection.data == "Yes":
            print(positive_form.pos_selection.data)
            return redirect(url_for("main.gratitude"))

    return render_template("index.html", form=form, negative_form=negative_form, positive_form=positive_form, quote=quote, author=author, accounts=accounts)



@main_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()


    previous_page = request.args.get('previous_page')
    print('Previous Page:', previous_page)

    if previous_page:
        session['previous_page'] = previous_page
    

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        for account in accounts:
            if (account['username'] == username or account['email'] == username) and account['password'] == password:
                session['logged_in'] = True
                session['user'] = account['id']
                print("previous_page:", previous_page)
                if previous_page:
                    return redirect(previous_page)
                else:
                    return redirect(url_for('main.index'))
            else:
                flash("The information you entered is incorrect", "danger")
        return render_template('login.html', form=form, error='Invalid username or password')
    return render_template('login.html', form=form)

@main_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        for account in accounts:
            if account['email'] == email:
                return redirect(url_for('main.reset_password', email=email))
        return render_template('forgot_password.html', form=form, error='Invalid email')
    return render_template('forgot_password.html', form=form)

@main_bp.route('/reset_password/<email>', methods=['GET', 'POST'])
def reset_password(email):
    form = ResetPasswordForm()
    if form.validate_on_submit():
        password = form.password.data
        for account in accounts:
            if account['email'] == email:
                account['password'] = password
                return redirect(url_for('main.login'))
        return render_template('forgot_password.html', form=form, error='Invalid email')
    return render_template('reset_password.html', form=form)



@main_bp.route('/register', methods=['GET', 'POST'])
def register():

    previous_page = request.args.get('previous_page')

    form = RegistrationForm()
    if form.validate_on_submit():
        entered_email = form.email.data.lower()
        if any(account['email'].lower() == entered_email for account in accounts):
            flash('This email is already in use', 'danger')
            return redirect(url_for('main.register'))
        if any(account['username'] == form.username.data for account in accounts):
            flash('This username is already in use', 'danger')
        else:
            accounts.append({
                "id": len(accounts) + 1,
                "email": entered_email,
                "name": form.name.data,
                "username": form.username.data,
                "password": form.password.data
            })
            session['logged_in'] = True
            session['user'] = len(accounts)
            print("previous_page:", previous_page)
            if previous_page:
                return redirect(previous_page)
            else:
                return redirect(url_for('main.index'))
    return render_template("register.html", form=form)

@main_bp.route('/redirect_logout')
def redirect_logout():
    session['previous_page'] = request.referrer
    session['logged_in'] = False
    session['user'] = 0
    return redirect(session['previous_page'])

@main_bp.route('/resources/')
def resources():

    return render_template("resources.html", resource_list=resource_list)

@main_bp.route('/resource/<id>')
def resource_info(id):
    return render_template("resource_info.html", resource=resource_list[int(id)], id=id)


@main_bp.route("/gratitude", methods=['GET', 'POST'])
def gratitude():
    
    form = GratitudeForm()
    username = session.get('user')     
   
    current_date = date.today()
    formatted_date = current_date.strftime("%d/%m")
    if form.validate_on_submit():
        key = len(gratitude_journal) + 1
        id = username
        name = accounts[username - 1]['username']
        gratitude = form.gratitude.data

        gratitude_journal[key] = {
            "id": id,
            "date": formatted_date,
            "name": name,
            "gratitude": gratitude
        }

        return redirect(url_for("main.gratitude"))
        
    return render_template('gratitude.html', gratitude_journal=gratitude_journal, form=form)


@main_bp.route('/delete/<int:key>')
def delete(key):
    if key in gratitude_journal:
        del gratitude_journal[key]
        flash("Your post has been deleted!", "success")
        return redirect(url_for("main.gratitude"))        


@main_bp.route("/relief", methods=['GET', 'POST'])
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