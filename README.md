# Tiny Bitly
A small Python wrapper to interface with the Bitly v4 API.

## Documentation
You can't do much with this wrapper, it only provides the essentials, that is expanding and shortening links:

- Use `bitly = Bitly("YOUR_API_TOKEN_HERE")` to initialize a bitly object.
- Use `bitly.shorten(long_url)` or `bitly.expand(short_url)` to get a Result object.

### Result object
both `shorten` and `expand` return this object, it has 4 parameters:

- `short` - *contains the short url*
- `long` - *contains the long link*
- `ok` - *contains either `True` or `False` depending on the outcome of the call*
- `error` - *contains the error message if the api call was not successful*

### Exceptions
bot `shorten` and `expand` will raise a `NullStringException` if the url passed to them is `None`

## Examples
shortening a link:

```
bitly = Bitly("YOUR_API_TOKEN_HERE")
original_link = "https://github.com/SudoOmbro"
result = bitly.shorten(original_link)
if result.ok:
    short_link = result.short
else:
    print(result.message)
    short_link = None
```

expanding a link:

```
bitly = Bitly("YOUR_API_TOKEN_HERE")
original_link = "https://bit.ly/2Tdl0We"
result = bitly.expand(original_link)
if result.ok:
    long_link = result.long
else:
    print(result.message)
    long_link = None
```

in these simple examples exceptions are not handled, it's good practice to handle them.