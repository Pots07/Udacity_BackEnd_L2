# User Instructions
#
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically
# render your escaped text as the corresponding symbols,
# but the grading script will still correctly evaluate it.
#

import cgi
def escape_html(s):
    return cgi.escape(s, quote = True)
    # escape = { '&': '&amp;','>': '&gt;', '<': '&lt;', '"': '&quot;'}
    # t = ''
    # for i in s:
    #     if i in escape.keys():
    #         t += escape[i]
    #     else:
    #         t += i
    # return t

# print escape_html('"hello, & = &amp;"')
# print escape_html('<b>html!</b>')
# print escape_html('>')
# print escape_html('<')
# print escape_html('"')
# print escape_html("&")
