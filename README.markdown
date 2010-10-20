Python docx
===========

## Introduction

This is a Python client for PIFilter, a paid, web based image recognition service.

It provides a simple True/False response to whether an image is adult related. It is useful in:

- User generated content sites 
- Content-filtering proxy scanners

### General thoughts on PIFilter

In my own experience as a customer PIFilter's service is like health product that works best with diet and exercise. It is useful as a basis to put specific posts ahead in a moderation queue, where the suspect posts are checked by a human. But it's not sufficient on its own to replace human moderations completely. 

With my own user generated content tests, accuracy was generally good with a tendency towards False positives rather than False negatives.

Of course, your milage may vary as you'll be working with a different set of input, so best to see for yourself.

### Filtering images

- Get a [pifilter account and customer ID](http://www.pifilter.com/).
- Then [download pyfilter](http://github.com/mikemaccana/pyfilter/tarball/master).
- Use **pip** or **easy_install** to fetch the **urllib2** and **poster** modules. 
- Then run:

	from pyfilter import checkimage
	
	checkimage('some/file.jpg','your_own_customer_id')

The response will be a simple True or False.

By default pyfilter runs in 'aggressive' mode, where 'maybe' responses are counted as True. You may prefer to run:

	checkimage('some/file.jpg','your_own_customer_id',aggressive=False)

which will count 'maybe' responses as False. 

### We love forks, changes and pull requests!

- For this project on github
- Send a pull request via github and we'll add your changes!

### License

Licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php)
Short version: this code is copyrighted to me (Mike MacCana), I give you permission to do what you want with it except remove my name from the credits. See the LICENSE file for specific terms.