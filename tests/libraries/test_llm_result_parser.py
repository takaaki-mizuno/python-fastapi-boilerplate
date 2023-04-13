from app.libraries.llm_result_parser import LLMResultParser


def test_instance_create():
    instance = LLMResultParser()
    assert instance is not None


def test_extract_markdown_list():
    instance = LLMResultParser()
    result = instance.extract_markdown_list('''
Text

- item1
- item2
  - item2-1
  - item2-2
- item3

Another text

''')
    assert len(result) == 3
    assert result[0]['item'] == 'item1'
    assert result[1]['item'] == 'item2'
    assert len(result[1]['children']) == 2
    assert result[1]['children'][0]['item'] == 'item2-1'
