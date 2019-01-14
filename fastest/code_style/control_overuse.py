import re


CURRENT_CONDITIONAL_THRESHOLD = 5
CURRENT_CONTROL_COMPLEXITY_THRESHOLD = 3


def has_too_many_if_statements(function_body):
    matches = re.findall(r' if | elif | else', function_body)
    return len(matches) >= CURRENT_CONDITIONAL_THRESHOLD, len(matches)


def get_indent_of_loop(statement):
    len(re.findall(r'\s+?(?=for)', statement)[0])


def get_statements_from_function_body(function_body):
    return [
        statement for statement
        in function_body.split('\n')
        if len(statement.strip()) > 0
    ]


def count_loop_indents(function_body):
    statements = get_statements_from_function_body(function_body)
    loops = []

    for statement in statements:
        if re.match(r'for ', statement.strip()):
            loops.append(get_indent_of_loop(statement))

    return loops


def get_loop_complexity(function_body):
    loop_indents = count_loop_indents(function_body)
    complexity = 0
    for i in range(len(loop_indents)):
        if loop_indents[i] < loop_indents[i + 1]:
            complexity += 1
    return CURRENT_CONTROL_COMPLEXITY_THRESHOLD < complexity, complexity