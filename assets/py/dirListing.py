INDEX_TEMPLATE = r"""
<html>
<body>
<h2>${header}</h2>
<p>
% for name in names:
    <li><a href="${name}">${name}</a></li>
% endfor
</p>
</body>
</html>
"""

EXCLUDED = ['index.html']

import os
import argparse

from mako.template import Template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_arugment("--header")
    args = parser.parse_args()
    fnames = [fname for fname in sortedos.listdir(args.directory) if fname not in EXCLUDED]
    header = (args.header if args.header else os.path.basename(args.directory))
    print(Template(INDEX_TEMPLATE).render(names=fnames, header=header))

if __name__ == '__main__':
    main()