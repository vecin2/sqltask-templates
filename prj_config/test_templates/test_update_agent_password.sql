--["admin","ccagent"]
update agent
set PASSWORD = (select PASSWORD from AGENT where username ='admin'),
 SALT = (select SALT from agent where username = 'admin'),
 EXPIRES = (select EXPIRES from AGENT where USERNAME = 'admin'),
 DISABLED ='no',
 LASTLOGGEDIN = CURRENT_DATE
where USERNAME in ('ccagent');
