from markdown import markdown

def read_file(name):
    with open(name, 'r') as input_file:
        return input_file.read()

html = read_file('prefix.html') + markdown(read_file('README.md')) + read_file('suffix.html')

with open('index.html', 'w') as output_file:
    output_file.write(html)
