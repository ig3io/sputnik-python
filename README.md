Sputnik
=======
Spotify Search API wrapper. Under development.

How it works
------------
Right now it only abstracts the connection and a few more things, but in the
end you have to work with JSON objects.

```python
import sputnik

search = sputnik.search("nine inch nails broken")
print search.info['num_results']
>> 119
for track in search:
    print track['name'] + ' - ' + track['album']['name']
>> Wish - Broken
>> Gave Up - Broken
>> ...
```    

License
-------
This code is under the MIT License.
