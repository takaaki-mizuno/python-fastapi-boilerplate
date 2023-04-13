import re
from typing import List


class LLMResultParser:

    class Type:
        GPT = 'gpt'

    def __init__(self, _type: str = Type.GPT):
        self._type = _type

    @staticmethod
    def extract_markdown_list(text: str):
        _lines = text.split('\n')
        while _lines and not _lines[0].strip():
            _lines.pop(0)
        while _lines and not _lines[-1].strip():
            _lines.pop()

        item_re = re.compile(r'^(\s*)([-*+]\s)(.*)$')

        def parse_lines(lines: List[str], indent: int = 0):
            result = []
            while lines:
                line = lines.pop(0)
                match = item_re.match(line)
                if not match:
                    continue
                item_indent = len(match.group(1))
                item_text = match.group(3)

                if item_indent < indent:
                    lines.insert(0, line)
                    return result
                elif item_indent > indent:
                    lines.insert(0, line)
                    child_items = parse_lines(lines, indent=item_indent)
                    result[-1]['children'] = child_items
                else:
                    result.append({'item': item_text, 'children': []})
            return result

        return parse_lines(_lines)
