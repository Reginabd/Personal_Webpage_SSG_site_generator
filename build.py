#!/usr/bin/env python3


def create_files(page):

    created_filename = page['filename']
    created_output = page['output']
    created_title = page['title']
    return created_filename, created_output, created_title 

def created_pages(created_filename, created_output, created_title):
    print("created_filename:", created_filename)
    print("created_output:", created_output)
    print("created_title:", created_title)
    template = open('./templates/base.html').read()
    content = open(created_filename).read()
    created_page = template.replace("{{content}}", content)
    created_page = created_page.replace("{{title}}", created_title)
    open(created_output, 'w+').write(created_page)
    print(content)

pages = [

{
	'filename': './content/index.html',
	'output': './docs/index.html',
	'title': 'Index',

},

{
	'filename': './content/about.html',
	'output': './docs/about.html',
	'title': 'About',

},

{
	'filename': './content/education.html',
	'output': './docs/education.html',
	'title': 'Education',

},

{
	'filename': './content/experience.html',
	'output': './docs/experience.html',
	'title': 'Experience',

},

{
	'filename': './content/skills.html',
	'output': './docs/skills.html',
	'title': 'Skills',

},

]




def main():
    for page in pages:
        preated_filename, created_output, created_title = create_files(page)
        created_pages(preated_filename, created_output, created_title)


main()