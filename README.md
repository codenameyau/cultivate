cultivate
=========

I spend a lot of time staring at black boxes.
So why not learn Japanaese in the meantime.

###Demo Output
```
$ python cultivate.py -l jpn

------------------------------
Tatoeba Sentence ID: 1771762
------------------------------

諦めては行けないのです。
akirame te ha ike nai no desu .

You must not give up.

```

###Installation
1. Clone this repository
2. Run: `pip install -r requirements.txt`
3. Run: `python cultivate.py -l jpn`

To take advatange of this program, you can create
an alias in your `.bashrc` and/or run it everytime
you open a new terminal, like so:

```bash
...
alias cultivate='python <path to cultivate.py>'
cultivate -l jpn
```

###Supported Languages
- 'cmn': Chinese
- 'deu': German
- 'eng': English
- 'fin': Finnish
- 'fra': French
- 'ita': Italian
- 'jpn': Japanese
- 'kor': Korean
- 'spa': Spanish
