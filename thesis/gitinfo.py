import subprocess
import sys


TMPL='''\\section{{Thesis Git repository info}}

\\noindent Build time: \\textbf{{\\today \\, \\currenttime}}\\\\

\\noindent \\textbf{{Git HEAD:}}

\\begin{{verbatim}}
{head}\\end{{verbatim}}

\\noindent \\textbf{{Repository status:}}
\\begin{{verbatim}}
{status}\\end{{verbatim}}
'''


def githead():
    return subprocess.check_output(['git', 'log', '-n' '1'])


def gitstatus():
    return subprocess.check_output(['git', 'status'])


def main():
    output = TMPL.format(head=githead(), status=gitstatus())
    print(output)


if __name__ == '__main__':
    sys.exit(main() or 0)
