import os

f = open('template.yml', 'r')
content = f.read()
f.close()

lines = ['nav:']
ignore = [
    'notes/img',
]


def generate_line(path, depth):
    f = open(path, 'r')
    name = f.readline().rstrip()[2:]
    f.close()
    return '  ' * (depth + 1) + '- ' + name + ': ' + path[6:]


def to_name(name):
    return ' '.join(map(lambda s: s.capitalize(), name.split('_')))

def add_dir(path, depth):
    for name in os.listdir(path):
        tmp_path = os.path.join(path, name)
        if tmp_path in ignore:
            continue
        if os.path.isdir(tmp_path):
            lines.append('  ' * (depth + 1) + '- ' + to_name(name) + ':')
            add_dir(tmp_path, depth + 1)
        else:
            lines.append(generate_line(tmp_path, depth))

add_dir('notes', 0)

f = open('mkdocs.yml', 'w')
f.write(content + '\n'.join(lines) + '\n')
f.close()
