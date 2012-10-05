# Name of the blog
blog_name = 'Charles\'s Blog'

# Your name (used for copyright info)
author_name = '<a href="mailto:mycguo@gmail.com">Charles Guo</a>'

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
    '<a href="http://blog.building-blocks.com/">Building Blocks</a>',       
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
	<li class="cnt" style="top: 93px; left: 78px; height: 52px;"><a class="tag c0" href="/tag/python" style="top: 93px;        left: 78px; font-size: 37px; height: 52px; line-height:38px;">python</a></li><li class="cnt" style="top: 24px; left: 78px; height: 37px;"><a class="tag c1" href="/tag/appengine" style="top: 24px;        left: 78px; font-size: 26px; height: 37px; line-height:24px;">appengine</a></li><li class="cnt" style="top: 79px; left: 35px; height: 24px;"><a class="tag c2" href="/tag/tridion" style="top: 79px;        left: 35px; font-size: 20px; height: 24px; line-height:14px;">tridion</a></li><li class="cnt" style="top: 64px; left: 73px; height: 15px;"><a class="tag c1" href="/tag/cms" style="top: 64px;        left: 73px; font-size: 17px; height: 15px; line-height:7px;">cms</a></li><li class="cnt" style="top: 93px; left: 8px; height: 17px;"><a class="tag c8" href="/tag/tag" style="top: 93px;        left: 8px; font-size: 11px; height: 17px; line-height:8px;">tag</a></li><li class="cnt" style="top: 138px; left: 65px; height: 17px;"><a class="tag c8" href="/tag/java" style="top: 138px;        left: 65px; font-size: 11px; height: 17px; line-height:8px;">java</a></li><li class="cnt" style="top: 72px; left: 113px; height: 14px;"><a class="tag c1" href="/tag/cloud" style="top: 72px;        left: 113px; font-size: 11px; height: 14px; line-height:6px;">cloud</a></li><li class="cnt" style="top: 125px; left: 33px; height: 14px;"><a class="tag c1" href="/tag/excel" style="top: 125px;        left: 33px; font-size: 11px; height: 14px; line-height:6px;">excel</a></li><li class="cnt" style="top: 54px; left: 27px; height: 17px;"><a class="tag c1" href="/tag/nodejs" style="top: 54px;        left: 27px; font-size: 11px; height: 17px; line-height:8px;">nodejs</a></li><li class="cnt" style="top: 111px; left: 16px; height: 14px;"><a class="tag c2" href="/tag/fckeditor" style="top: 111px;        left: 16px; font-size: 11px; height: 14px; line-height:6px;">fckeditor</a></li><li class="cnt" style="top: 68px; left: 155px; height: 13px;"><a class="tag c2" href="/tag/git" style="top: 68px;        left: 155px; font-size: 7px; height: 13px; line-height:5px;">git</a></li><li class="cnt" style="top: 140px; left: 105px; height: 13px;"><a class="tag c2" href="/tag/appegnine" style="top: 140px;        left: 105px; font-size: 7px; height: 13px; line-height:5px;">appegnine</a></li><li class="cnt" style="top: 0px; left: 123px; height: 13px;"><a class="tag c16" href="/tag/edge" style="top: 0px;        left: 123px; font-size: 7px; height: 13px; line-height:5px;">edge</a></li><li class="cnt" style="top: 84px; left: 154px; height: 13px;"><a class="tag c2" href="/tag/blog" style="top: 84px;        left: 154px; font-size: 7px; height: 13px; line-height:5px;">blog</a></li><li class="cnt" style="top: 139px; left: 16px; height: 13px;"><a class="tag c0" href="/tag/typescript" style="top: 139px;        left: 16px; font-size: 7px; height: 13px; line-height:5px;">typescript</a></li><li class="cnt" style="top: 110px; left: 0px; height: 13px;"><a class="tag c16" href="/tag/pil" style="top: 110px;        left: 0px; font-size: 7px; height: 13px; line-height:5px;">pil</a></li><li class="cnt" style="top: 14px; left: 125px; height: 9px;"><a class="tag c1" href="/tag/html5" style="top: 14px;        left: 125px; font-size: 7px; height: 9px; line-height:2px;">html5</a></li><li class="cnt" style="top: 28px; left: 8px; height: 12px;"><a class="tag c1" href="/tag/press" style="top: 28px;        left: 8px; font-size: 7px; height: 12px; line-height:4px;">press</a></li><li class="cnt" style="top: 41px; left: 24px; height: 13px;"><a class="tag c2" href="/tag/javascript" style="top: 41px;        left: 24px; font-size: 7px; height: 13px; line-height:5px;">javascript</a></li><li class="cnt" style="top: 182px; left: 68px; height: 9px;"><a class="tag c2" href="/tag/webdav" style="top: 182px;        left: 68px; font-size: 7px; height: 9px; line-height:2px;">webdav</a></li><li class="cnt" style="top: 177px; left: 27px; height: 13px;"><a class="tag c1" href="/tag/appfog" style="top: 177px;        left: 27px; font-size: 7px; height: 13px; line-height:5px;">appfog</a></li><li class="cnt" style="top: 101px; left: 61px; height: 8px;"><a class="tag c16" href="/tag/css" style="top: 101px;        left: 61px; font-size: 7px; height: 8px; line-height:1px;">css</a></li><li class="cnt" style="top: 167px; left: 98px; height: 13px;"><a class="tag c8" href="/tag/iphone" style="top: 167px;        left: 98px; font-size: 7px; height: 13px; line-height:5px;">iphone</a></li><li class="cnt" style="top: 166px; left: 18px; height: 9px;"><a class="tag c16" href="/tag/icloud" style="top: 166px;        left: 18px; font-size: 7px; height: 9px; line-height:2px;">icloud</a></li><li class="cnt" style="top: 166px; left: 60px; height: 9px;"><a class="tag c8" href="/tag/weddav" style="top: 166px;        left: 60px; font-size: 7px; height: 9px; line-height:2px;">weddav</a></li><li class="cnt" style="top: 0px; left: 27px; height: 9px;"><a class="tag c8" href="/tag/mobile" style="top: 0px;        left: 27px; font-size: 7px; height: 9px; line-height:2px;">mobile</a></li><li class="cnt" style="top: 5px; left: 91px; height: 13px;"><a class="tag c16" href="/tag/script" style="top: 5px;        left: 91px; font-size: 7px; height: 13px; line-height:5px;">script</a></li><li class="cnt" style="top: 86px; left: 109px; height: 9px;"><a class="tag c16" href="/tag/sdl" style="top: 86px;        left: 109px; font-size: 7px; height: 9px; line-height:2px;">sdl</a></li><li class="cnt" style="top: 181px; left: 107px; height: 13px;"><a class="tag c8" href="/tag/gmail" style="top: 181px;        left: 107px; font-size: 7px; height: 13px; line-height:5px;">gmail</a></li><li class="cnt" style="top: 10px; left: 13px; height: 13px;"><a class="tag c1" href="/tag/cygwin" style="top: 10px;        left: 13px; font-size: 7px; height: 13px; line-height:5px;">cygwin</a></li><li class="cnt" style="top: 154px; left: 108px; height: 13px;"><a class="tag c16" href="/tag/dynamic" style="top: 154px;        left: 108px; font-size: 7px; height: 13px; line-height:5px;">dynamic</a></li><li class="cnt" style="top: 17px; left: 89px; height: 13px;"><a class="tag c16" href="/tag/inspect" style="top: 17px;        left: 89px; font-size: 7px; height: 13px; line-height:5px;">inspect</a></li><li class="cnt" style="top: 155px; left: 71px; height: 9px;"><a class="tag c16" href="/tag/instant" style="top: 155px;        left: 71px; font-size: 7px; height: 9px; line-height:2px;">instant</a></li><li class="cnt" style="top: 13px; left: 47px; height: 13px;"><a class="tag c1" href="/tag/eclipse" style="top: 13px;        left: 47px; font-size: 7px; height: 13px; line-height:5px;">eclipse</a></li><li class="cnt" style="top: 71px; left: 18px; height: 9px;"><a class="tag c16" href="/tag/contacts" style="top: 71px;        left: 18px; font-size: 7px; height: 9px; line-height:2px;">contacts</a></li><li class="cnt" style="top: 27px; left: 36px; height: 13px;"><a class="tag c1" href="/tag/delivery" style="top: 27px;        left: 36px; font-size: 7px; height: 13px; line-height:5px;">delivery</a></li><li class="cnt" style="top: 59px; left: 114px; height: 13px;"><a class="tag c0" href="/tag/prettify" style="top: 59px;        left: 114px; font-size: 7px; height: 13px; line-height:5px;">prettify</a></li><li class="cnt" style="top: 151px; left: 17px; height: 13px;"><a class="tag c2" href="/tag/appeninge" style="top: 151px;        left: 17px; font-size: 7px; height: 13px; line-height:5px;">appeninge</a></li><li class="cnt" style="top: 82px; left: 10px; height: 9px;"><a class="tag c8" href="/tag/test" style="top: 82px;        left: 10px; font-size: 7px; height: 9px; line-height:2px;">test</a></li>
	</ul>

'''