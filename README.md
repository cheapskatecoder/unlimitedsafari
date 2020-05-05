# Unlimited Safari

I am too cheap to buy and too lazy to create accounts for [Safaribooks](https://www.oreilly.com/) everytime one expires. So I created this little scraper to create accounts store them in a DB and serve them to the user with the help of Django.

## Installation

Create a visualenv either by using `pyenv` (my preferred way of creating virtualenvs) and activate it.

```
pyenv virtualenv 3.8.0 unlimitedsafari

pyenv activate unlimitedsafari
```  
Then install the dependencies using 

```bash
pip install -r requirements.txt
```

The last step is to create a database and change credentials inside `settings/dev.py` 

## Running

```python
./manage.py migrate 

./manage.py runserver 0:8080

# to run the background tasks in order to create new accounts before they expire
./manage.py process_tasks
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
