# Name of the blog
blog_name = 'Charles\'s Blog'

# Your name (used for copyright info)
author_name = 'Charles Guo'

# (Optional) slogan
slogan = 'Keep Learning'

# The hostname this site will primarially serve off (used for Atom feeds)
host = 'charles-blog.appspot.com'

# Selects the theme to use. Theme names correspond to directories under
# the 'themes' directory, containing templates and static content.
theme = 'default'

# List of page templates
page_templates = {
	'Theme.html': 'Theme',
	'Simple.html': 'Simple',
	'Pretty.html': 'Pretty',
}

# Defines the URL organization to use for blog postings. Valid substitutions:
#   slug - the identifier for the post, derived from the title
#   year - the year the post was published in
#   month - the month the post was published in
#   day - the day the post was published in
post_path_format = '/%(year)d/%(month)02d/%(slug)s'

# A nested list of sidebar menus, for convenience. If this isn't versatile
# enough, you can edit themes/default/base.html instead.
sidebars = [
  ('Blogroll', [
    '<a href="http://charles-blog.appspot.com/">Charles Guo</a>',   
    '<a href="http://www.tridionarchitect.com/tridion/tridion-blogs.aspx">Tridion Architect</a>',
    '<a href="http://www.tridiondeveloper.com/">Tridion Developer</a>',        
    '<a href="http://blog.notdot.net/">Nick Johnsonz</a>',
    '<a href="http://www.codinghorror.com/blog/">Coding Horror</a>',
    '<a href="http://nunolinhares.blogspot.com/">Nuno Linhares</a>',
    '<a href="http://www.schneier.com/blog/">Schneier on Security</a>',
  ]),
]

# Number of entries per page in indexes.
posts_per_page = 10

# The mime type to serve HTML files as.
html_mime_type = "text/html; charset=utf-8"

# To use disqus for comments, set this to the 'short name' of the disqus forum
# created for the purpose.
use_disqus = True
disqus_forum = 'charles-blog'

# Length (in words) of summaries, by default
summary_length = 200

# If you want to use Google Analytics, enter your 'web property id' here
analytics_id = None

# If you want to use PubSubHubbub, supply the hub URL to use here.
hubbub_hub_url = 'http://pubsubhubbub.appspot.com/'

# If you want to ping Google Sitemap when your sitemap is generated change this to True, else False
# see: http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=34609 for more information
google_sitemap_ping = True

# If you want to use Google Site verification, go to
# https://www.google.com/webmasters/tools/ , add your site, choose the 'upload
# an html file' method, then set the NAME of the file below.
# Note that you do not need to download the file provided - just enter its name
# here.
google_site_verification = 'google0082d02ec857c8d7.html'

# Default markup language for entry bodies (defaults to html).
default_markup = 'html'

# Syntax highlighting style for RestructuredText and Markdown,
# one of 'manni', 'perldoc', 'borland', 'colorful', 'default', 'murphy',
# 'vs', 'trac', 'tango', 'fruity', 'autumn', 'bw', 'emacs', 'pastie',
# 'friendly', 'native'.
highlighting_style = 'friendly'

# Absolute url of the blog application use '/blog' for host/blog/
# and '' for host/.Also remember to change app.yaml accordingly
url_prefix = ''

# Defines where the user is defined in the rel="me" of your pages.
# This allows you to expand on your social graph.
rel_me = None

# For use a feed proxy like feedburne.google.com
feed_proxy = None

# To use Google Friends Connect.                                          
# If you want use Google Friends Connect, go to http://www.google.com/friendconnect/ 
# and register your domain for get a Google Friends connect ID.
google_friends_id = None
google_friends_comments = True # For comments.
google_friends_members  = True # For a members container.

# To format the date of your post.
# http://docs.djangoproject.com/en/1.1/ref/templates/builtins/#now
date_format = "d F, Y"

#tag cloud created using PyTagCloud
tagcloud = '''
<ul class="cloud">
	<li class="cnt" style="top: 112px; left: 93px; height: 50px;">
		<a class="tag c0" href="/tag/python" style="top: 112px;        left: 93px; font-size: 37px; height: 50px; line-height:36px;">python</a>
	</li>
	<li class="cnt" style="top: 96px; left: 42px; height: 26px;">
		<a class="tag c1" href="/tag/cloud" style="top: 96px;        left: 42px; font-size: 22px; height: 26px; line-height:15px;">cloud</a>
	</li>
	<li class="cnt" style="top: 70px; left: 47px; height: 28px;">
		<a class="tag c1" href="/tag/appengine" style="top: 70px;        left: 47px; font-size: 19px; height: 28px; line-height:17px;">appengine</a>
	</li>
	<li class="cnt" style="top: 120px; left: 33px; height: 26px;">
		<a class="tag c3" href="/tag/nodejs" style="top: 120px;        left: 33px; font-size: 17px; height: 26px; line-height:16px;">nodejs</a>
	</li>
	<li class="cnt" style="top: 96px; left: 111px; height: 21px;">
		<a class="tag c1" href="/tag/tag" style="top: 96px;        left: 111px; font-size: 16px; height: 21px; line-height:11px;">tag</a>
	</li>
	<li class="cnt" style="top: 148px; left: 60px; height: 17px;">
		<a class="tag c5" href="/tag/java" style="top: 148px;        left: 60px; font-size: 11px; height: 17px; line-height:8px;">java</a>
	</li>
	<li class="cnt" style="top: 62px; left: 42px; height: 13px;">
		<a class="tag c1" href="/tag/framework" style="top: 62px;        left: 42px; font-size: 9px; height: 13px; line-height:5px;">framework</a>
	</li>
	<li class="cnt" style="top: 60px; left: 127px; height: 9px;">
		<a class="tag c3" href="/tag/com" style="top: 60px;        left: 127px; font-size: 8px; height: 9px; line-height:2px;">com</a>
	</li>
	<li class="cnt" style="top: 144px; left: 36px; height: 13px;">
		<a class="tag c5" href="/tag/kind" style="top: 144px;        left: 36px; font-size: 8px; height: 13px; line-height:5px;">kind</a>
	</li>
	<li class="cnt" style="top: 155px; left: 104px; height: 15px;">
		<a class="tag c3" href="/tag/keyword" style="top: 155px;        left: 104px; font-size: 8px; height: 15px; line-height:7px;">keyword</a>
	</li>
	<li class="cnt" style="top: 92px; left: 30px; height: 8px;">
		<a class="tag c13" href="/tag/one" style="top: 92px;        left: 30px; font-size: 6px; height: 8px; line-height:1px;">one</a>
	</li>
	<li class="cnt" style="top: 181px; left: 121px; height: 9px;">
		<a class="tag c5" href="/tag/code" style="top: 181px;        left: 121px; font-size: 6px; height: 9px; line-height:2px;">code</a>
	</li>
	<li class="cnt" style="top: 177px; left: 77px; height: 9px;">
		<a class="tag c13" href="/tag/must" style="top: 177px;        left: 77px; font-size: 6px; height: 9px; line-height:2px;">must</a>
	</li>
	<li class="cnt" style="top: 96px; left: 145px; height: 13px;">
		<a class="tag c1" href="/tag/http" style="top: 96px;        left: 145px; font-size: 6px; height: 13px; line-height:5px;">http</a>
	</li>
	<li class="cnt" style="top: 35px; left: 34px; height: 13px;">
		<a class="tag c13" href="/tag/input" style="top: 35px;        left: 34px; font-size: 6px; height: 13px; line-height:5px;">input</a>
	</li>
	<li class="cnt" style="top: 33px; left: 89px; height: 13px;">
		<a class="tag c13" href="/tag/might" style="top: 33px;        left: 89px; font-size: 6px; height: 13px; line-height:5px;">might</a>
	</li>
	<li class="cnt" style="top: 47px; left: 139px; height: 13px;">
		<a class="tag c5" href="/tag/using" style="top: 47px;        left: 139px; font-size: 6px; height: 13px; line-height:5px;">using</a>
	</li>
	<li class="cnt" style="top: 36px; left: 118px; height: 12px;">
		<a class="tag c1" href="/tag/message" style="top: 36px;        left: 118px; font-size: 6px; height: 12px; line-height:4px;">message</a>
	</li>
	<li class="cnt" style="top: 37px; left: 53px; height: 13px;">
		<a class="tag c5" href="/tag/argument" style="top: 37px;        left: 53px; font-size: 6px; height: 13px; line-height:5px;">argument</a>
	</li>
	<li class="cnt" style="top: 49px; left: 38px; height: 9px;">
		<a class="tag c13" href="/tag/sometime" style="top: 49px;        left: 38px; font-size: 6px; height: 9px; line-height:2px;">sometime</a>
	</li>
	<li class="cnt" style="top: 48px; left: 91px; height: 13px;">
		<a class="tag c5" href="/tag/arguments" style="top: 48px;        left: 91px; font-size: 6px; height: 13px; line-height:5px;">arguments</a>
	</li>
	<li class="cnt" style="top: 164px; left: 49px; height: 13px;">
		<a class="tag c1" href="/tag/parameter" style="top: 164px;        left: 49px; font-size: 6px; height: 13px; line-height:5px;">parameter</a>
	</li>
	<li class="cnt" style="top: 170px; left: 97px; height: 9px;">
		<a class="tag c3" href="/tag/frameworks" style="top: 170px;        left: 97px; font-size: 6px; height: 9px; line-height:2px;">frameworks</a>
	</li>
	<li class="cnt" style="top: 51px; left: 9px; height: 8px;">
		<a class="tag c5" href="/tag/version" style="top: 51px;        left: 9px; font-size: 4px; height: 8px; line-height:1px;">version</a>
	</li>
	<li class="cnt" style="top: 64px; left: 105px; height: 8px;">
		<a class="tag c1" href="/tag/article" style="top: 64px;        left: 105px; font-size: 4px; height: 8px; line-height:1px;">article</a>
	</li>
	<li class="cnt" style="top: 0px; left: 110px; height: 9px;">
		<a class="tag c3" href="/tag/key" style="top: 0px;        left: 110px; font-size: 4px; height: 9px; line-height:2px;">key</a>
	</li>
	<li class="cnt" style="top: 148px; left: 3px; height: 9px;">
		<a class="tag c13" href="/tag/support" style="top: 148px;        left: 3px; font-size: 4px; height: 9px; line-height:2px;">support</a>
	</li>
	<li class="cnt" style="top: 201px; left: 42px; height: 9px;">
		<a class="tag c1" href="/tag/good" style="top: 201px;        left: 42px; font-size: 4px; height: 9px; line-height:2px;">good</a>
	</li>
	<li class="cnt" style="top: 86px; left: 160px; height: 8px;">
		<a class="tag c5" href="/tag/another" style="top: 86px;        left: 160px; font-size: 4px; height: 8px; line-height:1px;">another</a>
	</li>
	<li class="cnt" style="top: 193px; left: 4px; height: 8px;">
		<a class="tag c13" href="/tag/know" style="top: 193px;        left: 4px; font-size: 4px; height: 8px; line-height:1px;">know</a>
	</li>
	<li class="cnt" style="top: 154px; left: 153px; height: 9px;">
		<a class="tag c1" href="/tag/stepping" style="top: 154px;        left: 153px; font-size: 4px; height: 9px; line-height:2px;">stepping</a>
	</li>
	<li class="cnt" style="top: 42px; left: 160px; height: 8px;">
		<a class="tag c1" href="/tag/like" style="top: 42px;        left: 160px; font-size: 4px; height: 8px; line-height:1px;">like</a>
	</li>
	<li class="cnt" style="top: 211px; left: 117px; height: 8px;">
		<a class="tag c5" href="/tag/hard" style="top: 211px;        left: 117px; font-size: 4px; height: 8px; line-height:1px;">hard</a>
	</li>
	<li class="cnt" style="top: 67px; left: 10px; height: 9px;">
		<a class="tag c5" href="/tag/existing" style="top: 67px;        left: 10px; font-size: 4px; height: 9px; line-height:2px;">existing</a>
	</li>
	<li class="cnt" style="top: 19px; left: 174px; height: 8px;">
		<a class="tag c13" href="/tag/toes" style="top: 19px;        left: 174px; font-size: 4px; height: 8px; line-height:1px;">toes</a>
	</li>
	<li class="cnt" style="top: 190px; left: 44px; height: 9px;">
		<a class="tag c5" href="/tag/asking" style="top: 190px;        left: 44px; font-size: 4px; height: 9px; line-height:2px;">asking</a>
	</li>
	<li class="cnt" style="top: 26px; left: 1px; height: 7px;">
		<a class="tag c0" href="/tag/even" style="top: 26px;        left: 1px; font-size: 4px; height: 7px; line-height:0px;">even</a>
	</li>
	<li class="cnt" style="top: 201px; left: 134px; height: 8px;">
		<a class="tag c13" href="/tag/find" style="top: 201px;        left: 134px; font-size: 4px; height: 8px; line-height:1px;">find</a>
	</li>
	<li class="cnt" style="top: 42px; left: 11px; height: 8px;">
		<a class="tag c5" href="/tag/others" style="top: 42px;        left: 11px; font-size: 4px; height: 8px; line-height:1px;">others</a>
	</li>
	<li class="cnt" style="top: 8px; left: 122px; height: 9px;">
		<a class="tag c0" href="/tag/post" style="top: 8px;        left: 122px; font-size: 4px; height: 9px; line-height:2px;">post</a>
	</li>
	<li class="cnt" style="top: 55px; left: 71px; height: 8px;">
		<a class="tag c1" href="/tag/wait" style="top: 55px;        left: 71px; font-size: 4px; height: 8px; line-height:1px;">wait</a>
	</li>
	<li class="cnt" style="top: 62px; left: 156px; height: 9px;">
		<a class="tag c1" href="/tag/platform" style="top: 62px;        left: 156px; font-size: 4px; height: 9px; line-height:2px;">platform</a>
	</li>
	<li class="cnt" style="top: 23px; left: 95px; height: 9px;">
		<a class="tag c3" href="/tag/google" style="top: 23px;        left: 95px; font-size: 4px; height: 9px; line-height:2px;">google</a>
	</li>
	<li class="cnt" style="top: 18px; left: 33px; height: 8px;">
		<a class="tag c3" href="/tag/many" style="top: 18px;        left: 33px; font-size: 4px; height: 8px; line-height:1px;">many</a>
	</li>
	<li class="cnt" style="top: 177px; left: 147px; height: 8px;">
		<a class="tag c13" href="/tag/nature" style="top: 177px;        left: 147px; font-size: 4px; height: 8px; line-height:1px;">nature</a>
	</li>
	<li class="cnt" style="top: 19px; left: 143px; height: 8px;">
		<a class="tag c0" href="/tag/feed" style="top: 19px;        left: 143px; font-size: 4px; height: 8px; line-height:1px;">feed</a>
	</li>
	<li class="cnt" style="top: 164px; left: 143px; height: 8px;">
		<a class="tag c0" href="/tag/redo" style="top: 164px;        left: 143px; font-size: 4px; height: 8px; line-height:1px;">redo</a>
	</li>
	<li class="cnt" style="top: 188px; left: 137px; height: 9px;">
		<a class="tag c1" href="/tag/except" style="top: 188px;        left: 137px; font-size: 4px; height: 9px; line-height:2px;">except</a>
	</li>
	<li class="cnt" style="top: 58px; left: 20px; height: 8px;">
		<a class="tag c1" href="/tag/words" style="top: 58px;        left: 20px; font-size: 4px; height: 8px; line-height:1px;">words</a>
	</li>
	<li class="cnt" style="top: 13px; left: 80px; height: 7px;">
		<a class="tag c3" href="/tag/seems" style="top: 13px;        left: 80px; font-size: 4px; height: 7px; line-height:0px;">seems</a>
	</li>
	<li class="cnt" style="top: 101px; left: 13px; height: 8px;">
		<a class="tag c3" href="/tag/solutions" style="top: 101px;        left: 13px; font-size: 4px; height: 8px; line-height:1px;">solutions</a>
	</li>
	<li class="cnt" style="top: 169px; left: 24px; height: 9px;">
		<a class="tag c0" href="/tag/change" style="top: 169px;        left: 24px; font-size: 4px; height: 9px; line-height:2px;">change</a>
	</li>
	<li class="cnt" style="top: 194px; left: 22px; height: 7px;">
		<a class="tag c3" href="/tag/worse" style="top: 194px;        left: 22px; font-size: 4px; height: 7px; line-height:0px;">worse</a>
	</li>
	<li class="cnt" style="top: 198px; left: 148px; height: 8px;">
		<a class="tag c1" href="/tag/turns" style="top: 198px;        left: 148px; font-size: 4px; height: 8px; line-height:1px;">turns</a>
	</li>
	<li class="cnt" style="top: 92px; left: 4px; height: 9px;">
		<a class="tag c0" href="/tag/hijacked" style="top: 92px;        left: 4px; font-size: 4px; height: 9px; line-height:2px;">hijacked</a>
	</li>
	<li class="cnt" style="top: 119px; left: 8px; height: 8px;">
		<a class="tag c5" href="/tag/search" style="top: 119px;        left: 8px; font-size: 4px; height: 8px; line-height:1px;">search</a>
	</li>
	<li class="cnt" style="top: 127px; left: 0px; height: 9px;">
		<a class="tag c5" href="/tag/google's" style="top: 127px;        left: 0px; font-size: 4px; height: 9px; line-height:2px;">google's</a>
	</li>
	<li class="cnt" style="top: 194px; left: 170px; height: 9px;">
		<a class="tag c13" href="/tag/going" style="top: 194px;        left: 170px; font-size: 4px; height: 9px; line-height:2px;">going</a>
	</li>
	<li class="cnt" style="top: 189px; left: 158px; height: 8px;">
		<a class="tag c13" href="/tag/often" style="top: 189px;        left: 158px; font-size: 4px; height: 8px; line-height:1px;">often</a>
	</li>
	<li class="cnt" style="top: 41px; left: 172px; height: 9px;">
		<a class="tag c1" href="/tag/simple" style="top: 41px;        left: 172px; font-size: 4px; height: 9px; line-height:2px;">simple</a>
	</li>
	<li class="cnt" style="top: 14px; left: 99px; height: 8px;">
		<a class="tag c1" href="/tag/learn" style="top: 14px;        left: 99px; font-size: 4px; height: 8px; line-height:1px;">learn</a>
	</li>
	<li class="cnt" style="top: 19px; left: 117px; height: 8px;">
		<a class="tag c13" href="/tag/tools" style="top: 19px;        left: 117px; font-size: 4px; height: 8px; line-height:1px;">tools</a>
	</li>
	<li class="cnt" style="top: 206px; left: 92px; height: 7px;">
		<a class="tag c3" href="/tag/never" style="top: 206px;        left: 92px; font-size: 4px; height: 7px; line-height:0px;">never</a>
	</li>
	<li class="cnt" style="top: 16px; left: 51px; height: 8px;">
		<a class="tag c1" href="/tag/atizo" style="top: 16px;        left: 51px; font-size: 4px; height: 8px; line-height:1px;">atizo</a>
	</li>
	<li class="cnt" style="top: 57px; left: 0px; height: 9px;">
		<a class="tag c3" href="/tag/blog" style="top: 57px;        left: 0px; font-size: 4px; height: 9px; line-height:2px;">blog</a>
	</li>
	<li class="cnt" style="top: 31px; left: 15px; height: 8px;">
		<a class="tag c1" href="/tag/faced" style="top: 31px;        left: 15px; font-size: 4px; height: 8px; line-height:1px;">faced</a>
	</li>
	<li class="cnt" style="top: 30px; left: 160px; height: 8px;">
		<a class="tag c1" href="/tag/agree" style="top: 30px;        left: 160px; font-size: 4px; height: 8px; line-height:1px;">agree</a>
	</li>
	<li class="cnt" style="top: 25px; left: 126px; height: 9px;">
		<a class="tag c1" href="/tag/given" style="top: 25px;        left: 126px; font-size: 4px; height: 9px; line-height:2px;">given</a>
	</li>
	<li class="cnt" style="top: 201px; left: 61px; height: 9px;">
		<a class="tag c3" href="/tag/saying" style="top: 201px;        left: 61px; font-size: 4px; height: 9px; line-height:2px;">saying</a>
	</li>
	<li class="cnt" style="top: 162px; left: 0px; height: 8px;">
		<a class="tag c3" href="/tag/create" style="top: 162px;        left: 0px; font-size: 4px; height: 8px; line-height:1px;">create</a>
	</li>
	<li class="cnt" style="top: 183px; left: 9px; height: 9px;">
		<a class="tag c3" href="/tag/syntax" style="top: 183px;        left: 9px; font-size: 4px; height: 9px; line-height:2px;">syntax</a>
	</li>
	<li class="cnt" style="top: 179px; left: 172px; height: 8px;">
		<a class="tag c1" href="/tag/issues" style="top: 179px;        left: 172px; font-size: 4px; height: 8px; line-height:1px;">issues</a>
	</li>
	<li class="cnt" style="top: 164px; left: 162px; height: 9px;">
		<a class="tag c0" href="/tag/enjoyed" style="top: 164px;        left: 162px; font-size: 4px; height: 9px; line-height:2px;">enjoyed</a>
	</li>
	<li class="cnt" style="top: 61px; left: 176px; height: 9px;">
		<a class="tag c0" href="/tag/just" style="top: 61px;        left: 176px; font-size: 4px; height: 9px; line-height:2px;">just</a>
	</li>
	<li class="cnt" style="top: 182px; left: 96px; height: 8px;">
		<a class="tag c1" href="/tag/relearn" style="top: 182px;        left: 96px; font-size: 4px; height: 8px; line-height:1px;">relearn</a>
	</li>
	<li class="cnt" style="top: 6px; left: 47px; height: 9px;">
		<a class="tag c3" href="/tag/try" style="top: 6px;        left: 47px; font-size: 4px; height: 9px; line-height:2px;">try</a>
	</li>
	<li class="cnt" style="top: 217px; left: 95px; height: 7px;">
		<a class="tag c5" href="/tag/www" style="top: 217px;        left: 95px; font-size: 4px; height: 7px; line-height:0px;">www</a>
	</li>
	<li class="cnt" style="top: 51px; left: 161px; height: 8px;">
		<a class="tag c0" href="/tag/excited" style="top: 51px;        left: 161px; font-size: 4px; height: 8px; line-height:1px;">excited</a>
	</li>
	<li class="cnt" style="top: 207px; left: 149px; height: 7px;">
		<a class="tag c5" href="/tag/new" style="top: 207px;        left: 149px; font-size: 4px; height: 7px; line-height:0px;">new</a>
	</li>
	<li class="cnt" style="top: 11px; left: 151px; height: 8px;">
		<a class="tag c5" href="/tag/task" style="top: 11px;        left: 151px; font-size: 4px; height: 8px; line-height:1px;">task</a>
	</li>
	<li class="cnt" style="top: 102px; left: 0px; height: 8px;">
		<a class="tag c1" href="/tag/ide" style="top: 102px;        left: 0px; font-size: 4px; height: 8px; line-height:1px;">ide</a>
	</li>
	<li class="cnt" style="top: 160px; left: 28px; height: 9px;">
		<a class="tag c13" href="/tag/library" style="top: 160px;        left: 28px; font-size: 4px; height: 9px; line-height:2px;">library</a>
	</li>
	<li class="cnt" style="top: 201px; left: 112px; height: 9px;">
		<a class="tag c0" href="/tag/debug" style="top: 201px;        left: 112px; font-size: 4px; height: 9px; line-height:2px;">debug</a>
	</li>
	<li class="cnt" style="top: 201px; left: 21px; height: 9px;">
		<a class="tag c0" href="/tag/bog" style="top: 201px;        left: 21px; font-size: 4px; height: 9px; line-height:2px;">bog</a>
	</li>
	<li class="cnt" style="top: 80px; left: 0px; height: 8px;">
		<a class="tag c5" href="/tag/'value'" style="top: 80px;        left: 0px; font-size: 4px; height: 8px; line-height:1px;">'value'</a>
	</li>
	<li class="cnt" style="top: 80px; left: 19px; height: 9px;">
		<a class="tag c13" href="/tag/listening" style="top: 80px;        left: 19px; font-size: 4px; height: 9px; line-height:2px;">listening</a>
	</li>
	<li class="cnt" style="top: 111px; left: 10px; height: 8px;">
		<a class="tag c5" href="/tag/reference" style="top: 111px;        left: 10px; font-size: 4px; height: 8px; line-height:1px;">reference</a>
	</li>
	<li class="cnt" style="top: 95px; left: 162px; height: 8px;">
		<a class="tag c3" href="/tag/available" style="top: 95px;        left: 162px; font-size: 4px; height: 8px; line-height:1px;">available</a>
	</li>
	<li class="cnt" style="top: 75px; left: 158px; height: 9px;">
		<a class="tag c1" href="/tag/javascript" style="top: 75px;        left: 158px; font-size: 4px; height: 9px; line-height:2px;">javascript</a>
	</li>
	<li class="cnt" style="top: 104px; left: 164px; height: 9px;">
		<a class="tag c0" href="/tag/everything" style="top: 104px;        left: 164px; font-size: 4px; height: 9px; line-height:2px;">everything</a>
	</li>
	<li class="cnt" style="top: 190px; left: 64px; height: 9px;">
		<a class="tag c0" href="/tag/completely" style="top: 190px;        left: 64px; font-size: 4px; height: 9px; line-height:2px;">completely</a>
	</li>
	<li class="cnt" style="top: 173px; left: 3px; height: 9px;">
		<a class="tag c13" href="/tag/pretty" style="top: 173px;        left: 3px; font-size: 4px; height: 9px; line-height:2px;">pretty</a>
	</li>
	<li class="cnt" style="top: 26px; left: 38px; height: 8px;">
		<a class="tag c13" href="/tag/definition" style="top: 26px;        left: 38px; font-size: 4px; height: 8px; line-height:1px;">definition</a>
	</li>
	<li class="cnt" style="top: 190px; left: 95px; height: 9px;">
		<a class="tag c0" href="/tag/disappointed" style="top: 190px;        left: 95px; font-size: 4px; height: 9px; line-height:2px;">disappointed</a>
	</li>
	<li class="cnt" style="top: 137px; left: 0px; height: 9px;">
		<a class="tag c13" href="/tag/exception" style="top: 137px;        left: 0px; font-size: 4px; height: 9px; line-height:2px;">exception</a>
	</li>
	<li class="cnt" style="top: 180px; left: 34px; height: 9px;">
		<a class="tag c1" href="/tag/linuxjournal" style="top: 180px;        left: 34px; font-size: 4px; height: 9px; line-height:2px;">linuxjournal</a>
	</li>
	<li class="cnt" style="top: 23px; left: 67px; height: 9px;">
		<a class="tag c13" href="/tag/script" style="top: 23px;        left: 67px; font-size: 4px; height: 9px; line-height:2px;">script</a>
	</li>
	<li class="cnt" style="top: 158px; left: 91px; height: 8px;">
		<a class="tag c3" href="/tag/last" style="top: 158px;        left: 91px; font-size: 4px; height: 8px; line-height:1px;">last</a>
	</li>
	<li class="cnt" style="top: 43px; left: 0px; height: 9px;">
		<a class="tag c3" href="/tag/get" style="top: 43px;        left: 0px; font-size: 4px; height: 9px; line-height:2px;">get</a>
	</li>
	<li class="cnt" style="top: 33px; left: 0px; height: 9px;">
		<a class="tag c1" href="/tag/put" style="top: 33px;        left: 0px; font-size: 4px; height: 9px; line-height:2px;">put</a>
	</li>
</ul>


'''