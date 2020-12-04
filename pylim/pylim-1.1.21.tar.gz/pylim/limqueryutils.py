import datetime
import dateutil
import re
from pylim import limutils

curyear = datetime.datetime.now().year
prevyear = curyear - 1


def build_let_show_when_helper(lets, shows, whens):
    query = '''
LET
{0}
SHOW
{1}
WHEN
{2}
'''.format(lets, shows, whens)
    return query


def build_when_clause(start_date=None):
    when = ''
    if start_date is not None:
        if 'date is within' in start_date.lower():
            when = start_date
        else:
            if isinstance(start_date, str):
                start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            when = 'date is after %s' % (start_date.strftime('%m/%d/%Y'))
    return when


def build_series_query(symbols, metadata=None, start_date=None):
    q = 'Show \n'
    for symbol in symbols:
        qx = '{}: {}\n'.format(symbol, symbol)
        if limutils.check_pra_symbol(symbol):
            use_high_low = False
            if metadata is not None:
                meta = metadata[symbol]['daterange']
                if 'Low' in meta.index and 'High' in meta.index:
                    if 'Close' in meta.index and meta.start.Low < meta.start.Close:
                        use_high_low = True
                    if 'MidPoint' in meta.index and meta.start.Low < meta.start.MidPoint:
                        use_high_low = True
            if use_high_low:
                qx = '%s: (High of %s + Low of %s)/2 \n' % (symbol, symbol, symbol)

        q += qx

    when = build_when_clause(start_date)
    if when is not None and when != '':
        q += 'when %s' % when

    return q


def build_curve_query(symbols, column='Close', curve_date=None, curve_formula=None):
    """
    Build query for multiple symbols and single curve dates
    :param symbols:
    :param column:
    :param curve_date:
    :param curve_formula:
    :return:
    """
    lets, shows, whens = '', '', ''
    counter = 0

    for symbol in symbols:
        counter += 1
        curve_date_str = "LAST" if curve_date is None else curve_date.strftime("%m/%d/%Y")

        inc_or = ''
        if len(symbols) > 1 and counter != len(symbols):
            inc_or = 'OR'

        lets += 'ATTR x{1} = forward_curve({1},"{2}","{3}","","","days","",0 day ago)\n'.format(counter, symbol, column, curve_date_str)
        shows += '{0}: x{0}\n'.format(symbol)
        whens += 'x{0} is DEFINED {1}\n'.format(symbol, inc_or)

    if curve_formula is not None:
        if 'Show' in curve_formula or 'show' in curve_formula:
            curve_formula = curve_formula.replace('Show', '').replace('show', '')
        for symbol in symbols:
            curve_formula = curve_formula.replace(symbol, 'x%s' % (symbol))
        shows += curve_formula

    if curve_date is None: # when no curve date is specified we get a full history so trim
        last_month = (datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=1)).strftime('%m/%d/%Y')
        whens = '{ %s } and date is after %s' % (whens, last_month)

    return build_let_show_when_helper(lets, shows, whens)


def build_curve_history_query(symbols, column='Close', curve_dates=None):
    """
    Build query for single symbol and multiple curve dates
    :param symbols:
    :param column:
    :param curve_dates:
    :return:
    """

    if not isinstance(curve_dates, list) and not isinstance(curve_dates, tuple):
        curve_dates = [curve_dates]

    lets, shows, whens = '', '', ''
    counter = 0
    for curve_date in curve_dates:
        counter += 1
        curve_date_str, curve_date_str_nor = curve_date.strftime("%m/%d/%Y"), curve_date.strftime("%Y/%m/%d")

        inc_or = ''
        if len(curve_dates) > 1 and counter != len(curve_dates):
            inc_or = 'OR'
        lets += 'ATTR x{0} = forward_curve({1},"{2}","{3}","","","days","",0 day ago)\n'.format(counter, symbols[0], column, curve_date_str)
        shows += '{0}: x{1}\n'.format(curve_date_str_nor, counter)
        whens += 'x{0} is DEFINED {1}\n'.format(counter, inc_or)
    return build_let_show_when_helper(lets, shows, whens)


def build_continuous_futures_rollover_query(symbol, months=['M1'], rollover_date='5 days before expiration day', after_date=prevyear):
    lets, shows, whens = '', '', 'Date is after {}\n'.format(after_date)
    for month in months:
        m = int(month[1:])
        if m == 1:
            rollover_policy = 'actual prices'
        else:
            rollover_policy = '{} nearby actual prices'.format(m)
        lets += 'M{1} = {0}(ROLLOVER_DATE = "{2}",ROLLOVER_POLICY = "{3}")\n '.format(symbol, m, rollover_date, rollover_policy)
        shows += 'M{0}: M{0} \n '.format(m)

    return build_let_show_when_helper(lets, shows, whens)


def build_futures_contracts_formula_query(formula, matches, contracts, start_date=None):
    lets, shows = '', ''
    for cont in contracts:
        shows += '%s: x%s \n' % (cont, cont)
        t = formula
        for vsym in matches:
            t = re.sub(r'\b%s\b' % (vsym), '%s_%s' % (vsym, cont), t)

        if 'show' in t.lower():
            t = re.sub(r'\Show 1:', 'ATTR x%s = ' % cont, t)
        else:
            t = 'ATTR x%s = %s' % (cont, t)
        lets += '%s \n' % t

    when = build_when_clause(start_date)

    return build_let_show_when_helper(lets, shows, whens=when)


def build_structure_query(clause, symbols, mx, my, start_date=None):
    cx = clause
    cy = clause
    for match in symbols:
        if mx != 1:
            cx = cx.replace(match, '%s_%s' % (match, mx))
        if my != 1:
            cy = cy.replace(match, '%s_%s' % (match, my))

    q = 'Show M%s-M%s: (%s) - (%s)' % (mx, my, cx, cy)
    if start_date is not None:
        q = add_date_after_filter(query=q, date=start_date)
    return q


def add_date_after_filter(query, date):
    cutdate = dateutil.parser.parse(date).strftime('%m/%d/%Y')
    query += ' when date is after {}'.format(cutdate)
    return query


def extract_clause(query):
    """
    Given a string like Shop 1: x + y, return x + y
    :param query:
    :return:
    """
    return re.sub(r'Show \w:', '', query)
