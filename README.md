# Bitly URL shortener

This is a console URL shortener which uses bit.ly API and also counts clicks on the short link.

### How to use

Just run the python script main.py with the following concole command:
```
python main.py [your URL starting with http or https]
```
For example:
```
python main.py https://google.com
```
The result will be:
```
Битлинк: https://bit.ly/3hwtIZF
Число кликов: 0
```

### How to install dependencies

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
I don't think you need to use any virtual envs for such a small script.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
