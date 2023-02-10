This code is a script written in Python language and used with the Selenium library. The purpose of this code is to reduce false positive cases in XSS vulnerabilities to zero. It takes two different parameters, urls.txt and xsswordlist.txt. Add the parameters of the URLs you crawled to urls.txt. Add your XSS scripts to xsswordlist.txt, following the "=" sign. The code is also supported by the rate flag. You can specify it as -r 10. You will write your own XSS code for each parameter and communicate with Selenium, and open a window in Firefox. If a popup appears in Firefox, it will write "vulnerable: URL: payload" to the console.


Basic usage: python3 main.py urls.txt xssworldist.txt




note: powered with CGPT

İnstall 
           
           git clone github.com/kacakb/seleniumxssChecker.git
           
Basic Usage

           
           python3 main.py urls.txt xssworldist.txt -r 10

note: You can update the xss wordlist according to your requirements. In the urls.txt, enter the parameters of your scope, for example https://redacted.com/?q=FUZZ
