from flask import Flask, render_template, redirect, url_for, request
# import pickle
# from keras.preprocessing.sequence import pad_sequences
import numpy as np
from keras.models import model_from_json
from keras import backend as K
from instaloader import Instaloader, Profile
loader = Instaloader()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    category = None
    if request.method == 'POST':
        if request.form['target_profile']:
            target_profile = str(request.form['target_profile'])
            profile = Profile.from_username(loader.context, target_profile)

            num_followers = profile.followers
            total_num_likes = 0
            total_num_comments = 0
            total_num_posts = 0

            for post in profile.get_posts():
                total_num_likes += post.likes
                total_num_comments += post.comments
                total_num_posts += 1
            engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
            category = (engagement * 100)
            # category = target_profile

        else:
            category = "Enter Data"
    return render_template('home.html', category=category)

if __name__ == '__main__':
    app.run(debug = True)