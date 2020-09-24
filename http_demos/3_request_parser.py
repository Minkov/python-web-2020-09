def parse_url_and_method(resource):
    index = resource.rindex('/')
    (url, method) = (resource[:index], resource[index + 1:])
    return (url, method)


def register_resources():
    END_COMMAND = 'END'
    resources = {}

    while True:
        line = input()
        if line == END_COMMAND:
            break

        (url, method) = parse_url_and_method(line)
        if url not in resources:
            resources[url] = set()

        resources[url].add(method)

    return resources


def read_request():
    (method, url, _) = input().split(' ')
    return (method.lower(), url)


def error_message():
    return '''HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain

Not Found'''


def success_message():
    return '''HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain

OK'''


def solve():
    resources = register_resources()
    (method, url) = read_request()

    if url not in resources:
        return error_message()
    if method not in resources[url]:
        return error_message()

    return success_message()


print(solve())
