# pyink
Fast and easy way to print colored output to your console.


installation:

`pip3 install git+https://github.com/MattAndrzejczuk/pyink.git`


pyink is a fast and easy way to print to the python console using as little code as possible. You can also add colorful ink to any string for printing your own concatinated strings.


###Example Usage:
```python

from pyink import ink



def post_stuff_to_log(request, intercept):
    ink.print_gray(request.method, "")
    ink.print_purple(" ~~~> ", "\n")
    ink.print_darkblue(intercept, "\n")
    return HttpResponse("console logged successfully.")

```


![alt text](https://raw.githubusercontent.com/MattAndrzejczuk/pyink/example_1.png)
![alt text](https://raw.githubusercontent.com/MattAndrzejczuk/pyink/example_2.png)

