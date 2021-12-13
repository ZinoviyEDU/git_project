from flask import Flask
from flask import render_template, request
from dotenv import load_dotenv


app = Flask(__name__)
app.run(debug=True)
load_dotenv('.env')


@app.route("/home/")
def home():
    text_structures = {'title': "experience",
                       'heading': "Maxes acting experience end performances",
                       'text': "The table contains the names of the performances, name of the character and the year of\
                            participation"
                       }
    lists = {'heads': ["numbers", "years", "play", "character"],
             'rows': [["1", "2021-now", '"Moana"', "Heihei"],
                      ["2", "2020-2021", '"Alice in Wonderland"', "the Mad Hatter"],
                      ["3", "2020", '"Little Red Riding Hood"', "Big Bad Wolf"],
                      ["4", "2019", '"Frozen II"', "Olaf"],
                      ["5", "2016-2019", '"The Lion King"', "Zazu"],
                      ["6", "2018", '"Frozen"', "Olaf"],
                      ["7", "2018", '"Jumanji"', "Zebra"],
                      ["8", "2018", '"Zootopia"', "Officer Benjamin Clawhauser"],
                      ["9", "2018", '"Three from Prostokvashino"', "Gavryusha"],
                      ["10", "2017-2018", '"The Snow Queen"', "Kai"],
                      ["11", "2017", '"The Three Musketeers"', "d'Artagnan"],
                      ["12", "2016-2017", '"Puss in Boots"', "Cat"]]
             }
    output = render_template('experience.html', text=text_structures, table=lists)
    return output


def write_file(data):
    with open('containers.txt', 'a') as f:
        f.write('\n'.join(data))


@app.route("/contacts/", methods=['GET', 'POST'])
def contacts():
    text_structures = {'title': "contacts",
                       'heading': "contact max",
                       'text1': "If you want to contact Max, please fill out this form",
                       'alert': "Your feedback has been received. Thank you for your time.",
                       'name': "First name:",
                       'last_name': "Last name:",
                       'email': "Enter your email:",
                       'subject': "Choose a subject:",
                       'message': "Short message",
                       'option': ["Cooperation", "Donation", "Request more information", "Other"]}
    if request.method == 'POST':
        name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        subject = request.form['subject']
        text = request.form['text']
        feedback = ['\n\nNew feedback', name, last_name, email, subject, text]
        write_file(feedback)
        return render_template('contacts.html', success=True, text=text_structures)
    else:
        return render_template('contacts.html', text=text_structures)


@app.route("/about/")
def about():
    # raise Exception("error")  ## for test custom error page '500'
    text_structures = {'title': "about",
                       'heading': "about max",
                       'text': "Passionate children's play actor featured in numerous shows. \
                            Award-winning theatre performances. \
                            Accustomed to the demanding stage sets and backed by a network of stage contacts.\
                            Known for artistic integrity and classic mezzo-soprano.",
                       'text2': "Creative and organized specialist with 5+ years of experience in a deadline-driven,\
                            high-output environment. ",
                       'text3': "Glad to bring joy and miracle to children.",
                       'heading2': "Special Skills",
                       'new': "Horse riding",
                       'badge': "New"}
    lst_skills = ['Dance (improvisational, modern)', 'Singing (musical, pop)', 'Animal accents']
    output = render_template('all-about-max.html', lst=lst_skills, text=text_structures)
    return output


@app.errorhandler(404)
def page_not_found(e):
    text_structures = {'title': "error 404",
                       'heading': "404",
                       'message': "Something went wrong!",
                       'help': "Please, check your URL or choose topic from the menu on the left."}
    return render_template('404.html', text=text_structures), 404


@app.errorhandler(500)
def server_error(e):
    text_structures = {'title': "error 500",
                       'heading': "500",
                       'message': "Something went wrong!",
                       'help': "Please, try to refresh page or choose page from the menu on the left."}
    return render_template('500.html', text=text_structures), 500
