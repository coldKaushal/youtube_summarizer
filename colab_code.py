import os

if not os.path.exists('templates'):
  os.makedirs('templates')
if not os.path.exists('static'):
  os.makedirs('static')
  
  
  #create html files
  text = '''<!DOCTYPE html>
<html>

<head>
  <!-- <link rel="stylesheet" href="style.css"> -->
  <title>youtube Transcript summarizer</title>

  <meta name="viewport" content="width=device-width, initial-scale=1">


  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
    integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css"
    integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
  <!-- <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css"> -->
  <!-- <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script> -->
  <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
  <style>
    html {
      scroll-behavior: smooth;
    }

    body,
    html {
      color: white;
      height: 100%;
      width: 100%;
      margin: 0;
      padding: 0;
      background: #0c1627 !important;
    }
    h1{
      color: #F97300;
      margin-bottom: 2rem;
    }
    h3{
      color: #10828C;
    }
    img{
      margin: auto;
      height: 100%;
      width: 100%;
    }
    .searchbar {
      margin-bottom: auto;
      margin-top: auto;
      height: 60px;
      background-color: #162541;
      border-radius: 30px;
      padding: 10px;
    }

    @media screen and (min-width: 1000px) {
      .search_input {
        color: white;
        border: 0;
        outline: 0;
        background: none;
        padding: 0 10px;
        width: 480px;
        transition: width 0.4s linear;
        line-height: 40px;
      }
    }

    @media screen and (max-width: 1000px) {
      .search_input {
        color: white;
        border: 0;
        outline: 0;
        background: none;
        padding: 0 10px;
        width: auto;
        transition: width 0.4s linear;
        line-height: 40px;
      }
    }

    .searchbar:hover>.search_icon {
      background: white;
      color: #e74c3c;
    }


    .search_button {
      background-color: #0087cf;
      color: white;
      font-weight: bold;
      margin-right: 0.5rem;
    }

    .search_button:hover {
      background-color: white;
      color: #0087cf;
      font-weight: bold;
    }

    @media screen and (min-width: 1000px) {
      .navigation {
        font-size: x-large;
      }
    }

    @media screen and (max-width: 1000px) {
      .navigation {
        font-size: small;
      }
    }

    .about {
      margin: 4em 0;
      padding: 1em;
      position: relative;
    }

    .about h1 {
      color: #F97300;
      margin-bottom: 2rem;
    }

    .about img {
      height: 100%;
      width: 100%;
      border-radius: 50%
    }

    .about span {
      display: block;
      color: #888;
      position: absolute;
      left: 115px;
    }

    .about .desc {
      padding: 2em;
      border-left: 4px solid #10828C;
    }

    .about h3 {
      color: #10828C;
    }


    .contact-form h1 {
      padding: 2em 1px;
      color: #F97300;
    }

    .contact-form .right {
      max-width: 600px;
    }

    .contact-form .right .btn-secondary {
      background: #F97300;
      color: #fff;
      border: 0;
    }

    .contact-form .right .form-control::placeholder {
      color: #888;
      font-size: 16px;
    }
    .heading{
      font-weight: bolder;
    color: white;
    font: 6rem "YouTube Noto",Roboto,arial,sans-serif;
    text-align: center;
    }
  </style>
</head>

<body data-spy="scroll" data-target=".navbar" data-offset="50">

  <!-- The navbar - The <a> elements are used to jump to a section in the scrollable area -->
  <nav class="navbar navbar-expand-sm fixed-top" style="background-color: #0c1627;align-items: self-start;">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#home">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#extension">Extension</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#about">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#developer">Developer</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </nav>

  <!-- Section 1 -->
  <div id="home" style="padding-top: 5rem;">
    <div class="container h-100">
      <div style="text-align: center;margin-top: 3rem;">
        <div class="row">
          <div class="col-lg-2 col-md-4 col-sm-12">
            <img src="https://i.ibb.co/TrCz40N/Nice-Png-youtube-logo-png-157574.png" />
            <!-- <span class="text-justify">S.Web Developer</span> -->
          </div>
          <div class="col-lg-10 col-md-12 col-sm-12">
            <h1 class="heading">YT Summarizer</h3>
          </div>
        </div>
        
      </div>
      <div class="d-flex justify-content-center " style="height: 20%;margin-top: 5rem;">

        <div class="searchbar">
          <form class="search_bar" action="{{ url_for('fetchLink')}}" method="POST">
            <input type="text" name="url" class="search_input" placeholder="https://www.youtube.com/watch?v=">

            <input type="range" class="form-range" name="percent" id="customRange1" min="0" max="100" value="" oninput="document.getElementById('customRange1').value=this.value;
  document.getElementById('slidervalue').innerHTML=this.value;
  ">
            <button class="btn  search_button">
              submit
            </button>

          </form>

        </div>
      </div>
      <p id="labelforslider" style="color:white;font-size:1.2rem;
      text-align: center;margin-top: 2rem;">% Summarization : <span id="slidervalue">50</span></p>
      <div class="card text-white  mb-3" style="max-width: 50rem; background-color: #162541; margin: auto;">
        <div style="text-align: center;">Summary</div>
        <div class="card-body">
          <!-- <h5 class="card-title">Secondary card title</h5> -->
          {% block content %}{% endblock %}
            {% block error %}{% endblock %}
        </div>
      </div>
    </div>

  </div>

  <!-- section 2 -->

  <div id="extension" class = "container" style="padding-top:70px;padding-bottom:70px;margin-top: 8rem;">
    <h1>Extension</h1>
    <div class="row" style="margin-top: 4rem;">
      <div class="col-lg-8 col-md-8 col-sm-12">
        <p>
         Too lazy to open the website everytime you want the summary?
         Worry not, because we also provide you the all new powerful
         chrome extension that solves your problem.
         Follow along the steps provided below and setup the chrome extension
        </p>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-12">
        <a 
          href="https://github.com/nishantGcode10/yt-summarizer-extension/tree/master" target="_blank"><button type="button" class="btn btn-outline-success">Get Extension</button></a>
      </div>
    </div>
    <h3>Guide to install chrome extension</h3>
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" style="margin-top: 3rem;">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="5"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="6"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="7"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="8"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/help1.png?raw=true" alt="First slide">
          <div class="carousel-caption d-none d-md-block">
            <h5>STep1: Download file</h5>
            <p>click on the download button and download the file</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/help2.png?raw=true" alt="Second slide">
          <div class="carousel-caption d-none d-md-block">
            <h5>Step2: Extract the file</h5>
            <p>wait for the download and extract the downloaded file</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/help6.png?raw=true" alt="Third slide">
          <div class="carousel-caption d-none d-md-block">
            <h5>Step3: Chrome Extension</h5>
            <p>go to the chrome extension page</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/help3.png?raw=true" alt="Third slide">
          <div class="carousel-caption d-none d-md-block">
            <h5>Step4: Enable the developer mode</h5>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/help4.png?raw=true" alt="Third slide">
          <div class="carousel-caption d-none d-md-block">
            <h5>Step5: click on the load unpacked</h5>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/help5.png?raw=true" alt="Third slide">
          <div class="carousel-caption d-none d-md-block">
            <h5>Step6: load the folder</h5>
            <p>select the extracted folder</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/help8.png?raw=true" alt="Third slide">
          <div class="carousel-caption d-none d-md-block">
            <h5>Step7: Use the extension</h5>
            <p>choose any youtube video with captions and click on the extension</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/help9.png?raw=true" alt="Third slide">
          <div class="carousel-caption d-none d-md-block">
            <h5>Step8: Get the summary</h5>
            <p>choose the percentage and hit summary and wait until we do ur task</p>
          </div>
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>

  


  <!-- section 3 -->



  <div id="about" class = "container" style="padding-top:70px;padding-bottom:70px;margin-top: 8rem;">
    <h1>About</h1>
    <div class="row" style="margin-top: 4rem;">
      
      <div class="col-lg-8 col-md-8 col-sm-12">
        <p>
         Fed up of watching the long video to get some simple task done? Tired of watching wrong videos and realising
         in the end that the video was not meant for you? worry not, because we provide you the solution for all your 
         problems. Yt summatizer is here for your rescue, built on flask web framework and transformer api, fetches the
         transcript of the video and summarizes for you. millions of words in thousand for you within a minute. Try it 
         by pasting the video url that has captions, choose the percentage of the video that you want to summarize and hit the submit button.
         get your snacks ready while we generate the summary for you!
        </p>
      </div>
    </div>
    <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/about.png?raw=true" class="img-fluid" alt="monke">
  </div>


  <!-- section 4 -->
  <div id="developer" class="about" style="padding-top:70px;padding-bottom:70px;margin-top: 2rem;">
    <div class="container">
      <h1 class="text-center">About Us</h1>
      <div class="row">
        <div class="col-lg-4 col-md-4 col-sm-12">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/nishu.png?raw=true" class="img-fluid" alt="monke">
          <!-- <span class="text-justify">S.Web Developer</span> -->
        </div>
        <div class="col-lg-8 col-md-8 col-sm-12 desc">

          <h3>Nishant</h3>
          <p>
            ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </div>
      </div>

      <div class="row" style="margin-top: 4rem;">
        <div class="col-lg-8 col-md-8 col-sm-12">

          <h3>Kaushal</h3>
          <p>
            ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </div>
        <div class="desc col-lg-4 col-md-4 col-sm-12">
          <img src="https://github.com/coldKaushal/youtube_summarizer/blob/main/kaushal.png?raw=true" class="img-fluid" alt="monke">
          <!-- <span class="text-justify">S.Web Developer</span> -->
        </div>
      </div>


    </div>
  </div>
  <!-- section 4 end -->

  <!-- section 5 -->


  <div class="contact-form" id="contact" style="padding-top:70px;padding-bottom:70px;margin-top: 8rem;">
    <div class="container">
      <form action="mailto:infinitetsukiyome@gmail.com" method="post" enctype="text/plain">
        <div class="row">
          <div class="col-lg-4 col-md-4 col-sm-12">
            <h1>Get in Touch</h1>
          </div>
          <div class="col-lg-8 col-md-8 col-sm-12 right">
            <div class="form-group">
              <input type="text" class="form-control form-control-lg" placeholder="Your Name" name="">
            </div>
            <div class="form-group">
              <input type="email" class="form-control form-control-lg" placeholder="YourEmail@email.com" name="email">
            </div>
            <div class="form-group">
              <textarea class="form-control form-control-lg">

                </textarea>
            </div>
            <input type="submit" class="btn btn-secondary btn-block" value="Send" name="" >
          </div>
        </div>
      </form>
    </div>
  </div>

  <!-- section 5 end -->
</body>

</html>'''
f = open("templates/text.html", "w")
f.write(text)
f.close()

text2 = '''{% extends "text.html" %}

{%block content %}
<p class="card-text">{{summary}} </p>
{% endblock %}
{% block error %}
<p class="card-text" style="color: red;">{{message}} </p>
{% if scroll %}
<script>
    document.getElementById('{{ scroll }}').scrollIntoView();
</script>
{% endif %}
{% endblock %}

'''
f1 = open("templates/template.html", "w")
f1.write(text2)
f1.close()

#backend code

!pip install -q transformers
!pip install -q youtube_transcript_api
!pip install flask_ngrok


#import flask

from flask_ngrok import run_with_ngrok
from flask import Flask,jsonify,render_template,request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import urllib.parse as urlparse
from IPython.display import clear_output 
from flask import get_template_attribute
app = Flask(__name__)

run_with_ngrok(app)
summarization=pipeline("summarization")
#homepage endpoint
@app.route('/')
def main():
    return render_template('template.html', summary="Summary will be shown here")

#landing page after submit button
@app.route('/summary',methods = ["GET","POST"])
def fetchLink():
    try:
      if request.method =="POST":
          url=request.form.get("url")
          percent = request.form.get("percent")
          print(percent)
          percent = int(percent)
          url_data = urlparse.urlparse(url)
          query = urlparse.parse_qs(url_data.query)
          video_id = query["v"][0]
          return fetchSummary(video_id,percent)
      return render_template('template.html', message="Something went wrong please try again")
    except:
      return render_template('template.html', message="Please enter a valid email address or try again later")
# function for summarization of the video recieved by the form through post request
def fetchSummary(vid_id, percentage):
    try:
      transcript=YouTubeTranscriptApi.get_transcript(vid_id)
    except:
      return render_template('template.html', message="Something went wrong please try again")
    result = ""
    for i in transcript:
      result += ' ' + i['text']
    num_iters = int((len(result)*(percentage/100))/1000)
    summarized_text = []
    
    for i in range(0, num_iters + 1):
      start = 0
      start = i * 1000
      end = (i + 1) * 1000
      loader = (i/(num_iters+1))*100
      print(loader)
      if end-start>1000:
        return render_template('template.html', message="Video too long to summarize, please choose other video or reduce the percentage")
      try:
        out = summarization(result[start:end])
        out = out[0]
        out = out['summary_text']
      except:
        return render_template('template.html', message="Can not summarize now, please try later")
      summarized_text.append(out)
    summarized_string = ''.join(summarized_text)
    return render_template("template.html", summary=summarized_string, scroll="summaryBox")
    # content = get_template_attribute('template.html', 'content')
    # return content("summarized_text")

# @app.route('/<usr>')
# def fun(usr):
#     return jsonify(usr)

app.run()
