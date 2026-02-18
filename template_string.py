from string import Template

template = Template('Hello, this is $name, and he is $age years old')
message = template.substitute(name = "bob", age = 100)

print(message)

