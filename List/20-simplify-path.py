def simplifyPath( path):
    path = path.split('/')
    output = []
    for i in path:
        if i == "" or i=='.':
            continue
        elif i=='..':
            if output:
                output.pop(-1)
        else:
            output.append(i)
    path = '/'.join(output)
    return '/'+path

path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))