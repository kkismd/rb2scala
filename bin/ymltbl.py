#! /usr/bin/env python
# coding: utf-8

import pandocfilters as pandoc
import yaml, re

def walk(key, value, format, meta):
  if key == 'CodeBlock':
    [[ident, classes, keyvals], code] = value
    if u'ymltbl' in classes:
      data = yaml.load(code)
      attributes = list_to_dict(keyvals)
      return array2tbl(data, attributes)

def array2tbl(data, attributes):
  check_colsize(data)
  colsize = len(data[0])
  head = data[0]
  body = data[1:]
  return pandoc.Table(
    caption(attributes),
    aligns(colsize, attributes),
    widths(colsize, attributes),
    headers(head),
    rows(body))

def caption(attributes):
  capt = attributes.get("caption")
  if capt:
    return [pandoc.Str(unicode(capt))]
  else:
    return []

def aligns(size, attributes):
  """Attribute `aligns`: text-align keywords seperated with spaces.
     If not set, all aligns are set to default (align-left).
     :rtype: list of Pandoc json objects
  """
  def make_obj(label): return {"t": label, "c": []}
  def align_default(): return make_obj("AlignDefault")
  align_types = {
    "right": "AlignRight",
    "left": "AlignLeft",
    "center": "AlignCenter",
    "": "AlignDefault"
  }
  aligns = attributes.get("aligns")
  if aligns:
    return [make_obj(align_types[align]) for align in aligns.split(" ")]
  else:
    return [align_default() for x in range(size)]

def widths(size, attributes):
  """Attributes `widths`: table columns width percentages seperated with spaces.
     If not set, all widths are set to 0 (auto-sizing).
     :rtype: list of Pandoc json objects
  """
  widths = attributes.get("widths")
  if widths:
    return [float(x) for x in widths.split(" ")]
  else:
    return [0 for x in range(size)]

def headers(cols):
  """
     :param list of str cols: header columns
     :rtype: list of Pandoc json objects
  """
  return [parse(col) for col in cols]

def rows(data):
  """
     :param list of list of str data: table cell strings
     :rtype: list of Pandoc json objects
  """
  return [ [ cell(col, idx) for idx, col in enumerate(cols)] for cols in data]

klassname = [None, 'ruby', 'scala', None]
def cell(s, idx):
  #if re.search("""^[A-Za-z0-9(!'"<:]""", s):
  if klassname[idx]:
    # code block class
    return codeBlock(s, klassname[idx])
  else:
    return parse(s)

def codeBlock(s, klass):
    return [pandoc.CodeBlock(('', [klass], [('','')]), s)]

def plainStr(s): return [pandoc.Plain([pandoc.Str(s)])]

def parse(string):
  result = []
  tokens = unicode(string).split(" ")
  objects = [pandoc.Str(token) for token in tokens]
  for obj in objects:
    result.append(obj)
    result.append(pandoc.Space())
  result = result[:-1]
  return [pandoc.Plain(result)]

def list_to_dict(pairlist):
  """convert from assoc like nested arrays to dict.
  """
  result = {}
  for pair in pairlist:
    result[pair[0]] = pair[1]
  return result

def check_colsize(data):
  col_sizes = [len(cols) for cols in data]
  sample = col_sizes[0]
  if all([s is sample for s in col_sizes]):
    pass
  else:
    raise(TypeError("All rows MUST have same number of cols"))

import sys

def debug(msg):
  sys.stderr.write("[ymltbl] DEBUG: {0}\n".format(msg))

if __name__ == "__main__":
  pandoc.toJSONFilter(walk)
