#Spear Phishing Detection on Twitter 

**Team Member**  
Yuhang Wang,
Yuqian Huang,
Qingying Hao,
Ze yu
## Part 1 : Threat identify

Exciting and ground--‐breaking threat that exceeds current market and industry detections
The threat we are considering here is the spear phishing message spread through social media networks. Although spear phishing mostly targets at email users, we see the possibility of the emergence of spear phishing in social media platforms; ZeroFox has also paid attention to the threats of malicious / phishing / spam spreading through social media messages by having several corresponding suspicious link policies. The security threat we define here is the spear phishing messages based on social media networks which targets at specific user (group of users) and usually being published by “trustworthy” sources. 
 
Spear phishing, by definition, is 
>“an email or electronic communication scam targeting at specific individual, organization or business”. 
>

The spear phishing social media threat we concern here is phishing messages targeting at specific social media users or user groups, containing website links / file download links with keywords related to specific malware such as upgrade.exe (malicious code) or fake trustworthy websites such as www.b0a.com and are published by facetious authenticate sources such as “micros0ft365 team”. These spear phishing messages trick users to either download some malicious code, or to visit fake trustworthy websites (usually commercial websites) which may steal users’ private or important financial information. The anti-spear phishing message policy we propose to define on ZeroFox tends to work on all social media accounts which detects spear phishing related keywords and trigger appropriate alerts to users.



## Part 2 : Impact of spear phishing message in social media

Spear phishing has become a rising cybersecurity threat and been ranked as the top security concern for enterprises. 

> "Spear phishing are usually more deceptive that users are more easily get tricked as it provides real user details from “trustworthy” sources. "

Spear phishing messages based on social may result in the spread of malware, breach of private information and as well as financial or brand reputation loss. Although spear phishing messages in social media is less common in email environment, because of the quick broadcast speed and popularity of social media networks, social media spear phishing messages may security consequences, such as the spread of malware, much faster and broader. 

Since the spear phishing messages in social media usually pretended to be published from trustworthy sources and tempt users by providing some great deals. Individual users may be influenced by financial frauds, loss of private information through social media spear phishing messages. Besides, by asking users to download some programs from “trustworthy” publisher, users are prone to download malicious code and being infected by malware. 

For organizations and enterprises, in addition to the abovementioned influences on individual users, social media spear phishing may cause more significant financial loss or reputation damage of enterprises by involving in the phishing cybersecurity scams.  

## Part 3 : Existing Threats on Social Media


### 1. Insufficient Authentication Controls
A user may have several social media accounts, and one of these accounts may not meet the strict security control standard, but this person connected these accounts, some accounts connected to one account using single sign on, when hacker get this account’s password, he can access all these accounts.


###2. Cross Site Request Forgery
An attacker send user a malicious link via web page, email, social media apps, attacker trick user to click this link, usually, the malicious link is on the forum and user will open it as normal, then attacker can perform actions without users’ permission.

###3. Cross Site Scripting
Attackers inject the client-side scripting in a web page, and attackers make user’s web browser to execute some malicious code, then attackers may steal user’s information or impersonate the user.

###4. Phishing
Attackers sent users message using social media, and these message are pretended as official message, like using “Micros0ft” (should be Microsoft) to trick victim. Then user may click the link and malicious code will be executed. And attackers will send this information to the victim’s all friends.

###5. Information Leakage
People may share sensitive information on the social media, the information may be important to someone else or including the secret of business of people’s company. The sensitive data may be leaked by social media users, then attackers or bad people will get the information they want.

###6. Injection Flaws
Social media applications often rely on client side code, but the attacker could bypass the client-side input validation, attackers may pass malicious code through the web application.

###7. Insufficient Anti-automation
>“Insufficient Anti-automation occurs when an application permits an attacker to automate a process that was originally designed to be performed only in a manual fashion.”


## Part 4 : Feature Lists

### 1. File Extension

The spear phishing link always point to runnable/executable file. Thus the last part of the link is finished with some specific file extensions. Ths first feature-list is a dictionary to list all the possiblly malicious files.
		
		file-extension = {
			.exe
			.zip
			.script
			.tar
			.dmg
			.js
			.php
			
			...
		}

### 2. Fake Web Links

Some attack may use similar web name to the real web name. In the following dictionary we defined some sample fake web site.
		
		fake-web-name = {
			B0a.com
			Amaz0n.com
			App1e.com
			Micros0ft.com
		
			...
		} 
		
### 3. Real User Name

People who clicked the spear phishing link because they saw their name, which make spear phishing looks trusted. We need to detect the feature that a link or text contains a potential user's real name. What we do is storing all our client name in a dictionary.

**User Name dictionary(who are protected)**

		user-name = {
			Yuhang Wang,
			Nancy Hao,
			Yuqian Huang,
			Ze Yu
			
			...
		}
		
		
## Part 5 : Alert Level 

After define the features of spear phishing. We define alert level based on how many features contained in each tweet.

1. file extension
2. Fake web link
3. Real user name

| Feature List | Threat Description| Alert Level |
| ------| ------ | ------ |
| 1 |file extension| low |
| 2 |Fake web link| low|
| 1 + 3|file extension + Real user name| medium|
| 2 + 3|Fake web link + Real user name| medium|
| 1 + 2 + 3|file extension + Fake web link + Real user name| high|

## Part 6: Classifier

For more accurate alert level, we can assign each feature f with a weight w. For each tweet we can compute a weight sum and decide which level of alert should be trigger.



![](https://github.com/Nautilus1993/SP-C/blob/master/img/classifier.jpg)

###Contingency Plan: Classifier

This is actually a more flexible way to subsititute "alert level policy" in part4, which just simply combines the features. We can setup a weight vector based on the potency of each feature. One more advantage: it is easy to extend more feature in the future, by simply adding one more number in feature list and weight vector. 


**Input:**    A tweet (Plain text + Super link)

**Output:**   Alert Level

**Step 1:**
Given a tweet, check if it contains the features presented in part 3.

**Step2:**
Based on the result in step1, generate a feature vector. For example the tweet in picture have feature 1, 2, 3. So its feature vector = {1, 1, 1}


Setup weight vector and compute the tweet's **malicious value**. 
In this example, we set weightVector = {2, 1, 2}

**Step3:**

Calculate **"malicious value" (MV)** with featureVector and weightVector.

In this case we have:


$$ MV(tweet) = \vec{W} \cdot \vec{F} = \sum_{i = 1}^{i = 3} Wi \cdot Fi $$

In this example we got tweet malicious value 5. Sending this value into classifier. 

**Step4:**


Set classifier interval to classify a malicious value to low, medium, or high level of alert. For example we set [1,2] as low level alert, [2,4] as medium level alert, [4,5] as high level alert. The MV(tweet) we got in step 3 will trigger a high level alert.



## Part 7 : Test

### Test Environment

**Social media platform:** Twitter

**Threat monitoring platform:** ZeroFox

**Test participant:** Twitter user whose account is linked with and under the protecting policy of ZeroFox.

### Scenario 1 (file extension):

The Twitter user (potential malicious spear phishing attacker) sends a moment message on Twitter, which includes a link (invalid link that end with update.exe).
The target user @richardyuze1 intended to update his windows and clicked the link. 

**Test 1:**

The content which includes file extension elements (keywords in the dictionary: such as .exe, .zip, .script, .tar, .dmg, .js ) will trigger the first kind of low level alert in spear phishing message policy. As the ZeroFox detects those keywords a low level alert with pop up in the Alert Notification.

![](https://github.com/Nautilus1993/SP-C/blob/master/img/1.jpg)

###Scenario 2 (fake web link)

The Twitter user (potential malicious spear phishing attacker) sends a moment (message) on Twitter, which includes a fake web link. The link looks trustworthy by pretending the format from amazon (change “o” to “0”). 
The target user @richardyuze1 intended to go to amazon webpage, but he ignored the change and clicked the fake link.

**Test 2:**

The content which includes fake web link elements (keywords in the dictionary: such as B0a.com, Amaz0n.com, App1e.com, Micros0ft.com) will trigger the second kind of low level alert in spear phishing message policy. As the ZeroFox detects those keywords a low level alert with pop up in the Alert Notification.

![](https://github.com/Nautilus1993/SP-C/blob/master/img/2.jpg)

### Scenario 3 (file extension + real user name)

The Twitter user (potential malicious spear phishing attacker) sends a moment message on Twitter, which begins with the real name of the user and includes a link (invalid link that end with update.exe). The content looks more trustworthy by given the real name (compared with scenario 1). 
The target user @richardyuze1 intended to update his windows and clicked the link. 

Test 3:

The content which includes real user name and file extension elements (keywords in the dictionary: such as .exe, .zip, .script, .tar, .dmg, .js ) will trigger the first kind of medium level alert in spear phishing message policy. As the ZeroFox detects those keywords a medium level alert with pop up in the Alert Notification.

![](https://github.com/Nautilus1993/SP-C/blob/master/img/3.jpg)

###Scenario 4 (fake web link + real user name):

The Twitter user (potential malicious spear phishing attacker) sends a moment (message) on Twitter, which begins with the real name of the user and includes a fake web link. The link more looks trustworthy by pretending the format from amazon and mentioned the real name in the content (compared with scenario 2). 
The target user @richardyuze1 intended to go to amazon webpage but clicked the 
fake link. 

**Test 4:**
The content which includes real user name and fake web link elements (keywords in the dictionary: such as B0a.com, Amaz0n.com, App1e.com, Micros0ft.com) will trigger the second kind of medium level alert in spear phishing message policy. As the ZeroFox detects those keywords a medium level alert with pop up in the Alert Notification.

![](https://github.com/Nautilus1993/SP-C/blob/master/img/4.jpg)

###Scenario 5 (file extension + fake web link + real user name):

The Twitter user (potential malicious spear phishing attacker) sends a moment message on Twitter, which begins with the real name of the user and includes a fake web link (invalid link that end with update.exe). The content looks more trustworthy by given the real name and a pretending official web link. (compared with scenario 3 and 4). 
The target user @richardyuze1 intended to update his windows and clicked the link. 

**Test 5:**
The content which includes real user name, fake web link and file extension elements (keywords in the dictionary) will trigger the high level alert in spear phishing message policy. As the ZeroFox detects those keywords a high level alert with pop up in the Alert Notification.

![](https://github.com/Nautilus1993/SP-C/blob/master/img/5.jpg)



## Reference

[What is Spear Phishing](https://usa.kaspersky.com/internet-security-center/definitions/spear-phishing#.V_7O8egrI2w)

[Social Media Security and the Phishing Threat](http://blog.vadesecure.com/en/social-media-security/)

[Reducing the Risks of Social Media to Your Organization. ](https://www.sans.org/reading-room/whitepapers/policyissues/reducing-risks-social-media-organization-33749)

[Appvigil Documentation, 2005](https://appvigil.co/documentation/doku.php?id=appvigil_documentation)



<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>



	
		
 
