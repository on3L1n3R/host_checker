**********************Examples of uses*******************************
#DNS
checker.py --method dns --host 8.8.8.8
checker.py --method dns --host google.com
checker.py --method dns --host https://google.com
<ip> / <domain name> / <URL> 

#PING
checker.py --method ping --host 8.8.8.8
checker.py --method ping --host google.com
checker.py --method ping --host https://google.com
<ip> / <domain name> / <URL> 

#HTTP
checker.py --method http --host google.com
checker.py --method http --host https://google.com
<domain name> / <URL> 

#TCP
checker.py --method tcp --host google.com
checker.py --method tcp --host https://google.com
<domain name> / <URL> 


