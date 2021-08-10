# Connect Four Game: 

## Table of Content

  * [Overview](#overview)
  * [Demo](#demo)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)



## Overview
This is a Flask web app of a gameing appi.e connect four.
5-in-a-Row, a variation of the famous Connect Four game, is a two-player connection game in which the players first choose a color and then take turns dropping colored discs from the top into a nine-column, six-row vertically suspended grid. The pieces fall straight down, occupying the next available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of five of one's own discs.

Below Image help you understand the game better.
![image](https://user-images.githubusercontent.com/6366237/128812597-2412db1f-afd9-4b36-bf33-c64c801a9066.png)

## Demo
 * Home Screen :
   ![image](https://user-images.githubusercontent.com/6366237/128811304-9445e536-7d47-4163-9a21-d66d4c9a9cb2.png)
   
 * Chat Screen
  ![image](https://user-images.githubusercontent.com/6366237/128811744-441963ac-f792-4664-9a1f-52eea8d609f1.png)

 * Winning Screen
   ![image](https://user-images.githubusercontent.com/6366237/128812275-2ea8ba41-7370-4687-a572-b0d93e17e78f.png)


## Installation
The Code is written in Python 3.8.6 . If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
Plese use the versions specified in requirements.txt to make the code work as expected.

```bash
pip install -r requirements.txt
open the project in pycham , right click on app.py and select Run app.py 
Once the server gets started , open two tabs in chore window , with the URL http://127.0.0.1:5000
and start playing the game.
```

## Directory Tree 
```
├── static 
│   ├── bootstrap.min.css
│   ├── style.css
├── template
│   ├── index.html
│   ├── chat.html
├── 5-in-a-row challenge v2.pdf
├── Readme.md
├── app.py
├── create_board.py
├── gamePlay.py
├── requirements.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/)

## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue]

## Future Scope

* Adding More validations arround users playing the game
* Front-End with more graphics diven immplementation
* Deployement on Heroku
