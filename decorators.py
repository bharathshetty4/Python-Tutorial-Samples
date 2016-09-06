def p_decorator(func):
	def func_wrapper(name):
		return '<p> {0} </p>'.format(func(name))
	return func_wrapper


def strong_decorator(func):
        def func_wrapper(name):
                return '<strong> {0} </strong>'.format(func(name))
        return func_wrapper


def div_decorator(func):
        def func_wrapper(name):
                return '<div> {0} </div>'.format(func(name))
        return func_wrapper


@div_decorator
@strong_decorator
@p_decorator
def get_text(name):
	return 'Hello ' + name

#print get_text('Ramesh')


#passing arguments to avoid redundant decorators

def tags(*tag_name):
	def tags_decorator(func):
		def func_wrapper(name):
			return '<{0}> {1} </{0}>'.format(tag_name, func(name))
		return func_wrapper
	return tags_decorator

@tags('p','div')
def get_text(name):
	return 'hello ' + name

print get_text('ramesh')
