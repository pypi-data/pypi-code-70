# -*- coding: utf-8 -*-
"""
    pygments.lexers.php
    ~~~~~~~~~~~~~~~~~~~

    Lexers for PHP and related languages.

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, default, using, \
    this, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Other
from pygments.util import get_bool_opt, get_list_opt, iteritems

__all__ = ['ZephirLexer', 'PhpLexer']


class ZephirLexer(RegexLexer):
    """
    For `Zephir language <http://zephir-lang.com/>`_ source code.

    Zephir is a compiled high level language aimed
    to the creation of C-extensions for PHP.

    .. versionadded:: 2.0
    """

    name = 'Zephir'
    aliases = ['zephir']
    filenames = ['*.zep']

    zephir_keywords = ['fetch', 'echo', 'isset', 'empty']
    zephir_type = ['bit', 'bits', 'string']

    flags = re.DOTALL | re.MULTILINE

    tokens = {
        'commentsandwhitespace': [
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline)
        ],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            (r'/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/'
             r'([gim]+\b|\B)', String.Regex, '#pop'),
            default('#pop')
        ],
        'badregex': [
            (r'\n', Text, '#pop')
        ],
        'root': [
            (r'^(?=\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            (r'\+\+|--|~|&&|\?|:|\|\||\\(?=\n)|'
             r'(<<|>>>?|==?|!=?|->|[-<>+*%&|^/])=?', Operator, 'slashstartsregex'),
            (r'[{(\[;,]', Punctuation, 'slashstartsregex'),
            (r'[})\].]', Punctuation),
            (r'(for|in|while|do|break|return|continue|switch|case|default|if|else|loop|'
             r'require|inline|throw|try|catch|finally|new|delete|typeof|instanceof|void|'
             r'namespace|use|extends|this|fetch|isset|unset|echo|fetch|likely|unlikely|'
             r'empty)\b', Keyword, 'slashstartsregex'),
            (r'(var|let|with|function)\b', Keyword.Declaration, 'slashstartsregex'),
            (r'(abstract|boolean|bool|char|class|const|double|enum|export|extends|final|'
             r'native|goto|implements|import|int|string|interface|long|ulong|char|uchar|'
             r'float|unsigned|private|protected|public|short|static|self|throws|reverse|'
             r'transient|volatile)\b', Keyword.Reserved),
            (r'(true|false|null|undefined)\b', Keyword.Constant),
            (r'(Array|Boolean|Date|_REQUEST|_COOKIE|_SESSION|'
             r'_GET|_POST|_SERVER|this|stdClass|range|count|iterator|'
             r'window)\b', Name.Builtin),
            (r'[$a-zA-Z_][\w\\]*', Name.Other),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ]
    }


class PhpLexer(RegexLexer):
    """
    For `PHP <http://www.php.net/>`_ source code.
    For PHP embedded in HTML, use the `HtmlPhpLexer`.

    Additional options accepted:

    `startinline`
        If given and ``True`` the lexer starts highlighting with
        php code (i.e.: no starting ``<?php`` required).  The default
        is ``False``.
    `funcnamehighlighting`
        If given and ``True``, highlight builtin function names
        (default: ``True``).
    `disabledmodules`
        If given, must be a list of module names whose function names
        should not be highlighted. By default all modules are highlighted
        except the special ``'unknown'`` module that includes functions
        that are known to php but are undocumented.

        To get a list of allowed modules have a look into the
        `_php_builtins` module:

        .. sourcecode:: pycon

            >>> from pygments.lexers._php_builtins import MODULES
            >>> MODULES.keys()
            ['PHP Options/Info', 'Zip', 'dba', ...]

        In fact the names of those modules match the module names from
        the php documentation.
    """

    name = 'PHP'
    aliases = ['php', 'php3', 'php4', 'php5']
    filenames = ['*.php', '*.php[345]', '*.inc']
    mimetypes = ['text/x-php']

    # Note that a backslash is included in the following two patterns
    # PHP uses a backslash as a namespace separator
    _ident_char = r'[\\\w]|[^\x00-\x7f]'
    _ident_begin = r'(?:[\\_a-z]|[^\x00-\x7f])'
    _ident_end = r'(?:' + _ident_char + ')*'
    _ident_inner = _ident_begin + _ident_end

    flags = re.IGNORECASE | re.DOTALL | re.MULTILINE
    tokens = {
        'root': [
            (r'<\?(php)?', Comment.Preproc, 'php'),
            (r'[^<]+', Other),
            (r'<', Other)
        ],
        'php': [
            (r'\?>', Comment.Preproc, '#pop'),
            (r'(<<<)([\'"]?)(' + _ident_inner + r')(\2\n.*?\n\s*)(\3)(;?)(\n)',
             bygroups(String, String, String.Delimiter, String, String.Delimiter,
                      Punctuation, Text)),
            (r'\s+', Text),
            (r'#.*?\n', Comment.Single),
            (r'//.*?\n', Comment.Single),
            # put the empty comment here, it is otherwise seen as
            # the start of a docstring
            (r'/\*\*/', Comment.Multiline),
            (r'/\*\*.*?\*/', String.Doc),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'(->|::)(\s*)(' + _ident_inner + ')',
             bygroups(Operator, Text, Name.Attribute)),
            (r'[~!%^&*+=|:.<>/@-]+', Operator),
            (r'\?', Operator),  # don't add to the charclass above!
            (r'[\[\]{}();,]+', Punctuation),
            (r'(class)(\s+)', bygroups(Keyword, Text), 'classname'),
            (r'(function)(\s*)(?=\()', bygroups(Keyword, Text)),
            (r'(function)(\s+)(&?)(\s*)',
             bygroups(Keyword, Text, Operator, Text), 'functionname'),
            (r'(const)(\s+)(' + _ident_inner + ')',
             bygroups(Keyword, Text, Name.Constant)),
            (r'(and|E_PARSE|old_function|E_ERROR|or|as|E_WARNING|parent|'
             r'eval|PHP_OS|break|exit|case|extends|PHP_VERSION|cfunction|'
             r'FALSE|print|for|require|continue|foreach|require_once|'
             r'declare|return|default|static|do|switch|die|stdClass|'
             r'echo|else|TRUE|elseif|var|empty|if|xor|enddeclare|include|'
             r'virtual|endfor|include_once|while|endforeach|global|'
             r'endif|list|endswitch|new|endwhile|not|'
             r'array|E_ALL|NULL|final|php_user_filter|interface|'
             r'implements|public|private|protected|abstract|clone|try|'
             r'catch|throw|this|use|namespace|trait|yield|'
             r'finally)\b', Keyword),
            (r'(true|false|null)\b', Keyword.Constant),
            include('magicconstants'),
            (r'\$\{\$+' + _ident_inner + '\}', Name.Variable),
            (r'\$+' + _ident_inner, Name.Variable),
            (_ident_inner, Name.Other),
            (r'(\d+\.\d*|\d*\.\d+)(e[+-]?[0-9]+)?', Number.Float),
            (r'\d+e[+-]?[0-9]+', Number.Float),
            (r'0[0-7]+', Number.Oct),
            (r'0x[a-f0-9]+', Number.Hex),
            (r'\d+', Number.Integer),
            (r'0b[01]+', Number.Bin),
            (r"'([^'\\]*(?:\\.[^'\\]*)*)'", String.Single),
            (r'`([^`\\]*(?:\\.[^`\\]*)*)`', String.Backtick),
            (r'"', String.Double, 'string'),
        ],
        'magicfuncs': [
            # source: http://php.net/manual/en/language.oop5.magic.php
            (words((
                '__construct', '__destruct', '__call', '__callStatic', '__get', '__set',
                '__isset', '__unset', '__sleep', '__wakeup', '__toString', '__invoke',
                '__set_state', '__clone', '__debugInfo',), suffix=r'\b'),
             Name.Function.Magic),
        ],
        'magicconstants': [
            # source: http://php.net/manual/en/language.constants.predefined.php
            (words((
                '__LINE__', '__FILE__', '__DIR__', '__FUNCTION__', '__CLASS__',
                '__TRAIT__', '__METHOD__', '__NAMESPACE__',),
                suffix=r'\b'),
             Name.Constant),
        ],
        'classname': [
            (_ident_inner, Name.Class, '#pop')
        ],
        'functionname': [
            include('magicfuncs'),
            (_ident_inner, Name.Function, '#pop'),
            default('#pop')
        ],
        'string': [
            (r'"', String.Double, '#pop'),
            (r'[^{$"\\]+', String.Double),
            (r'\\([nrt"$\\]|[0-7]{1,3}|x[0-9a-f]{1,2})', String.Escape),
            (r'\$' + _ident_inner + '(\[\S+?\]|->' + _ident_inner + ')?',
             String.Interpol),
            (r'(\{\$\{)(.*?)(\}\})',
             bygroups(String.Interpol, using(this, _startinline=True),
                      String.Interpol)),
            (r'(\{)(\$.*?)(\})',
             bygroups(String.Interpol, using(this, _startinline=True),
                      String.Interpol)),
            (r'(\$\{)(\S+)(\})',
             bygroups(String.Interpol, Name.Variable, String.Interpol)),
            (r'[${\\]', String.Double)
        ],
    }

    def __init__(self, **options):
        self.funcnamehighlighting = get_bool_opt(
            options, 'funcnamehighlighting', True)
        self.disabledmodules = get_list_opt(
            options, 'disabledmodules', ['unknown'])
        self.startinline = get_bool_opt(options, 'startinline', False)

        # private option argument for the lexer itself
        if '_startinline' in options:
            self.startinline = options.pop('_startinline')

        # collect activated functions in a set
        self._functions = set()
        if self.funcnamehighlighting:
            from pygments.lexers._php_builtins import MODULES
            for key, value in iteritems(MODULES):
                if key not in self.disabledmodules:
                    self._functions.update(value)
        RegexLexer.__init__(self, **options)

    def get_tokens_unprocessed(self, text):
        stack = ['root']
        if self.startinline:
            stack.append('php')
        for index, token, value in \
                RegexLexer.get_tokens_unprocessed(self, text, stack):
            if token is Name.Other:
                if value in self._functions:
                    yield index, Name.Builtin, value
                    continue
            yield index, token, value

    def analyse_text(text):
        rv = 0.0
        if re.search(r'<\?(?!xml)', text):
            rv += 0.3
        return rv
