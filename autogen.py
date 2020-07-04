import os

f = open('template.yml', 'r')
content = f.read()
f.close()

lines = ['nav:', '  - Home: index.md']
ignore = [
    'notes/index.md',
    'notes/img',
    'notes/javascript',
]


def generate_line(path, depth):
    print(path)
    f = open(path, 'r')
    name = f.readline().rstrip()[2:]
    f.close()
    return '  ' * (depth + 1) + '- ' + name + ': ' + path[6:]


def to_name(name):
    return ' '.join(map(lambda s: s.capitalize(), name.split('_')))

def add_dir(path, depth):
    files = []
    dirs = []
    sub_dirs = {}
    for name in os.listdir(path):
        tmp_path = os.path.join(path, name)
        if tmp_path in ignore:
            continue
        if os.path.isdir(tmp_path):
            name_line = '  ' * (depth + 1) + '- ' + to_name(name) + ':'
            dirs.append(name_line)
            sub_dirs[name_line] = add_dir(tmp_path, depth + 1)
        elif tmp_path.endswith('md'):
            files.append(generate_line(tmp_path, depth))
    ret = []
    for dir_name in sorted(dirs):
        ret.append(dir_name)
        ret += sub_dirs[dir_name]
    files = sorted(files)
    if path.endswith('leetcode'):
        files = sorted(files, key=lambda x: int(x.strip().split(' ')[1].split('.')[0]))
    return ret + files

lines += add_dir('notes', 0)

f = open('mkdocs.yml', 'w')
f.write(content + '\n'.join(lines) + '\n')
f.close()
