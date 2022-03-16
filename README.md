1. get a database, register a number and upload it
2. git commit
3. add your code to template.py and rename it
4. replace lines 22 and 23 in the dockerfile with your stuff
5. if you need any dependencies, add them to pyproject.toml and run `poetry lock` 
5. create a fly app and replace/edit fly.toml


---


getting a database:

if you `fly launch`, fly will prompt you to create a PostgreSQL database. if you do, you'll get a password. the fly app should "just work", but you need to connect to it locally to upload a datastore.

grab a number, currently at <https://signal.me/#p/+12185009004>

to save the captcha, you can run 

```bash
git clone https://github.com/forestcontact/message-in-a-bottle
cd message-in-a-bottle
cp 00-signal-captcha.desktop /usr/share/applications/
cp save_signal_captcha /opt
sudo update-desktop-database
```

then go to <https://signalcaptchas.org/registration/generate.html>, solve the captcha, then go back and

```bash
signal-cli --config . --username <number> register --captcha $(cat /tmp/captcha)`
signal-cli --config . --username <number> verify <code>
poetry install 
flyctl proxy 5432:15432 -a <fly app name for db> &
DATABASE_URL=postgres://postgres:<password>@localhost:15432 poetry run python -m forest.datastore upload --path . "testbot9000"
```
