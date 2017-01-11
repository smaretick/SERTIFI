# SERTIFI
samples

1. login to your BrowserStack account (BS1.png)
2. once you’re logged in BrowserStack ‘knows’ your account so when you 
   navigate to https://www.browserstack.com/automate/python and get the 
   example code with the sample for running your Python/Selenium code the 
   sample code will contain your UserName & Access key so all you need do is 
   copy/paste the sample code into your Python editor 
   (BS3.png, BS4.png & BS5.png)
3. you can also find your UserName & Access key by going to:
   https://www.browserstack.com/automate (BS2.png)
4. download & start the BrowserStackLocal tunneling process which needs to be running
   while running your Python/Selenium code so you can connect to BrowserStack & run
   ———>download exec from https://www.browserstack.com/automate/python
   WINDOWS==https://www.browserstack.com/browserstack-local/BrowserStackLocal-win32.zip
   
5. since I am using Mac/unix/command line here’s what it looks like when I start the 
   process:
=====================================================================================
MacBook-Air:Desktop scottmaretick$ ./BrowserStackLocal MDKicy4nya2192zewKpz
BrowserStackLocal v6.7

You can now access your local server(s) in our remote browser.

Press Ctrl-C to exit

=====================================================================================
6. run your Python program
7. NOTE: to turn on Visual Logs you need to add “browserstack.debug=true”
   Visual Logs not enabled. To view visual logs, set browserstack.debug=true in the input capabilities for the test:

desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'IE', 'browser_version': '7.0', 'browserstack.debug': 'true' }

8. view your test on https://www.browserstack.com/automate
9. you can download the video created…IMO best Opensource player is VLC Player (https://www.videolan.org/vlc/)
   (Sertifi.py vid included= bs-video-logs-use.mp4)
