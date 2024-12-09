from functools import wraps


def with_indent(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self._next_indent()
        try:
            result = func(self, *args, **kwargs)
            return result
        finally:
            self._prev_indent()

    return wrapper


def escape_unicode(x):
    return x.encode('unicode_escape').decode().replace('\\', '')
