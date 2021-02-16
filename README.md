# Welcome to the Rock, Paper, Scissors GitHub repository.

A Rock, Paper, Scissors Discord bot built on Python

<h2>Don't want to host?</h2>
Just Invite it with this link <a href="https://discord.com/oauth2/authorize?client_id=%20809509629788160010&permissions=23552&scope=bot">here!</a><br>
Uptime Checker is <a href="https://rockpaperscissors.lucyclelland.repl.co/">here!</a>


<h2>Commands</h2>

**Prefix** - "rps "

`Rock, rock, R, r` - Choose rock as your move

`Paper, paper, P, p` - Choose paper as your move

`Scissors, scissors, S, s` - Choose scissors as your move

`help` - Desplays all avalible commands

<h2 text-align:center>
How to host this Bot
</h2>

[Repl.it](#r)

[Keeping the bot alive on repl.it](#r2)

[On Your PC](#m)

## <a name="r"></a>Repl.it

Go to [repl.it](https://repl.it) (Create an account) and create a new **BASH** Project

Copy all the files from the ["Repl.it Code" Branch](https://github.com/LucyUwI/RockPaperScissors/edit/repl.it-code), delete the main.sh that is already on your repl, and drag and drop the files onto the file list on repl.it.

Edit the `.env` file to include your bot Token

Go to "Shell" on repl.it and type `pip3 install discord.py` & `pip3 install flask` (IGNORE ERRORS it will ask you to install `typeing` and update `pip` don't do this will make it so your bot will not launch)

A new tab will open, (Copy the link if you're going to procced to the next step)

Click the green "Run" Button

#### <a name="r2"></a>Keeping the bot alive on repl.it

Go to [UpTime Robot](https://uptimerobot.com/) and create an account

Once you're at your dashboard click "Create new monitor" and set it to "HTTP(s)" 

Give it a Freindly name (this can be anything)

Paste the link you copied before and click "Save" or "Done"

## <a name="m"></a>On your PC

Download or clone this repository 

 Replace "[TOKEN]" with you bot token in the `example.token.json` file
 
 Rename `example.token.json` to `token.json`
 
Download and install Python and PiP ([Linux](#Linux),[MacOS](#MacOS),[Windows](#Windows))

From a Terminal or Command Prompt run `pip3 install discord.py`

CD into thr root of the PP Rate Directory in Terminal or Command Promt

From Terminal on Linux and MaxOS run ```python3 ./bot.py``` On Command Promt on Windows run ```Py3 ./bot.py```


## <a name="Linux"></a>Install Python and PiP on Linux
[Debain/Ubuntu](#deb) [Arch](#arch)
### <a name="deb"></a> Debain/Ubuntu

```$ sudo apt update```

```$ sudo apt install python3```

### <a name="arch"></a> Arch

```# pacman -S python3```

## <a name="MacOS"></a>Install Python and PiP on MacOS

Follow the instructions [Here](https://www.python.org/downloads/release/python-391/)

## <a name="Windows"></a>Install Python and PiP on Windows

Follow the instructions [Here](https://www.python.org/downloads/release/python-391/)

