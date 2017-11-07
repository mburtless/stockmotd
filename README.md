# stockmotd
> Grab the latest stock quotes and use it for your Message of the Day!

A short python script to fetch the latest stock prices for symbols and output them in a format suitable for using as your MOTD.  All data provided for free by [IEX](https://iextrading.com/developer).

## Installation
This varies by distro and personal preference.  One quick and dirty method would be to call it directly from your user's .bash_profile.  Alternatively, to set this for all users, copy the script to /etc/profile.d and create a shell script to call it

## Usage
```python stockmotd.py --symbol [LIST OF SYMBOLS TO QUOTE]```
