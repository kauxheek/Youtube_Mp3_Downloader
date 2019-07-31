import urllib.request
import urllib.parse
import re

x = eval(input("Enter The name of the File: "))
query_string = urllib.parse.urlencode({"search_query": x})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
x = ("http://www.youtube.com/watch?v=" + search_results[1])



