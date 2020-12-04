"""Section segmentation for English.

This module implements section segmentation in English using simple
machine learning classifiers.

Todo:
  * Standardize model (re-)generation
"""

# Imports
import os
import string
import unicodedata

from typing import Generator

# Packages
import pandas
import regex as re
import joblib

# Project imports
from lexnlp.nlp.en.segments.utils import build_document_line_distribution
from lexnlp.utils.map import Map
from lexnlp.utils.decorators import safe_failure

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/1.8.0/LICENSE"
__version__ = "1.8.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


# Setup module path
MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

# Load segmenters
SECTION_SEGMENTER_MODEL = joblib.load(os.path.join(MODULE_PATH, "./section_segmenter.pickle"))


def build_section_break_features(lines, line_id, line_window_pre, line_window_post, characters=string.printable,
                                 include_doc=None):
    """
    Build a feature vector for a given line ID with given parameters.

    :param lines:
    :param line_id:
    :param line_window_pre:
    :param line_window_post:
    :param characters:
    :param include_doc:
    :return:
    """
    # Feature vector
    feature_vector = {}

    # Check start offset
    if line_id < line_window_pre:
        line_window_pre = line_id

    # Check final offset
    if (line_id + line_window_post) >= len(lines):
        line_window_post = len(lines) - line_window_post - 1

    # Iterate through window
    for i in range(-line_window_pre, line_window_post + 1):
        try:
            line = lines[line_id + i]
        except IndexError:
            continue

        # Count length
        feature_vector["line_len_{0}".format(i)] = len(line)
        feature_vector["line_lenstrip_{0}".format(i)] = len(line.strip())
        feature_vector["line_title_case_{0}".format(i)] = line == line.title()
        feature_vector["line_upper_case_{0}".format(i)] = line == line.upper()

        # Count characters
        feature_vector["line_n_alpha_{0}".format(i)] = sum([1 for c in line if unicodedata.category(c).startswith("L")])
        feature_vector["line_n_number_{0}".format(i)] = sum(
            [1 for c in line if unicodedata.category(c).startswith("N")])
        feature_vector["line_n_punct_{0}".format(i)] = sum([1 for c in line if unicodedata.category(c).startswith("P")])
        feature_vector["line_n_whitespace_{0}".format(i)] = sum(
            [1 for c in line if unicodedata.category(c).startswith("Z")])

    # Simple checks
    line = lines[line_id]
    feature_vector["section"] = 1 if "section" in line else 0
    feature_vector["SECTION"] = 1 if "SECTION" in line else 0
    feature_vector["Section"] = 1 if "Section" in line else 0
    feature_vector["article"] = 1 if "article" in line else 0
    feature_vector["ARTICLE"] = 1 if "ARTICLE" in line else 0
    feature_vector["Article"] = 1 if "Article" in line else 0
    feature_vector["sw_section"] = 1 if line.strip().lower().startswith("section") else 0
    feature_vector["sw_article"] = 1 if line.strip().lower().startswith("article") else 0
    feature_vector["first_char_punct"] = (line.strip()[0] in string.punctuation) if len(line.strip()) > 0 else False
    feature_vector["last_char_punct"] = (line.strip()[-1] in string.punctuation) if len(line.strip()) > 0 else False
    feature_vector["first_char_number"] = (line.strip()[0] in string.digits) if len(line.strip()) > 0 else False
    feature_vector["last_char_number"] = (line.strip()[-1] in string.digits) if len(line.strip()) > 0 else False

    # Build character vector
    for character in characters:
        feature_vector["char_{0}".format(character)] = lines[line_id].count(character)

    # Add doc if requested
    if include_doc:
        feature_vector.update(include_doc)

    return feature_vector


@safe_failure
def get_sections(text, window_pre=3, window_post=3, score_threshold=0.5) -> Generator:
    """
    Get sections from text.
    NLP-based detection of sections.
    :param text:
    :param window_pre:
    :param window_post:
    :param score_threshold:
    :return:
    """

    # Get document character distribution
    doc_distribution = build_document_line_distribution(text)
    lines = text.splitlines()
    test_feature_data = []
    for line_id in range(len(lines)):
        test_feature_data.append(
            build_section_break_features(lines, line_id, window_pre, window_post, include_doc=doc_distribution))

    # Predict page breaks
    test_feature_df = pandas.DataFrame(test_feature_data).fillna(-1)
    test_predicted_lines = SECTION_SEGMENTER_MODEL.predict_proba(test_feature_df)
    predicted_df = pandas.DataFrame(test_predicted_lines, columns=["prob_false", "prob_true"])
    section_breaks = predicted_df.loc[predicted_df["prob_true"] >= score_threshold, :].index.tolist()

    if len(section_breaks) > 0:
        # Get first break
        pos0 = 0
        pos1 = section_breaks[0]
        section = "\n".join(lines[pos0:pos1])
        if len(section.strip()) > 0:
            yield section

        # Iterate through section breaks
        for i in range(len(section_breaks) - 1):
            # Get breaks
            pos0 = section_breaks[i]
            pos1 = section_breaks[i + 1]
            # Get text
            section = "\n".join(lines[pos0:pos1])
            if len(section.strip()) > 0:
                yield section

        # Yield final section
        section = "\n".join(lines[section_breaks[-1]:])
        if len(section.strip()) > 0:
            yield section


SECTION_TITLE_PTN = r"""
\s*
(
    (?i:(?:appendix|part|section|article|(?:sub)?title|EXHIBIT|SCHEDULE)\s+)?
    (?-i:\d+(?:\.\d+)?
         |
         \p{Lu}(?:-\d+(?:\.\d+)?)?
         |
         [XVILCM]+
         |
         \((?:\d{1,3}|\p{L}+)\)
    )
)
(?:\.|\s|$)
"""
SECTION_TITLE_RE1 = re.compile(r'(?<=[,\.:>;\d\n\s]\n)' + SECTION_TITLE_PTN, re.M | re.X)
SECTION_TITLE_RE2 = re.compile(r'\A' + SECTION_TITLE_PTN, re.M | re.X)


@safe_failure
def get_sections_re(text) -> Generator:
    """
    Get sections from text.
    Regex-based detection of text sections.
    :param text: str - source full text
    :return: generator of str
    """
    prev_start = None
    for match in SECTION_TITLE_RE1.finditer(text):
        start = match.start()
        if prev_start:
            yield text[prev_start:start]
        elif start != 0:
            yield text[0:start]
        prev_start = start
    if prev_start:
        yield text[prev_start:]


@safe_failure
def get_section_spans(text, use_ml=True,
                      return_text=True, skip_empty_headers=False,
                      sections_hierarchy=None) -> Generator:
    """
    Get sections from text.
    Use NLP-based detection OR regex-bases detection of sections - see use_ml param.
    :param text: str - source full text
    :param use_ml: bool - use sklearn classifier otherwise use regex-based detection
    :param return_text: bool - return section text
    :param skip_empty_headers: bool - return results containing headers only
    :param sections_hierarchy: list of regexes
    :return: Generator of dicts
    """

    _start_index_counter = 0
    level_parser = SectionLevelParser(sections_hierarchy=sections_hierarchy)
    sections_detector = get_sections if use_ml else get_sections_re

    for section in sections_detector(text):
        start_index = _start_index_counter + text[_start_index_counter:].index(section)
        end_index = start_index + len(section)
        _start_index_counter = end_index
        try:
            title = SECTION_TITLE_RE2.findall(section)[0]
            title_start = start_index + section.index(title)
            title_end = title_start + len(title)
        except IndexError:
            # wrong number of features (short text or smth similar)
            title = title_start = title_end = None
        if skip_empty_headers and not title:
            continue

        # try to get level
        level, abs_level = level_parser.detect(title)

        res = dict(
            start=start_index,
            end=end_index,
            title=title,
            title_start=title_start,
            title_end=title_end,
            level=level,
            abs_level=abs_level,
        )
        if return_text:
            res['text'] = section
        yield res


class SectionLevelParser:

    DEFAULT_SECTION_HIERARCHY = [
        r'(?i:(appendix|exhibit|schedule|part|title)\s+\S+)',
        r'(?i:subtitle\s+\S+)',
        r'(?i:section\s+\S+)',
        r'(?i:subsection\s+\S+)',
        r'(?i:article\s+\S+)',
        r'\p{Lu}+(?:-\d+(?:\.\d+)?)?',
        r'[\d\.]+',
        r'\p{L}+(?:-\d+(?:\.\d+)?)?',
        r'\([\p{L}\d]+\)'
    ]

    def __init__(self, sections_hierarchy=None):
        if not sections_hierarchy:
            sections_hierarchy = self.DEFAULT_SECTION_HIERARCHY
        self.default_sections_hierarchy = [Map(regex=re.compile(i),
                                               abs_level=n,
                                               rel_level=None)
                                           for n, i in enumerate(sections_hierarchy, start=1)]
        self.level = 1        # represents previous->current relative level (new custom hierarchy)
        self.abs_level = 1    # represents previous->current absolute level from sections_hierarchy
        self.prev_level_re = None
        self.title = ''

    @property
    def current_sections_hierarchy(self):
        return [i for i in self.default_sections_hierarchy if i.rel_level]

    def detect(self, title):
        self.title = title
        if not title:
            return 0, 0
        elif self.prev_level_re and self.prev_level_re.match(title):
            return self.level, self.abs_level
        elif self.current_sections_hierarchy:
            levels = self.get_from_detected()
            if levels is not None:
                return levels
        self.get_from_default()
        return self.level, self.abs_level

    def get_from_detected(self):
        for level_data in self.current_sections_hierarchy:
            if level_data.regex.match(self.title):
                self.level = level_data.rel_level
                self.abs_level = level_data.abs_level
                self.prev_level_re = level_data.regex
                return self.level, self.abs_level

    def get_from_default(self):
        for level_data in self.default_sections_hierarchy:
            if level_data.regex.match(self.title):
                if level_data.abs_level > self.abs_level:
                    self.level += 1
                elif level_data.abs_level < self.abs_level:
                    self.level -= 1
                level_data.rel_level = self.level
                self.abs_level = level_data.abs_level
                self.prev_level_re = level_data.regex
                break
