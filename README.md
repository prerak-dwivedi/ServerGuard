# ServerGuard

Small python project that reads a web server log, finds the requests that look like attacks and saves them to a csv. I made it because going through logs by hand is slow and you end up missing stuff.

It's a first-pass filter, not a real security tool. Don't use it instead of a WAF or anything like that.

## What it does

It goes through the log file one line at a time and grabs the IP, the request path and the status code. Then every path is checked against a list of keywords (SQL injection stuff like `union` and `drop`, XSS stuff like `<script>`, and path traversal like `../`). Anything that matches goes into `unsafe_logs.csv`.

If a line is broken and can't be parsed it doesn't crash, the line just gets saved in `failed_server_logs.txt` and the program moves on.

## Running it

No libraries needed, just python (I used 3.14, anything 3.10+ should be fine).

```
git clone https://github.com/prerak-dwivedi/ServerGuard.git
cd ServerGuard
python main.py
```

Run it from inside the folder since the paths are relative.
It reads `server_logs.txt` by default, which is a sample log I put together with a mix of normal traffic and attacks.

On the sample file you get this:

```
execution complete!
clean logs parsed: 93
corrupt logs separated: 1
threats detected: 10
```

and the csv looks like

```
ip address,path,status
10.0.0.5,/search?q=<script>alert('XSS')</script>,403
172.16.0.12,/../../../../etc/passwd,403
10.0.0.55,/login?user=admin'; DROP TABLE users; --,403
```

## Files

* `main.py` runs everything in order
* `config.py` has the file paths and the keyword list, change stuff here
* `parser.py` reads the log and splits it into clean and corrupt lines
* `error_logger.py` writes the corrupt lines out
* `threat_engine.py` does the keyword matching
* `reporter.py` makes the csv

To use your own log change `log_file_path` in `config.py`. It expects the normal apache/nginx combined format, like `IP - - [time] "GET /path HTTP/1.1" 200 1234 "-" "user-agent"`.

## What it doesn't do (yet)

Being honest here, detection is just keyword matching so it misses a lot. In the sample data it doesn't catch `' OR 1=1 --`, the `onerror=` / `onload=` XSS ones or the `xp_cmdshell` one. Short keywords like `select` and `drop` can also flag totally normal paths.

Brute force detection isn't in there either, even tho the sample logs have a few IPs spamming login with 401s. That's the next thing I want to add.

Other small things: only the path is checked (not user agent or POST data), and the failed logs file is opened in append mode so running it twice duplicates the corrupt lines.

## Todo

* brute force detection (lots of 401s from one IP)
* regex instead of plain keywords
* put the attack type and timestamp in the csv
* take the log file as a command line argument
* tests

Issues and PRs are fine if you want to add signatures or fix something.

Made by [@prerak-dwivedi](https://github.com/prerak-dwivedi)
