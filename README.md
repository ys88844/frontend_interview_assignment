Frontend Interview - Assignment
===============================

In this folder, find the file ``frontend_interview_http_server.py``. It functions as follows:

1. It responds to a GET request with the url ``/get_update`` by sending a JSON response (to be expounded upon later)
2. It responds to any other GET request by trying to return a file with that path and name

Run it using ``python3 frontend_interview_http_server.py``: It will start an HTTP server on port 7000. Go to [http://127.0.0.1:7000/](http://127.0.0.1:7000/) and see the response. Also examine the responses at the url [http://127.0.0.1:7000/get_update](127.0.0.1:7000/get_update).

Essentially, ``/get_update`` returns a single item (as JSON) which is part of some list. A sample is: ``{"display": "Frank Exchange Of Views", "item_id": 22, "selected": 1}``. Here, ``item_id`` is the position in the list. It can be any non-negative integer; ``display`` is the text that shown beside that item and ``selected`` is whether the item is highlighted.


Okay, got it. So what do I do?
------------------------------

You have to make an HTML + JS page which runs in a browser (we will test on Google Chrome) and does the following:

1. Makes an AJAX query to ``/get_update`` once every second
2. The item contained in the response is to be shown as a list (ordered by ``item_id``)
3. If an ``item_id`` is repeated, it should replace the old one in the list
4. If ``selected`` is non-zero, then highlight the item


### Notes:

1. We leave the formatting up to you. Do as you deem best
2. You can use jQuery and/or Bootstrap (+Theme) if you desire
3. Your JS can be inline or served as a seperate file. ``frontend_interview_http_server.py`` will dutifully serve any file from the folder so your JS, CSS, fonts, etc can be put alongside with ease
4. We will be reachable on chat and via email during the duration of this assignment to clear doubts regarding the assignment. No hints will be given though


That was easy. What next?
-------------------------

Good. Now, you may attempt the following enhancements to your solution for additional credit:

1. Format it (the displayed document) nicely, in a tabular manner using Bootstrap Theme
2. Highlight only 1 item at a time. New items with a non-zero ``selected`` tag will cause old selected items to automatically de-select
3. Show an error on the page if the server is not responding correctly or if there was any problem in parsing the response
4. Serve the pages and the JSON responses from different programs. (For example, the updates on port 7070). You may need to modify the server code as well. **Hint:** Cross-origin resource sharing (CORS)
5. Add a filter such that only items which match the (regex) filter are displayed and the rest are hidden


### Notes (Reprise):

1. You may solve the enhancements section problems in any order, or skip any which are too difficult
2. Scoring is as follow:

Question         | Credits
-----------------|----------:
Primary Section  | 50
Enhancement - 1  | 5
Enhancement - 2  | 10
Enhancement - 3  | 5
Enhancement - 4  | 15
Enhancement - 5  | 15



