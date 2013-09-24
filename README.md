Sputnik
=======
Spotify Search API wrapper. Under development.

 [![Build Status](https://travis-ci.org/ignaciocontreras/sputnik-python.png)](https://travis-ci.org/ignaciocontreras/sputnik-python)


How it works
------------
Right now it only abstracts the connection and a few more things, but in the
end you have to work with JSON objects.

```python
import sputnik

search = sputnik.search("nine inch nails broken")
print search.['info']['num_results']
>> 119
for track in search['tracks']:
    print track['name'] + ' - ' + track['album']['name']
>> Wish - Broken
>> Gave Up - Broken
>> ...
```

Copyright
---------
Released under the terms of the MIT License.
